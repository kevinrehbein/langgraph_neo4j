import json
import os
import random
import sys
from pathlib import Path

from chunking import chunks
from dotenv import load_dotenv
from langchain_neo4j import LLMGraphTransformer, Neo4jGraph
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from config import llm_graph_transformer  # noqa: E402

transformer = LLMGraphTransformer(
    llm=llm_graph_transformer,  # pyright: ignore[reportArgumentType]
    allowed_nodes=[
        "Projeto",
        "Acao",
        "Ferramenta",
        "Publico",
        "Conceito",
        "Area",
        "Resultado",
        "Instituicao",
        "Local",
    ],
    allowed_relationships=[
        "REALIZA",
        "DESENVOLVE",
        "VINCULADO_A",
        "LOCALIZADO_EM",
        "DIRIGIDA_A",
        "ABORDA",
        "PRODUZ",
        "PERTENCE_A",
        "BENEFICIA",
    ],
    strict_mode=True,
    node_properties=["descricao"],
    additional_instructions=(
        "Escreva em português. Use nomes consistentes para as entidades. "
        "OBRIGATÓRIO: preencha a propriedade descricao em TODO nó, com 1 frase "
        "baseada no texto. "
        "Use apenas os tipos de nó e de relação permitidos, exatamente "
        "como escritos, sem acentos. "
        "Respeite a direção e os tipos de cada relação: "
        "Projeto REALIZA Acao; "
        "Projeto DESENVOLVE Ferramenta; "
        "Projeto VINCULADO_A Projeto (projetos relacionados entre si); "
        "Projeto VINCULADO_A Instituicao; "
        "Instituicao, Acao, Projeto ou Local LOCALIZADO_EM Local "
        "(use sempre para dizer onde algo fica ou acontece); "
        "Acao ou Ferramenta DIRIGIDA_A Publico; "
        "Projeto, Acao ou Ferramenta ABORDA Conceito; "
        "Acao ou Ferramenta PRODUZ Resultado; "
        "Projeto ou Conceito PERTENCE_A Area; "
        "Resultado BENEFICIA Publico."
    ),
    ignore_tool_usage=False,
)


load_dotenv()

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

CHECKPOINT = ROOT / "ingestion" / "checkpoint_done.txt"
FALHAS = ROOT / "ingestion" / "checkpoint_falhas.jsonl"


def add_metadata(doc):
    m = doc.metadata
    graph.query(
        """
        MERGE (a:Artigo {id: $artigo_id})
        SET a.titulo = $titulo, a.url_artigo = $url_artigo, a.url_pdf = $url_pdf
        WITH a
        MATCH (d:Document {id: $chunk_id})
        MERGE (d)-[:PARTE_DE]->(a)
        WITH a
        MERGE (e:Edicao {nome: $edicao})
        MERGE (a)-[:PUBLICADO_EM]->(e)
        WITH a
        UNWIND $autores AS nome
        MERGE (au:Autor {nome: nome})
        MERGE (a)-[:ESCRITO_POR]->(au)
        """,
        {
            "artigo_id": m["artigo_id"],
            "titulo": m["titulo"],
            "url_artigo": m["url_artigo"],
            "url_pdf": m["url_pdf"],
            "chunk_id": m["id"],
            "edicao": m["edicao"].replace("\xa0", " ").strip(),
            "autores": [a.strip() for a in m["autores"].split(",")],
        },
    )


def chunk_id(chunk) -> str:
    return chunk.metadata["id"]


def carregar_feitos() -> set[str]:
    if CHECKPOINT.exists():
        return set(CHECKPOINT.read_text().split())
    return set()


def anexar_linha(path: Path, linha: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(linha + "\n")


@retry(
    retry=retry_if_exception_type(Exception),
    wait=wait_exponential_jitter(initial=1, max=10),
    stop=stop_after_attempt(3),
    reraise=True,
)
def extrair_grafo(lote):
    return transformer.convert_to_graph_documents(lote)


random.seed(13)
chunks = random.sample(chunks, 5)  # Teste com 5 aleatorios

feitos = carregar_feitos()
pendentes = [(chunk_id(c), c) for c in chunks if chunk_id(c) not in feitos]
print(f"Total: {len(chunks)} | já feitos: {len(feitos)} | pendentes: {len(pendentes)}")


try:
    for n, (cid, doc) in enumerate(pendentes, start=1):
        try:
            graph_docs = extrair_grafo([doc])
            print(graph_docs)

            if graph_docs:
                graph.add_graph_documents(
                    graph_docs, baseEntityLabel=False, include_source=True
                )
                add_metadata(doc)

            anexar_linha(CHECKPOINT, cid)  # só marca depois de gravar

        except Exception as e:  # noqa: BLE001
            anexar_linha(
                FALHAS,
                json.dumps({"id": cid, "erro": str(e)}, ensure_ascii=False),
            )
            print(f"Falha no chunk {n}: {e}", flush=True)

except KeyboardInterrupt:
    print("\nInterrompido. O progresso está salvo; rode de novo para retomar.")

print("Fim da execução.")
