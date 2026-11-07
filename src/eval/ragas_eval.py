"""Avalia resultados_baseline.jsonl e resultados_grafo.jsonl com RAGAS.

Requisitos: pip install ragas
Cada linha dos .jsonl precisa ter: pergunta, resposta e contextos.
Sem resposta de referência: só métricas que não precisam de gabarito.
"""

import json
from pathlib import Path

import pandas as pd
import torch
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_huggingface import HuggingFaceEmbeddings
from ragas import EvaluationDataset, SingleTurnSample, evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import Faithfulness, ResponseRelevancy
from ragas.run_config import RunConfig

ROOT = Path(__file__).resolve().parent
ARQUIVOS = {
    "baseline": ROOT / "resultados_baseline.jsonl",
    "grafo": ROOT / "resultados_grafo.jsonl",
}

load_dotenv()

llm = init_chat_model(
    model="gemini-3.5-flash",
    model_provider="google_genai",
    temperature=0,
)
# Juiz: de preferência um modelo diferente do que gera as respostas (gemma).
juiz = LangchainLLMWrapper(langchain_llm=llm) # type: ignore

embeddings = LangchainEmbeddingsWrapper(
    HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
)


METRICAS = [
    Faithfulness(llm=juiz),  # resposta fiel ao contexto? (geração)
    ResponseRelevancy(llm=juiz, embeddings=embeddings),  # responde à pergunta?
]


def como_texto(resp) -> str:
    """O Gemma via google_genai pode devolver lista de blocos em vez de str."""
    if isinstance(resp, str):
        return resp
    return "".join(
        b["text"] if isinstance(b, dict) and "text" in b else str(b)
        for b in resp
        if not (isinstance(b, dict) and b.get("type") not in (None, "text"))
    )


def carregar(path: Path) -> EvaluationDataset:
    samples = []
    for linha in path.open(encoding="utf-8"):
        if not linha.strip():
            continue
        q = json.loads(linha)
        samples.append(
            SingleTurnSample(
                user_input=q["pergunta"],
                response=como_texto(q["resposta"]),
                retrieved_contexts=q["contextos"],
            )
        )
    return EvaluationDataset(samples=samples)


if __name__ == "__main__":
    medias = {}
    for nome, path in ARQUIVOS.items():
        print(f"== {nome} ==", flush=True)
        res = evaluate(
            dataset=carregar(path),
            metrics=METRICAS,
            run_config=RunConfig(max_workers=4, timeout=300),
        )
        df = res.to_pandas()
        df.to_csv(ROOT / f"ragas_{nome}.csv", index=False)
        medias[nome] = df.select_dtypes("number").mean()

    tabela = pd.DataFrame(medias).round(3)
    print(tabela)
    tabela.to_csv(ROOT / "ragas_comparacao.csv")
