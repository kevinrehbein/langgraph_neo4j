import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# --- Diretórios ---
ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT_DIR / "data" / "outputs"

# --- Grafo (Neo4j) ---
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# --- Hiperparâmetros GraphRAG ---
TOP_K = 6
N_ENTIDADES = 5
SCORE_MIN = 0.5
TETO_GRAU = 350
K_GRAFO = 3
RELACOES_POR_ENTIDADE = 4
MAX_RELACOES = 20

# --- Limites do Grafo de Agentes ---
MAX_ITERATIONS = 3
