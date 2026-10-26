"""Converte os PDFs de ``data/raw_pdfs`` em Markdown para uso em GraphRAG.

A estrutura de diretórios é preservada e apenas o conteúdo textual é mantido
(sem imagens), gerando arquivos adequados para chunking e extração de entidades.
"""

from __future__ import annotations

import re
from pathlib import Path

import pymupdf4llm

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw_pdfs"
OUTPUT_DIR = ROOT / "data" / "markdowns"

_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)", re.DOTALL)
_SUP_SUB_RE = re.compile(r"<su[pb]>.*?</su[pb]>", re.DOTALL | re.IGNORECASE)
_PICTURE_TEXT_RE = re.compile(
    r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->",
    re.DOTALL | re.IGNORECASE,
)
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
_ITALIC_RE = re.compile(
    r"(?<![\w_])_(?!_)(.+?)(?<!_)_(?![\w_])",
    re.DOTALL,
)
_REFERENCES_RE = re.compile(
    r"^#{1,6}\s+"
    r"(?:refer[êe]ncias?(?:\s+bibliogr[áa]ficas?)?|references?|bibliografia)"
    r"\s*$.*",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
_MULTI_SPACE_RE = re.compile(r"[ \t]{2,}")
_SPACE_BEFORE_PUNCT_RE = re.compile(r"[ \t]+([,.;:!?])")
_TRAILING_SPACE_RE = re.compile(r"[ \t]+$", re.MULTILINE)
_MULTI_BLANK_RE = re.compile(r"\n{3,}")
_DEHYPHENATE_RE = re.compile(r"([^\W\d_])-\s*\n\s*([^\W\d_])")
_BR_HYPHEN_RE = re.compile(r"(?<=[^\W\d_])-<br\s*/?>", re.IGNORECASE)
_BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)

# Alguns PDFs usam fontes Type1 cujo texto extraído traz o acento separado da
# letra (ex.: "Computac¸˜ao"). Estes ajustes recuperam os caracteres corretos.
_ACCENT_FIXES = {
    "´a": "á", "´e": "é", "´i": "í", "´o": "ó", "´u": "ú",
    "´A": "Á", "´E": "É", "´I": "Í", "´O": "Ó", "´U": "Ú",
    "`a": "à", "`e": "è", "`A": "À",
    "˜a": "ã", "˜o": "õ", "˜n": "ñ", "˜A": "Ã", "˜O": "Õ", "˜N": "Ñ",
    "ˆa": "â", "ˆe": "ê", "ˆo": "ô", "ˆA": "Â", "ˆE": "Ê", "ˆO": "Ô",
    "¸c": "ç", "¸C": "Ç", "c¸": "ç", "C¸": "Ç",
    "¨a": "ä", "¨o": "ö", "¨u": "ü",
    "´ı": "í", "`ı": "ì",
}


def _fix_accents(text: str) -> str:
    for source, target in _ACCENT_FIXES.items():
        text = text.replace(source, target)
    return text.replace("ı", "i")


def clean_markdown(text: str) -> str:
    """Remove imagens, referências e marcações de formatação do Markdown."""
    text = _fix_accents(text)
    text = _PICTURE_TEXT_RE.sub("", text)
    text = _IMAGE_RE.sub("", text)
    text = _SUP_SUB_RE.sub("", text)
    text = _DEHYPHENATE_RE.sub(r"\1\2", text)
    text = _BR_HYPHEN_RE.sub("", text)
    text = _BR_RE.sub(" ", text)
    text = _BOLD_RE.sub(r"\1", text)
    text = _REFERENCES_RE.sub("", text)
    text = _ITALIC_RE.sub(r"\1", text)
    text = _MULTI_SPACE_RE.sub(" ", text)
    text = _SPACE_BEFORE_PUNCT_RE.sub(r"\1", text)
    text = _TRAILING_SPACE_RE.sub("", text)
    text = _MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip() + "\n"


def convert_pdf(
    pdf_path: Path,
    output_dir: Path = OUTPUT_DIR,
    raw_dir: Path = RAW_DIR,
) -> Path:
    """Converte um PDF e retorna o caminho do Markdown gerado."""
    pdf_path = pdf_path.resolve()
    raw_dir = raw_dir.resolve()
    relative_path = pdf_path.relative_to(raw_dir).with_suffix(".md")
    destination = output_dir.resolve() / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)

    markdown = pymupdf4llm.to_markdown(
        str(pdf_path),
        header=False,
        footer=False,
        use_ocr=False,
        write_images=False,
        ignore_code=True,
    )
    destination.write_text(clean_markdown(markdown), encoding="utf-8")
    return destination


def convert_all(
    raw_dir: Path = RAW_DIR,
    output_dir: Path = OUTPUT_DIR,
) -> None:
    """Converte todos os PDFs encontrados, preservando a estrutura de pastas."""
    raw_dir = raw_dir.resolve()
    output_dir = output_dir.resolve()
    pdfs = sorted(raw_dir.rglob("*.pdf"))
    if not pdfs:
        print(f"Nenhum PDF encontrado em {raw_dir}")
        return

    failures: list[tuple[Path, Exception]] = []
    for index, pdf_path in enumerate(pdfs, start=1):
        try:
            destination = convert_pdf(pdf_path, output_dir, raw_dir)
        except Exception as error:  # noqa: BLE001
            failures.append((pdf_path, error))
            print(f"[{index}/{len(pdfs)}] ERRO: {pdf_path.name}: {error}")
            continue

        print(f"[{index}/{len(pdfs)}] {destination.relative_to(output_dir.parent)}")

    if failures:
        raise SystemExit(f"{len(failures)} PDF(s) não puderam ser convertidos.")


if __name__ == "__main__":
    convert_all()
