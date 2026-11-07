from langchain_core.prompts import ChatPromptTemplate

from .prompts import PLANNER_PROMPT
from .schemas import ProjectPlan
from .state import AgentState
from .utils import get_llm


def planejador_node(state: AgentState) -> dict:
    """
    Agente responsável por estruturar um Projeto.
    Retorna OBRIGATORIAMENTE um JSON (dicionário) validado pelo Pydantic.
    """
    feedback = state.get("feedback")

    # Encontra a pergunta original
    mensagens_humanas = [m for m in state["messages"] if m.type == "human"]
    ultima_mensagem = mensagens_humanas[-1].content if mensagens_humanas else ""

    # Apenas contexto da última iteração
    tool_messages = []
    for msg in reversed(state["messages"]):
        if msg.type == "tool":
            tool_messages.append(msg)
            break

    context = "\n\n".join(
        [f"--- Origem: {msg.name} ---\n{msg.content}" for msg in tool_messages]
    )

    alerta_feedback = ""
    if feedback:
        alerta_feedback = (
            f"\n\n🚨 ALERTA DE REVISÃO DO AVALIADOR 🚨\n"
            f"Seu plano anterior falhou na validação acadêmica:\n"
            f"'{feedback}'\n"
            f"Reestruture o plano garantindo que este erro seja corrigido e embasado no contexto."
        )

    prompt = ChatPromptTemplate.from_messages(
        [("system", PLANNER_PROMPT), ("user", "Solicitação do usuário: {input}")]
    )

    llm = get_llm()

    structured_llm = llm.with_structured_output(ProjectPlan)

    chain = prompt | structured_llm

    projeto = chain.invoke(
        {"contexto": context, "alerta": alerta_feedback, "input": ultima_mensagem}
    )

    return {"draft": projeto.model_dump()}
