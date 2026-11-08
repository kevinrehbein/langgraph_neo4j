"""Consultas Cypher estruturadas usadas pelas ferramentas do pesquisador.

ASSUMPTIONS sobre o schema do grafo (ajuste se o seu for diferente):
- (:Document)-[:PARTE_DE]->(:Artigo {titulo})
- (:Document)-[:MENTIONS]->(:__Entity__ {id})
- Autores são entidades com o label `Author` (id = nome).
"""

import re
import unicodedata

from .connection import get_graph

MAX_TOKENS = 6  # limita termos vindos do LLM

def normalizar(texto: str) -> str:
    """Minúsculas, sem acentos, sem nbsp, pontuação e espaços colapsados."""
    texto = unicodedata.normalize("NFKD", texto.replace("\xa0", " "))
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^\w\s]", " ", texto.lower())
    return re.sub(r"\s+", " ", texto).strip()



def find_similar_projects_by_keyword(
    keywords: list[str], limit: int = 10
) -> list[dict]:
    cleaned = [k for k in (normalizar(k) for k in keywords if k) if k]
    if not cleaned:
        return []
    return get_graph().query(
        """
        MATCH (e:__Entity__)
        WHERE any(k IN $kws WHERE toLower(e.id) CONTAINS k)
        MATCH (d:Document)-[:MENTIONS]->(e)
        MATCH (d)-[:PARTE_DE]->(a:Artigo)
        RETURN a.titulo AS titulo,
               collect(DISTINCT e.id)[..8] AS temas_em_comum,
               count(DISTINCT e) AS aderencia
        ORDER BY aderencia DESC
        LIMIT $limit
        """,
        {"kws": cleaned, "limit": limit},
    )

def _tokens(texto: str) -> list[str]:
    return texto.lower().replace("\xa0", " ").split()[:6]


def find_author_works(nome: str, limit: int = 20) -> list[dict]:
    tokens = _tokens(nome)
    if not tokens:
        return []
    return get_graph().query(
        """
        MATCH (au:Autor)
        WHERE all(t IN $tokens WHERE toLower(au.nome) CONTAINS t)
        WITH au LIMIT $limit
        MATCH (a:Artigo)-[:ESCRITO_POR]->(au)
        RETURN au.nome AS autor,
               collect(DISTINCT {titulo: a.titulo, url: a.url_artigo}) AS artigos
        """,
        {"tokens": tokens, "limit": limit},
    )


def find_articles_by_title(titulo: str, limit: int = 20) -> list[dict]:
    tokens = _tokens(titulo)
    if not tokens:
        return []
    return get_graph().query(
        """
        MATCH (a:Artigo)
        WHERE all(t IN $tokens WHERE toLower(a.titulo) CONTAINS t)
        WITH a LIMIT $limit
        OPTIONAL MATCH (a)-[:ESCRITO_POR]->(au:Autor)
        RETURN a.titulo AS titulo, a.url_artigo AS url,
               collect(au.nome) AS autores
        """,
        {"tokens": tokens, "limit": limit},
    )
