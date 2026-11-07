from langchain_core.prompts import ChatPromptTemplate
from prompts import SUPERVISOR_PROMPT

from .schemas import SupervisorDecision
from .state import AgentState
from .utils import get_llm


def supervisor_node(state: AgentState) -> dict:

    ultima_mensagem = state["messages"][-1].content
    iteracao_atual = state.get("iteration_count", 0)
    intent = state.get("intent", "")
    feedback = state.get("feedback", "")
    is_valid = state.get("is_valid", False)

    if iteracao_atual > 0:
        print(f"[Supervisor] ReAct Loop (Iteração {iteracao_atual})")

    prompt = ChatPromptTemplate.from_messages(
        [("system", SUPERVISOR_PROMPT), ("user", "{input}")]
    )

    llm = get_llm()

    structured_llm = llm.with_structured_output(SupervisorDecision)

    pipe = prompt | structured_llm

    ultima_mensagem = state["messages"][-1].content

    resultado = pipe.invoke(
        {
            "input": ultima_mensagem,
            "intent": intent,
            "feedback": feedback,
            "iteracao": iteracao_atual,
        }
    )

    print(f"[Supervisor] Intent: {resultado.intent}")
    print(f"[Supervisor] Nova Diretiva: {resultado.research_directive}")

    return {
        "intent": resultado.intent,
        "research_directive": resultado.research_directive,
        "is_valid": is_valid,
    }
