import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_neo4j import Neo4jGraph

from config import (
    K_GRAFO,
    MAX_RELACOES,
    N_ENTIDADES,
    NEO4J_PASSWORD,
    NEO4J_URI,
    NEO4J_USERNAME,
    RELACOES_POR_ENTIDADE,
    SCORE_MIN,
    TETO_GRAU,
    TOP_K,
)


class HybridRetriever:
    _instance = None

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3",
            model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
            encode_kwargs={"normalize_embeddings": True, "batch_size": 16},
        )

        self.graph = Neo4jGraph(
            url=NEO4J_URI,
            username=NEO4J_USERNAME,
            password=NEO4J_PASSWORD,
        )

    @classmethod
    def get_instance(cls):
        """Padrão Singleton para evitar recarregar o BGE-M3."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _chunks_entrada(self, vec: list[float]) -> list[dict]:
        return self.graph.query(
            """
            MATCH (d:Document)
                SEARCH d IN (VECTOR INDEX chunk_embedding FOR $vec LIMIT $k)
                SCORE AS score
            OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
            RETURN d.id AS id, d.text AS texto, score, a.titulo AS titulo
            """,
            {"k": TOP_K, "vec": vec},
        )

    def _entidades_entrada(self, vec: list[float]) -> list[dict]:
        return self.graph.query(
            """
            MATCH (e:__Entity__)
                SEARCH e IN (VECTOR INDEX entity_embedding FOR $vec LIMIT $n)
                SCORE AS score
            WHERE score >= $min AND e.grau <= $teto
            RETURN elementId(e) AS eid, e.id AS nome,
                   coalesce(e.descricao, '') AS descricao, score
            """,
            {"n": N_ENTIDADES, "vec": vec, "min": SCORE_MIN, "teto": TETO_GRAU},
        )

    def _relacoes_do_grafo(self, eids: list[str], vec: list[float]) -> list[dict]:
        return self.graph.query(
            """
            MATCH (e:__Entity__) WHERE elementId(e) IN $eids
            MATCH (e)-[r]-(v:__Entity__)
            WHERE v.grau <= $teto AND v.embedding IS NOT NULL
            WITH e, r, vector.similarity.cosine(v.embedding, $vec) AS sim
            ORDER BY sim DESC
            WITH e, collect({r: r, sim: sim})[..$por_entidade] AS top
            UNWIND top AS t
            WITH t.r AS r, max(t.sim) AS sim
            ORDER BY sim DESC
            LIMIT $max
            RETURN startNode(r).id AS origem, type(r) AS rel, endNode(r).id AS destino,
                   coalesce(startNode(r).descricao, '') AS desc_origem,
                   coalesce(endNode(r).descricao, '') AS desc_destino,
                   elementId(startNode(r)) AS eid_origem, elementId(endNode(r)) AS eid_destino, sim
            """,
            {
                "eids": eids,
                "vec": vec,
                "teto": TETO_GRAU,
                "por_entidade": RELACOES_POR_ENTIDADE,
                "max": MAX_RELACOES,
            },
        )

    def _chunks_do_grafo(self, ents: list[str], excluir: list[str]) -> list[dict]:
        return self.graph.query(
            """
            UNWIND $ents AS eid
            MATCH (x:__Entity__) WHERE elementId(x) = eid
            MATCH (d:Document)-[:MENTIONS]->(x)
                WHERE NOT d.id IN $excluir
            WITH d, sum(1.0 / log(1 + x.n_mentions)) AS relevancia
            ORDER BY relevancia DESC
            LIMIT $k
            OPTIONAL MATCH (d)-[:PARTE_DE]->(a:Artigo)
            RETURN d.id AS id, d.text AS texto, relevancia, a.titulo AS titulo
            """,
            {"ents": ents, "excluir": excluir, "k": K_GRAFO},
        )

    def recuperar_contexto(self, pergunta: str) -> str:
        """Executa o pipeline GraphRAG e retorna o contexto em texto formatado para o LLM."""
        vec = self.embedding_model.embed_query(pergunta)

        chunks_base = self._chunks_entrada(vec)
        nos_entrada = self._entidades_entrada(vec)
        eids = [e["eid"] for e in nos_entrada]

        relacoes_grafo, chunks_extras = [], []
        if eids:
            relacoes_grafo = self._relacoes_do_grafo(eids, vec)
            ents = set(eids)
            for r in relacoes_grafo:
                ents.update((r["eid_origem"], r["eid_destino"]))
            chunks_extras = self._chunks_do_grafo(
                list(ents), excluir=[c["id"] for c in chunks_base]
            )

        # Montagem do texto (antiga parte inicial do responder)
        desc = {e["nome"]: e["descricao"] for e in nos_entrada if e.get("descricao")}
        for rel in relacoes_grafo:
            if rel["desc_origem"]:
                desc.setdefault(rel["origem"], rel["desc_origem"])
            if rel["desc_destino"]:
                desc.setdefault(rel["destino"], rel["desc_destino"])

        if relacoes_grafo:
            bloco_entidades = "\n".join(f"- {n}: {d}" for n, d in desc.items())
            bloco_relacoes = "\n".join(
                f"{f['origem']} -[{f['rel']}]-> {f['destino']}" for f in relacoes_grafo
            )
            relacoes_texto = f"=== ENTIDADES DO GRAFO ===\n{bloco_entidades}\n\n=== RELAÇÕES ===\n{bloco_relacoes}\n\n"
        else:
            relacoes_texto = "Nenhuma relação direta encontrada no grafo.\n\n"

        chunks = chunks_base + chunks_extras
        contexto = "=== TRECHOS DE ARTIGOS (CHUNKS) ===\n"
        contexto += "\n\n".join(f"[FONTE: {c['titulo']}]\n{c['texto']}" for c in chunks)

        return relacoes_texto + contexto
