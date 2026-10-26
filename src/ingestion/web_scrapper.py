import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

WEB_SCRAP = True
BAIXAR = True
RAIZ = Path(__file__).resolve().parents[2]
OUTPUT_DIR = RAIZ / "data" / "raw_pdfs"
METADADOS = RAIZ / "data" / "metadata.json"
OUTPUT_DIR.mkdir(exist_ok=True)


def salvar_metadados(artigos: list[dict]) -> None:
    METADADOS.write_text(
        json.dumps(artigos, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def carregar_metadados() -> list[dict]:
    if not METADADOS.exists():
        return []

    try:
        dados = METADADOS.read_text(encoding="utf-8")
        return json.loads(dados)
    except json.JSONDecodeError, ValueError:
        return []


def get_soup(url: str) -> BeautifulSoup:
    resposta = requests.get(url, timeout=30)
    resposta.raise_for_status()
    return BeautifulSoup(resposta.text, "html.parser")


def slug(txt: str | None, n: int = 150) -> str:
    txt = "" if txt is None else txt
    return re.sub(r"[^\w\-]+", "_", txt).strip("_")[:150]


def run() -> None:
    artigos: list[dict] = []

    if WEB_SCRAP:
        url = "https://sol.sbc.org.br/index.php/wit/issue/archive"

        soup = get_soup(url)

        edicoes: list[tuple[str, str]] = [
            (a.get_text(strip=True), href)
            for a in soup.select("ul.issues_archive a.title")
            if isinstance((href := a.get("href")), str)
        ]

        for titulo, url in edicoes:
            print(titulo, "->", url)

        for ed_titulo, ed_url in edicoes:
            pagina = get_soup(ed_url)
            for item in pagina.select(".obj_article_summary"):
                a = item.select_one(".title a")
                pdf = item.select_one("a.obj_galley_link.pdf")
                h2 = item.find_previous("h2")
                autores = item.select_one(".authors")
                pdf_href = pdf.get("href") if pdf else None
                href_artigo = a.get("href") if a else ""
                titulo_texto = a.get_text(strip=True) if a else ""
                id_artigo = slug(titulo_texto)

                artigos.append(
                    {
                        "id": id_artigo,
                        "edicao": ed_titulo,
                        "secao": h2.get_text(strip=True) if h2 else "",
                        "titulo": titulo_texto,
                        "autores": autores.get_text(strip=True) if autores else "",
                        "url_artigo": href_artigo
                        if isinstance(href_artigo, str)
                        else "",
                        "url_pdf": (
                            str(pdf_href).replace(
                                "/article/view/", "/article/download/"
                            )
                            if pdf_href
                            else None
                        ),
                    }
                )
            print(
                f"{ed_titulo}: "
                f"{sum(1 for x in artigos if x['edicao'] == ed_titulo)} artigos"
            )
        salvar_metadados(artigos)

    if BAIXAR:
        OUTPUT_DIR.mkdir(exist_ok=True)

        if not artigos:
            artigos = carregar_metadados()

        for art in artigos:
            if art["url_pdf"] is None:
                continue
            pasta = OUTPUT_DIR / slug(art["edicao"])
            pasta.mkdir(exist_ok=True)
            arquivo = pasta / (slug(art["titulo"]) + ".pdf")
            if arquivo.exists():
                continue
            r = requests.get(art["url_pdf"], timeout=30)
            r.raise_for_status()
            arquivo.write_bytes(r.content)
            print("baixado:", arquivo)

        salvar_metadados(artigos)


if __name__ == "__main__":
    run()
