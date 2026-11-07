from langchain_core.prompts import ChatPromptTemplate

from .prompts import WRITER_PROMPT
from .state import AgentState
from .utils import get_llm


def redator_node(state: AgentState) -> dict:
    """
    Agente responsável por responder perguntas diretas (QA) ou criar sínteses acadêmicas.
    Usa os dados coletados pelas ferramentas e reescreve caso haja feedback do Verificador.
    """
    intent = state.get("intent", "qa")
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

    instrucao = (
        "Escreva uma resposta curta e direta respondendo exatamente o que foi perguntado."
        if intent == "qa"
        else "Escreva uma síntese acadêmica detalhada, separada por seções (Markdown) e cite as fontes."
    )

    if feedback:
        instrucao += (
            f"\n\n🚨 ALERTA DE REVISÃO DO AVALIADOR 🚨\n"
            f"Sua tentativa anterior foi REJEITADA pelo seguinte motivo:\n"
            f"'{feedback}'\n"
            f"CORRIJA ESTE ERRO AGORA. Baseie-se apenas nas evidências acima."
        )

    prompt = ChatPromptTemplate.from_messages(
        [("system", WRITER_PROMPT), ("user", "Pergunta do usuário: {input}")]
    )

    llm = get_llm(temperature=0.3)
    chain = prompt | llm

    resposta = chain.invoke(
        {"contexto": context, "instrucao": instrucao, "input": ultima_mensagem}
    )

    return {"draft": resposta.content}
