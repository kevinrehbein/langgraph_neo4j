import json

from langchain_core.prompts import ChatPromptTemplate

from .prompts import VERIFIER_PROMPT
from .schemas import Review
from .state import AgentState
from .utils import get_llm


def verificador_node(state: AgentState) -> dict:
    """
    Avalia se o draft (rascunho) gerado pelo redator ou planejador é fiel
    às evidências do grafo. Se houver alucinação, reprova e manda refazer.
    """
    intent = state.get("intent", "qa")
    draft = state.get("draft", "")
    iteration_count = state.get("iteration_count", 0)

    # Resgata o contexto original (saída das ferramentas)
    tool_messages = [msg for msg in state["messages"] if msg.type == "tool"]
    texto_evidencias = "\n\n".join(
        [f"--- Origem: {msg.name} ---\n{msg.content}" for msg in tool_messages]
    )

    # O draft pode ser uma string (QA/Síntese) ou um JSON (ProjectPlan)
    if isinstance(draft, dict):
        draft_str = json.dumps(draft, ensure_ascii=False, indent=2)
    else:
        draft_str = str(draft)

    prompt_verificador = ChatPromptTemplate.from_messages(
        [("system", VERIFIER_PROMPT), ("user", "Rascunho a ser avaliado:\n\n{draft}")]
    )

    llm = get_llm()
    structured_llm = llm.with_structured_output(Review)
    chain = prompt_verificador | structured_llm

    review = chain.invoke(
        {"intent": intent, "contexto": texto_evidencias, "draft": draft_str}
    )

    nova_iteracao = iteration_count + 1
    estado_atualizado = {
        "iteration_count": nova_iteracao,
        "is_valid": review.is_valid,
    }

    print(f"[Verificador] Iteração {nova_iteracao} | Válido? {review.is_valid}")

    if not review.is_valid:
        print(f"[Verificador] Crítica: {review.feedback}")
        estado_atualizado["feedback"] = review.feedback
    else:
        estado_atualizado["final_response"] = draft
        estado_atualizado["feedback"] = None

    return estado_atualizado
