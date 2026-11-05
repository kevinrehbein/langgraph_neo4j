import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph

DIM = 1024
LOTE = 64

load_dotenv()

# Modelo para indexação dos embeddings dos nós do grafo
# (PyTorch)
embeddings_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True, "batch_size": 32},
)

# Grafo Neo4j hospedado no AuraDB
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)


def criar_indices():
    for nome, label in [
        ("chunk_embedding", "Document"),
        ("entity_embedding", "__Entity__"),
    ]:
        graph.query(
            f"""
            CREATE VECTOR INDEX {nome} IF NOT EXISTS
            FOR (n:`{label}`) ON (n.embedding)
            OPTIONS {{indexConfig: {{
              `vector.dimensions`: {DIM},
              `vector.similarity_function`: 'cosine'
            }}}}
            """
        )


def criar_embedding(label, text):
    total = 0
    while True:
        rows = graph.query(
            f"""
            MATCH (n:`{label}`)
            WHERE n.embedding IS NULL
            WITH n, {text} AS texto
            WHERE texto IS NOT NULL AND texto <> ''
            RETURN elementId(n) AS eid, texto
            LIMIT $n
            """,
            {"n": LOTE},
        )
        if not rows:
            break

        vecs = embeddings_model.embed_documents([r["texto"] for r in rows])

        graph.query(
            """
            UNWIND $rows AS r
            MATCH (n) WHERE elementId(n) = r.eid
            CALL db.create.setNodeVectorProperty(n, 'embedding', r.vec)
            """,
            {"rows": [{"eid": r["eid"], "vec": v} for r, v in zip(rows, vecs)]},
        )
        total += len(rows)
        print(f"{label}: {total}", flush=True)


if __name__ == "__main__":
    criar_indices()

    # chunks
    criar_embedding("Document", "n.text")

    # entidades: "Tipo: nome. descrição"
    criar_embedding(
        "__Entity__",
        "head([l IN labels(n) WHERE l <> '__Entity__']) + ': ' + n.id "
        "+ coalesce('. ' + n.descricao, '')",
    )

    print("Fim.")
