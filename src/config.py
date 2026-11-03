from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_neo4j import Neo4jGraph
import os

load_dotenv()
"""
llm = init_chat_model(
    model="qwen3.5:9b",
    model_provider="ollama",
)
"""


# llm_backup1 = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")
# llm_backup2 = init_chat_model("openai/gpt-oss-120b", model_provider="groq")

# llm = llm_principal.with_fallbacks([llm_backup1, llm_backup2])
