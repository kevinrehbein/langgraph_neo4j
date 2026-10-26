# Análise Perceptiva de Estratégias de Conteúdo do projeto Katie em Mídias Sociais

Barbara de Lima, Jucyelle Barros do Nascimento, Eliana Silva de Almeida, Raquel da Silva Cabral

1Ciência da Computação – Universidade Federal de Alagoas (UFAL) CEP 57.309-005 – Arapiraca – AL – Brasil

2Faculdade de Medicina – Universidade Federal de Alagoas (FAMED/UFAL) CEP 57.072-900 – Maceió – AL – Brasil

`{barbara.lima,jucyelle.nascimento}@arapiraca.ufal.br,`

`{eliana.almeida,raquel.cabral}@laccan.ufal.br`

Abstract. Katie is an extension project of the Federal University of Alagoas (UFAL) dedicated to increasing female representation in the areas of Science, Technology, Engineering and Mathematics (STEM). Recognizing Instagram as the main tool to promote ideas and causes, the research seeks to identify effective strategies to expand the group's reach on this platform. The research methodology includes descriptive and exploratory data analysis, as well as statistical methods and visual tools for a more in-depth understanding of engagement patterns. The results indicate that, currently, the publications with the highest engagement are related to entertainment reels associated with technology.

Resumo. O Katie é um projeto de extensão da Universidade Federal de Alagoas (UFAL) dedicado a aumentar a representatividade feminina nas áreas de Ciência, Tecnologia, Engenharia e Matemática (STEM). Reconhecendo o Instagram como ferramenta principal para promover ideias e causas, a pesquisa busca identificar estratégias eficazes para ampliar o alcance do grupo nessa plataforma. A metodologia da pesquisa inclui análise descritiva e exploratória de dados, além de métodos estatísticos e ferramentas visuais para uma compreensão mais aprofundada dos padrões de engajamento. Os resultados indicam que, atualmente, as publicações de maior engajamento estão relacionadas a reels de entretenimento associado à tecnologia.

## 1. Introdução

A presença digital é uma ferramenta indispensável para a disseminação de ideias, criação de comunidades e promoção de causas relevantes. O engajamento nas redes sociais é crucial para alcançar esses objetivos, e compreender os mecanismos que impulsionam o sucesso nesse ambiente é essencial. As redes sociais, especialmente o Instagram, desempenham um papel fundamental na estratégia de marketing de conteúdo digital, permitindo conexões significativas com o público através de curtidas, comentários e hashtags [Kotler 2017] [De Lira e Araújo 2015].

O Instagram se destaca por sua ênfase no conteúdo visual, um aspecto que aproveita a natureza visual dos seres humanos, como diz Martha Gabriel [Flores 2017]. A plataforma possibilita que as marcas contem histórias cativantes por meio de imagens e vídeos, criando uma conexão profunda com o público e gerando maior engajamento e visibilidade. No entanto, o conceito de engajamento vai além de ações isoladas, sendo um processo dinâmico que envolve progressivamente o consumidor, conforme De Lira

e Araújo (2015). Nesse sentido, a análise contínua e contextualizada dessas métricas permite que a empresa ajuste sua abordagem de marketing de conteúdo para melhor atender às expectativas e interesses em constante mutação de seu público-alvo.

Diante do exposto, o presente trabalho visa aprimorar a presença no Instagram do projeto intitulado “Katie: saindo do buraco negro e impulsionando as meninas para a computação”, um projeto que propõe-se a incentivar a participação feminina nas áreas de Ciência, Tecnologia, Engenharia e Matemática (STEM) [Katie 2023]. Leão e Silva (2020) em uma análise do Katie quanto suas Contribuições em Meios Digitais concluem que o número de postagens do perfil observado ainda era baixo e inconstante, trazendo a importância do estudo aqui proposto. Vale ressaltar que outras análises de perfis do Instagram, como as realizadas por Costa et al. (2023) e Silva et al. (2021), também contribuíram significativamente para o entendimento dos mecanismos que impulsionam o sucesso na plataforma.

Dessa forma, a pergunta de pesquisa que orienta o estudo se delineia da seguinte forma: “Quais são os fatores determinantes para o alcance e engajamento positivo nas postagens do Instagram do projeto Katie?”. O objetivo geral é entender que fatores influenciam o alcance e engajamento nas postagens do Instagram do Katie, e contribuir para o fortalecimento da participação feminina nas STEM. Para isso, são analisadas métricas de alcance, engajamento e interação, utilizando uma abordagem descritiva e exploratória. A metodologia analisa os dados das postagens por meio de métodos estatísticos e gráficos, o que permitiu diferenciar padrões de sucesso nas postagens e estratégias de conteúdo. Como resultado, espera-se identificar padrões, explorar correlações e capturar insights que permitam aprimorar a estratégia de conteúdo e promover interações mais impactantes e significativas.

## 2. Metodologia

Realizamos uma avaliação por meio de uma análise descritiva e exploratória dos dados das postagens do Katie no Instagram. Isso envolve métodos estatísticos básicos, como testes de comparação, tendência e correlação, para examinar métricas de alcance e engajamento. Também estamos criando gráficos de barras, séries temporais, diagramas de dispersão e boxplot para visualizar distribuições e padrões das análises.

As questões norteadoras desta pesquisa são: (i) Q1: Quais são as características específicas das postagens que geram maior alcance e engajamento no Instagram?; (ii) Q2: Existe uma relação entre o conteúdo visual (imagens, vídeos) das postagens e seu desempenho em termos de alcance e engajamento?; (iii) Q3: Há dias e horários específicos em que as postagens obtêm resultados melhores em termos de interações positivas?; (iv) Q4: Fatores externos, como call-to-actions (CTAs), parcerias e hashtags, influenciam no engajamento, independentemente do conteúdo visual?.

Os fatores que estão sendo variados e estudados neste experimento são: Conteúdo e tipo das postagens; Dia da semana e horário de postagem; Frequência de postagem; CTAs; Parcerias e Colaborações; Hashtags.

A Figura 1 ilustra as etapas para a realização do estudo: a coleta de dados, o pré-processamento e a análise. A fonte dos dados é obtida manualmente, diretamente da conta do Instagram do Katie (@katie.ufal). Esse acesso direto proporciona uma visão detalhada e abrangente das postagens, métricas de engajamento e interações com os seguidores, garantindo a integridade e a autenticidade dos dados coletados.

Figura 1. Apresentação gráfica da metodologia aplicada

São utilizados dados de fevereiro de 2022 a setembro de 2023 para captar informações do período pós-pandemia, junto ao retorno às aulas presenciais na UFAL.

O dataset InstagramKatie [Lima e Nascimento 2024] foi elaborado a partir da coleta de informações relevantes de 118 publicações do Instagram, em conformidade com as políticas de privacidade e termos de uso da Meta. As informações foram extraídas para compor as colunas do dataset e fornecer dados para as seguintes métricas iniciais:

(i) Alcance Médio por Postagem: Quantidade média de visualizações por postagem; (ii) Engajamento Médio: Média de curtidas, comentários, compartilhamentos e salvamentos por postagem; (iii) Melhores Dias e Horários: Identificação dos dias e horários com maior taxa de interação; (iv) Análise Visual: Identificação de características visuais de cada postagem.

Após a coleta dos dados, é realizado um pré-processamento que envolve a formatação de datas e horários de postagem – facilitando análises temporais e a identificação de tendências – e o tratamento de lacunas – podendo resultar na exclusão da postagem correspondente ou na manutenção das lacunas em branco, considerando a viabilidade de aproveitar informações de outras partes do conteúdo.

Com os dados devidamente pré-processados e um total de 112 publicações, avança-se para a etapa de análise, que é conduzida através da aplicação de alguns testes estatísticos: (i) Testes de Comparação (Teste t de Student) [Gaspar 2023]; (ii) Testes de Tendência (Teste de Mann-Kendall) [Mann 1945] [Kendall 1975]; (iii) Testes de Correlação (Teste de Correlação de Pearson) [Gaspar 2023].

As simulações são realizadas utilizando a linguagem de programação Python e as bibliotecas matplotlib, pandas, scipy e seaborn, no ambiente do Google Colab, uma plataforma colaborativa baseada em nuvem, ideal para manipulação e visualização de dados. Elas são divididas em três sessões distintas: testes de comparação para as hipóteses H1, H2, H3, H5 e H6; análise de tendência para a hipótese H4; e análise de correlação para a hipótese H7. A Tabela 1 fornece tanto a hipótese nula quanto a hipótese alternativa associadas a cada hipótese.

Tabela 1. Hipóteses H1-H7

|Hipótese|Hipótese nula (H0) Hipótese alternativa (H1)|
|---|---|

|Postagens explicativas sobre tópicos diversos de computação podem maximizar o engajamento (H1)|Não há diferença significativa no engajamento entre as postagens do tipo “Explicação” e as postagens de outros tipos de conteúdo;|As postagens do tipo “Explicação” têm um engajamento diferente (maior ou menor) em relação às postagens de outros tipos de conteúdo.|
|---|---|---|
|A utilização de_reels_pode estimular a um alcance maior nas postagens (H2)|A utilização de_reels_no Instagram não tem impacto estatisticamente significativo no alcance médio das postagens em comparação com postagens que não utilizam_reels_;|A utilização de_reels_no Instagram está associada a um aumento estatisticamente significativo no alcance médio das postagens em comparação com postagens que não utilizam_reels_.|
|Dias úteis em horários de pico na mídia social são momentos ideais para maximizar a interação dos seguidores (H3)|Não há diferença significativa na interação dos seguidores em dias úteis em horários de pico e em outros momentos na mídia social;|A interação dos seguidores em dias úteis em horários de pico na mídia social é significativamente maior do que em outros momentos.|
|A manutenção de uma programação regular semanal contribuirá para a construção de uma comunidade engajada ao longo do tempo (H4)|Não há tendência significativa no engajamento da comunidade ao longo das semanas;|Há uma tendência significativa no engajamento da comunidade ao longo das semanas.|
|O uso de CTAs nas postagens resulta em impactos positivos mais significativos (H5)|A utilização de CTAs não tem correlação com os resultados de impactos positivos mais significativos nas postagens;|A utilização de CTAs tem correlação com os resultados de impactos positivos mais significativos nas postagens.|
|Influência de parcerias estratégicas, com perfis de projetos e organizações ligadas às STEM, no alcance positivo de publicações (H6)|Não há influência significativa das parcerias estratégicas com perfis de projetos e organizações ligadas às STEM no alcance positivo de publicações;|Existe uma influência significativa das parcerias estratégicas com perfis de projetos e organizações ligadas às STEM no alcance positivo de publicações.|
|A utilização de_hashtags_ relevantes e populares ampliará a visibilidade das postagens e, consequentemente, seu alcance (H7)|A utilização de_hashtags_relevantes e populares não tem correlação com o alcance das publicações;|A utilização de_hashtags_relevantes e populares tem correlação com o alcance das publicações.|

## 3. Resultados e Discussões

Esta seção apresenta os resultados e discussões após a avaliação de cada hipótese, conforme a Tabela 1. O teste t de Student foi aplicado para avaliar as hipóteses H1, H2, H3, H5 e H6, sendo o resultado interpretado considerando um nível de significância de 0.05. Para a hipótese H4, foi adotada uma análise de tendência, o teste de Mann-Kendall. No caso da hipótese H7, realizou-se um teste de correlação de Pearson.

Na hipótese H1, ao comparar as médias de engajamento entre as postagens do tipo “Explicação” e outros grupos de publicação, observa-se uma disparidade significativa. A média de engajamento para postagens do tipo “Explicação” é aproximadamente 108,19, enquanto para outros tipos é cerca de 187,28, com um valor-p de 0,0020, rejeitando a hipótese nula H0. Isso indica que as postagens explicativas têm um engajamento significativamente menor. Para a hipótese H2, o teste t mostra que o alcance médio das publicações com reels é 4252,87, comparado a 1258,44 para publicações sem reels, com um valor-p de 0,000006, rejeitando a hipótese nula H0 e sugerindo que o uso de reels aumenta significativamente o alcance.

Para a hipótese H3, avaliando o envolvimento das postagens nos horários de pico em comparação com os outros momentos, o valor-p encontrado é 0,87, com médias de 175,48 e 171,59, respectivamente, mantendo a hipótese nula H0, pois não há evidências de diferença significativa no engajamento. Na hipótese H4, analisando o engajamento ao longo das semanas, o valor-p de 0,0036 leva à rejeição da hipótese nula H0, indicando uma tendência significativa no engajamento semanal. Para a hipótese H5, comparando postagens com e sem CTAs, as médias de engajamento são 176,07 e 157,68, respectivamente, com um valor-p de 0,47, não rejeitando a hipótese nula H0, sugerindo que CTAs não impactam significativamente o engajamento.

Na hipótese H6, a comparação do alcance médio entre publicações com e sem parcerias mostra médias de 1880,88 e 1604,90, respectivamente, com valor-p de 0,60, mantendo a hipótese nula H0, indicando que parcerias não afetam significativamente o alcance. Por fim, na hipótese H7, o teste de correlação de Pearson mostra um coeficiente de 0,13 e um valor-p de 0,16, sugerindo que o uso de hashtags não tem uma correlação significativa com o alcance das publicações, mantendo a hipótese nula H0.

Com as simulações é possível responder às questões de pesquisa. Em relação às hipóteses H1 e H2, conclui-se que conteúdos do tipo entretenimento em formato de vídeos curtos ( reels ) destacam-se, alcançando cerca de 4.253 contas e obtendo uma média de 315,5 interações. O desempenho de conteúdos visuais corrobora-se os resultados da hipótese H2, que demonstram que conteúdos visuais no formato de vídeo superam em alcance e engajamento as outras formas de publicação. A hipótese H3 argumenta que não existe uma diferença significativa entre os dias e horários específicos em que as postagens obtêm resultados superiores em termos de interações positivas. No entanto, a hipótese H4 evidencia uma tendência significativa de aumento no engajamento ao longo das semanas, sugerindo que um cronograma regular de postagens aumenta o engajamento. As hipóteses H5, H6 e H7 destacam que os seguidores são principalmente influenciados pelo tipo de conteúdo visual, enquanto que o emprego de fatores externos, como CTAs, parcerias e hashtags, não exibe uma diferença significativa em termos de alcance e engajamento.

## 4. Conclusão

Com base nos insights revelados, um plano de ação com estratégias de conteúdo específicas será implementado. O plano de ação priorizará a criação de vídeos curtos no formato reels dado à sua eficácia em termos de alcance e engajamento. Adicionalmente, será mantido um cronograma regular de postagens para aumentar o engajamento, com foco na otimização do tipo de conteúdo visual.

No entanto, a análise apresenta limitações devido à homogeneidade dos seguidores, sugerindo a necessidade de novas estratégias. Trabalhos futuros poderão incluir análises de sentimentos para compreender as reações emocionais dos seguidores e adaptar o conteúdo conforme suas preferências. Além disso, é recomendada a análise de grupos heterogêneos para avaliar variações na resposta às estratégias de conteúdo.

Apesar das limitações deste estudo, os resultados da análise são uma fonte valiosa de conhecimento e inspiração para futuras investigações. Os processos de simulação e seus resultados fornecem orientações cruciais para pesquisas posteriores, ajudando no desenvolvimento de estratégias mais eficazes para aumentar o engajamento e alcance nas redes sociais, beneficiando o projeto Katie e outras contas do Instagram.
