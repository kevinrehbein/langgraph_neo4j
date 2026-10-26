# Mapas de resistência: Inteligência Artificial no combate ao feminicídio

Rayane Pimentel, Kalinka Castelo Branco, Isadora Ferrão

1Serviço Nacional de Aprendizagem do Comércio (Senac) – São Carlos, SP, Brasil

2Universidade de São Paulo (USP) – São Carlos, SP, Brasil

3Université de Bretagne Occidentale - Brest, France

rayane.lpimentel@senacsp.edu.br, kalinka@icmc.usp.br isadoraferrao@usp.br

Abstract. This study proposes a predictive model to estimate the risk of femicide in public spaces in Brazil by integrating urban infrastructure indicators and data from public reporting systems. Using Random Forest and open data sources such as Disque 180, SNIS, and FBSP, the model achieved a mean absolute error of 0.25 cases per 100,000 women. The variable with the greatest predictive power was the rate of violence reports, followed by urban lighting coverage and time of day. The tool includes an interactive simulator, allowing scenario analysis for policy support. Results reveal critical territorial patterns and support evidence-based public safety planning.

Resumo. Este estudo propõe um modelo preditivo para estimar o risco de feminicídio em espaços públicos no Brasil, integrando indicadores urbanos e dados de denúncias públicas. Utilizando Random Forest e bases abertas como Disque 180, SNIS e FBSP, o modelo obteve um Erro Absoluto Médio (MAE), de 0,25 casos por 100 mil mulheres. A variável mais relevante foi a taxa de denúncias, seguida da cobertura de iluminação pública e do horário de pico. A ferramenta desenvolvida inclui um simulador interativo para análise de cenários e apoio à formulação de políticas. Os resultados revelam padrões territoriais críticos e reforçam a importância do planejamento baseado em evidências.

## 1. Introdução

A violência contra a mulher representa uma das mais persistentes e alarmantes violações dos direitos humanos no Brasil, configurando-se também como um grave problema de saúde pública [FIDELES 2023]. Mesmo com avanços legislativos e institucionais, como a Lei Maria da Penha [Bianchini and GOMES 2014], a Lei do Feminicídio [ALMEIDA et al. 2015] e a criação do Disque 180 [Bandeira 2014], os números seguem elevados. Em 2023, foram registradas 302.856 notificações de violência contra mulheres, das quais 71,6% ocorreram em ambiente doméstico e 14,7% em vias públicas [das Mulheres do Brasil 2025].

Além da permanência dos altos índices de notificações, observa-se uma lacuna na forma como esses dados são utilizados para orientar ações preventivas. A maioria dos estudos e políticas de enfrentamento concentra-se na esfera doméstica [Cavalcanti and Oliveira 2017], deixando de lado abordagens que considerem variáveis estruturais do espaço urbano na avaliação do risco. Faltam modelos analíticos e preditivos capazes de traduzir os dados disponíveis em subsídios práticos para gestão territorial e políticas públicas [Cerqueira et al. 2020]. Neste estudo, define-se o risco de feminicídio em espaços públicos como a probabilidade de ocorrência de violência letal

ou extrema contra mulheres fora do ambiente doméstico, condicionada por fatores contextuais como infraestrutura urbana precária, baixa iluminação, isolamento territorial e ausência de proteção institucional [Cerqueira et al. 2020]. Essa delimitação permite uma abordagem mais ampla e preventiva, considerando o espaço urbano como variável fundamental na análise da vulnerabilidade.

Estudos existentes sobre risco de feminicídio baseiam-se majoritariamente em dados individuais, como entrevistas [Oliveira et al. 2016], formulários [Soares et al. 2023] e registros policiais [de Avila and Pessoa 2020], o que limita sua aplicabilidade em larga escala e seu uso em sistemas automatizados de prevenção. Por outro lado, há uma crescente disponibilidade de bases de dados abertas e georreferenciadas [de Lima ], como o Disque 180 [Ministério dos Direitos Humanos 2019], o SNIS [Brasil 2023] e os dados do Fórum Brasileiro de Segurança Pública [de Segurança Pública 2024], que ainda são subutilizadas em modelos preditivos.

Diante disso, esta pesquisa propõe e implementa uma ferramenta preditiva que estima o risco de feminicídio em espaços urbanos com base na integração de variáveis espaciais, urbanas e de denúncia. A solução foi desenvolvida com técnicas de Aprendizado de Máquina (AM), utilizando algoritmos como Random Forest (RF) [Rigatti 2017], treinados a partir de dados do Disque 180, georreferenciados por Unidade Federativa (UF), indicadores urbanos (ex.: cobertura de iluminação pública) e variáveis temporais (ex.: horários de pico de circulação). A análise concentra-se em dados de escala nacional, segmentada por UF, a fim de identificar padrões regionais e fornecer subsídios adaptáveis a governos locais. A ferramenta inclui visualizações interativas que permitem identificar áreas de maior risco e explorar os fatores que mais contribuem para a vulnerabilidade feminina em espaços públicos.

Além da construção do modelo, o estudo realizou uma análise exploratória e espacial das denúncias de violência contra mulheres no Brasil, identificando padrões regionais, calculando taxas de incidência por 100 mil habitantes e correlacionando-as com indicadores socioeconômicos e urbanos. Os resultados revelam desigualdades territoriais e confirmam a relevância das variáveis urbanas na composição do risco.

Os objetivos específicos incluem mapear denúncias por UF, calcular taxas padronizadas por 100 mil habitantes, correlacionar com variáveis urbanas e desenvolver um modelo preditivo de risco.

Ao integrar AM com análise espacial aplicada à segurança pública, esta pesquisa oferece uma contribuição concreta para a construção de cidades mais seguras para as mulheres. Seus resultados podem orientar ações territorializadas e baseadas em evidências, promovendo maior eficácia nas políticas de enfrentamento à violência de gênero.

O restante deste texto está organizado como segue: a Seção 2 apresenta os trabalhos relacionados sobre análise espacial e violência de gênero; a Seção 3 detalha a metodologia; a Seção 4 expõe os resultados do modelo preditivo; e a Seção 5 traz as conclusões e implicações para políticas públicas.

## 2. Trabalhos Relacionados

O uso de ciência de dados, AM e análise espacial tem ampliado os estudos sobre violência de gênero, embora ainda predomine o foco na violência doméstica [Leal et al. 2021]. As abordagens existentes se concentram em três eixos: predição com dados individuais, revisões metodológicas sobre crimes e análises do espaço urbano como fator de risco.

No Brasil, a maioria dos trabalhos é qualitativa ou descritiva, voltada aos efeitos de

políticas como a Lei Maria da Penha [Dias et al. 2023] e às dificuldades de subnotificação [de Oliveira Ruiz et al. 2022].

Modelos preditivos recentes, utilizam AM para estimar reincidência com dados criminais e sociodemográficos, mas sem incorporar variáveis espaciais ou urbanas. Em linha semelhante, [Costa 2023] aplicou algoritmos como RF e XGBoost a dados da PCSVDFMulher, com bons resultados (F1 = 81%), mas ainda focado no ambiente doméstico. Já [Mandalapu et al. 2023] destaca a importância crescente de dados espaciais para identificação de hotspots, embora sem foco específico em gênero.

Estudos como o de [Borrion et al. 2020] relacionam o ambiente construído à criminalidade, mas há escassez de pesquisas que tratem diretamente do risco de feminicídio em espaços públicos. No Brasil, a literatura sobre variáveis urbanas (iluminação, mobilidade, densidade) é limitada a análises exploratórias. Já o trabalho de [Garfias Royo et al. 2020], no México, mostra como baixa infraestrutura, visibilidade reduzida e restrições à mobilidade aumentam a vulnerabilidade feminina, reforçando a relevância de variáveis como iluminação pública, utilizadas neste estudo.

Assim, embora existam avanços, são raras as abordagens que integram dados urbanos e modelos preditivos aplicados ao risco de feminicídio em espaços públicos. Este estudo busca preencher essa lacuna com uma proposta metodológica baseada em evidências e territorialização.

## 3. Metodologia

Este estudo foi conduzido em cinco etapas principais: (1) seleção e coleta das fontes de dados, (2) procedimentos de pré-processamento e estruturação dos dados, (3) configuração e treinamento do modelo de AM, (4) avaliação de desempenho com métricas específicas e (5) análise crítica do modelo gerado. O fluxo metodológico adotado buscou garantir replicabilidade, coerência com os dados disponíveis e aplicabilidade prática para políticas públicas territoriais.

### 3.1. Seleção e coleta das fontes de dados

Foram utilizadas quatro bases públicas para análise de violência de gênero e infraestrutura urbana. A principal fonte foi o Disque 180 - Central de Atendimento à Mulher, fornecido pelo Ministério da Mulher, Família e Direitos Humanos [Ministério dos Direitos Humanos 2019], escolhido por sua abrangência nacional e variáveis territorializadas (tipo de violência, UF e município).

Como variável dependente, foram utilizadas as taxas de feminicídio por 100 mil mulheres por UF, obtidas do Atlas da Violência (IPEA [Cerqueira et al. 2020]/FBSP [de Segurança Pública 2024]). As variáveis independentes basearam-se em: (i) SNIS [Brasil 2023] (iluminação pública urbana) e (ii) FBSP [de Segurança Pública 2024] (horário de pico de ocorrências violentas). As fontes foram selecionadas por complementaridade e relevância para o estudo da vulnerabilidade urbana sob a perspectiva de gênero.

### 3.2. Pré-processamento dos dados

O pré-processamento foi realizado no Google Colab, com a integração manual das bases e organização dos dados por UF. As colunas foram padronizadas para permitir a junção correta entre as fontes, utilizando como chave principal a sigla da UF. A variável categórica Horario ~~p~~ ico foi transformada em valor numérico, com base no ponto médio de cada faixa horária, prática comum para tratar variáveis temporais em modelos de regressão.

As taxas por 100 mil habitantes, como Tx ~~1~~ 00k ~~2~~ 019 e Feminicidio ~~1~~ 00k, foram mantidas conforme disponibilizadas nas fontes originais, garantindo comparabilidade com os indicadores oficiais. Além disso, a padronização geográfica foi essencial para conectar os dados a mapas interativos, por meio de arquivos GeoJSON. O processo completo, incluindo os scripts utilizados, está documentado em repositório público (oculto para revisão).

### 3.2.1. Análise exploratória dos dados (AED)

Antes da modelagem preditiva, foi realizada uma análise exploratória dos dados com o objetivo de compreender a distribuição das variáveis, identificar possíveis outliers, padrões regionais e relações entre os fatores analisados. Foram gerados histogramas, gráficos de dispersão e uma matriz de correlação para as variáveis quantitativas. Essa etapa permitiu validar a integridade dos dados e orientar a escolha do algoritmo e das variáveis mais promissoras.

Como destaque, observou-se correlação positiva entre a taxa de denúncias (Ligue180 ~~1~~ 00k) e a taxa de feminicídios (Feminicidio ~~1~~ 00k), bem como padrões regionais na cobertura de iluminação pública, especialmente em estados do Norte e Nordeste.

### 3.3. Configuração e treinamento dos modelos de AM

Foi utilizado o algoritmo RandomForestRegressor, da biblioteca scikit-learn, por sua robustez com bases pequenas, capacidade de lidar com variáveis heterogêneas e interpretabilidade por meio da importância das variáveis.

O modelo foi configurado com n ~~e~~ stimators=100 e random ~~s~~ tate=42, conforme boas práticas para garantir reprodutibilidade. As variáveis independentes foram: denúncias por 100 mil mulheres (Ligue180 ~~1~~ 00k), percentual de iluminação pública adequada (Iluminacao ~~a~~ dequada) e horário de pico convertido em valor numérico (Horario ~~p~~ ico ~~n~~ um). A variável alvo foi a taxa de feminicídio por 100 mil mulheres (Feminicidio ~~1~~ 00k).

A validação foi feita com KFold (5 divisões), utilizando MAE como métrica principal. Após o treinamento, foi gerada uma análise de importância das variáveis. Testes com regressão linear foram realizados como baseline, mas o modelo de floresta aleatória apresentou melhor desempenho. Futuras versões devem incluir comparação com outros algoritmos, como XGBoost e redes neurais.

### 3.4. Avaliação de desempenho

A validação do modelo foi realizada com KFold (5 divisões), shuffle=True e random ~~s~~ tate=42, estratégia adequada para bases pequenas e prevenção de overfitting. A métrica utilizada foi o MAE, apropriado para lidar com outliers e de fácil interpretação. Também foi avaliada a importância relativa das variáveis no modelo, indicando o peso de cada fator na predição.

### 3.4.1. Ambiente de testes

Os testes foram realizados no Google Colab, com ambiente Python padrão (12 GB RAM), utilizando bibliotecas como pandas, scikit-learn e plotly.

### 3.5. Análise comparativa

Embora apenas um algoritmo tenha sido testado nesta versão do estudo, a escolha pela RF se justificou pela estabilidade frente a pequenas amostras e pela possibilidade de interpretar a influência de cada variável. A ausência de comparação com outros algoritmos é uma limitação reconhecida, que será abordada em trabalhos futuros.

Um diferencial deste estudo é a criação de um painel interativo que permite testar cenários simulados com diferentes combinações de entrada. O usuário insere valores para cada uma das variáveis preditoras, e o modelo retorna a estimativa de risco de feminicídio para aquele cenário. Essa funcionalidade reforça o potencial da ferramenta como apoio à formulação de políticas públicas baseadas em evidências.

input data = [[ligue, iluminacao, horario ]] predicao = model.predict( input data)[0]

O painel interativo foi concebido como uma interface de simulação de cenários, conectada ao backend do modelo treinado. A camada de visualização e interação com o usuário ( frontend ) foi implementada em plotly no ambiente Jupyter do Google Colab, enquanto o backend computacional de previsão foi inteiramente construído em Python 3, utilizando scikit-learn. Essa separação garante modularidade e facilita futuras adaptações para plataformas web.

### 3.6. Discussão ética e reprodutibilidade

Por tratar-se de um tema sensível, com forte impacto social e institucional, este estudo buscou adotar práticas éticas em todas as etapas metodológicas. As bases utilizadas são públicas e institucionalmente reconhecidas, e não envolvem dados pessoais ou identificáveis. Ainda assim, é importante ressaltar que a agregação dos dados por UF pode ocultar dinâmicas locais importantes, e que o uso preditivo de indicadores sociais exige cuidado para não reforçar estigmas regionais ou vieses de interpretação.

Para garantir transparência e reprodutibilidade, todo o código desenvolvido no Google Colab está disponível em repositório público no GitHub (OCULTO PARA REVIS AO AS CEGAS). O notebook inclui desde o carregamento dos dados até a geração de previsões e visualizações interativas. Como as bases utilizadas são públicas, qualquer pesquisador pode reproduzir ou adaptar a metodologia para outros contextos territoriais, respeitando os mesmos parâmetros adotados neste estudo.

## 4. Resultados

Esta seção apresenta os principais achados do estudo, estruturados em seis dimensões analíticas: (1) distribuição territorial das denúncias, (2) desempenho preditivo do modelo, (3) importância relativa das variáveis utilizadas, (4) análise espacial das taxas de feminicídio, (5) exploração de cenários simulados e (6) implicações práticas para políticas públicas.

### 4.1. Distribuição territorial das denúncias

A Figura 1 apresenta o Mapa de Segurança para Mulheres, construído com base na taxa de denúncias ao Disque 180 por 100 mil mulheres, em 2019. As categorias de risco

> 1Notebook disponível em: https://colab.research.google.com/drive/ 1-cHLFnneaqnXZJxicBmXioNMMlqS0ESX.

(baixo, moderado, alto e muito alto) foram definidas a partir de intervalos percentuais e aplicadas sobre os dados territorializados por UF.

Figura 1. Mapa de Segurança para Mulheres com base em denúncias ao Disque 180

Fonte: Disque 180 [Ministério dos Direitos Humanos 2019]. Elaboração: Próprios autores.

A média nacional foi de 21,0 denúncias por 100 mil mulheres. O estado com maior taxa foi o Rio de Janeiro, com 52,8 denúncias/100 mil, sendo classificado como de risco muito alto. Por outro lado, Roraima apresentou o menor índice (8,9), sendo classificado como risco baixo. A distribuição entre as categorias foi a seguinte: 3 estados em nível muito alto, 2 em alto, 15 em moderado e 7 em baixo. Essa heterogeneidade pode indicar a presença de disparidades no acesso à rede de proteção, podendo refletir tanto diferenças reais na incidência da violência quanto variações nos níveis de conscientização, cobertura de serviços e cultura de denúncia.

Para ampliar a utilidade prática do estudo, foi implementado um painel interativo de simulação de risco, no qual o usuário pode ajustar três variáveis principais: (i) taxa de denúncias ao Disque 180, (ii) percentual de iluminação pública adequada e (iii) faixa de horário com maior incidência de ocorrências. A partir dessas combinações, o modelo retorna uma estimativa da taxa de feminicídio por 100 mil mulheres, bem como a classificação de risco associada.

Como exemplo, ao configurar um cenário com 88 denúncias/100 mil mulheres, 69% de cobertura de iluminação pública e horário de pico entre 14h e 18h, o modelo retorna uma taxa estimada de 2,0 feminicídios por 100 mil mulheres para o estado do Mato Grosso (Figura 2). Essa funcionalidade permite avaliar o impacto relativo de diferentes variáveis em contextos territoriais específicos e simular potenciais efeitos de políticas públicas.

#### Figura 2. Mapa com simulaç ão aplicada ao estado do Mato Grosso

Fonte: Dados de denúncias: [Ministério dos Direitos Humanos 2019]. Dados territoriais: 18º Anuário Brasileiro de Segurança Pública [de Segurança Pública 2024]. Dados SNIS [Brasil 2023] Elaboração: Próprios autores.

### 4.2. Desempenho preditivo do modelo

O modelo preditivo baseado em RandomForestRegressor obteve um MAE de 0,25 feminicídios por 100 mil mulheres, conforme validação cruzada com 5 partições. Considerando que os valores reais da variável-alvo variaram entre 1,2 e 3,9, esse desvio médio é considerado satisfatório para um modelo baseado em dados agregados por UF. O resultado reforça a funcionalidade do algoritmo Random Forest para bases pequenas, com variáveis heterogêneas e sem a necessidade de pré-processamentos mais sofisticados, como normalizações.

### 4.3. Importância relativa das variáveis

A análise de importância das variáveis revelou que a Ligue180 ~~1~~ 00k foi, de forma destacada, o fator mais relevante, contribuindo com 84,6% da variância explicada no modelo. Em segundo lugar, veio a variável Iluminacao ~~a~~ dequada, com 10,6%, seguida do Horario ~~p~~ ico ~~n~~ um, com 4,8%. Esses dados estão representados na Tabela 1.

Tabela 1. Contribuiç ão das variáveis no modelo preditivo

|Fator|Influência|l (%)|
|---|---|---|
|Denúncias (Ligue 180)||84,6|
|Iluminação pública||10,6|
|Horário de pico||4,8|

Fontes: Denúncias (Ligue 180): [Ministério dos Direitos Humanos 2019]. Iluminação pública: [Brasil 2023]. Horário de pico: [de Segurança Pública 2024].

O peso expressivo da variável relacionada às denúncias pode ser interpretado de duas formas complementares: por um lado, ela reflete maior incidência de violência real. Por outro, pode indicar maior mobilização social e institucional em determinados territórios. Já o impacto da iluminação pública, embora menor, reforça achados da literatura que associam ambientes urbanos escuros à insegurança e vulnerabilidade. A variável do horário de pico, por sua vez, teve influência reduzida, mas ainda assim relevante para cenários noturnos de risco elevado. O painel é ilustrado na Figura 3 (D)

Figura 3. Distribuiç ão espacial de feminicídios por 100 mil mulheres. Tons vermelhos indicam maior risco

Fonte: Dados primários: [Ministério dos Direitos Humanos 2019], [Brasil 2023] e [de Segurança Pública 2024]. Elaboração: Próprios autores.

### 4.4. Análise espacial das taxas de feminicídio

O mapa gerado a partir dos dados e do modelo preditivo Figura 3 (C). revela um gradiente territorial marcante: maiores taxas no Sul/Sudeste e menores no Norte. Essa tendência pode refletir tanto maior efetividade das redes de denúncia em regiões urbanizadas quanto subnotificação em áreas menos assistidas.

O Rio de Janeiro lidera com 3,9 casos/100 mil mulheres, seguido por Alagoas (3,8) e Pernambuco (3,3). Roraima (1,2) e Tocantins (1,5), com as menores taxas, sugerem influência de baixa densidade populacional e subnotificação. Os padrões reforçam a necessidade de abordagens territorializadas adaptadas às realidades locais.

### 4.5. Exploração de cenários simulados

A Tabela 2 apresenta cenários simulados combinando denúncias, iluminação e horário. Os resultados mostram interações complexas, com destaque a ”horário de pico”, que, apesar de menor peso geral, influencia riscos em contextos específicos.

Em cenários como denúncias altas (250/100k) e iluminação ideal (100%), o risco permanece alto (3,34/100k) à noite, indicando a necessidade de políticas noturnas. Já bai-

Tabela 2. Resultados de simulaç ões representativas

|Denúncias|Iluminação|Horário|Estimativa|Risco|
|---|---|---|---|---|
|50/100k|50%|Madrugada|1.52|Baixo|
|150/100k|75%|Tarde|2.96|Alto|
|250/100k|100%|Noite|3.34|Alto|
|80/100k|75%|Noite|2.21|Médio|
|150/100k|75%|Tarde|2.21|Alto|

Nota: Cenários hipotéticos gerados pelo modelo preditivo com base nas variáveis selecionadas.

xas denúncias e iluminação precária (1,52/100k) sugerem subnotificação ou invisiblização da violência, uma limitação dos dados institucionais.

### 4.6. Implicações

Os achados deste estudo apontam para três direções estratégicas para políticas públicas baseadas em evidências: (i) o fortalecimento de canais de denúncia, especialmente em regiões de risco moderado e baixo, onde os índices podem mascarar realidades subnotificadas; (ii) o investimento em infraestrutura urbana, como iluminação pública, que embora não tenha se mostrado o principal preditor, pode atuar como fator de proteção em contextos vulneráveis; e (iii) o reforço do policiamento ostensivo em horários críticos, especialmente no período noturno, que demonstrou elevar significativamente o risco previsto, mesmo em cenários com bons indicadores nos demais fatores.

## 5. Conclusões

Este estudo comprovou a viabilidade de aplicar modelos preditivos baseados em variáveis urbanas e dados de denúncia para estimar o risco de feminicídio em espaços públicos. A taxa de denúncias ao Disque 180 foi o principal fator explicativo, respondendo por 84,6% da variação do modelo. Isso destaca a importância de políticas que incentivem a notificação e ampliem o alcance dos canais institucionais. A iluminação pública apareceu como um fator complementar, com 10,6% de influência. Embora seu impacto direto seja menor, ela pode ser determinante em contextos urbanos vulneráveis, especialmente à noite. Foram identificados padrões territoriais críticos, com destaque para estados como Rio de Janeiro, Alagoas e Pernambuco. Nessas regiões, as taxas de feminicídio chegaram a ser três vezes maiores que a média nacional, indicando a necessidade de estratégias regionalizadas.
