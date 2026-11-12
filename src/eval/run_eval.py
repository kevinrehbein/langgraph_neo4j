import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # raiz = src/

from langchain.chat_models import init_chat_model
import pandas as pd
from langchain_ollama import ChatOllama
from ragas import EvaluationDataset, SingleTurnSample, evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import Faithfulness, ResponseRelevancy
from ragas.run_config import RunConfig

from agents.utils import message_text
from config import K_GRAFO, TOP_K, validate_config
from retrieval.hybrid import HybridRetriever

ROOT = Path(__file__).resolve().parent

PROMPT = """Você é um assistente do Programa Meninas Digitais.
Responda à pergunta usando APENAS o contexto abaixo. Se o contexto não contiver a
resposta, diga que não encontrou. Cite as fontes pelo título do artigo. Em perguntas
de lista, liste todos os itens encontrados, com nomes próprios de projetos, locais
e instituições.

{relacoes}

Trechos dos artigos:
{contexto}

Pergunta: {pergunta}
Resposta:"""

Q_SEMANTICO = """
MATCH (d:Document)
    SEARCH d IN (VECTOR INDEX chunk_embedding FOR $vec LIMIT $k)
    SCORE AS score
OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
RETURN d.id AS id, d.text AS texto, a.titulo AS titulo, a.url_artigo AS url
"""

validate_config()
r = HybridRetriever.get_instance()
emb = r.embedding_model

gen_llm = init_chat_model(
    model=os.getenv("GEN_MODEL", "gemma-4-26b-a4b-it"),
    model_provider=os.getenv("GEN_PROVIDER", "google_genai"),
    temperature=0,
    max_retries=5,
)

judge_llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "qwen3.5:9b"),
    reasoning=False,
    temperature=0,
    num_ctx=16384,
)


def semantico(vec):
    # mesmo orçamento de chunks do híbrido
    return r.graph.query(Q_SEMANTICO, {"vec": vec, "k": TOP_K + K_GRAFO}), ""


def hibrido(vec):
    base = r._chunks_entrada(vec)
    entradas = r._entidades_entrada(vec)
    eids = [e["eid"] for e in entradas]
    if not eids:
        return base, ""
    rels = r._relacoes_do_grafo(eids, vec)
    todos = set(eids)
    for rel in rels:
        todos.update((rel["eid_origem"], rel["eid_destino"]))
    extras = r._chunks_do_grafo(list(todos), [c["id"] for c in base], vec)
    return r._ordenar_por_score(base + extras), r._formatar_relacoes(entradas, rels)


def fmt(c):
    return f"[FONTE: {c.get('titulo') or 'Sem título'} | {c.get('url') or ''}]\n{c['texto']}"


def rodar(sistema, recuperar, perguntas):
    rows = []
    for q in perguntas:
        chunks, rels = recuperar(emb.embed_query(q["pergunta"]))
        prompt = PROMPT.format(
            relacoes=f"{rels}\n" if rels else "",
            contexto="\n\n".join(map(fmt, chunks)),
            pergunta=q["pergunta"],
        )
        resposta = message_text(gen_llm.invoke(prompt))
        print(q["id"], sistema, len(chunks), bool(rels), flush=True)
        rows.append(
            SingleTurnSample(
                user_input=q["pergunta"],
                response=resposta,
                retrieved_contexts=[fmt(c) for c in chunks] + ([rels] if rels else []),
            )
        )
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=3, help="nº de perguntas (0 = todas)")
    n = ap.parse_args().n

    todas = [
        json.loads(l)
        for l in (ROOT / "perguntas.jsonl").open(encoding="utf-8")
        if l.strip()
    ]
    perguntas = todas[:n] if n else todas

    emb.embed_query("ping")
    juiz, juiz_emb = LangchainLLMWrapper(judge_llm), LangchainEmbeddingsWrapper(emb) # pyright: ignore[reportArgumentType]
    metricas = [
        Faithfulness(llm=juiz),
        ResponseRelevancy(llm=juiz, embeddings=juiz_emb),
    ]

    res = {}
    for nome, fn in {"semantico": semantico, "hibrido": hibrido}.items():
        amostras = rodar(nome, fn, perguntas)
        df = evaluate(
            EvaluationDataset(samples=amostras),
            metrics=metricas,
            run_config=RunConfig(max_workers=1, timeout=600),
        ).to_pandas()
        df.insert(0, "id", [q["id"] for q in perguntas])
        res[nome] = df

    cols = list(res["semantico"].select_dtypes("number").columns)
    tabela = pd.concat({k: v.set_index("id")[cols] for k, v in res.items()}, axis=1).round(3)
    tabela.to_csv(ROOT / "ragas_por_pergunta.csv")
    for k, v in res.items():
        v.to_csv(ROOT / f"ragas_{k}.csv", index=False)  # inclui respostas para inspeção
    print("\nPor pergunta:\n", tabela)
    print("\nMédia:\n", pd.DataFrame({k: v[cols].mean() for k, v in res.items()}).round(3))
