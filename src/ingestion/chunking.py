import hashlib
import json
from pathlib import Path

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

ROOT_PATH = Path(__file__).resolve().parents[2]
MARKDOWNS_PATH = ROOT_PATH / "data" / "markdowns"
METADATA_PATH = ROOT_PATH / "data" / "metadata.json"

headers = [("#", "h1"), ("##", "h2"), ("###", "h3")]
md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)
char_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200, chunk_overlap=150, separators=["\n\n", "\n", ". ", " ", ""]
)

metadados = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
dict_metadados = {artigo["id"]: artigo for artigo in metadados if "id" in artigo}

chunks = []
for _, filepath in enumerate(sorted(MARKDOWNS_PATH.rglob("*.md"))):
    id_artigo = filepath.stem
    artigo_metadados = dict_metadados.get(id_artigo, {})

    text_content = filepath.read_text(encoding="utf-8")
    secoes = md_splitter.split_text(text_content)

    for i, c in enumerate(char_splitter.split_documents(secoes)):
        c.metadata.update(artigo_metadados)
        raw_id = f"{id_artigo}_{i}"
        c.metadata["chunk_id"] = hashlib.md5(raw_id.encode("utf-8")).hexdigest()
        chunks.append(c)

print(f"Total de chunks gerados: {len(chunks)}")
