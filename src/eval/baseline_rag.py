import json
import os
from pathlib import Path

import torch
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph

TOP_K = 10  # número de de resultados retornados por RAG Vetorial

ROOT = Path(__file__).resolve().parent
ENTRADA = ROOT / "perguntas.jsonl"
SAIDA = ROOT / "resultados_baseline.jsonl"

load_dotenv()

llm = init_chat_model(
    model="gemma-4-31b-it",
    model_provider="google_genai",
    temperature=0,
)

embedding_llm = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
    encode_kwargs={"normalize_embeddings": True, "batch_size": 16},
)

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)

PROMPT = """Você é um assistente do Programa Meninas Digitais.
Responda à pergunta usando APENAS o contexto abaixo. Se o contexto não
contiver a resposta, diga que não encontrou. Cite as fontes pelo título.
 
Contexto: {contexto}
 
Pergunta: {pergunta}
Resposta:"""


def recuperar(pergunta: str, k: int = TOP_K) -> list[dict]:
    vec = embedding_llm.embed_query(pergunta)
    return graph.query(
        """
        MATCH (node:Document)
            SEARCH node IN (VECTOR INDEX chunk_embedding FOR $vec LIMIT $k)
            SCORE AS score
        OPTIONAL MATCH (node)-[:PARTE_DE]->(a:Artigo)
        RETURN node.text AS texto, score,
                a.titulo AS titulo, a.url_pdf AS url_pdf
        """,
        {"k": k, "vec": vec},
    )


def responder(pergunta: str) -> dict:
    docs = recuperar(pergunta)
    contexto = "\n\n".join(f"[{d['titulo']}]\n{d['texto']}" for d in docs)
    resposta = llm.invoke(PROMPT.format(contexto=contexto, pergunta=pergunta)).content
    return {
        "resposta": resposta,
        "contextos": [d["texto"] for d in docs],
        "fontes": sorted({d["titulo"] for d in docs if d["titulo"]}),
    }


if __name__ == "__main__":
    perguntas = [json.loads(l) for l in ENTRADA.open(encoding="utf-8") if l.strip()]

    with SAIDA.open("w", encoding="utf-8") as f:
        for q in perguntas:
            r = responder(q["pergunta"])
            f.write(json.dumps({**q, **r}, ensure_ascii=False) + "\n")
