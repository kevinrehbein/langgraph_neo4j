# Tide: Chatbot de Apoio à Comunicação Clínica na Menopausa baseado em Geração Aumentada por Recuperação

Karolina Azevedo, Michele A. Brandão, Mirella M. Moro

Universidade Federal de Minas Gerais (UFMG), Belo Horizonte – MG – Brazil

`{karolina.azevedo, michele.brandao, mirella}@dcc.ufmg.br`

Abstract. Menopause involves physical and emotional changes that affect women’s quality of life. In Brazil, the lack of reliable information and difficulties in communication with healthcare professionals contribute to misinformation and insufficient preparation for clinical follow-up. This work proposes a chatbot in Brazilian Portuguese to mitigate the information asymmetry between women in the climacteric period and healthcare professionals. In addition to answering questions, the system organizes symptom reports and generates structured summaries to support medical consultations. In comparative experiments, a general-purpose model achieved 48% correct responses, while the proposed system reached 93%, demonstrating significant gains in reliability.

Resumo. A menopausa envolve mudanças físicas e emocionais que impactam a qualidade de vida das mulheres. No Brasil, a falta de informação confiável e as dificuldades na comunicação com profissionais de saúde contribuem para a desinformação e para um preparo insuficiente para o acompanhamento clínico. Este trabalho propõe um chatbot em português-BR para mitigar a assimetria de informação entre mulheres no climatério e profissionais de saúde. Além de responder dúvidas, o sistema organiza relatos de sintomas e gera relatórios estruturados que auxiliam na consulta. Em experimentos comparativos, um modelo de uso geral obteve 48% de respostas corretas, enquanto o sistema proposto alcançou 93%, evidenciando ganhos significativos de confiabilidade.

## 1. Introdução

As transições biológicas do ciclo de vida feminino, da menarca à menopausa, frequentemente carecem de suporte clínico e informacional adequado. Na prática clínica, a subabordagem da saúde sexual e o manejo inadequado da Síndrome Geniturinária da Menopausa (SGM) comprometem a qualidade assistencial, demandando estratégias baseadas em comunicação clara e tomada de decisão compartilhada ( shared decision-making ) [Kaufman et al. 2023, Paschou et al. 2024].

Embora diretrizes clínicas apontem que lacunas de comunicação impactam a qualidade de vida das pacientes [Paschou et al. 2024], intervenções em saúde digital ( digital health ) mostram-se eficazes quando fundamentadas em técnicas de mudança de comportamento e design centrado na usuária [Sediva et al. 2022]. Na saúde da mulher, evidências de meta-análise indicam que agentes conversacionais ( chatbots ) reduzem sintomas de ansiedade e depressão e promovem o autocuidado. Contudo, a heterogeneidade metodológica e de métricas observada na literatura restringe a generalização dos achados e exige maior rigor avaliativo [Kim 2024].

No subdomínio da menopausa, Grandes Modelos de Linguagem (LLMs) são explorados para suporte informacional [Deva et al. 2025, Garg and Munshi 2024]. Todavia, limitações estruturais impedem sua aplicação clínica direta [Bélisle Pipon 2024]. O principal risco reside nas alucinações, em que o modelo gera saídas plausíveis, mas factualmente incorretas [Yu et al. 2025]. Somam-se a isso problemas de rastreabilidade, obsolescência do conhecimento e superconfiança na geração textual [Deng et al. 2023]. Em contextos de saúde, essas vulnerabilidades exigem mecanismos que vinculem a geração de conteúdo a fontes curadas e verificáveis.

Para mitigar tais limitações, as arquiteturas de Geração Aumentada por Recuperação (RAG, Retrieval-Augmented Generation ) surgem como uma alternativa robusta. Essa abordagem integra LLMs a mecanismos de recuperação de informação operando sobre bases de conhecimento curadas, garantindo que as respostas sejam fundamentadas em documentos rastreáveis e alinhadas a diretrizes clínicas.

Nesse panorama, este artigo propõe e valida o chatbot Tide, projetado para mitigar a assimetria informacional e qualificar a comunicação entre mulheres no climatério e profissionais de saúde. Desenvolvido sob a metodologia Design Science Research (DSR), o artefato estruturou-se em quatro fases: (1) engenharia de requisitos; (2) projeto e implementação; (3) estruturação da base de conhecimento; e (4) avaliação. A base compreende diretrizes clínicas oficiais, artigos científicos e manuais públicos de instituições de saúde referenciadas, priorizando o idioma português do Brasil (pt-BR). Durante a interação, o sistema estrutura os relatos de sintomas das usuárias em um relatório clínico em PDF para subsidiar as consultas médicas.

Para avaliar a confiabilidade do Tide, realizou-se um experimento comparativo contra o modelo de linguagem base isolado ( zero-shot ). Os resultados demonstraram incrementos estatisticamente significativos em qualidade e segurança informacional, mitigando alucinações e provendo rastreabilidade explícita.

O restante deste artigo está organizado da seguinte forma. A Seção 2 revisa os trabalhos relacionados. A Seção 4 detalha a arquitetura do Tide. A Seção 3 formaliza a metodologia DSR. A Seção 5 analisa os resultados experimentais e a Seção 6 apresenta as conclusões e trabalhos futuros.

## 2. Trabalhos Relacionados

O domínio de FemTech (tecnologias direcionadas à saúde e ao bem-estar feminino) tem evoluído de sistemas puramente informativos para soluções interativas baseadas em Inteligência Artificial (IA). Estudos indicam alta aceitabilidade de agentes conversacionais aplicados ao manejo da menopausa, desde que assegurados requisitos de privacidade, empatia computacional e acurácia clínica [Garg and Munshi 2024]. Contudo, as soluções computacionais vigentes frequentemente se dividem em aplicações de monitoramento estáticas e reativas, as quais falham em oferecer suporte personalizado ou subsidiar ativamente tomadas de decisão clínica. Em contrapartida, o uso direto e não mediado de Grandes Modelos de Linguagem (LLMs, Large Language Models ) por pacientes apresenta riscos críticos associados aos princípios de IA Responsável (RAI, Responsible Artificial Intelligence ), destacando-se a ocorrência de alucinações e a opacidade algorítmica.

No cenário nacional de FemTech, destacam-se iniciativas com vertentes educacionais voltadas à saúde e ao empoderamento feminino. O sistema EMPFO

[Silva et al. 2025b] valida a relevância de soluções engenharia de software culturalmente adaptadas para mulheres e meninas em situação de vulnerabilidade social e violência. Igualmente, jogos sérios ( serious games ) como Mundo Bit Byte [Briceño et al. 2021] e Peg.Ada [Vinhal and Odakura 2023], bem como frameworks de capacitação e letramento digital para idosas [Silva et al. 2025a], ilustram o potencial de tecnologias instrucionais como instrumentos de conscientização, formação e inclusão digital. Para saúde assistencial e segurança, arquiteturas ciber-físicas como o SALVE TODAS [Ribeiro and Pereira 2022] e plataformas orientadas a dados como a Nossa Voz [Silva et al. 2021] atuam na mitigação de problemas estruturais complexos, a exemplo da violência de gênero.

No subdomínio do climatério e da menopausa, destaca-se o aplicativo Raquel Menopausa, que oferece conteúdos educativos, diário de sintomas, inferência do estágio hormonal, relatórios personalizados compartilháveis com profissionais de saúde e ambiente de apoio mútuo. Contudo, não há transparência pública acerca de sua arquitetura tecnológica, do uso de modelos de IA ou de mecanismos técnicos de governança e segurança de dados, caracterizando-se como um software proprietário fechado de natureza comercial. Sob a perspectiva acadêmica nacional, o sistema IaraMed [Färber et al. 2025] compreende um agente conversacional em português baseado em RAG voltado à saúde da mulher. Embora mitigue alucinações ao ancorar as respostas em repositórios externos, sua base de conhecimento incorpora dados extraídos via web scraping, técnica que pode introduzir ruído informacional e inconsistência factual ao sistema.

No cenário internacional, o sistema MenoEaze [Suraj et al. 2025] propõe um assistente baseado em RAG e alinhado por Aprendizado por Reforço a partir do Feedback Humano (RLHF, Reinforcement Learning from Human Feedback ) para fornecer suporte empático. Embora o MenoEaze inove na modelagem de empatia computacional, seu escopo primário limita-se ao acolhimento diário e à mitigação do isolamento social. Outras soluções comerciais globais baseadas no modelo Software as a Service (SaaS) — como Sofia AI e The Menopause Coach — combinam telemetria de sintomas e guias de bemestar, incluindo a geração de relatórios para consultas médicas. Entretanto, operam como sistemas de caixa-preta ( black-box systems ), omitindo a proveniência dos dados clínicos e os métodos de processamento utilizados.

Atualmente, as tecnologias direcionadas ao climatério caracterizam-se como um ecossistema fragmentado, no qual diferentes ferramentas abordam o problema de forma isolada. Algumas priorizam o registro passivo de métricas fisiológicas, outras concentramse na educação em saúde, enquanto assistentes conversacionais focam no suporte informativo ou emocional. Embora tais soluções ofereçam contribuições relevantes, nenhuma delas integra, simultaneamente, uma arquitetura de recuperação fundamentada em diretrizes clínicas homologadas, adaptação ao contexto regulatório e epidemiológico brasileiro e mecanismos que apoiem ativamente a preparação para consultas médicas. Ademais, dimensões como a curadoria estrita das fontes de dados e a instrumentalização ativa da paciente permanecem pouco exploradas na literatura.

> 1Aplicativo Raquel Menopausa: `https://www.raquelmenopausa.com`

> 2Startups FemTech: `https://l1nq.com/lNkch`

> 3Técnica automatizada de extração de dados que converte conteúdos estruturados ou semiestruturados de páginas web (como HTML) em bases de dados organizadas.

> 4App Store: `https://apps.apple.com/br/app/sofia-ai/id6744707879`

> 5App Store: `https://apps.apple.com/br/app/the-menopause-coach/id6448751138`

Tabela 1. Comparação de trabalhos relacionados e nossa proposta (TIDE)

|Ferramenta|Público-alvo|Gratuito|IA Conversacional|Fontes Curadas|Transparência|Relatório Clínico|Contexto BR|
|---|---|---|---|---|---|---|---|
|EMPFO|Mulheres em geral|✓|||||✓|
|Raquel Menopausa|Menopausa|✓||✓||✓|✓|
|IaraMed|Saúde da mulher|✓|✓||||✓|
|MenoEaze|Menopausa|✓|✓|✓|✓|||
|Sofia AI|Menopausa||✓|||✓||
|The Menopause Coach|Menopausa|||||✓||
|TIDE|Menopausa|✓|✓|✓|✓|✓|✓|

A ferramenta introduzida neste artigo, chamada Tide, busca preencher essa lacuna ao propor uma abordagem integrada baseada em quatro elementos: (1) arquitetura RAG fundamentada em diretrizes clínicas oficiais e com rastreabilidade explícita das fontes; (2) geração de um artefato clínico tangível, na forma de relatório estruturado em PDF; (3) adaptação ao contexto brasileiro; e (4) instrumentalização da paciente. Diferentemente das soluções existentes, Tide integra esses elementos em um único sistema, contribuindo para reduzir a assimetria informacional e apoiar uma triagem médica mais eficiente e objetiva, conforme resumido na Tabela 1.

## 3. Metodologia

A metodologia deste trabalho foi delineada para orientar sistematicamente o processo de concepção, especificação, desenvolvimento e avaliação experimental do assistente conversacional Tide, assegurando critérios de segurança clínica e confiabilidade informacional. Esta seção descreve o levantamento exploratório e a subsequente formalização do problema (Seção 3.1); o fluxo de desenvolvimento de software e a engenharia de computação aplicada à construção da base de conhecimento do mecanismo de recuperação (Seção 3.2); e, por fim, o protocolo de avaliação experimental empregado para mensurar o desempenho do sistema RAG (Seção 3.3).

Este estudo adota a abordagem metodológica DSR, consolidada no desenvolvimento e avaliação de artefatos tecnológicos projetados para mitigar problemas complexos em contextos reais. Alinhada aos preceitos da DSR, a fase inicial concentrou-se na delimitação do problema e na exploração do domínio de aplicação.

### 3.1. Definição do Problema e Levantamento Exploratório

Na primeira fase, conduziu-se a identificação do problema e o levantamento preliminar de requisitos de software. Para tanto, realizou-se um estudo exploratório direcionado à compreensão do estado da arte e ao mapeamento de lacunas de informação relacionadas ao climatério e à menopausa. Essa etapa compreendeu uma análise comparativa e estrutural de ferramentas digitais e assistentes conversacionais voltados à saúde da mulher, operando como um benchmark técnico para identificar funcionalidades correlatas, abordagens informacionais e limitações arquiteturais nessas soluções vigentes.

Adicionalmente, aplicaram-se métodos de investigação qualitativa exploratória para expandir a compreensão do contexto de uso e das barreiras comunicacionais enfrentadas pelas usuárias. As estratégias de levantamento incluíram a observação passiva de interações em comunidades virtuais de saúde (especificamente fóruns da plataforma

Figura 1. Fluxo metodológico de construção da base de conhecimento.

Reddit, em que usuárias compartilham dúvidas e relatos empíricos sobre a menopausa) e a condução de entrevistas informais não estruturadas com grupos de discussão no círculo social das pesquisadoras. Essas interações subsidiaram a identificação de temas recorrentes, tipologias de dúvidas comuns e assimetrias de informação, fornecendo insumos para a especificação inicial de requisitos de engenharia e para o escopo funcional do assistente conversacional.

Com base nesse diagnóstico, o problema de pesquisa foi formalizado como a ausência de uma solução computacional de acesso gratuito, no idioma português do Brasil, capaz de viabilizar simultaneamente: (1) a provisão de suporte informacional confiável e dotado de ancoragem ( grounding ) explícita em fontes científicas verificáveis; e (2) a síntese automatizada de um relatório clínico estruturado que atue como guia para otimizar as consultas médicas presenciais.

### 3.2. Desenvolvimento do Sistema e Construção da Base de Conhecimento

A segunda fase compreendeu o projeto arquitetural e a implementação do assistente conversacional. O sistema adota uma arquitetura baseada em RAG, detalhada na Seção 4, que integra um modelo de linguagem a um mecanismo de busca por similaridade semântica em uma base de conhecimento local. A orquestração dos fluxos de diálogo, o gerenciamento de memória contextual e a execução de consultas para recuperação de documentos relevantes foram implementados com o emprego do framework LangChain.

Na terceira fase da DSR, procedeu-se à construção e curadoria da base de conhecimento utilizada pelo módulo de recuperação de informação. Esse processo englobou a seleção, extração, transformação e indexação (ETL) de documentos textuais provenientes de instituições de saúde referenciadas, visando garantir a acurácia factual do sistema. O fluxo metodológico dessa infraestrutura de dados está ilustrado na Figura 1, sendo dividido em três etapas sequenciais: (1) seleção e coleta de fontes; (2) pré-processamento e segmentação textual ( chunking ); e (3) enriquecimento de metadados e indexação em banco de dados vetorial.

A eficácia informacional de sistemas RAG correlaciona-se diretamente à confiabilidade e à qualidade do corpus de dados subjacente. Desse modo, a etapa de curadoria priorizou literatura médica consolidada sobre o climatério. A coleta de dados abrangeu 82 documentos provenientes de 10 entidades de saúde corporativas e governamentais, totalizando 34 arquivos no formato PDF e 48 páginas web de hipertexto. A distribuição institucional, os respectivos formatos de mídia e os períodos cronológicos de publicação

Tabela 2. Fontes da base.

|Fonte|Formato Qtde. |Período|
|---|---|---|
|FEBRASGO|PDF 32|2004–2019|
|Ministério da Saúde|PDF 1|2008|
|Brazilian Journals|PDF 1|2020|
|Tua Saúde|web 35|2016–2025|
|Abbott Brasil|web 4|2024–2025|
|Drauzio Varella|web 3|2024–2025|
|Biblioteca Virtual em Saúde|web 3|2004–2020|
|Prefeitura de São Paulo|web 2|2020, 2025|
|MedSênior|web 2|2019, 2025|
|Unimed|web 1|2025|
|Total|82|2004–2025|

Figura 2. Distribuição de artigos.

estão sistematizados na Tabela 2. As fontes públicas foram selecionadas a partir de critérios de autoridade institucional e adequação de linguagem ao público-alvo, priorizando diretrizes clínicas validadas e materiais instrucionais acessíveis. Adicionalmente, a Figura 2 detalha o mapeamento cronológico dessas publicações, evidenciando uma concentração de fontes contemporâneas na composição do corpus, assegurando o alinhamento do sistema às evidências científicas e condutas clínicas vigentes.

Durante a fase de tratamento dos dados, aplicou-se um pipeline de filtragem e normalização textual para garantir a qualidade léxica e a consistência semântica das instâncias no banco vetorial. Nos conteúdos extraídos via web de páginas hipertexto, executou-se a remoção de elementos não textuais, metadados espúrios ou de baixa densidade informacional, tais como anúncios publicitários, credenciais de profissionais de saúde, hiperlinks multimídia externos e elementos de navegação em árvore. Essa operação eliminou ruídos estruturais do HTML, preservando estritamente o conteúdo discursivo de interesse.

No tocante aos artigos científicos e diretrizes em formato PDF, o protocolo de depuração orientou-se à exclusão de metadados acadêmicos redundantes. Foram suprimidas informações de autoria, filiações institucionais, notas de rodapé operacionais, agradecimentos a agências de fomento e listas de referências bibliográficas, retendo-se exclusivamente o escopo analítico e os dados clínicos centrais de cada documento.

Complementarmente, realizou-se a normalização de texto, abrangendo a regularização de espaços em branco duplicados, hifens e pontuações, a correção de concatenações indesejadas de strings e o alinhamento à norma ortográfica vigente. Esse tratamento mitigou inconsistências ortográficas e ruídos textuais, promovendo homogeneidade linguística e otimizando a qualidade das representações vetoriais ( embeddings ). Após o processamento, cada registro do corpus foi serializado como um objeto individual em arquivos no formato JSON Lines (.jsonl), assegurando uma leitura sequencial de alta eficiência e compatibilidade com pipelines de pré-processamento de dados em larga escala.

Concluída a etapa de curadoria, o corpus foi submetido ao processo de fragmentação textual ( chunking ), preparando as estruturas para a geração de vetores densos via modelos de embeddings, essenciais para a busca por similaridade de cosseno. Para a computação dos vetores de características, adotou-se o modelo gemini-embedding-001. Testes preliminares foram conduzidos utilizando arquiteturas da biblioteca Sentence Transformers; contudo, a solução da Google demonstrou superioridade qualitativa na recuperação semântica sobre textos estruturados em português do Brasil (pt-BR), motivando sua seleção

para a topologia final do artefato. Alinhado às heurísticas documentadas do LangChain, estabeleceu-se uma janela de segmentação fixa de 1.000 caracteres por fragmento, com uma sobreposição ( overlap ) de 200 caracteres, equilibrando custos computacionais e retenção de contexto clínico. Cada fragmento foi indexado em um banco de dados vetorial associado a metadados contendo o hiperlink da fonte original. Essa arquitetura RAG viabiliza a citação dinâmica e explícita dos documentos recuperados, promovendo a transparência, explicabilidade e auditabilidade do sistema por meio da rastreabilidade pontual das respostas geradas.

### 3.3. Protocolo de Avaliação

Na quarta etapa da DSR, validou-se a qualidade das respostas sintéticas geradas pelo artefato por meio da metodologia de avaliação automatizada LLM-as-a-Judge [Zheng et al. 2023]. Essa abordagem emprega um LLM avançado operando como avaliador estatístico e conceitual para mensurar o desempenho do chatbot frente a critérios axiomáticos predefinidos, incluindo aderência ao contexto recuperado, consistência factual e utilidade clínica da resposta.

O desenho experimental estruturou-se em três etapas consecutivas. Inicialmente, o modelo GPT-5 foi parametrizado para gerar um conjunto de dados ( dataset ) sintético contendo 100 consultas de teste cobrindo cenários do climatério e da menopausa. Posteriormente, essas perguntas foram submetidas em paralelo ao sistema proposto (Tide) e a uma linha de base ( baseline ) de uso geral, representada pelo modelo gpt-oss-120b acessado via API. Ressalta-se que o Tide emprega o referido modelo base acoplado à arquitetura RAG projetada, enquanto o baseline reflete o modelo operando em modo isolado ( zero-shot, sem injeção de contexto curado). Finalmente, o modelo qwen3-32b foi instanciado como juiz automatizado, avaliando as saídas com base em quatro métricas de desempenho: veracidade factual, acurácia biológica, escopo temático e segurança médica.

O protocolo de avaliação foi calibrado para discriminar e categorizar duas classes fundamentais de falhas de sistemas conversacionais: (1) erros de aterramento informacional, tipificados como alucinações, nos quais o modelo infere dados factualmente incorretos ou não suportados pelo contexto; e (2) falhas de alinhamento médico, tipificadas como respostas inseguras, caracterizadas por violações éticas e operacionais de segurança em saúde, tais como a indicação de diagnósticos fechados, prescrição de posologias ou recomendações terapêuticas específicas. Essa taxonomia permite isolar desvios de factualidade de riscos críticos à integridade e segurança das usuárias.

## 4. O Chatbot Conversacional Tide

A concepção da ferramenta partiu da análise de como um LLM poderia atuar como suporte informacional e comunicacional durante o climatério, garantindo alinhamento com diretrizes clínicas, segurança das respostas e adequação linguística ao público-alvo. A proposta busca equilibrar rigor clínico e linguagem acessível, adaptando-se a diferentes níveis de letramento em saúde. Com base nessa definição conceitual, o desenvolvimento iniciou-se pela curadoria de um corpus em português-BR de conhecimento composto por diretrizes, revisões e estudos de alta qualidade sobre o climatério.

> 6LangChain Tutorials: `https://sl1nk.com/t4jxA`

A partir desse corpus, foi estruturada a arquitetura do sistema e seus mecanismos de controle. Na camada de orquestração, estratégias de prompt engineering atuam como mecanismos de controle comportamental. O modelo é instruído a usar linguagem inclusiva, evitar especulações e embasar suas respostas apenas nos documentos recuperados. A interface também promove transparência no uso da ferramenta. Logo na mensagem de boas-vindas, o sistema explicita seu escopo de atuação e informa que não substitui o aconselhamento médico profissional. Ainda, ao final de cada resposta, são exibidas as fontes utilizadas, permitindo que a usuária rastreie a origem das informações apresentadas.

Em termos de funcionamento, o chatbot Tide possui dois fluxos de interação: (1) o modo de conversa, no qual o sistema responde às perguntas das usuárias; e (2) o modo de formulários, em que são coletadas algumas informações pessoais para estruturar e gerar um guia personalizado com base nos dados fornecidos. Esse fluxo está representado na Figura 3, no lado esquerdo.

Figura 3. Formas de interagir com TIDE (esquerda) e seus módulo de chat ( tools_chat em LangChain, direita)

Visando assegurar a confiabilidade informacional e o rigor clínico, a ferramenta adota a arquitetura RAG ilustrada na Figura 3 à direita, que ancora as respostas do LLM em uma base de conhecimento confiável. A abordagem RAG funciona em um processo de duas etapas descritas a seguir.

1. Recuperação: Quando uma pergunta é feita, o sistema realiza a busca em uma base de conhecimento pré-selecionada (neste caso, uma coleção revisada sobre menopausa para encontrar os trechos de informação mais relevantes);

2. Geração Aumentada: O LLM recebe a pergunta original acompanhada do contexto recuperado e de instruções de sistema ( system prompts ) para formular a resposta exclusivamente com base nessas fontes.

Essa orquestração garante que o conhecimento entregue seja rastreável e transforma o modelo em um sistema mais controlado, verificável e fundamentado em evidências científicas. O sistema utiliza a biblioteca LangChain como camada de orquestração, responsável por integrar o LLM, o mecanismo de recuperação de informações baseado em RAG e os fluxos de interação com a usuária. Essa camada gerencia o processamento das consultas, incluindo a recuperação de documentos relevantes e a geração de respostas contextualizadas. Além disso, também coordena o fluxo de formulários, quando a usuária

> 7LangChain: `https://www.langchain.com`

Notação: Os nós (caixas) representam os estados de processamento. As arestas contínuas indicam a transição determinística entre as etapas, enquanto as arestas pontilhadas ilustram o roteamento dinâmico baseado nas intenções da usuária.

Figura 4. Arquitetura de orquestração baseada em LangChain

solicita a geração do guia personalizado, o sistema identifica essa intenção e direciona a interação para o fluxo responsável por sua geração. Os componentes e fluxos do sistema são apresentados na Figura 4. A figura é gerada automaticamente pelo próprio LangChain a partir da estrutura do código implementado. Nesse grafo, os dois fluxos principais do sistema são representados. O nó router_node é responsável por identificar a intenção da usuária e direcionar a execução para o fluxo apropriado.

O Tide encontra-se atualmente em estágio de protótipo funcional, implementado em Streamlit para fins de pesquisa e validação experimental. A interface preliminar do sistema e exemplos de interação foram apresentados em trabalho anterior [Azevedo et al. 2026], enquanto a arquitetura da base vetorial permite atualização incremental com novos documentos e diretrizes clínicas curadas.

## 5. Avaliação e Resultados

A Figura 5 apresenta a distribuição das classificações atribuídas pelo modelo avaliador ao sistema proposto e ao modelo de linha de base. O modelo de uso geral ( baseline ) obteve 48 de respostas classificadas como corretas e três parcialmente corretas. Foram ainda registrados 12 casos classificados como inseguros, relacionados a prescrições ou inconsistências conceituais, e 29 respostas classificadas como alucinação.

Em contraste, o sistema Tide apresentou desempenho significativamente superior, com 93 de respostas corretas e três parcialmente corretas. Não foram identificadas respostas inseguras, e apenas quatro ocorrências foram classificadas como alucinação. Considerando que ambos os sistemas utilizam o mesmo modelo base ( gpt-oss-120b ), os resultados indicam que a melhoria observada decorre principalmente do uso do RAG.

Observa-se ainda uma diferença qualitativa relevante quanto à transparência das informações. O modelo baseline, por não acessar fontes externas, apresentou casos de alucinação de referências, nos quais citações ou dados bibliográficos são mencionados sem correspondência em documentos reais. Já o Tide recupera trechos diretamente da base de conhecimento e apresenta os respectivos hiperlinks de origem, permitindo rastrear a procedência das informações e aumentando a auditabilidade das respostas — aspecto relevante em aplicações sensíveis como sistemas informacionais em saúde.

Embora a abordagem LLM-as-a-Judge permita uma avaliação sistemática e escalável das respostas geradas, esta estratégia apresenta limitações inerentes, especialmente

> 8Link protótipo: `https://chatbot-menopausa-pjsy4k7cw3nxkvdjbb88wj.streamlit.app/`

20º Women In Information Technology (WIT 2026): Ferramentas

Figura 5. Comparação modelos: baseline e Tide

em contextos médico-informacionais. O uso de perguntas sintéticas pode não representar integralmente dúvidas reais de usuárias, enquanto a utilização de um avaliador automático pode introduzir vieses relacionados ao próprio modelo de linguagem empregado. Dessa forma, os resultados obtidos devem ser interpretados como uma avaliação preliminar da solução, não substituindo estudos futuros com usuárias e profissionais de saúde em cenários reais de uso.

## 6. Conclusão

Este trabalho apresentou o desenvolvimento e a avaliação preliminar do Tide, um agente conversacional baseado em RAG e no modelo gpt-oss-120b, voltado para mitigar a lacuna de informações confiáveis e as barreiras de comunicação clínica no contexto brasileiro. Os experimentos indicam que a arquitetura proposta melhora a qualidade e a confiabilidade das respostas em comparação ao uso isolado de modelos de linguagem, ao restringir a geração a um corpus curado de diretrizes oficiais e literatura revisada.

Além da técnica, a contribuição central do trabalho está na mediação informacional entre usuária e profissional de saúde. A geração automática de um relatório estruturado em PDF funciona como um artefato de apoio à consulta, organizando sintomas e informações relevantes para facilitar a comunicação clínica e apoiar a tomada de decisão compartilhada.

Como trabalhos futuros, destacam-se a realização de estudos com usuárias e profissionais de saúde para avaliar a usabilidade e a aceitação da ferramenta. Pretende-se também disponibilizar a ferramenta Tide para uso público após a realização desses estudos; contudo, o modelo de disponibilização e possíveis custos de utilização ainda serão definidos. Bem como a expansão da base de conhecimento com novas diretrizes clínicas. Pretende-se também investigar a incorporação de fontes multimodais, como vídeos, podcasts e conteúdos educativos produzidos por profissionais de saúde, ampliando o escopo informacional do sistema. Adicionalmente, será explorado o suporte a entradas e saídas por áudio, com o objetivo de ampliar a acessibilidade da ferramenta. Os resultados sugerem que a combinação entre geração de linguagem e recuperação de conhecimento pode contribuir para o desenvolvimento de assistentes conversacionais mais seguros e transparentes em aplicações sensíveis como a saúde.

## Agradecimentos

Esta pesquisa foi parcialmente financiada pelo Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) e pela Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (Capes).

## Uso de Inteligência Artificial

Ferramentas de inteligência artificial foram utilizadas para auxiliar na tradução do resumo para o inglês e na síntese de alguns trechos do texto.

## 7. Referências

- Azevedo, K., Machado, L., and Moro, M. M. (2026). Tide - colaboração mediada por inteligência artificial na saúde da mulher: Apoio à comunicação clínica e à decisão compartilhada no climatério. In Anais do XXI Simpósio Brasileiro de Sistemas Colaborativos. SBC.

- Briceño, A. J., Silvestre, A. S., Castro, B., Soares, H., Oliveira, T., Silva, T., Araujo, A., Castanho, C., Koike, C., Holanda, M., and Oliveira, R. (2021). Mundo bit byte: Um jogo digital para disseminar o conhecimento sobre personalidades femininas na computação. In Anais do XV Women in Information Technology, pages 121–130, Porto Alegre, RS, Brasil. SBC.

- Bélisle Pipon, J.-C. (2024). Why we need to be careful with LLMs in medicine. Frontiers in Medicine (Lausanne), 11(1495582):1–2.

- Deng, J., Zubair, A., and Park, Y.-J. (2023). Limitations of large language models in medical applications. Postgraduate Medical Journal, 99(1178):1298–1299.

- Deva, R., S, M., Zhou, J., Chahine, E., Davenport-Nicholson, A., Kaonga, N., Bozkurt, S., and Ismail, A. (2025). A Mixed-Methods Evaluation of LLM-Based Chatbots for Menopause. In Medical Informatics Europe Conference, volume 327, pages 1175 – 1179.

- Färber, F., Dollis, J., Ribeiro, P., Brito, I., Sousa, R., and Filho, A. G. (2025). IaraMed: A women’s healthcare chatbot for portuguese speakers. In Anais do XXV Simpósio Brasileiro de Computação Aplicada à Saúde, pages 931–942, Porto Alegre, RS, Brasil. SBC.

- Garg, R. and Munshi, A. (2024). Revolutionizing Menopause Management: Harnessing the Potential of Artificial Intelligence. Journal of Mid-life Health, 15(2):53–54.

- Kaufman, M. R., Ackerman, L. A., Amin, K. A., and et al. (2023). The AUA/SUFU/AUGS Guideline on Genitourinary Syndrome of Menopause. The Journal of Urology, 214(3):242–250.

- Kim, H.-K. (2024). The effects of artificial intelligence chatbots on women’s health: A systematic review and meta-analysis. Healthcare, 12(5):534.

- Paschou, S. A., Athanasiadou, K. I., Hafford-Letchfield, T., Hinchliff, S., Mauskar, M., Rees, M., Simon, J. A., Armeni, E., Erel, C. T., Fistonic, I., et al. (2024). Sexual health and wellbeing and the menopause: An EMAS clinical guide. Maturitas, 189:108055.

- Ribeiro, M. and Pereira, M. (2022). SALVE TODAS: um sistema inteligente para auxiliar na segurança de mulheres. In Anais do XVI Women in Information Technology, pages 133–144, Porto Alegre, RS, Brasil. SBC.

- Sediva, H., Cartwright, T., Robertson, C., and Deb, S. (2022). Behavior change techniques in digital health interventions for midlife women: Systematic review. JMIR mHealth and uHealth, 10(11):e37234.

- Silva, D. H., Morais, A., and Morais, A. (2021). Nossa voz: uma plataforma digital para visualização de dados sobre violência contra a mulher no brasil. In Anais do XV Women in Information Technology, pages 315–319, Porto Alegre, RS, Brasil. SBC.

- Silva, J., Silva, V., and Figueiredo, A. (2025a). Capacitação digital para mulheres 60+: Promovendo inclusão e autonomia através do letramento digital. In Anais do XIX Women in Information Technology, pages 419–428, Porto Alegre, RS, Brasil. SBC.

- Silva, K., Mendonça, A., Oliveira, P., and Silva, A. (2025b). Informação e empoderamento de meninas e mulheres em vulnerabilidade: incorporando ferramentas de inovação em práticas pedagógicas para desenvolvimento de aplicativo por meninas do território de manguinhos. In Anais do XIX Women in Information Technology, pages 895–906, Porto Alegre, RS, Brasil. SBC.

- Suraj, A., Khurana, K., Jain, H., and Mishra, H. (2025). MenoEaze: An empathetic retrieval-augmented generation companion for menopause management. International Journal of Engineering Research & Technology (IJERT), 14(12).

- Vinhal, A. and Odakura, V. (2023). Peg.ada: Um jogo educacional para abordar a importância da pegada digital no futuro profissional de jovens meninas. In Anais do XVII Women in Information Technology, pages 228–238, Porto Alegre, RS, Brasil. SBC.

- Yu, E., Chu, X., Zhang, W., et al. (2025). Large language models in medicine: Applications, challenges, and future directions. International Journal of Medical Sciences, 22(11):2792–2801.

- Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E., Zhang, H., Gonzalez, J. E., and Stoica, I. (2023). Judging LLM-asa-Judge with MT-Bench and Chatbot Arena. In Proceedings of the 37th International Conference on Neural Information Processing Systems, pages 46595–46623.
