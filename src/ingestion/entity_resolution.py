"""
UNIR ENTIDADES DUPLICADAS NO NEO4J
==================================

O que este script faz, em 4 passos:

  1. Lê todos os nós :Entity do seu grafo.
  2. Calcula uma "chave" para cada nó. Nós com a mesma chave são considerados
     duplicados. A chave ignora:
        - maiúsculas/minúsculas      (Machine Learning = machine learning)
        - acentos                    (rede neural      = rede neural)
        - espaços                    (machine learning = machinelearning)
        - underlines e hífens        (machine_learning = machine-learning)
        - siglas conhecidas          (ML               = machine learning)
  3. Mostra os grupos de duplicatas encontrados (para você conferir).
  4. Se DRY_RUN = False, une cada grupo em um único nó.

COMO USAR
---------
  1. Faça BACKUP do banco antes (merge não tem desfazer).
  2. Instale:   pip install neo4j
  3. O Neo4j precisa ter o plugin APOC instalado.
  4. Ajuste a seção "CONFIGURAÇÃO" abaixo.
  5. Rode primeiro com DRY_RUN = True, confira a lista, e só depois
     mude para False.
"""

import os
import re
import unicodedata
from collections import defaultdict

from dotenv import load_dotenv
from neo4j import GraphDatabase

# =============================================================================
# CONFIGURAÇÃO  (ajuste aqui)
# =============================================================================

load_dotenv()

URI = os.getenv("NEO4J_URI")
USUARIO = os.getenv("NEO4J_USERNAME")
SENHA = os.getenv("NEO4J_PASSWORD")

LABEL = "__Entity__"  # label dos nós de entidade
PROP_NOME = "id"  # propriedade que guarda o nome da entidade
PROP_TIPO = None  # propriedade com o tipo (pessoa, método...).
# Use None se não tiver: aí só o nome decide.

# True  = só mostra o que SERIA unido, sem alterar nada (recomendado primeiro)
# False = realmente une os nós
DRY_RUN = True

# Dicionário de siglas. A chave é a sigla e o valor é a forma completa.
# Preencha com as siglas do seu domínio. Só coloque siglas sem ambiguidade.
SIGLAS_MANUAIS = {
    "ml": "machine learning",
    "cnn": "convolutional neural network",
    "nlp": "natural language processing",
}


# =============================================================================
# PASSO 1 - FUNÇÕES DE NORMALIZAÇÃO
# =============================================================================


def so_letras_e_numeros(texto: str) -> str:
    """
    Transforma qualquer texto em uma sequência só de letras minúsculas
    e números, sem acentos, espaços ou símbolos.

    Exemplos:
        "Aprendizado_de_Máquina"  -> "aprendizadodemaquina"
        "Aprendizado de máquina"  -> "aprendizadodemaquina"
        "AprendizadoDeMáquina"    -> "aprendizadodemaquina"
    """
    texto = texto.replace("_", " ")
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.lower()

    return re.sub(r"[^a-z0-9]", "", texto)


# Dicionário de siglas já normalizado: {"ml": "machinelearning", ...}
SIGLAS = {
    so_letras_e_numeros(sigla): so_letras_e_numeros(completo)
    for sigla, completo in SIGLAS_MANUAIS.items()
}


def calcular_chave(nome: str, tipo: str | None) -> tuple:
    """
    Devolve a chave que identifica a entidade.
    Dois nós com a MESMA chave são tratados como duplicatas.

    A chave é (tipo, nome_normalizado). Incluir o tipo evita unir coisas
    diferentes que têm o mesmo nome (ex.: "Python" linguagem x "Python" cobra).
    """
    chave_nome = so_letras_e_numeros(nome)

    # Se for uma sigla conhecida, troca pela forma completa.
    chave_nome = SIGLAS.get(chave_nome, chave_nome)

    return (tipo, chave_nome)


# =============================================================================
# PASSO 2 - ESCOLHER QUAL NOME FICA COMO "OFICIAL" EM CADA GRUPO
# =============================================================================


def pontuacao_do_nome(nome: str) -> tuple:
    """
    Dá uma nota ao nome. Quanto maior, mais bonito/correto ele é.
    Preferimos (nesta ordem):
        1. nomes sem underline
        2. nomes com espaços
        3. nomes com acento (ex.: "Máquina" é melhor que "Maquina")
        4. nomes com capitalização mista (não tudo maiúsculo/minúsculo)
    """
    sem_acento = "".join(
        c for c in unicodedata.normalize("NFKD", nome) if not unicodedata.combining(c)
    )
    return (
        "_" not in nome,
        " " in nome,
        nome != sem_acento,
        nome != nome.lower() and nome != nome.upper(),
    )


# =============================================================================
# PASSO 3 - LER O GRAFO E AGRUPAR DUPLICATAS
# =============================================================================


def buscar_grupos_duplicados(session) -> list[list[dict]]:
    """
    Lê todos os nós, calcula a chave de cada um e devolve só os grupos
    que têm mais de um nó (ou seja, as duplicatas).
    """
    tipo_cypher = f"e.{PROP_TIPO}" if PROP_TIPO else "null"
    consulta = f"""
        MATCH (e:{LABEL})
        WHERE e.{PROP_NOME} IS NOT NULL
        RETURN elementId(e) AS id, e.{PROP_NOME} AS nome, {tipo_cypher} AS tipo
    """
    nos = session.run(consulta).data()

    # Agrupa os nós pela chave.
    grupos = defaultdict(list)
    for no in nos:
        grupos[calcular_chave(no["nome"], no["tipo"])].append(no)

    # Fica só com grupos de 2+ nós (os que têm duplicata).
    return [g for g in grupos.values() if len(g) > 1]


# =============================================================================
# PASSO 4 - UNIR OS NÓS DE UM GRUPO
# =============================================================================
'''
def unir_grupo(session, grupo: list[dict]) -> None:
    """
    Une todos os nós do grupo em um só.
 
    - O nó "principal" é o que tem o melhor nome (ver pontuacao_do_nome).
    - As relações dos outros nós passam a apontar para o principal.
    - Todos os nomes antigos ficam guardados na propriedade 'aliases'.
    """
    frequencia = Counter(n["nome"] for n in grupo)
 
    # Ordena: melhor nome primeiro (desempate: o nome mais frequente).
    grupo.sort(
        key=lambda n: (pontuacao_do_nome(n["nome"]), frequencia[n["nome"]]),
        reverse=True,
    )
    principal = grupo[0]
    outros = grupo[1:]
    aliases = sorted(frequencia)  # todos os nomes originais, sem repetir
 
    session.run(
        f"""
        MATCH (principal:{LABEL}) WHERE elementId(principal) = $id_principal
        MATCH (outro:{LABEL})     WHERE elementId(outro) IN $ids_outros
        WITH principal, collect(outro) AS outros
 
        // apoc junta os nós. O PRIMEIRO da lista é o que sobrevive.
        CALL apoc.refactor.mergeNodes([principal] + outros, {{
            properties: 'discard',     // mantém as propriedades do principal
            mergeRels: true,           // junta relações repetidas
            produceSelfRel: false      // não cria laço do nó para ele mesmo
        }}) YIELD node
 
        SET node.aliases = $aliases    // guarda os nomes antigos
        """,
        id_principal=principal["id"],
        ids_outros=[n["id"] for n in outros],
        aliases=aliases,
    )
'''

# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================


def main() -> None:
    driver = GraphDatabase.driver(URI, auth=(USUARIO, SENHA))

    with driver.session() as session:
        grupos = buscar_grupos_duplicados(session)

        # Mostra o que foi encontrado, do maior grupo para o menor.
        grupos.sort(key=len, reverse=True)
        print(f"Grupos de duplicatas encontrados: {len(grupos)}")
        print(
            f"Nós que serão removidos pelo merge: {sum(len(g) - 1 for g in grupos)}\n"
        )

        for g in grupos[:50]:  # mostra só os 30 primeiros para não poluir
            print(" | ".join(sorted({n["nome"] for n in g})))

        if DRY_RUN:
            print(
                "\nDRY_RUN ativo: nada foi alterado. "
                "Confira a lista acima e mude DRY_RUN para False."
            )
            return

        # Une de fato.
        """
        for i, g in enumerate(grupos, start=1):
            unir_grupo(session, g)
            if i % 100 == 0:
                print(f"  {i}/{len(grupos)} grupos unidos...")
 
        print("\nConcluído.")
        """
    driver.close()


if __name__ == "__main__":
    main()


# =============================================================================
# DEPOIS DE RODAR (checklist)
# =============================================================================
# 1. Recalcule os embeddings dos nós unidos (a descrição pode ter mudado).
# 2. Se as entidades tinham várias descrições, resuma-as com um LLM.
# 3. Reexecute a detecção de comunidades (Leiden) e os resumos de comunidade.
# 4. Evite que as duplicatas voltem: nas próximas ingestões, use
#    calcular_chave() ANTES de criar o nó, e faça MERGE por essa chave.
#
# CUIDADOS
# --------
# - Se a lista do DRY_RUN mostrar unions erradas (ex.: dois termos diferentes
#   com a mesma chave), remova a sigla problemática de SIGLAS_MANUAIS
#   ou ajuste a regra antes de ir para DRY_RUN = False.
# - Termos muito curtos (2-3 letras) são os mais propensos a colisão.
#   Revise-os com atenção na lista.
