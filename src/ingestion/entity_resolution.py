"""
Une nós :__Entity__ com o mesmo nome no Neo4j (ignorando maiúsculas,
acentos, espaços, "_" e "-"). Requer o plugin APOC.

Faça BACKUP antes. Rode com DRY_RUN = True, confira, e só então mude para False.
"""

import os
import re
import unicodedata
from collections import defaultdict

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
USUARIO = os.getenv("NEO4J_USERNAME")
SENHA = os.getenv("NEO4J_PASSWORD")

LABEL = "__Entity__"
PROP_NOME = "id"
DRY_RUN = True

def chave(nome: str) -> str:
    """'Aprendizado_de_Máquina' -> 'aprendizadodemaquina'"""
    nome = unicodedata.normalize("NFKD", nome.replace("_", " "))
    nome = "".join(c for c in nome if not unicodedata.combining(c))
    nome = re.sub(r"[^a-z0-9]", "", nome.lower())
    return nome


def melhor_nome(nome: str) -> tuple:
    """Prefere nomes sem '_', com espaços e com capitalização."""
    return ("_" not in nome, " " in nome, nome != nome.lower())


def buscar_grupos(session) -> list[list[dict]]:
    nos = session.run(
        f"""
        MATCH (e:{LABEL}) WHERE e.{PROP_NOME} IS NOT NULL
        RETURN elementId(e) AS id, e.{PROP_NOME} AS nome
        """
    ).data()

    grupos = defaultdict(list)
    for no in nos:
        grupos[chave(no["nome"])].append(no)

    return [g for g in grupos.values() if len(g) > 1]


def unir_grupo(session, grupo: list[dict]) -> None:
    grupo.sort(key=lambda n: melhor_nome(n["nome"]), reverse=True)
    principal, outros = grupo[0], grupo[1:]
    aliases = sorted({n["nome"] for n in grupo})

    session.run(
        f"""
        MATCH (p:{LABEL}) WHERE elementId(p) = $id_principal
        MATCH (o:{LABEL}) WHERE elementId(o) IN $ids_outros
        WITH p, collect(o) AS outros
        CALL apoc.refactor.mergeNodes([p] + outros, {{
            properties: {{ description: 'combine', `.*`: 'discard' }},
            mergeRels: true,
            produceSelfRel: false
        }}) YIELD node
        SET node.aliases = $aliases
        """,
        id_principal=principal["id"],
        ids_outros=[n["id"] for n in outros],
        aliases=aliases,
    )


def main() -> None:
    driver = GraphDatabase.driver(URI, auth=(USUARIO, SENHA))
    try:
        with driver.session() as session:
            grupos = buscar_grupos(session)
            grupos.sort(key=len, reverse=True)

            print(f"Grupos de duplicatas: {len(grupos)}")
            print(f"Nós removidos pelo merge: {sum(len(g) - 1 for g in grupos)}\n")

            for g in grupos[:50]:
                print(" | ".join(sorted({n["nome"] for n in g})))

            if DRY_RUN:
                print("\nDRY_RUN ativo: nada foi alterado.")
                return

            for i, g in enumerate(grupos, start=1):
                unir_grupo(session, g)
                if i % 100 == 0:
                    print(f"  {i}/{len(grupos)} grupos unidos...")
            print("\nConcluído.")
    finally:
        driver.close()


if __name__ == "__main__":
    main()