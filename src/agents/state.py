import operator
from collections.abc import Sequence
from typing import Annotated, Any, TypedDict

from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    intent: str | None
    research_directive: str | None
    draft: str | None
    final_response: Any
    iteration_count: int
    is_valid: bool
    feedback: str | None
