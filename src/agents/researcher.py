from langchain_core.prompts import ChatPromptTemplate

from .prompts import RESEARCHER_PROMPT
from .state import AgentState
from .tools import RESEARCHER_TOOLS
from .utils import get_llm


def pesquisador_node(state: AgentState) -> dict:
    """Usa a intenção do usuário para decidir e executar as melhores ferramentas."""
    ultima_mensagem = state["messages"][-1].content
    intent = state.get("intent", "qa")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", RESEARCHER_PROMPT),
            ("user", "{input}"),
        ]
    )

    llm = get_llm()

    llm_with_tools = llm.bind_tools(RESEARCHER_TOOLS)
    chain = prompt | llm_with_tools

    resposta = chain.invoke({"intent": intent, "input": ultima_mensagem})

    return {"messages": [resposta]}
