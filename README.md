# agents
graphrag/
├── docker-compose.yml        # Neo4j (com APOC, se precisar)
├── .env                      # NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, OPENAI_API_KEY
├── pyproject.toml            # ou requirements.txt
├── data/
│   └── markdown/             # sua base .md
└── src/
    ├── config.py             # carrega .env, instancia llm, embeddings, graph
    ├── schema.py             # ALLOWED_NODES, ALLOWED_RELATIONSHIPS
    ├── ingestion/
    │   ├── loader.py         # lê os .md e faz o chunking por headers
    │   ├── extract.py        # LLMGraphTransformer → graph_docs
    │   ├── store.py          # add_graph_documents + índices (vetor, full-text)
    │   └── pipeline.py       # orquestra: load → extract → store → embeddings
    ├── retrieval/
    │   ├── hybrid.py         # Neo4jVector + retrieval_query (vetor + grafo)
    │   ├── text2cypher.py    # GraphCypherQAChain
    │   └── queries.py        # strings Cypher
    ├── agent/
    │   ├── tools.py          # @tool buscar_contexto, consultar_grafo
    │   └── agent.py          # create_agent + system prompt
    └── eval/
        ├── dataset.json      # perguntas e respostas de referência
        └── run_eval.py
scripts/
├── ingest.py                 # python scripts/ingest.py
└── chat.py                   # loop interativo com o agente