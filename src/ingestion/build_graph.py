import asyncio
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

CONCORRENCIA_POR_GPU = 4

ROOT = Path(__file__).resolve().parents[1]
FALHAS = ROOT / "ingestion" / "checkpoint_falhas.jsonl"

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from config import llm_graph_transformer_0, llm_graph_transformer_1


def make_LLMGraphTransformer(llm):
    return LLMGraphTransformer(
        llm=llm,
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
            "IMPACTA",
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
            "Resultado IMPACTA Publico."
        ),
        ignore_tool_usage=False,
    )


LLMGraphTransformers = [
    make_LLMGraphTransformer(llm_graph_transformer_0),
    make_LLMGraphTransformer(llm_graph_transformer_1),
]

sems = [asyncio.Semaphore(CONCORRENCIA_POR_GPU) for _ in LLMGraphTransformers]
db_lock = asyncio.Lock()

load_dotenv()

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)


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


graph.query(
    "CREATE CONSTRAINT checkpoint_id IF NOT EXISTS "
    "FOR (c:Checkpoint) REQUIRE c.id IS UNIQUE"
)


def carregar_feitos() -> set[str]:
    rows = graph.query("MATCH (c:Checkpoint) RETURN c.id AS id")
    return {r["id"] for r in rows}


def marcar_feito(cid: str) -> None:
    graph.query("MERGE (:Checkpoint {id: $id})", {"id": cid})


def anexar_linha(path: Path, linha: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(linha + "\n")


@retry(
    retry=retry_if_exception_type(Exception),
    wait=wait_exponential_jitter(initial=1, max=3),
    stop=stop_after_attempt(3),
    reraise=True,
)
async def extrair_grafo(lote, transformer):
    return await asyncio.wait_for(
        transformer.aconvert_to_graph_documents(lote), timeout=420
    )

def gravar(graph_docs, doc, cid):
    graph.add_graph_documents(
        graph_docs, baseEntityLabel=True, include_source=True
    )
    add_metadata(doc)
    marcar_feito(cid)

async def processar(i, cid, doc):
    k = i % len(LLMGraphTransformers)  # GPU deste chunk
    try:
        async with sems[k]:
            graph_docs = await extrair_grafo([doc], LLMGraphTransformers[k])
        # semáforo liberado

        if not graph_docs or not graph_docs[0].nodes:
            raise ValueError("extração retornou vazio")

        async with db_lock:  # um write por vez no Neo4j
            await asyncio.to_thread(gravar, graph_docs, doc, cid)

    except Exception as e:  # noqa: BLE001
        anexar_linha(
            FALHAS, json.dumps({"id": cid, "erro": str(e)}, ensure_ascii=False)
        )
        print(f"Falha no chunk {cid}: {e}", flush=True)

async def main():
    await asyncio.gather(
        *(processar(i, cid, doc) for i, (cid, doc) in enumerate(pendentes))
    )

random.seed(13)
chunks = random.sample(chunks, 30)  # Teste com 5 aleatorios

feitos = carregar_feitos()
pendentes = [(chunk_id(c), c) for c in chunks if chunk_id(c) not in feitos]
print(f"Total: {len(chunks)} | Feitos: {len(feitos)} | Pendentes: {len(pendentes)}")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nInterrompido. O progresso está salvo, rode de novo para retomar.")

print("Fim da execução.")
