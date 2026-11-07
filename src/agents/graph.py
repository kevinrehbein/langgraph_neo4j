from typing import Literal

from langgraph.constants import END, START
from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from config import MAX_ITERATIONS

from .planner import planejador_node
from .researcher import pesquisador_node
from .state import AgentState
from .supervisor import supervisor_node
from .tools import RESEARCHER_TOOLS
from .verifier import verificador_node
from .writer import redator_node


def route_from_supervisor(state: AgentState) -> Literal["pesquisador", "__end__"]:
    intent = state.get("intent")
    if intent == "fora_dominio":
        return "__end__"
    return "pesquisador"  # qa, sintese e plano vão para busca de contexto primeiro


def route_from_pesquisador(state: AgentState):

    destino = tools_condition(state)

    if destino == "tools":
        return "pesquisador_tools"

    return "planejador" if state.get("intent") == "plano" else "redator"


def route_after_pesquisador(state: AgentState):

    intent = state.get("intent")
    return "planejador" if intent == "plano" else "redator"


def route_from_verifier(state: AgentState):

    if state["is_valid"]:
        return END

    if state["iteration_count"] >= MAX_ITERATIONS:
        print("[Alerta] Limite de iterações atingido. Encerrando com a resposta atual.")
        return END  # Desiste e entrega o que tem para não gastar todos os tokens do universo

    return "supervisor"


def graph_builder() -> CompiledStateGraph:
    builder = StateGraph(AgentState)

    pesquisador_tool_node = ToolNode(RESEARCHER_TOOLS)

    builder.add_node("supervisor", supervisor_node)
    builder.add_node("pesquisador", pesquisador_node)
    builder.add_node("pesquisador_tools", pesquisador_tool_node)
    builder.add_node("redator", redator_node)
    builder.add_node("planejador", planejador_node)
    builder.add_node("verificador", verificador_node)

    builder.add_edge(START, "supervisor")

    builder.add_conditional_edges(
        "supervisor", route_from_supervisor, ["pesquisador", END]
    )

    builder.add_conditional_edges(
        "pesquisador",
        route_from_pesquisador,
        ["pesquisador_tools", "planejador", "redator"],
    )

    builder.add_conditional_edges(
        "pesquisador_tools",
        route_after_pesquisador,
        ["planejador", "redator"],
    )

    builder.add_edge("redator", "verificador")
    builder.add_edge("planejador", "verificador")

    builder.add_conditional_edges(
        "verificador", route_from_verifier, [END, "supervisor"]
    )

    return builder.compile()
