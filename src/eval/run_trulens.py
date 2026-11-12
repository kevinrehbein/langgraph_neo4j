import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # raiz = src/

from litellm import api_base
import numpy as np
from trulens.apps.app import TruApp
from trulens.core import Metric, Selector, TruSession
from trulens.core.otel.instrument import instrument
from trulens.dashboard import run_dashboard
from trulens.otel.semconv.trace import SpanAttributes
from langchain_ollama import ChatOllama
from trulens.providers.langchain import Langchain

from agents.graph import graph_builder
from agents.state import initial_state
from agents.utils import format_final_response
from config import GRAPH_RECURSION_LIMIT, validate_config
from retrieval.hybrid import HybridRetriever

JUDGE_MODEL = "ollama/qwen3.5:9b"
OLLAMA_URL = "http://localhost:11434"

APP_VERSION = "v1"  # mude a cada experimento para comparar no Leaderboard

PERGUNTAS = [
    "Quais artigos falam sobre mentoria para meninas?",
    "Faça um panorama sobre a inclusão de mulheres na computação.",
    "Crie um plano de projeto de oficina de programação para alunas do ensino médio.",
]

RETRIEVAL = SpanAttributes.SpanType.RETRIEVAL
QUERY = SpanAttributes.RETRIEVAL.QUERY_TEXT
CONTEXTS = SpanAttributes.RETRIEVAL.RETRIEVED_CONTEXTS


# ------------------------------------------------------------------ RETRIEVAL
def _attrs_chunks(ret, exception, *args, **kwargs) -> dict:
    """Cada trecho de artigo recuperado vira um contexto avaliado."""
    chunks = args[0] if args else kwargs.get("chunks", [])
    consulta = kwargs.get("consulta") or (args[1] if len(args) > 1 else "")
    contexts = [
        f"[FONTE: {c.get('titulo') or 'Sem título'} | {c.get('url') or ''}]\n{c['texto']}"
        for c in chunks
    ]
    return {QUERY: consulta, CONTEXTS: list(dict.fromkeys(contexts))}

def _attrs_relations(ret, exception, *args, **kwargs) -> dict:
    """Bloco de entidades/relações do GraphRAG como um único contexto."""
    return {QUERY: "relações do grafo", CONTEXTS: [ret] if ret else []}


def instrument_retriever() -> None:
    """Instrumenta o retriever por fora; src/ continua sem TruLens."""
    HybridRetriever._formatar_chunks = staticmethod(
        instrument(span_type=RETRIEVAL, attributes=_attrs_chunks)(
            HybridRetriever._formatar_chunks
        )
    )
    HybridRetriever._formatar_relacoes = staticmethod(
        instrument(span_type=RETRIEVAL, attributes=_attrs_relations)(
            HybridRetriever._formatar_relacoes
        )
    )


# ------------------------------------------------------------------------ APP
class MeninasDigitaisApp:
    """Adaptador: traduz o estado do grafo em (pergunta: str) -> (resposta: str)."""

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
judge = Langchain(
    chain=ChatOllama(
        model="qwen3.5:9b",
        reasoning=False,
        temperature=0,
        num_ctx=16384,
        base_url="http://localhost:11434",
    )
)

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
            span_type=RETRIEVAL,
            span_attribute=CONTEXTS,
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
            span_type=RETRIEVAL,
            span_attribute=CONTEXTS,
            collect_list=True,  # todos os contextos juntos
        ),
        "statement": Selector.select_record_output(),
    },
)


# ----------------------------------------------------------------------- MAIN
def main() -> None:
    validate_config()
    # Acorda o Space de embeddings fora dos registros (não distorce latência/notas).
    HybridRetriever.get_instance().embedding_model.embed_query("ping")

    session = TruSession()  # sem reset_database(): preserva o histórico entre versões
    instrument_retriever()

    app = MeninasDigitaisApp()
    tru = TruApp(
        app,
        app_name="meninas-digitais",
        app_version=APP_VERSION,
        main_method=app.ask,
        feedbacks=[f_answer, f_context, f_ground],
    )

    with tru as recording:
        for pergunta in PERGUNTAS:
            app.ask(pergunta)

    ids = [r.record_id for r in recording.records]
    print("Aguardando a conclusão das avaliações...")
    print(tru.retrieve_feedback_results(record_ids=ids, timeout=300))

    run_dashboard(session)


if __name__ == "__main__":
    main()
