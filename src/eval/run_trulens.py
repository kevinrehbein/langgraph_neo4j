"""Avaliação com TruLens: Answer Relevance, Context Relevance e Groundedness.

Execute na raiz do projeto:  uv run src/eval/run_trulens.py

Pré-requisito: todas as ferramentas de busca devolvem a evidência via
`retrieval.formatting.formatar_fontes` (formato único `[FONTE: título | url]`).
Este script instrumenta essa função, que vira o único span de RETRIEVAL.
"""

import os

os.environ["TRULENS_OTEL_TRACING"] = "1"  # tem que vir ANTES de importar o trulens

import sys

sys.path.insert(0, "src")

import numpy as np
from trulens.apps.langgraph import TruGraph
from trulens.core import Metric, Selector, TruSession
from trulens.core.otel.instrument import instrument
from trulens.dashboard import run_dashboard
from trulens.otel.semconv.trace import SpanAttributes
from trulens.providers.litellm import LiteLLM

from agents.graph import graph_builder
from agents.state import initial_state
from agents.utils import format_final_response
from config import GRAPH_RECURSION_LIMIT, validate_config
from retrieval import formatting
from retrieval.hybrid import HybridRetriever

JUDGE_MODEL = "gemini/gemini-3.1-flash-lite"  # juiz diferente dos modelos da LLM_CHAIN
APP_VERSION = "v1"  # mude a cada experimento para comparar no Leaderboard

PERGUNTAS = [
    "Quais artigos falam sobre mentoria para meninas?",
    "Faça um panorama sobre a inclusão de mulheres na computação.",
    "Crie um plano de projeto de oficina de programação para alunas do ensino médio.",
]


# ------------------------------------------------------------------ RETRIEVAL
def _attrs_formatador(ret, exception, *args, **kwargs):
    """Cada chamada de formatar_fontes vira um span RETRIEVAL.

    A saída é um texto com blocos `[FONTE: título | url]`; aqui cada bloco
    vira um contexto separado para o juiz.
    """
    consulta = kwargs.get("consulta") or (args[1] if len(args) > 1 else "")
    texto = ret if isinstance(ret, str) else ""
    contextos = ["[FONTE: " + p.strip() for p in texto.split("[FONTE: ") if p.strip()]
    return {
        SpanAttributes.RETRIEVAL.QUERY_TEXT: consulta,
        SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS: contextos,
    }


# Instrumenta por fora: o código em src/ continua sem TruLens. Funciona porque
# hybrid.py e tools.py chamam `formatting.formatar_fontes(...)` pelo módulo.
formatting.formatar_fontes = instrument(
    span_type=SpanAttributes.SpanType.RETRIEVAL,
    attributes=_attrs_formatador,
)(formatting.formatar_fontes)


class MeninasDigitaisApp:
    def __init__(self) -> None:
        self.graph = graph_builder()

    @instrument(
        span_type=SpanAttributes.SpanType.RECORD_ROOT,
        attributes={
            SpanAttributes.RECORD_ROOT.INPUT: "pergunta",
            SpanAttributes.RECORD_ROOT.OUTPUT: "return",
        },
    )
    def ask(self, pergunta: str) -> str:
        state = self.graph.invoke(
            initial_state(pergunta),
            config={"recursion_limit": GRAPH_RECURSION_LIMIT},
        )
        return format_final_response(state.get("final_response"))


# -------------------------------------------------------------------- MÉTRICAS
judge = LiteLLM(model_engine=JUDGE_MODEL)

f_answer = Metric(
    implementation=judge.relevance_with_cot_reasons,
    name="Answer Relevance",
    selectors={
        "prompt": Selector.select_record_input(),
        "response": Selector.select_record_output(),
    },
)

f_context = Metric(
    implementation=judge.context_relevance_with_cot_reasons,
    name="Context Relevance",
    selectors={
        "question": Selector.select_record_input(),
        "context": Selector(
            span_type=SpanAttributes.SpanType.RETRIEVAL,
            span_attribute=SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS,
            collect_list=False,  # um score por contexto
        ),
    },
    agg=np.mean,
)

f_ground = Metric(
    implementation=judge.groundedness_measure_with_cot_reasons,
    name="Groundedness",
    selectors={
        "source": Selector(
            span_type=SpanAttributes.SpanType.RETRIEVAL,
            span_attribute=SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS,
            collect_list=True,  # todos os contextos de todas as ferramentas juntos
        ),
        "statement": Selector.select_record_output(),
    },
)


# ------------------------------------------------------------------------ RODAR
def main() -> None:
    validate_config()
    # Acorda o Space de embeddings fora dos registros (não distorce latência/notas).
    HybridRetriever.get_instance().embedding_model.embed_query("ping")

    session = TruSession()
    session.reset_database()  # descomente SÓ numa execução para apagar o histórico

    app = MeninasDigitaisApp()
    tru = TruGraph(
        app,
        app_name="meninas-digitais",
        app_version=APP_VERSION,
        main_method=app.ask,
        feedbacks=[f_answer, f_context, f_ground],
    )

    with tru:
        for pergunta in PERGUNTAS:
            app.ask(pergunta)

    run_dashboard(session)
    # Mantém o processo vivo: o juiz roda em segundo plano e precisa terminar.
    input("Dashboard no ar. Espere as notas aparecerem e aperte Enter para encerrar...\n")


if __name__ == "__main__":
    main()