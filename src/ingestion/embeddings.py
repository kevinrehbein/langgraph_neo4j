import os

import torch
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

DIM = 1024
LOTE = 32

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
    encode_kwargs={"normalize_embeddings": True, "batch_size": 16},
)

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

# label: (índice, texto)
ALVOS = {
    "Document": ("chunk_embedding", "n.text"),
    "__Entity__": (
        "entity_embedding",
        "head([l IN labels(n) WHERE l <> '__Entity__']) + ': ' + n.id "
        "+ coalesce('. ' + n.descricao, '')",
    ),
}

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=2, max=30),
    reraise=True,
)
def query(cypher: str, params: dict | None = None):
    return graph.query(cypher, params or {})



def embedar(label: str, indice: str, texto: str) -> None:
    query(
        f"""
        CREATE VECTOR INDEX {indice} IF NOT EXISTS
        FOR (n:`{label}`) ON (n.embedding)
        OPTIONS {{indexConfig: {{
          `vector.dimensions`: {DIM},
          `vector.similarity_function`: 'cosine'}}}}
        """
    )

    rows = query(
        f"""
        MATCH (n:`{label}`)
        WHERE n.embedding IS NULL AND coalesce(n.skip_embedding, false) = false
        WITH n, {texto} AS texto
        WHERE texto IS NOT NULL AND trim(texto) <> ''
        RETURN elementId(n) AS eid, texto
        """
    )
    print(f"{label}: {len(rows)} pendentes", flush=True)

    for i in range(0, len(rows), LOTE):
        lote = rows[i : i + LOTE]
        vecs = embedding_model.embed_documents([r["texto"] for r in lote])
        query(
            """
            UNWIND $rows AS r
            MATCH (n) WHERE elementId(n) = r.eid
            CALL db.create.setNodeVectorProperty(n, 'embedding', r.vec)
            """,
            {"rows": [{"eid": r["eid"], "vec": v} for r, v in zip(lote, vecs)]},
        )
        print(f"{label}: {min(i + LOTE, len(rows))}/{len(rows)}", flush=True)


if __name__ == "__main__":
    for label, (indice, texto) in ALVOS.items():
        embedar(label, indice, texto)
    print("Fim.")
