import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings
from retrieval.embeddings import SpaceEmbeddings
from config import EMBEDDING_SPACE

q = "mentoria para meninas na computação"
local = HuggingFaceEmbeddings(
    model_name= "BAAI/bge-m3",
    encode_kwargs={"normalize_embeddings": True, "batch_size": 16},
).embed_query(q)
remoto = SpaceEmbeddings(EMBEDDING_SPACE).embed_query(q) # type: ignore
print(np.dot(local, remoto))