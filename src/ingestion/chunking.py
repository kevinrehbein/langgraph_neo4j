import hashlib
import json
from pathlib import Path

from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

ROOT_PATH = Path(__file__).resolve().parents[2]
MARKDOWNS_PATH = ROOT_PATH / "data" / "markdowns"
METADATA_PATH = ROOT_PATH / "data" / "metadata.json"

metadados = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
dict_metadados = {artigo["id"]: artigo for artigo in metadados if "id" in artigo}

splitter = RecursiveCharacterTextSplitter.from_language(
    Language.MARKDOWN, chunk_size=3000, chunk_overlap=0
)

chunks = []
for filepath in sorted(MARKDOWNS_PATH.rglob("*.md")):
    id_artigo = filepath.stem
    artigo_metadados = dict_metadados.get(id_artigo, {})
    text = filepath.read_text(encoding="utf-8")

    for i, c in enumerate(splitter.create_documents([text])):
        c.metadata.update(artigo_metadados)
        c.metadata["artigo_id"] = c.metadata.pop("id", id_artigo)
        c.metadata["id"] = hashlib.md5(f"{id_artigo}_{i}".encode()).hexdigest()
        chunks.append(c)

print(f"Total de chunks gerados: {len(chunks)}")
