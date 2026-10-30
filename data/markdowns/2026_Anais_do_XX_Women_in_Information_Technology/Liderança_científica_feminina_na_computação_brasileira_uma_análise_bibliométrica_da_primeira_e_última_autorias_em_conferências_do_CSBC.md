# Liderança científica feminina na computação brasileira: uma análise bibliométrica da primeira e última autorias em conferências do CSBC

Érica Carneiro, Gustavo Guedes

1Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ)

erica.silva@aluno.cefet-rj.br, gustavo.guedes@cefet-rj.br

Abstract. In Computer Science, first authorship is often associated with direct involvement in the study, whereas last authorship is related to seniority and supervision. This work analyzes papers published in conferences of the Brazilian Computer Society Congress (CSBC) over an eight-year period. Initially, it presents an overview of the distribution of female and male authorship in the analyzed publications. It then investigates the representation of women in first- and last-author positions, contributing to the understanding of gender asymmetries.

Resumo. Na Computação, a primeira autoria costuma estar associada ao envolvimento direto com o estudo, enquanto a última se relaciona à senioridade e à supervisão. Este trabalho analisa artigos publicados em conferências do Congresso da Sociedade Brasileira de Computação (CSBC) ao longo de oito anos. Inicialmente, apresenta uma visão geral da distribuição da autoria entre os gêneros feminino e masculino nas publicações analisadas. Em seguida, investiga a representação feminina nas posições de primeira e última autoria, contribuindo para a compreensão de assimetrias de gênero.

## 1. Introdução

A posição na lista de autores é frequentemente usada como um indicador indireto, embora imperfeito, da distribuição de crédito e responsabilidade científica. Em diferentes áreas, a primeira autoria costuma estar associada à condução do estudo e à redação do manuscrito, enquanto a última se relaciona à senioridade, supervisão ou liderança do grupo de pesquisa [Tscharntke et al., 2007; Costas and Bordons, 2011]. Essa distinção é relevante para estudos de gênero: West et al. [2013] observaram que as mulheres apresentavam avanços limitados na primeira autoria e permaneciam fortemente sub-representadas na última, enquanto Larivière et al. [2013] identificaram disparidades globais de gênero na produção científica e no reconhecimento acadêmico. Na Ciência da Computação, embora as convenções de ordenação variem entre subáreas, Fernandes et al. [2022] observaram, a partir da trajetória de ACM Fellows, que pesquisadores em estágios iniciais tendem a aparecer nas primeiras posições, enquanto pesquisadores mais seniores tendem a aparecer nas últimas. Essa distinção também é operacionalizada por bases bibliométricas consolidadas. No Web of Science/InCites, a posição de autoria é disponibilizada como dimensão de análise, permitindo filtrar e calcular indicadores para First Author, Last Author e Corresponding Author [Clarivate, 2024]. No Scopus, a documentação do perfil de autor associa a primeira autoria à contribuição mais significativa e a última autoria ao papel de supervisão ou pesquisador principal, oferecendo métricas específicas por posição, como número de documentos, citações médias e FWCI [Elsevier, 2026].

Com base nesse referencial, este trabalho trata a primeira e a última autoria como indicadores bibliométricos indiretos de protagonismo e de senioridade ou supervisão, reconhecendo os limites dessa inferência. Essa escolha analítica é relevante porque pesquisas recentes mostram que a desigualdade de gênero na ciência não se limita à participação geral, mas também afeta a atribuição de crédito e a ocupação de posições de maior prestígio acadêmico [Ross et al., 2022; Barreiro-Gen et al., 2022]. Já no contexto brasileiro, alguns trabalhos vêm discutindo a presença de mulheres na Computação a partir de diferentes recortes. Santana and Braga [2020] analisaram as publicações do Congresso da Sociedade Brasileira de Computação (CSBC) sob a perspectiva da participação feminina, enquanto Soares et al. [2023] investigaram a distribuição de gênero entre autores de artigos apresentados em eventos do CSBC. Outros estudos se concentraram em mapear a produção da SBC sobre a temática Mulheres na Computação [Nolasco et al., 2023].

Embora essas investigações sejam fundamentais para compreender a presença feminina na Computação brasileira, a distribuição de gênero em posições estratégicas de autoria permanece pouco explorada. Nesse sentido, considerar apenas a presença numérica de autoras não permite inferir como protagonismo científico e senioridade acadêmica se distribuem entre a autoria masculina e feminina. Diante disso, este trabalho analisa a representação feminina nas posições de primeira e última autoria em artigos publicados em conferências do CSBC, com uma abordagem bibliométrica aplicada a trabalhos de doze eventos ao longo de oito anos. Para isso, caracteriza-se inicialmente a composição de gênero das equipes autorais; em seguida, examinam-se especificamente a primeira e a última autoria, buscando identificar padrões de participação feminina em posições associadas ao protagonismo na execução da pesquisa e à senioridade ou supervisão científica. O estudo também se articula a agendas públicas mais amplas de promoção da igualdade de gênero, como o Objetivo de Desenvolvimento Sustentável 5, promovido pela Organização das Nações Unidas. Assim, busca-se contribuir para uma compreensão mais refinada das dinâmicas de gênero na produção científica da Computação no Brasil.

Este artigo está organizado em quatro seções, além desta introdução. A Seção 2 apresenta os trabalhos relacionados, a Seção 3 descreve a metodologia, a Seção 4 discute os resultados e a Seção 5 reúne as considerações finais.

## 2. Trabalhos Relacionados

Estudos bibliométricos mostram que a desigualdade de gênero na ciência não se manifesta apenas na participação de mulheres, mas também na distribuição de posições de autoria. West et al. [2013], a partir de uma análise da produção científica indexada na base JSTOR, observaram que as mulheres apresentavam avanços limitados na primeira autoria e permaneciam fortemente sub-representadas na última autoria. Em perspectiva global, Larivière et al. [2013] também identificaram disparidades de gênero na ciência, indicando que os desequilíbrios permaneciam visíveis na produção e no reconhecimento acadêmico.

Além da distribuição das posições de autoria, a literatura evidencia desigualdades na atribuição de crédito científico. Ross et al. [2022], com base em dados de equipes de pesquisa, produção científica e atribuição de autoria, mostraram que mulheres são menos propensas do que homens a receber crédito de autoria, padrão observado em diferentes fontes de dados, campos científicos e estágios de carreira. Esse resultado sugere que a desigualdade de gênero na autoria científica não decorre apenas da participação quantitativa,

mas também de mecanismos de reconhecimento e visibilidade no interior das equipes.

No caso da Computação, Fernandes et al. [2022] analisaram a evolução da posição de autores ao longo da carreira com base em pesquisadores prestigiados, em especial ACM Fellows. Os autores partiram da hipótese de que pesquisadores mais jovens tendem a aparecer nas primeiras posições da lista de autores, enquanto pesquisadores mais seniores tendem a ocupar a última posição. Os resultados confirmam essa hipótese e sustentam que, embora não seja uma convenção uniforme em todas as subáreas, a última autoria pode ser interpretada como um indicador bibliométrico indireto de senioridade e supervisão na Computação.

No contexto brasileiro, Santana and Braga [2020] desenvolveram um trabalho pioneiro sobre o tema ao conduzir uma análise cienciométrica das publicações do CSBC sob a perspectiva da participação feminina. Mais recentemente, Soares et al. [2023] investigaram a distribuição de gênero entre autores de artigos publicados em eventos do CSBC nos cinco anos anteriores ao estudo e identificaram predominância masculina na autoria dos trabalhos analisados. Em um recorte complementar, Nolasco et al. [2023] mapearam as publicações da SBC sobre a temática Mulheres na Computação e mostraram que o assunto se distribui por diferentes veículos da sociedade, com forte concentração no WIT.

Esses estudos mostram avanços na caracterização da presença feminina na Computação, mas ainda exploram pouco a distribuição de gênero em posições estratégicas de autoria. É nessa lacuna que este trabalho se insere, ao investigar a representação feminina na primeira e na última autoria em conferências do CSBC.

## 3. Material e métodos

Este estudo analisa artigos publicados em anais do CSBC no período entre 2018 e 2025. Para definir o conjunto de eventos investigados, adota-se o recorte utilizado por Soares et al. [2023], contemplando as 12 conferências apresentadas na Tabela 1.

|Sigla|Evento|Tipo|Qtd|
|---|---|---|---|
|BraSNAM|Brazilian Workshop on Social Network Analysis and Mining|Satélite|184|
|BreSci|Brazilian e-Science Workshop|Satélite|120|
|CTD|Concurso de Teses e Dissertações da SBC|Base|131|
|ENCompIF|Encontro Nacional de Computação dos Institutos Federais|Satélite|129|
|ETC|Encontro de Teoria da Computação|Satélite|244|
|SBCUP|Simpósio Brasileiro de Computação Ubíqua e Pervasiva|Satélite|138|
|SEMISH|Seminário Integrado de Software e Hardware|Base|216|
|WASHES|Workshop sobre Aspectos Sociais, Humanos e Econ. de Soft.|Satélite|97|
|WCAMA|Workshop de Comp. Apli. à Gestão do Meio Amb. e Rec. Nat.|Satélite|164|
|WEI|Workshop sobre Educação em Computação|Base|478|
|WIT|Women in Information Technology|Base|366|
|WPerformance|Workshopem Desemp. de Sist. Comput. e de Comunicação|Satélite|125|

#### Tabela 1. Conferências do CSBC analisadas neste estudo, com base em Soares et al. [2023]. O conjunto reúne 2.392 trabalhos de 12 eventos no período de 2018 a 2025.

Os dados foram coletados por meio de web scraping, com uso da biblioteca Selenium em Python, a partir dos anais do SBC OpenLib. Para cada trabalho, foram extraídos

> 1https://sol.sbc.org.br/index.php/anais

o nome do evento, o ano de publicação, o título do artigo e a lista de autores com a ordem preservada. Foram considerados resumos estendidos, pôsteres, artigos curtos, artigos longos, ensaios, artigos de pesquisa, relatos de experiência ou intervenção, teses de doutorado e dissertações de mestrado, estas duas últimas vinculadas ao CTD. Ao todo, o corpus final compreende 2.392 trabalhos.

Diferentemente de estudos anteriores, esta pesquisa se concentra na distribuição de gênero dos autores, partindo de uma análise geral da composição das equipes autorais e, em seguida, examinando posições estratégicas de autoria. Assim, para cada trabalho, identificam-se a primeira e a última autoria, buscando examinar a representação feminina tanto em posições associadas ao protagonismo na execução da pesquisa quanto em posições relacionadas à senioridade, à supervisão ou à liderança científica.

Visto que os anais não informam o gênero dos autores, foi efetuada uma etapa de rotulação manual, na qual dois pesquisadores classificaram cada caso, com divergências resolvidas por consenso. Quando o gênero não pôde ser inferido a partir do nome, foram feitas consultas à Plataforma Lattes, ao Google Scholar e a mecanismos de busca. Foi adotada a classificação em feminino e masculino, uma vez que o nome sozinho não permite inferir com segurança a identidade de gênero.

A unidade de análise empregada foi o trabalho individual, e não o autor de forma única. Assim, autores e autoras que publicaram mais de uma vez, no mesmo evento ou em anos distintos, foram contabilizados a cada nova ocorrência.

## 4. Resultados

Inicialmente, apresenta-se uma visão geral da composição de gênero das equipes autorais nas conferências. Em seguida, examinam-se as posições de primeira e última autoria, com ênfase na representação feminina em posições estratégicas da produção.

### 4.1. Panorama da composição de gênero das equipes autorais

Busca-se, a princípio, caracterizar a composição de gênero das equipes autorais para apresentar um panorama que contextualize os resultados relativos à primeira e à última autoria. Utilizam-se dois indicadores complementares: o índice de Blau, como medida de heterogeneidade de gênero das equipes, e o indicador de predominância de gênero (IPG), como medida da direção da predominância masculina ou feminina.

O índice de Blau é uma medida clássica de heterogeneidade categórica, calculada por meio da expressão B = 1 − p i cada categoria Blau [1977]. No presente estudo, o índice é calculado para cada artigo a partir das proporções de autores e autoras em sua equipe. Nesse caso, o valor do índice varia entre 0 e 0, 5: valores próximos de 0 indicam equipes homogêneas, compostas predominantemente por um único gênero, enquanto valores mais próximos de 0, 5 indicam equipes mais equilibradas. Após o cálculo individual por artigo, obtém-se a média do índice por conferência em cada ano, permitindo observar padrões agregados de diversidade.

A Figura 1 apresenta o heatmap do índice de Blau por conferência e ano. De modo geral, observa-se que a maior parte das conferências apresenta valores intermediários, sugerindo equipes com alguma composição mista de gênero, mas ainda distantes de equilí-

> 2Conjunto de dados anonimizado: https://eic.cefet-rj.br/mmcomp/CSBC2018-2025.

brio pleno. Conferências como WEI, BraSNAM e, em alguns anos, BreSci e WASHES, apresentam valores mais elevados, indicando maior heterogeneidade de gênero em suas equipes. Em contraste, CTD e WPerformance exibem, de modo recorrente, alguns dos menores valores do índice, o que sugere equipes mais homogêneas. Esses resultados indicam que, mesmo quando há autores do gênero feminino e masculino nos artigos, o grau de equilíbrio entre esses grupos varia de forma importante entre as conferências.

Uma limitação do índice de Blau decorre do fato de que equipes com maioria masculina e maioria feminina podem apresentar níveis semelhantes de heterogeneidade, como, por exemplo, ocorre em 2022, com WIT em 0,14 e WPerformance em 0,16. Para suprir essa limitação, calcula-se também o IPG de cada artigo: a diferença entre o número de autoras e o número de autores, dividida pelo total de autores do trabalho, isto é, IPG = <u>FF</u> − + <u>MM</u> masculino na equipe autoral. Esse indicador varia entre − 1 e 1: valores negativos indicam predominância masculina, valores positivos indicam predominância feminina e valores próximos de zero correspondem a equipes mais equilibradas. Assim como no caso do índice de Blau, o IPG é calculado por artigo e, em seguida, tem sua média obtida por conferência em cada ano.

|BraSNAM|0_.31|0.19|0.29|0.19|0.24|0.29|0.23|0.28|0.5 Blau|
|---|---|---|---|---|---|---|---|---|---|
|BreSci|0.3|0.18|0.28|0.24|0.2|0.37|0.25|0.22||
|CTD|0.2|0.14|0.17|0.06|0.11|0.15|0.13|0.11|0.4|
|ENCompIF|0.2|0.3|0.27|0.26|0.24|0.27|0.23|0.19||
|ETC cia|0.22|0.15|0.16|0.22|0.2|0.16|0.23|0.12|03|
|SBCUP rên|0.26|0.08|0.21|0.22|0.22|0.26|0.28|0.26|.|
|SEMISH nfe|0.24|0.24|0.27|0.19|0.22|0.18|0.3|0.16||
|WASHES Co|0.13|0.26|0.23|0.23|0.25|0.34|0.21|0.32|0.2|
|WCAMA|0.24|0.3|0.14|0.22|0.34|0.22|0.31|0.26||
|WEI|0.31|0.28|0.32|0.32|0.34|0.26|0.28|0.3|0.1|
|WIT|0.22|0.14|0.17|0.12|0.14|0.19|0.16|0.19||
|WPerformance|0.13|0.08|0.21|0.27|0.16|0.08|0.25|0.14|0|
||2018|2019|2020|2021 A|2022 no|2023|2024|2025||

Figura 1. _Heatmap do Índice de Blau por conferência/ano. Valores variam de 0 a 0,5.

A Figura 2 mostra o heatmap do IPG por conferência e ano. Observa-se predominância masculina em praticamente todas as conferências analisadas, evidenciada pela recorrência de valores negativos ao longo dos anos. Esse padrão é acentuado no CTD, SBCUP, ETC e WPerformance, cujos valores permanecem distantes de zero e concentrados na faixa negativa. Em contrapartida, o WIT constitui uma exceção clara, apresentando saldo positivo em todos os anos analisados, o que indica predominância feminina sistemática em suas equipes autorais. Algumas conferências, como BraSNAM, BreSci, WEI e WASHES, exibem valores negativos menos intensos em determinados anos, sugerindo

20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

uma composição menos assimétrica, ainda que majoritariamente masculina.

Figura 2. Heatmap do IPG de gênero por conferência e ano. Valores negativos indicam predominância masculina; valores positivos indicam predominância feminina.

Em conjunto, as Figuras 1 e 2 permitem uma leitura complementar da composição de gênero das equipes. Enquanto o índice de Blau evidencia o grau de heterogeneidade das equipes, o IPG sinaliza a predominância masculina ou feminina. Essa leitura combinada sugere que, embora existam diferenças relevantes nos níveis de diversidade de gênero, a produção científica analisada permanece marcada por predominância masculina, com exceção do WIT. Esse panorama contextualiza a análise da primeira e da última posição de autoria.

### 4.2. Representação feminina nas posições de primeira e última autoria

No conjunto dos 2.392 trabalhos analisados, identificam-se 840 artigos com primeira autoria feminina, o que corresponde a 35,12% do total, e 848 artigos com última autoria feminina, equivalentes a 35,45%. Em termos agregados, portanto, a diferença entre as duas posições é pequena, com ligeira vantagem da última autoria feminina sobre a primeira, de apenas 0,33 ponto percentual. Esse resultado sugere que, no plano global do corpus, a participação feminina em posições de protagonismo inicial e em posições associadas à senioridade apresenta magnitude semelhante. Entretanto, a análise por conferência revela variações importantes.

A Figura 3 mostra que a distribuição da autoria feminina por conferência é desigual. Nesse recorte, o WIT se destaca em ambas as posições, com 94,81% de primeira autoria feminina e 80,60% de última autoria feminina, constituindo-se como um caso singular no conjunto analisado. Em seguida, o WEI também apresenta valores elevados, com 36,19% de primeira autoria feminina e 41,00% de última autoria feminina. Em contraste, conferências como CTD, WPerformance e SBCUP exibem os menores percentuais de

autoria feminina, especialmente na primeira posição, reforçando a persistência de assimetrias de gênero em parte da produção científica analisada.

Figura 3. Representação feminina na primeira e na última autoria por conferência. Os rótulos indicam o percentual e, entre parênteses, o número absoluto.

Quando se compara diretamente a primeira à última autoria feminina por conferência, observam-se padrões distintos. Em seis eventos, a participação feminina é maior na última autoria do que na primeira, com destaque para BraSNAM (+12, 5 p.p.), SBCUP (+12, 32 p.p.) e CTD (+9, 93 p.p.). Em outros eventos, verifica-se o movimento inverso, isto é, maior participação feminina na primeira autoria do que na última, como em WIT ( − 14, 21 p.p.), ENCompIF ( − 8, 52 p.p.) e WASHES ( − 6, 19 p.p.). Esses resultados sugerem que a presença feminina em posições estratégicas não se distribui de maneira uniforme entre protagonismo inicial e senioridade, variando conforme a comunidade científica de cada conferência.

A análise temporal, apresentada nos heatmaps das Figuras 4 e 5, reforça essa heterogeneidade. No caso da primeira autoria feminina, o WIT apresenta percentuais elevados ao longo de toda a série histórica, variando entre 88,1% e 100,0%. O WEI também se destaca por manter valores consistentemente superiores aos da maior parte das demais conferências, oscilando entre 31,2% e 42,5%. Em contraste, CTD e WPerformance permanecem em patamares mais baixos na maior parte do período. Algumas conferências, como BreSci e WASHES, exibem oscilações mais acentuadas entre os anos, o que sugere que seus percentuais podem ser mais sensíveis à variação no volume anual de trabalhos.

Em relação à última autoria feminina, o padrão geral permanece semelhante, mas com nuances relevantes. Novamente, o WIT ocupa posição de destaque, com percentuais entre 70,4% e 90%, indicando forte presença feminina também em posições associadas à senioridade. Na sequência, o WEI aparece como a segunda conferência com maior presença feminina na última autoria, alcançando 54% em 2023 e mantendo valores su-

- 20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

Figura 5. Heatmap da última autoria feminina por conferência e ano.

periores a 40% em diferentes anos. O BraSNAM também chama atenção por registrar crescimento da última autoria feminina em alguns anos, chegando a 59,3% em 2023. Por outro lado, CTD, WPerformance e parte das séries de ETC e SBCUP mantêm percentuais baixos de última autoria feminina, o que sugere menor inserção feminina em posições de supervisão científica.

Uma dimensão adicional da análise consiste nas combinações entre os gêneros da primeira e da última autoria. No corpus completo, a combinação M-M é a mais frequente, com 1.186 artigos (49,58%), seguida por F-F, com 482 artigos (20,15%), M-F, com 366

artigos (15,3%), e F-M, com 358 artigos (14,97%). Em termos agregados, observa-se, portanto, que em praticamente metade dos trabalhos predomina o gênero masculino na primeira e na última autoria (M-M), ao passo que as combinações mistas somadas correspondem a 30,27% dos artigos. Desse modo, embora a configuração predominantemente masculina ainda seja a mais recorrente, há uma parcela relevante de trabalhos em que a autoria é compartilhada entre os gêneros.

Percentual (%)

Figura 6. Distribuição das combinações de primeira e última autoria por conferência.

A Figura 6 mostra que essa distribuição varia entre as conferências. O WIT constitui novamente um caso singular, com predominância da combinação F-F (76,8%) e ocorrência reduzida de M-M (1,4%). Já em eventos como CTD e WPerformance, a combinação M-M domina amplamente, correspondendo a 77,9% e 72,8% dos artigos, respectivamente. O WEI, por sua vez, apresenta uma distribuição mais equilibrada, com 41,2% de M-M, 22,6% de M-F, 17,8% de F-M e 18,4% de F-F, sugerindo uma configuração menos concentrada em um único padrão de composição. Além disso, algumas conferências, como WASHES e ENCompIF, apresentam presença elevada de combinações mistas, refletindo uma distribuição mais diversa.

### 4.3. Síntese dos resultados

Os resultados obtidos mostram que a análise da ordem de autoria amplia a compreensão da participação feminina na produção científica da Computação brasileira. Na primeira etapa, a caracterização da composição de gênero das equipes autorais revela que, embora haja heterogeneidade entre as conferências, a predominância masculina ainda constitui o padrão mais frequente no conjunto analisado. O índice de Blau indica níveis variados de diversidade de gênero entre os eventos, enquanto o IPG mostra que a maior parte das conferências se mantém em faixa negativa ao longo do período, sinalizando predominância masculina recorrente. Nesse panorama, o WIT se destaca como exceção, apresentando predominância feminina consistente; em contraste, conferências como CTD, ETC, SBCUP e WPerformance exibem menor heterogeneidade e maior concentração masculina.

A segunda etapa da análise mostra que essa composição geral não se traduz automaticamente em presença proporcional das autoras em posições estratégicas de autoria. Embora, no agregado do corpus, os percentuais de primeira e última autoria feminina sejam próximos, a análise por conferência revela diferenças importantes entre protagonismo inicial e senioridade. WIT e WEI apresentam os maiores percentuais femininos em ambas as posições, sugerindo contextos mais favoráveis à inserção feminina em posições de visibilidade e supervisão. Em contraste, CTD, WPerformance, SBCUP e ETC registram baixa participação feminina, sobretudo na primeira autoria, o que reforça a permanência de assimetrias em parte da produção.

A articulação entre as duas subseções permite uma leitura mais precisa dos achados. Em conferências com maior diversidade e menor predominância masculina, como WIT e WEI, a presença feminina tende também a ser mais expressiva na primeira e na última autoria. Já em eventos com equipes mais homogêneas e predominantemente masculinas, a baixa participação feminina se reproduz nas posições estratégicas de autoria. Esse padrão é reforçado pela análise das combinações entre primeira e última autoria, na qual a configuração M-M é a mais frequente, enquanto o WIT apresenta predominância de F-F. Em conjunto, os resultados sugerem que a desigualdade de gênero na Computação não se expressa apenas na composição das equipes, mas também na distribuição do protagonismo e da senioridade científica.

## 5. Considerações Finais

Este trabalho analisou a representação feminina nas posições de primeira e última autoria em artigos publicados em conferências do CSBC, articulando a investigação à composição de gênero das equipes. Para isso, combinou indicadores de heterogeneidade e predominância de gênero com a análise da ordem de autoria, ultrapassando a contagem agregada de autores e autoras para oferecer uma leitura mais refinada da participação feminina na produção científica da Computação brasileira.

Os resultados mostraram que a configuração mais frequente no corpus analisado foi a combinação masculino–masculino nas posições de primeira e última autoria, correspondente a 49,58% dos trabalhos. Esse dado indica que a ocupação simultânea dessas posições por autores do gênero masculino ainda constitui o padrão predominante nas publicações analisadas. Embora a participação feminina seja relevante no corpus, sua distribuição permanece desigual entre conferências e posições de autoria. O WIT e, em menor medida, o WEI apresentaram maior presença feminina tanto na primeira quanto na última autoria, enquanto eventos como CTD, WPerformance, SBCUP e ETC concentraram percentuais mais baixos. Em conjunto, esses achados sugerem que a desigualdade de gênero na Computação brasileira não se manifesta apenas em termos quantitativos, mas também na forma como protagonismo e senioridade se distribuem entre os gêneros.

Como limitação, destaca-se que a identificação de gênero foi realizada por rotulação manual a partir dos nomes dos autores e consultas complementares a fontes públicas, procedimento que, embora criterioso, não elimina completamente ambiguidades. Além disso, a interpretação da primeira e da última autoria como indicadores de protagonismo e senioridade deve ser compreendida com cautela. Como trabalhos futuros, sugere-se aprofundar a análise por trilhas temáticas e subáreas, bem como investigar redes de coautoria, recorrência de colaboração, senioridade acadêmica e filiação institucional.

## Agradecimentos

O presente trabalho foi realizado com apoio da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior, Brasil (CAPES), Código de Financiamento 001.

## Uso de Inteligência Artificial

Neste trabalho, foram utilizadas tecnologias de Inteligência Artificial Generativa como apoio à redação acadêmica. Especificamente, foi utilizada a ferramenta ChatGPT, da OpenAI, para apoio na revisão textual. Todas as decisões analíticas, interpretativas e redacionais finais permanecem sob responsabilidade integral dos autores.
