import json
import os
from pathlib import Path

import torch
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph

TOP_K = 6  # chunks do vetor; igual ao baseline
N_ENTIDADES = 5  # entidades de entrada
SCORE_MIN = 0.5  # descarta entidades pouco parecidas
TETO_GRAU = 350  # entidade com mais relações semânticas que isso não é expandida
K_GRAFO = 3  # chunks extras vindos do grafo
RELACOES_POR_ENTIDADE = 4
MAX_RELACOES = 20

ROOT = Path(__file__).resolve().parent
ENTRADA = ROOT / "perguntas.jsonl"
SAIDA = ROOT / "resultados_grafo.jsonl"

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
Responda à pergunta usando APENAS o contexto abaixo (Relações do grafo e trechos
de artigos). Se o contexto não contiver a resposta, diga que não encontrou.
Cite as fontes pelo título do artigo. Em perguntas de lista, liste todos os
itens encontrados, com nomes próprios de projetos, locais e instituições.

Relações do grafo:
{relacoes}

Trechos dos artigos:
{contexto}

Pergunta: {pergunta}
Resposta:"""


def chunks_entrada(vec: list[float]) -> list[dict]:
    return graph.query(
        """
        MATCH (d:Document)
            SEARCH d IN (VECTOR INDEX chunk_embedding FOR $vec LIMIT $k)
            SCORE AS score
        OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
        RETURN d.id AS id, d.text AS texto, score, a.titulo AS titulo
        """,
        {"k": TOP_K, "vec": vec},
    )


def entidades_entrada(vec: list[float]) -> list[dict]:
    """Pontos de entrada no grafo. Hubs (grau semântico alto) ficam de fora."""
    return graph.query(
        """
        MATCH (e:__Entity__)
            SEARCH e IN (VECTOR INDEX entity_embedding FOR $vec LIMIT $n)
            SCORE AS score
        WHERE score >= $min AND e.grau <= $teto
        RETURN elementId(e) AS eid, e.id AS nome,
                coalesce(e.descricao, '') AS descricao, score
        """,
        {"n": N_ENTIDADES, "vec": vec, "min": SCORE_MIN, "teto": TETO_GRAU},
    )


def relacoes_do_grafo(eids: list[str], vec: list[float]) -> list[dict]:
    """Única expansão do grafo: vizinhos mais similares à pergunta, por entidade."""
    return graph.query(
        """
        MATCH (e:__Entity__) WHERE elementId(e) IN $eids
        MATCH (e)-[r]-(v:__Entity__)
        WHERE v.grau <= $teto AND v.embedding IS NOT NULL
        WITH e, r, vector.similarity.cosine(v.embedding, $vec) AS sim
        ORDER BY sim DESC
        WITH e, collect({r: r, sim: sim})[..$por_entidade] AS top
        UNWIND top AS t
        WITH t.r AS r, max(t.sim) AS sim
        ORDER BY sim DESC
        LIMIT $max
        RETURN startNode(r).id AS origem,
               type(r) AS rel,
               endNode(r).id AS destino,
               coalesce(startNode(r).descricao, '') AS desc_origem,
               coalesce(endNode(r).descricao, '') AS desc_destino,
               elementId(startNode(r)) AS eid_origem,
               elementId(endNode(r)) AS eid_destino,
               sim
        """,
        {
            "eids": eids,
            "vec": vec,
            "teto": TETO_GRAU,
            "por_entidade": RELACOES_POR_ENTIDADE,
            "max": MAX_RELACOES,
        },
    )


def chunks_do_grafo(ents: list[str], excluir: list[str]) -> list[dict]:
    """Chunks que mencionam as entidades já selecionadas (entradas + pontas das
    relações). Entidades raras (poucas menções) pesam mais, tipo IDF."""
    return graph.query(
        """
        UNWIND $ents AS eid
        MATCH (x:__Entity__) WHERE elementId(x) = eid
        MATCH (d:Document)-[:MENTIONS]->(x)
            WHERE NOT d.id IN $excluir
        WITH d, sum(1.0 / log(1 + x.n_mentions)) AS relevancia
        ORDER BY relevancia DESC
        LIMIT $k
        OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
        RETURN d.id AS id, d.text AS texto, relevancia, a.titulo AS titulo
        """,
        {"ents": ents, "excluir": excluir, "k": K_GRAFO},
    )

def recuperar(pergunta: str) -> dict:
    vec = embedding_llm.embed_query(pergunta)

    chunks_base = chunks_entrada(vec)
    nos_entrada = entidades_entrada(vec)
    eids = [e["eid"] for e in nos_entrada]

    relacoes_grafo, chunks_extras = [], []
    if eids:
        relacoes_grafo = relacoes_do_grafo(eids, vec)
        ents = set(eids)
        for r in relacoes_grafo:
            ents.update((r["eid_origem"], r["eid_destino"]))
        chunks_extras = chunks_do_grafo(
            list(ents), excluir=[c["id"] for c in chunks_base]
        )

    return {
        "base": chunks_base,
        "extras": chunks_extras,
        "relacoes": relacoes_grafo,
        "entradas": nos_entrada,
    }


def responder(pergunta: str) -> dict:
    r = recuperar(pergunta)

    # 1) Descrições: entidades de entrada + pontas das triplas (relacoes)
    desc = {e["nome"]: e["descricao"] for e in r["entradas"] if e.get("descricao")}
    for rel in r["relacoes"]:
        if rel["desc_origem"]:
            desc.setdefault(rel["origem"], rel["desc_origem"])
        if rel["desc_destino"]:
            desc.setdefault(rel["destino"], rel["desc_destino"])

    # 2) Bloco de relações: entidades (com descrição) e relacionamentos
    if r["relacoes"]:
        bloco_entidades = "\n".join(f"- {n}: {d}" for n, d in desc.items())
        bloco_relacoes = "\n".join(
            f"{f['origem']} -[{f['rel']}]-> {f['destino']}" for f in r["relacoes"]
        )
        relacoes_texto = f"Entidades:\n{bloco_entidades}\n\nRelações:\n{bloco_relacoes}"
    else:
        relacoes_texto = "(nenhum)"

    chunks = r["base"] + r["extras"]
    contexto = "\n\n".join(f"[{c['titulo']}]\n{c['texto']}" for c in chunks)

    resposta = llm.invoke(
        PROMPT.format(
            relacoes=relacoes_texto,
            contexto=contexto,
            pergunta=pergunta,
        )
    ).content

    return {
        "resposta": resposta,
        "contextos": [c["texto"] for c in chunks]
        + ([relacoes_texto] if r["relacoes"] else []),
        "fontes": sorted({c["titulo"] for c in chunks if c["titulo"]}),
        # diagnóstico
        "debug": {
            "entradas_grafo": [
                {"nome": e["nome"], "score": round(e["score"], 3)}
                for e in r["entradas"]
            ],
            "chunks_base": [
                {"id": c["id"], "titulo": c["titulo"], "score": round(c["score"], 3)}
                for c in r["base"]
            ],
            "chunks_extra": [
                {"id": c["id"], "titulo": c["titulo"], "relevancia": c["relevancia"]}
                for c in r["extras"]
            ],
            "relacoes": [
                f"{f['origem']} -[{f['rel']}]-> {f['destino']}" for f in r["relacoes"]
            ],
        }
    }


if __name__ == "__main__":
    perguntas = [json.loads(l) for l in ENTRADA.open(encoding="utf-8") if l.strip()]

    with SAIDA.open("w", encoding="utf-8") as f:
        for q in perguntas:
            r = responder(q["pergunta"])
            f.write(json.dumps({**q, **r}, ensure_ascii=False) + "\n")

            d = r["debug"]
            print(
                f"{q['id']} | entradas={[e['nome'] for e in d['entradas_grafo']]} "
                f"base={len(d['chunks_base'])} extra={len(d['chunks_extra'])} "
                f"relacoes={len(d['relacoes'])}",
                flush=True,
            )
