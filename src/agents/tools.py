import json

from langchain_community.tools import BaseTool
from langchain_core.tools import tool

from retrieval.hybrid import HybridRetriever
from retrieval import graph_queries


@tool
def buscar_artigos_wit(query: str) -> str:
    """
    Busca artigos na base de dados do evento Women in Information Technology (WIT) com base em um texto ou pergunta.
    Use esta ferramenta para encontrar evidências textuais, resumos e informações gerais sobre tópicos de pesquisa.

    Args:
        query: O termo de busca ou pergunta (ex: "inclusão de mulheres na programação").
    """
    results = graph_queries.search_wit_papers(query)
    if not results:
        return "Nenhum artigo encontrado para esta busca no WIT."
    # Retornamos como string JSON para o LLM processar facilmente no prompt
    return json.dumps(results, ensure_ascii=False, indent=2)

@tool
def pesquisar_contexto_wit(pergunta: str) -> str:
    """
    Busca informações cruciais na base de dados do evento Women in Information Technology (WIT).
    Usa GraphRAG para cruzar similaridade de artigos com relações de entidades no Neo4j.
    Sempre use esta ferramenta para coletar evidências antes de responder ou planejar.
    
    Args:
        pergunta: A dúvida ou tópico a ser pesquisado (ex: "projetos de mentoria para meninas").
    """
    retriever = HybridRetriever.get_instance()
    return retriever.recuperar_contexto(pergunta)

@tool
def buscar_projetos_semelhantes(palavras_chave: list[str]) -> str:
    """
    Encontra artigos e projetos no WIT que focam especificamente em um conjunto de palavras-chave estruturais.
    Útil para o agente verificar lacunas na literatura ou levantar projetos que já fizeram algo similar.

    Args:
        palavras_chave: Lista de strings com os temas de interesse (ex: ["Mentoria", "Meninas na Computação"]).
    """
    results = graph_queries.find_similar_projects_by_keyword(palavras_chave)
    if not results:
        return "Nenhum projeto estruturalmente semelhante encontrado com essas palavras-chave."
    return json.dumps(results, ensure_ascii=False, indent=2)


@tool
def perfil_entidade(nome: str, tipo: str = "Author") -> str:
    """
    Busca o perfil completo de uma entidade no grafo, como um autor específico.
    Retorna o total de publicações, títulos e os principais tópicos pesquisados por essa pessoa no evento WIT.

    Args:
        nome: O nome exato da entidade (ex: "Renata Reiser").
        tipo: O tipo da entidade (atualmente apenas "Author").
    """
    results = graph_queries.get_entity_profile(nome, tipo)
    if not results or not results[0].get("name"):
        return f"Perfil não encontrado para {nome}."
    return json.dumps(results, ensure_ascii=False, indent=2)


RESEARCHER_TOOLS: list[BaseTool] = [
    buscar_artigos_wit,
    pesquisar_contexto_wit,
    buscar_projetos_semelhantes,
    perfil_entidade,
]