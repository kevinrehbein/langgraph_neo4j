from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()
"""
llm = init_chat_model(
    model="qwen3.5:9b",
    model_provider="ollama",
)
"""

llm_graph_transformer = ChatOllama(
    model="qwen3:8b",
    reasoning=False,
    temperature=0,
    num_ctx=8192,
)
# llm_backup1 = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")
# llm_backup2 = init_chat_model("openai/gpt-oss-120b", model_provider="groq")

# llm = llm_principal.with_fallbacks([llm_backup1, llm_backup2])
