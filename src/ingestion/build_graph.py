import json
import os
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

from config import llm

transformer = LLMGraphTransformer(
    llm=llm,  # pyright: ignore[reportArgumentType]
    allowed_nodes=[
        "Iniciativa",
        "Acao",
        "Ferramenta",
        "Publico",
        "Conceito",
        "Resultado",
        "Organizacao",
        "Local",
    ],
    allowed_relationships=[
        ("Iniciativa", "REALIZA", "Acao"),
        ("Iniciativa", "DESENVOLVE", "Ferramenta"),
        ("Iniciativa", "VINCULADA_A", "Iniciativa"),
        ("Iniciativa", "SEDIADA_EM", "Organizacao"),
        ("Organizacao", "LOCALIZADA_EM", "Local"),
        ("Acao", "OCORRE_EM", "Local"),
        ("Local", "DENTRO_DE", "Local"),
        ("Acao", "DIRIGIDA_A", "Publico"),
        ("Ferramenta", "DIRIGIDA_A", "Publico"),
        ("Iniciativa", "ABORDA", "Conceito"),
        ("Acao", "ABORDA", "Conceito"),
        ("Ferramenta", "ABORDA", "Conceito"),
        ("Acao", "PRODUZ", "Resultado"),
        ("Ferramenta", "PRODUZ", "Resultado"),
    ],
    node_properties=["descricao"],
    strict_mode=True,
)

load_dotenv()

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

CHECKPOINT = ROOT / "src" / "ingestion" / "checkpoint_done.txt"
FALHAS = ROOT / "src" / "ingestion" / "checkpoint_falhas.jsonl"
MAX_FALHAS_SEGUIDAS = 5
ERROS = (ConnectionError, TimeoutError)


def chunk_id(chunk) -> str:
    return chunk.metadata["chunk_id"]


def carregar_feitos() -> set[str]:
    if CHECKPOINT.exists():
        return set(CHECKPOINT.read_text().split())
    return set()


def anexar_linha(path: Path, linha: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(linha + "\n")


@retry(
    retry=retry_if_exception_type(ERROS),
    wait=wait_exponential_jitter(initial=5, max=60),
    stop=stop_after_attempt(5),
    reraise=True,
)
def extrair_grafo(lote):
    return transformer.convert_to_graph_documents(lote)


chunks = chunks[:5]  # Teste com 5
feitos = carregar_feitos()
pendentes = [(chunk_id(c), c) for c in chunks if chunk_id(c) not in feitos]
print(f"Total: {len(chunks)} | já feitos: {len(feitos)} | pendentes: {len(pendentes)}")

falhas_seguidas = 0

try:
    for n, (cid, doc) in enumerate(pendentes, start=1):
        try:
            graph_docs = extrair_grafo([doc])

            if graph_docs:
                graph.add_graph_documents(
                    graph_docs, baseEntityLabel=True, include_source=True
                )

            anexar_linha(CHECKPOINT, cid)  # só marca depois de gravar
            falhas_seguidas = 0

        except Exception as e:  # noqa: BLE001
            falhas_seguidas += 1
            anexar_linha(
                FALHAS,
                json.dumps({"id": cid, "erro": str(e)}, ensure_ascii=False),
            )
            print(f"Falha no chunk {n}: {e}", flush=True)

            if falhas_seguidas >= MAX_FALHAS_SEGUIDAS:
                print(
                    f"{MAX_FALHAS_SEGUIDAS} falhas seguidas. "
                    "Verifique Ollama/Neo4j e rode de novo."
                )
                break

except KeyboardInterrupt:
    print("\nInterrompido. O progresso está salvo; rode de novo para retomar.")

print("Fim da execução.")
