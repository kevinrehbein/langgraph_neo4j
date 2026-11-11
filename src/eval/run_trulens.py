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

JUDGE_MODEL = "gemini/gemini-3.1-flash-lite"
APP_VERSION = "v1"  # mude a cada experimento para comparar no Leaderboard

PERGUNTAS = [
    "Quais artigos falam sobre mentoria para meninas?",
    "Faça um panorama sobre a inclusão de mulheres na computação.",
    "Crie um plano de projeto de oficina de programação para alunas do ensino médio.",
]

# Contextos já enviados ao juiz na pergunta atual (evita duplicatas inflando
# Groundedness quando várias ferramentas devolvem os mesmos chunks).
_vistos: set[str] = set()


def _novos(contextos: list[str]) -> list[str]:
    out = []
    for c in contextos:
        if c not in _vistos:
            _vistos.add(c)
            out.append(c)
    return out


# ------------------------------------------------------------------ RETRIEVAL
def _attrs_formatador(ret, exception, *args, **kwargs):
    """Cada chamada de formatar_fontes vira um span RETRIEVAL.

    Os contextos são montados direto de `itens` (sem re-parsear a string).
    """
    itens = args[0] if args else kwargs.get("itens", [])
    consulta = kwargs.get("consulta") or (args[1] if len(args) > 1 else "")
    contextos = _novos(
        [
            f"[FONTE: {i.get('titulo') or 'Sem título'} | {i.get('url') or ''}]\n"
            f"{i.get('corpo') or ''}".rstrip()
            for i in itens
        ]
    )
    return {
        SpanAttributes.RETRIEVAL.QUERY_TEXT: consulta,
        SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS: contextos,
    }


def _attrs_relacoes(ret, exception, *args, **kwargs):
    """Bloco de entidades/relações do GraphRAG como contexto para o juiz."""
    texto = ret.strip() if isinstance(ret, str) else ""
    vazio = not texto or texto.startswith("Nenhuma relação direta")
    return {
        SpanAttributes.RETRIEVAL.QUERY_TEXT: "relações do grafo",
        SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS: [] if vazio else _novos([texto]),
    }


# Instrumenta por fora: o código em src/ continua sem TruLens.
formatting.formatar_fontes = instrument(
    span_type=SpanAttributes.SpanType.RETRIEVAL,
    attributes=_attrs_formatador,
)(formatting.formatar_fontes)

HybridRetriever._formatar_relacoes = staticmethod(
    instrument(
        span_type=SpanAttributes.SpanType.RETRIEVAL,
        attributes=_attrs_relacoes,
    )(HybridRetriever._formatar_relacoes)
)


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
        _vistos.clear()
        state = self.graph.invoke(
            initial_state(pergunta),
            config={"recursion_limit": GRAPH_RECURSION_LIMIT},
        )
        return format_final_response(state.get("final_response"))


# MÉTRICAS
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

def main() -> None:

    validate_config()
    # Acorda o Space de embeddings fora dos registros (não distorce latência/notas).
    HybridRetriever.get_instance().embedding_model.embed_query("ping")

    session = TruSession()
    session.reset_database()

    app = MeninasDigitaisApp()
    tru = TruGraph(
        app,
        app_name="meninas-digitais",
        app_version=APP_VERSION,
        main_method=app.ask,
        feedbacks=[f_answer, f_context, f_ground],
    )

    with tru as recording:
        for pergunta in PERGUNTAS:
            app.ask(pergunta)
    record_ids = [record.record_id for record in recording.records]

    print("Aguardando a conclusão das avaliações...")
    resultados = tru.retrieve_feedback_results(record_ids=record_ids, timeout=300)
    print(resultados)

    run_dashboard(session)


if __name__ == "__main__":
    main()