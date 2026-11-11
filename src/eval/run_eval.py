"""Comparação RAG vetorial x GraphRAG (expansão por grafo) com RAGAS.

Arquivo autocontido: não importa nada do projeto. Tudo que importa para a prova
(hiperparâmetros, queries Cypher, prompt, gerador, juiz) está aqui.

Uso:
    python run_eval.py             # gera respostas + avalia
    python run_eval.py --skip-gen  # só reavalia resultados_*.jsonl já gerados

Variáveis de ambiente: NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD, GOOGLE_API_KEY.

Justiça da comparação:
  * mesmo embedding da pergunta (calculado uma vez);
  * mesmo LLM gerador (temperatura 0) e mesmo prompt;
  * mesmo orçamento de chunks: baseline = TOP_K + K_GRAFO chunks vetoriais;
    GraphRAG = TOP_K chunks vetoriais + até K_GRAFO chunks vindos do grafo
    (os TOP_K primeiros são idênticos nos dois sistemas);
  * a única diferença no contexto é o bloco de relações do grafo;
  * juiz (RAGAS) diferente do gerador.
"""

import argparse
import json
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph
from ragas import EvaluationDataset, SingleTurnSample, evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import (
    FactualCorrectness,
    Faithfulness,
    LLMContextRecall,
    ResponseRelevancy,
)
from ragas.run_config import RunConfig
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

# ------------------------------------------------------------ hiperparâmetros
TOP_K = 5  # chunks vetoriais (entrada) - igual ao config.py de produção
N_ENTIDADES = 5  # entidades de entrada no grafo
SCORE_MIN = 0.7  # similaridade mínima da entidade de entrada
TETO_GRAU = 350  # entidades "hub" (grau acima disso) não são expandidas
K_GRAFO = 5  # chunks extras vindos do grafo
RELACOES_POR_ENTIDADE = 4
MAX_RELACOES = 20
CHUNK_NUM = TOP_K + K_GRAFO  # chunks que o baseline recebe

ROOT = Path(__file__).resolve().parent
PERGUNTAS = ROOT / "perguntas.jsonl"
SISTEMAS = ("baseline", "grafo")

GEN_MODEL = "gemma-4-26b-a4b-it"
JUDGE_MODEL = "gemma-4-31b-it"  # diferente do gerador

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

# ----------------------------------------------------------------- recursos
print("⏳ 1. Inicializando modelos LLM...", flush=True)
llm = init_chat_model(model=GEN_MODEL, model_provider="google_genai", temperature=0)
judge_llm = init_chat_model(
    model=JUDGE_MODEL, model_provider="google_genai", temperature=0
)

print("⏳ 2. Inicializando modelo de Embeddings (bge-m3)...", flush=True)
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    encode_kwargs={"normalize_embeddings": True, "batch_size": 16},
)

print("⏳ 3. Conectando ao Neo4j...", flush=True)
graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)
print("✅ Tudo carregado! Iniciando processamento...", flush=True)
# ------------------------------------------------------------------- queries
Q_CHUNKS = """
MATCH (d:Document)
    SEARCH d IN (VECTOR INDEX chunk_embedding FOR $vec LIMIT $k)
    SCORE AS score
OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
RETURN d.id AS id, d.text AS texto, score, a.titulo AS titulo, a.url_artigo AS url
"""

Q_ENTIDADES = """
MATCH (e:__Entity__)
    SEARCH e IN (VECTOR INDEX entity_embedding FOR $vec LIMIT $n)
    SCORE AS score
WHERE score >= $min AND e.grau <= $teto
RETURN elementId(e) AS eid, e.id AS nome,
       coalesce(e.descricao, '') AS descricao, score
"""

Q_RELACOES = """
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
RETURN startNode(r).id AS origem, type(r) AS rel, endNode(r).id AS destino,
       coalesce(startNode(r).descricao, '') AS desc_origem,
       coalesce(endNode(r).descricao, '') AS desc_destino,
       elementId(startNode(r)) AS eid_origem,
       elementId(endNode(r)) AS eid_destino, sim
"""

Q_CHUNKS_DO_GRAFO = """
UNWIND $ents AS eid
MATCH (x:__Entity__) WHERE elementId(x) = eid
MATCH (d:Document)-[:MENTIONS]->(x)
    WHERE NOT d.id IN $excluir
WITH d, sum(1.0 / log(1 + CASE WHEN coalesce(x.n_mentions, 0) < 1
                               THEN 1 ELSE x.n_mentions END)) AS relevancia
ORDER BY relevancia DESC
LIMIT $k
OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
RETURN d.id AS id, d.text AS texto, relevancia, a.titulo AS titulo, a.url_artigo AS url
"""


# ------------------------------------------------------------- recuperação
def recuperar_baseline(vec: list[float]) -> tuple[list[dict], str]:
    """RAG vetorial puro: só os chunks mais próximos da pergunta."""
    chunks = graph.query(Q_CHUNKS, {"vec": vec, "k": CHUNK_NUM})
    return chunks, ""


def recuperar_grafo(vec: list[float]) -> tuple[list[dict], str]:
    """GraphRAG: chunks vetoriais + expansão por entidades/relações do grafo."""
    base = graph.query(Q_CHUNKS, {"vec": vec, "k": TOP_K})
    entradas = graph.query(
        Q_ENTIDADES, {"vec": vec, "n": N_ENTIDADES, "min": SCORE_MIN, "teto": TETO_GRAU}
    )
    eids = [e["eid"] for e in entradas]
    if not eids:
        return base, ""

    relacoes = graph.query(
        Q_RELACOES,
        {
            "eids": eids,
            "vec": vec,
            "teto": TETO_GRAU,
            "por_entidade": RELACOES_POR_ENTIDADE,
            "max": MAX_RELACOES,
        },
    )
    ents = set(eids)
    for r in relacoes:
        ents.update((r["eid_origem"], r["eid_destino"]))
    extras = graph.query(
        Q_CHUNKS_DO_GRAFO,
        {"ents": list(ents), "excluir": [c["id"] for c in base], "k": K_GRAFO},
    )

    if not relacoes:
        return base + extras, ""

    desc = {e["nome"]: e["descricao"] for e in entradas if e["descricao"]}
    for r in relacoes:
        if r["desc_origem"]:
            desc.setdefault(r["origem"], r["desc_origem"])
        if r["desc_destino"]:
            desc.setdefault(r["destino"], r["desc_destino"])
    bloco_entidades = "\n".join(f"- {n}: {d}" for n, d in desc.items())
    bloco_relacoes = "\n".join(
        f"{r['origem']} -[{r['rel']}]-> {r['destino']}" for r in relacoes
    )
    texto = f"Entidades:\n{bloco_entidades}\n\nRelações:\n{bloco_relacoes}"
    return base + extras, texto


# ----------------------------------------------------------------- geração
def fmt_chunk(c: dict) -> str:
    return f"[FONTE: {c.get('titulo') or 'Sem título'} | {c.get('url') or ''}]\n{c['texto']}"


def texto_da_resposta(msg) -> str:
    """Alguns provedores devolvem lista de blocos (inclusive 'thinking')."""
    if isinstance(msg.content, str):
        return msg.content
    return "".join(
        b if isinstance(b, str) else b.get("text", "")
        for b in msg.content
        if isinstance(b, str) or b.get("type") in (None, "text")
    )


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=30, max=120))
def responder(pergunta: str, chunks: list[dict], relacoes_txt: str) -> str:
    bloco = f"Relações do grafo:\n{relacoes_txt}\n\n" if relacoes_txt else ""
    prompt = PROMPT.format(
        relacoes=bloco,
        contexto="\n\n".join(fmt_chunk(c) for c in chunks),
        pergunta=pergunta,
    )
    return texto_da_resposta(llm.invoke(prompt)).strip()


def gerar() -> None:
    perguntas = [json.loads(l) for l in PERGUNTAS.open(encoding="utf-8") if l.strip()]
    saidas = {
        s: (ROOT / f"resultados_{s}.jsonl").open("w", encoding="utf-8")
        for s in SISTEMAS
    }
    try:
        for q in perguntas:
            vec = embedding_model.embed_query(q["pergunta"])  # compartilhado
            recuperadores = {"baseline": recuperar_baseline, "grafo": recuperar_grafo}
            for sistema, recuperar in recuperadores.items():
                chunks, relacoes_txt = recuperar(vec)
                contextos = [fmt_chunk(c) for c in chunks]
                if relacoes_txt:
                    contextos.append(relacoes_txt)
                rec = {
                    **q,
                    "resposta": responder(q["pergunta"], chunks, relacoes_txt),
                    "contextos": contextos,
                    "n_chunks": len(chunks),
                    "fontes": sorted({c["titulo"] for c in chunks if c.get("titulo")}),
                }
                saidas[sistema].write(json.dumps(rec, ensure_ascii=False) + "\n")
                saidas[sistema].flush()
                print(
                    f"{q['id']} | {sistema:8s} | chunks={len(chunks)} "
                    f"| relações={'sim' if relacoes_txt else 'não'}",
                    flush=True,
                )
    finally:
        for f in saidas.values():
            f.close()


# --------------------------------------------------------------- avaliação
def dataset(rows: list[dict]) -> EvaluationDataset:
    return EvaluationDataset(
        samples=[
            SingleTurnSample(
                user_input=r["pergunta"],
                response=r["resposta"],
                retrieved_contexts=r["contextos"],
                reference=r.get("referencia") or None,
            )
            for r in rows
        ]
    )


def avaliar_sistema(rows: list[dict], juiz, embeddings) -> pd.DataFrame:
    cfg = RunConfig(max_workers=1, timeout=300, max_retries=10)

    # Sem gabarito: todas as perguntas.
    df = evaluate(
        dataset=dataset(rows),
        metrics=[
            Faithfulness(llm=juiz),
            ResponseRelevancy(llm=juiz, embeddings=embeddings),
        ],
        run_config=cfg,
    ).to_pandas()
    df["id"] = [r["id"] for r in rows]
    df["tipo"] = [r.get("tipo", "") for r in rows]

    # Com gabarito: só perguntas com `referencia` preenchida.
    com_ref = [r for r in rows if r.get("referencia")]
    if com_ref:
        ref = evaluate(
            dataset=dataset(com_ref),
            metrics=[LLMContextRecall(llm=juiz), FactualCorrectness(llm=juiz)],
            run_config=cfg,
        ).to_pandas()
        nums = ref.select_dtypes("number").copy()
        nums["id"] = [r["id"] for r in com_ref]
        df = df.merge(nums, on="id", how="left")
    return df


def avaliar() -> None:
    juiz = LangchainLLMWrapper(judge_llm)
    embeddings = LangchainEmbeddingsWrapper(embedding_model)

    frames = {}
    for sistema in SISTEMAS:
        path = ROOT / f"resultados_{sistema}.jsonl"
        rows = [json.loads(l) for l in path.open(encoding="utf-8") if l.strip()]
        print(f"== avaliando {sistema} ({len(rows)} perguntas) ==", flush=True)
        frames[sistema] = avaliar_sistema(rows, juiz, embeddings)
        frames[sistema].to_csv(ROOT / f"ragas_{sistema}.csv", index=False)

    metricas = list(frames["baseline"].select_dtypes("number").columns)
    media = pd.DataFrame({s: f[metricas].mean() for s, f in frames.items()})
    media["delta (grafo - baseline)"] = media["grafo"] - media["baseline"]
    media = media.round(3)
    media.to_csv(ROOT / "ragas_comparacao.csv")
    print("\nMédia geral:\n", media)

    por_tipo = pd.concat(
        {s: f.groupby("tipo")[metricas].mean() for s, f in frames.items()}, axis=1
    ).round(3)

    por_tipo.to_csv(ROOT / "ragas_por_tipo.csv")
    print("\nPor tipo de pergunta:\n", por_tipo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-gen", action="store_true", help="reusa resultados_*.jsonl")
    args = ap.parse_args()

    if not args.skip_gen:
        gerar()
    avaliar()
