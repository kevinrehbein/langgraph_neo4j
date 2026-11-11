import functools
import logging
from typing import Literal

from langchain_core.tools import BaseTool, tool

from config import TOOL_ERROR
from retrieval import queries, formatting
from retrieval.hybrid import HybridRetriever

logger = logging.getLogger(__name__)


def _safe_tool(func):
    """Falha de infraestrutura (Neo4j, embeddings) vira texto, não derruba o grafo."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logger.exception("Falha na ferramenta %s", func.__name__)
            return TOOL_ERROR

    return wrapper


@tool
@_safe_tool
def pesquisar_contexto_wit(pergunta: str, listar_artigos: bool = False) -> str:
    """
    Busca informações cruciais na base de dados do evento Women in Information Technology (WIT).
    Usa GraphRAG para cruzar similaridade de artigos com relações de entidades no Neo4j.
    Sempre use esta ferramenta para coletar evidências antes de responder ou planejar.

    Args:
        pergunta: A dúvida ou tópico a ser pesquisado (ex: "projetos de mentoria para meninas").
        listar_artigos: True para perguntas de listagem ("quais artigos...?"),
            devolvendo no máximo um trecho por artigo.
    """
    return HybridRetriever.get_instance().recuperar_contexto(
        pergunta, um_por_artigo=listar_artigos
    )


@tool
@_safe_tool
def buscar_projetos_semelhantes(palavras_chave: list[str]) -> str:
    """
    Encontra artigos e projetos no WIT que focam especificamente em um conjunto de palavras-chave.
    Útil para verificar lacunas na literatura ou levantar projetos que já fizeram algo similar.

    Args:
        palavras_chave: Lista de strings com os temas de interesse (ex: ["Mentoria", "Meninas na Computação"]).
    """
    results = queries.find_similar_projects_by_keyword(palavras_chave)
    if not results:
        return "Nenhum projeto estruturalmente semelhante encontrado com essas palavras-chave."
    return formatting.formatar_fontes(
        [{"titulo": r["titulo"], "url": r["url"],
        "corpo": f"Temas em comum: {', '.join(r['temas_em_comum'])} (aderência: {r['aderencia']})"}
        for r in results],
        consulta=", ".join(palavras_chave),
    )


@tool
@_safe_tool
def artigos_do_autor(nome: str) -> str:
    """
    Lista os artigos do WIT escritos por uma pessoa (autora ou autor), com link.
    Aceita nome parcial e ignora acentos e maiúsculas (ex: "Laura Jurgina").
    Não tolera erros de digitação: em caso de falha, tente o sobrenome isolado.

    Args:
        nome: Nome ou parte do nome da pessoa.
    """
    results = queries.find_author_works(nome)
    if not results:
        return (
            f"Nenhum autor encontrado com o nome '{nome}'. "
            "Tente outra variação (apenas o sobrenome, por exemplo)."
        )

    return formatting.formatar_fontes(
        [{"titulo": a["titulo"], "url": a["url"], "corpo": f"Autor(a): {r['autor']}"}
        for r in results for a in r["artigos"]],
        consulta=nome,
    )



@tool
@_safe_tool
def autores_do_artigo(titulo: str) -> str:
    """
    Encontra um artigo do WIT pelo título (ou palavras distintivas dele)
    e retorna seus autores e link.

    Args:
        titulo: Título completo ou palavras-chave do título.
    """
    results = queries.find_articles_by_title(titulo)
    if not results:
        return (
            f"Nenhum artigo encontrado para '{titulo}'. "
            "Tente menos palavras, só as mais distintivas."
        )
    return formatting.formatar_fontes(
        [{"titulo": r["titulo"], "url": r["url"],
        "corpo": f"Autores: {', '.join(r['autores'])}"} for r in results],
        consulta=titulo,
    )


RESEARCHER_TOOLS: list[BaseTool] = [
    pesquisar_contexto_wit,
    buscar_projetos_semelhantes,
    artigos_do_autor,
    autores_do_artigo,
]
