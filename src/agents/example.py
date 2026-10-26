# noqa: CPY001
from collections.abc import Sequence
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, START, StateGraph, add_messages
from rich import print
from rich.markdown import Markdown

load_dotenv()
llm = init_chat_model(model="gemma-4-31b-it", model_provider="google_genai")


# 1 - Crio o State
class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


# 2 - Crios os nodes
def node_a(state: State) -> State:
    llm_result = llm.invoke(state["messages"])
    return {"messages": [llm_result]}


# Crio o StateGraph (Graph Builder)
builder = StateGraph(
    State, context_schema=None, input_schema=State, output_schema=State
)

# Adcionar nodes e arestas ao grafo
builder.add_node("node_A", node_a)
builder.add_edge(START, "node_A")
builder.add_edge("node_A", END)

# Compilar grafo
graph = builder.compile()

if __name__ == "__main__":
    current_messages: Sequence[BaseMessage] = []

    while True:
        user_input = input("Digite sua mensagem aqui: ")
        print(Markdown("---"))

        if user_input.lower() in ["q", "quit"]:
            print("Bye!")
            print(Markdown("---"))
            break

        human_message = HumanMessage(user_input)
        current_messages = [*current_messages, human_message]

        result = graph.invoke({"messages": current_messages})
        current_messages = result["messages"]

        print(Markdown(str(result["messages"][-1].content)))
        print(Markdown("---"))
