# Análise da presença feminina no corpo docente e sua relação com o corpo discente feminino nos cursos de TIC

Laís Pisetta Van Vossen, Maria Teresa Silva Santos, Daniella Martins Vasconcellos, Guilherme Tomaselli Borchardt, Carlos Daniel Schmitt Bunn, Eric Carvalho da Silveira, Isabela Gasparini, Luciana Bolan Frigo

1Universidade do Estado de Santa Catarina (UDESC)

Joinville, Santa Catarina, Brasil

2Universidade Federal de Santa Catarina (UFSC) Araranguá, Santa Catarina, Brasil

{ lais.vossen, maria.santos2805, daniella.vasconcellos, guilherme.borchardt, carlos.bunn, eric.silveira } @edu.udesc.br, isabela.gasparini@udesc.br, luciana.frigo@ufsc.br

Abstract. According to the Organization for Economic Cooperation and Development, women make up the majority of teachers at all levels of education in many countries, however, in Information Technology and Communication (ITC) courses, this reality is different. This study analyzed data from Brazilian higher education institutions from 2015 to 2019 in universities that offer only ITC courses. The aim was to evaluate the impact of having a higher proportion of female teachers on female presence and dropout rates in these courses. The results indicate a positive correlation between a higher percentage of female teachers and a greater number of female students, as well as a decrease in their dropout rates in ITC courses.

Resumo. Segundo a Organização para a Cooperação e Desenvolvimento Econômico, as mulheres são maioria dos docentes em todos os níveis de ensino em diversos países, no entanto, em cursos de Tecnologia da informação e Comunicação (TIC), essa realidade é diferente. Este estudo analisou dados do ensino superior brasileiro de 2015 a 2019 em universidades que oferecem apenas cursos de TIC. O objetivo foi avaliar o impacto de ter um corpo docente com mais mulheres na presença e evasão feminina nesses cursos. Os resultados indicam que há uma correlação positiva entre a maior porcentagem de professoras e uma maior quantidade de estudantes mulheres e a diminuição de sua evasão nos cursos.

## 1. Introdução

A análise de dados educacionais é uma ferramenta poderosa na luta contra a evasão educacional e na promoção da diversidade nas instituições de ensino. A partir dos dados coletados é possível identificar padrões e tendências que podem ajudar a prevenir evasões e contribuir com a criação de programas e políticas públicas de retenção de estudantes. No Brasil, organizações como o Instituto Nacional de Estudos e Pesquisas Educacionais

Anísio Teixeira (INEP) se dedicam a coletar e disponibilizar publicamente dados sobre o ensino em diversos contextos, inclusive no ensino superior.

Outro aspecto importante que a pesquisa com dados educacionais acarreta é a possibilidade de observar a disparidade de gênero (apenas feminino e masculino de acordo com a variável TP ~~S~~ EXO utilizada pelo INEP) no ensino superior. Esta disparidade é um fenômeno bastante comum na área de tecnologia, tanto no Brasil, em que apenas 17% dos concluintes de cursos de tecnologia entre 2000 e 2013 eram mulheres [Maia 2016], mas também em outros países, como é o caso dos Estados Unidos, em que em 2020, apenas 26% dos bacharéis na área eram mulheres [NCSES 2023].

As escolhas das meninas e mulheres pela área de TIC são influenciadas por diversos fatores socioculturais. No entanto, segundo West et al. (2009), as professoras desempenham um papel significativo nessa decisão, uma vez que mulheres tendem a se interessar mais por cursos na área de ciências, tecnologia, engenharia e matemática ( Science, Technology, Engineering and Mathematics, ou STEM) quando são ensinadas por professoras em disciplinas introdutórias de ciências e matemática nas universidades. Além disso, um corpo docente composto por mais professoras resulta em um melhor desempenho das meninas em matemática já no ensino fundamental [UNESCO 2018].

Considerando o que foi apresentado, o objetivo deste trabalho é entender o cenário brasileiro na relação de estudantes e docentes do sexo feminino, utilizando dos microdados do ensino superior disponibilizados pelo INEP, dos anos de 2015 a 2019. Com isso, busca-se analisar uma possível influência na retenção e acréscimo do número de mulheres em cursos de tecnologia que um corpo docente com mais professoras no ensino superior poderia proporcionar.

Para isso, as seguintes questões de pesquisa foram levantadas para serem respondidas no decorrer deste artigo: Q1: Em faculdades na área de TIC com uma porcentagem maior de professoras, há mais estudantes mulheres? Q2: Em faculdades na área de TIC com uma porcentagem maior de professoras, há uma evasão menor entre as estudantes mulheres? A escolha deste cenário se deu por uma limitação técnica da base de dados, em que não era possível associar docentes a um curso ou categoria de curso, somente a uma instituição. Portanto, a única forma de analisar apenas aqueles que ministram aulas na área de Tecnologia da Informação e Comunicação (TIC) foi selecionando aqueles que trabalham em instituição que possuem unicamente cursos de TIC.

Este trabalho se divide em seis seções. A seção 1 apresenta a introdução, objetivos do artigo e as questões de pesquisa. A seção 2 traz os trabalhos relacionados com o tema. Na seção 3 são apresentados os procedimentos metodológicos e uma análise geral dos dados utilizados nesse artigo. A seção 4 apresenta a forma como os dados foram analisados. Na seção 5 são apresentadas as análises a fim de responder as questões de pesquisa. A seção 6 possui as conclusões do artigo, seguido da apresentação dos trabalhos futuros.

## 2. Trabalhos relacionados

A importância do docente na educação e sucesso de estudantes na área de STEM é uma problemática bastante discutida na literatura, e os vieses de gênero que carregam pode

> 1https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

influenciar a escolha de evadir do curso ou continuar os estudos na área. Como visto em Amador et al. (2021), o papel do docente nessa escolha inicia já no ensino fundamental, onde estudantes começam a perguntar sobre carreiras para os docentes no quarto ano. Isso evidencia o potencial do docente em ser um aliado na divulgação das áreas de tecnologias para as meninas, que hoje são minoria nos cursos de TIC.

Além disso, a relação do docente com os estudantes pode afetar significativamente a trajetória acadêmica, visto que, segundo o estudo de [Bardagi and Hutz 2012], os estudantes relataram que seu relacionamento interpessoal com colegas e docentes contribuía tanto para postergar a saída do curso (em situações em que o relacionamento era percebido como positivo), quanto para justificar a evasão (em situações em que o relacionamento era percebido como negativo).

Esta relação docente e estudante é impactada também por vieses de gênero, visto que o estilo de ensino pode perpetuar estereótipos, se tornando um agravante na questão da evasão feminina [Isphording et al. 2019]. Em especial, na área de STEM, o sexo do docente pode afetar não apenas o desempenho das mulheres do curso, mas também sua perseverança na conclusão do mesmo [West et al. 2009]. Além disso, estudantes mulheres tendem a se sentir mais pertencentes a área de STEM quando estão na presença de professoras que as inspiram [Dennehy and Dasgupta 2017].

Este trabalho se diferencia dos demais por realizar uma análise mais quantitativa dos dados para observar essa influência do sexo do docente na presença e evasão feminina. Além disso, este artigo trata um cenário bastante amplo por analisar dados de diversas instituições brasileiras, tanto privadas quanto públicas.

## 3. Metodologia

Este artigo tem como cenário de pesquisa, todas as Instituições de Ensino Superior (IES) que possuem apenas cursos de tecnologia, classificados desta forma pela Classificação Internacional Normalizada da Educação Adaptada para Cursos de Graduação e Sequenciais (CINE). Além disso, foram escolhidas apenas as instituições que possuíam dados em todos os anos de 2015 a 2019 para uma melhor análise. Sendo assim, as instituições retornadas da busca foram as seguintes:

- Faculdade de Ciências Tecnológicas de Fortaleza (FCTFOR)

- Faculdade Tecnologia Eduvale — Avaré (FATEC EDUVALE)

- Faculdade Cotemig (COTEMIG)

- Faculdade de Educação Tecnológica do Estado do Rio de Janeiro FAETERJ da cidade de Rio de Janeiro (FAETERJ R DE JANEIRO) e de Petrópolis (FAETERJ PETR OPOLIS)

- Faculdade de Tecnologia Informática (FATI)

- Faculdade de Computação de Montes Claros (FACOMP)

- Faculdade de Tecnologia Bandeirantes (BANDTEC)

- Faculdade JK de Tecnologia (FACJK)

- Faculdade de Tecnologia Alcides Maya (AMTEC)

- Faculdade JK Brasília — Recanto das Emas II (FAJKEMASII).

Destas, a faculdade FAJKEMASII possuía outro nome nos anos de 2015 e 2016, sendo chamada de Faculdade de Tecnologia Rogacionista, então para facilitar a análise

dos dados e produção de gráficos, o nome foi padronizado para o mais recente, e a sigla FAJKEMASII foi adotada.

Para obter a base de dados que gerou os gráficos das análises realizadas, foram utilizadas a linguagem de programação Python em conjunto com bibliotecas de análise de dados para processar as bases de dados do INEP de docentes, de IES e de alunos dos anos 2015 a 2019. Para a limpeza da base, foram preenchidos dados faltantes, como a sigla de duas universidades, a FACOMP, que não estava preenchida em 2018 e 2019, e a FAJKEMASII. O código responsável por isso se encontra disponível no GitHub.

Os dados utilizados nas análises presentes nas seções 4 e 5 foram fornecidos pelo INEP e portanto, todas categorias de análises se baseiam nas divisões feitas na própria base, então, por conta disso, uma divisão binária rasa de sexo (feminino e masculino) foi aplicada, mesmo sabendo que esta se trata de uma construção cultural e uma divisão mais diversa representaria melhor o mundo que nos cerca. Além dessa limitação, a pesquisa se restringiu aos anos de 2015 a 2019 por conta do formato dos dados, já que a partir de 2020 a forma de disponibilizar esses dados foi alterada e impossibilitou análises como as feitas neste artigo.

## 4. Análise de dados

Esta seção tem o objetivo de apresentar como são os dados analisados, dando um panorama sobre as universidades escolhidas e observando as relações de gênero (apenas feminino e masculino conforme a variável TP ~~S~~ EXO utilizada pelo INEP) dos estudantes destas universidades, bem como produzindo gráficos e análises para observar essa relação de sexo no corpo docente. Para isso, inicia-se pontuando que cinco das universidades são privadas com fins lucrativos (AMTEC, BANDTEC, COTEMIG, FACOMP e FATI), quatro são privadas sem fins lucrativos (FACJK, FAJKEMASII, FCTFOR e FATEC EDUVALE) e duas são públicas estaduais (FAETERJ DE R JANEIRO e FAETERJ PETR OPOLIS).

Figura 1. Porcentagem de docentes mulheres e homens em todas as instituiç ões por ano.

2https://github.com/Artigos-e-Amigos/WIT-2023

Além disso, os gráficos presentes nessa seção tratam de valores em porcentagens, então, para que se tenha uma noção da grandeza dos dados apresentados, a Tabela 1 traz os valores absolutos da quantidade de estudantes que estão cursando ou formados e docentes homens e mulheres dividido por instituição, considerando o total ao longo dos anos de 2015 a 2019.

<u>Tabela 1. Quantidade absoluta de estudantes e docentes Homens e Mulheres</u>

||Estud|antes|Doce|ntes|
|---|---|---|---|---|
||Homem|Mulher|Homem|Mulher|
|AMTEC|754|77|82|15|
|BANDTEC|1308|255|72|23|
|COTEMIG|1218|185|73|14|
|FACJK|652|110|100|18|
|FACOMP|796|128|60|35|
|FAETERJ PETROPOLIS|1707|323|106|32|
|FAETERJ R DE JANEIRO|1466|343|92|32|
|FAJKEMASII|249|22|49|10|
|FATEC EDUVALE|326|46|47|5|
|FATI|124|15|44|23|
|FCTFOR|252|35|45|26|

A Figura 1 apresenta a porcentagem de docentes femininas e masculinos, por ano, em todas as universidades observadas. Com isso, é possível observar que há uma redução do corpo docente feminino, que em 2015 era de 25.33% e passou a ser apenas 18.35% em 2019, atingindo um pico de 26.48% em 2016. O baixo número de professoras não é algo que ocorre em todas as áreas. De fato, ao considerar todos os níveis de ensino, dados provenientes dos países membros da Organização para a Cooperação e Desenvolvimento Econômico (OCDE) indicam que mulheres constituem 70% do corpo docente. No entanto, essa proporção diminui à medida que o nível de ensino aumenta, e em média, nos países da OCDE, apenas 44% das docentes no ensino superior são mulheres [OECD 2019].

A Figura 2 apresenta a distribuição, em porcentagem, da escolaridade dos docentes de todas as IES observadas, dividido por sexo, considerando os dados de 2015 a 2019. Nele é possível observar que, dentre as mulheres, há uma maior porcentagem de doutoras e mestres do que entre os homens, que apresentam porcentagens maiores de docentes com especialização em comparação com outros níveis de escolaridade. Com isso, o gráfico evidencia que as mulheres tendem a ter um nível de escolaridade maior do que os homens. Isso também é observado em diversos outros países, em que a diferença de mulheres para homens que completam o bacharelado em qualquer área chega a ser de 12% [OECD 2022].

A Figura 3 apresenta a porcentagem de estudantes e docentes femininas por universidade em todos os anos analisados, ocultando a porcentagem de docentes masculinos

Figura 2. Porcentagem de escolaridade docente por sexo.

Figura 3. Porcentagem de estudantes e docentes mulheres por instituiç ão.

de ambas as categorias a fim de facilitar as análises. Nela, é possível observar que a porcentagem de estudantes femininas não ultrapassa 20% em nenhuma das IES observadas, atingindo um máximo de 18.96% na FATERJ do Rio de Janeiro, e um mínimo de 8.12% de estudantes do sexo feminino em FAJKEMASII. Analisando a porcentagem feminina de docentes, é possível observar que a universidade FATEC EDUVALE possui a menor porcentagem de docentes femininas, enquanto a FACOMP possui a maior porcentagem do corpo docente composto por mulheres. E interessante notar que a universidade FATEC EDUVALE é a única cuja porcentagem de estudantes do sexo feminino ultrapassada a de professoras.

## 5. Respostas às questões de pesquisa

Nas seções 5.1 e 5.2 são apresentadas as análises para responder às questões de pesquisa propostas. Para isso, utilizou-se da análise estatística dos dados através da correlação entre as variáveis e da realização do teste de significância do p-valor, considerando um valor de corte de 0. 05, ou seja, quando o P for < 0. 05, estamos diante de um resultado estatisticamente significativo.

### 5.1. Q1: Em faculdades na área de TIC com uma porcentagem maior de professoras, há mais estudantes mulheres?

Para responder à questão de pesquisa Q1, a Figura 4 apresenta a relação entre o percentual de mulheres no corpo docente e o percentual de estudantes do sexo feminino nas universidades. Cada ponto no gráfico representa a porcentagem de estudantes e docentes femininas em uma das onze universidades analisadas, considerando a média de 2015 a 2019. A equação polinômica na legenda é a correlação entre as duas variáveis (estudantes mulheres e docentes mulheres).

Figura 4. Percentual de estudantes e docentes mulheres em todas as instituiç ões de 2015 a 2019.

Com isso, considerando a reta presente na Figura 4, é possível afirmar que há uma correlação positiva entre ter um corpo docente mais composto por mulheres e uma quantidade maior de mulheres no curso. No entanto, por conta da baixa quantidade de dados levantados, não é possível determinar causalidade de um valor sobre o outro (pvalor = 0.621 > 0. 05).

### 5.2. Q2: Em faculdades na área de TIC com uma porcentagem maior de professoras, há uma evasão menor entre as estudantes do sexo feminino?

Para responder esta pergunta, primeiro é necessário definir evasão. Para tanto, baseouse na definição dada pela Diretoria de Estatísticas Educacionais, apresentada em [Silva Santos et al. 2022], que define como evadido, os estudantes que foram desvinculados do curso ou foram transferidos para outro curso da mesma IES, e como não evadidos, os estudantes que estão cursando, se formaram ou estão com a matrícula trancada. Importante notar que os estudantes que faleceram não se encontram em nenhuma das categorias, visto que não é possível concluir sobre suas intenções de evadir ou não do curso.

Com o conceito de evasão definido para este contexto, as Figuras 5 e 6 foram elaboradas para responder à questão de pesquisa Q2. Os gráficos apresentam a relação entre estudantes mulheres evadidas e não evadidas e a porcentagem de docentes do sexo feminino que há nas universidades. Em ambos os gráficos, os pontos representam a porcentagem de estudantes e docentes mulheres em uma das IES analisadas. O cálculo da porcentagem de estudantes evadidas se deu somando a quantidade de mulheres desvinculadas do curso e a quantidade que foram transferidas para outro curso da mesma IES e dividindo pelo total de estudantes mulheres em uma determinada universidade ao longo de 2015 a 2019. Para calcular a porcentagem de não evadidas, foi realizada uma operação similar, porém a somou-se a quantidade de estudantes que estão cursando, se formaram ou estão com a matrícula trancada.

Figura 5. Percentual de estudantes evadidas e docentes mulheres em todas as instituiç ões de 2015 a 2019.

A Figura 5 demonstra que há uma correlação negativa entre o aumento do percentual feminino no corpo docente das IES e o percentual de estudantes caracterizadas como evadidas, ou seja, uma maior presença de professoras pode ocasionar em uma menor evasão de estudantes do sexo feminino. No entanto, não é possível afirmar que essa redução de evasão é de fato causada pelo aumento de mulheres no corpo docente, há apenas uma correlação entre as variáveis que indica isso (p-valor = 0.710 > 0. 05).

De forma semelhante, a Figura 6 apresenta as estudantes não evadidas correlacionada com o aumento percentual de professoras nas IES. A reta presente no gráfico indica uma correlação positiva, porém, essa correlação não implica causalidade e seria necessários mais dados para chegar em conclusões concretas sobre a causa desse aumento (p-valor = 0.710 > 0. 05).

Figura 6. Percentual de estudantes não evadidas e docentes mulheres em todas as instituiç ões de 2015 a 2019.

## 6. Conclusão e trabalhos futuros

Este artigo teve como principal objetivo explorar o impacto que a maior presença de mulheres no corpo docente das universidades de TIC do Brasil tem sobre a quantidade de alunas mulheres e suas taxas de evasão dos cursos. Para isso, foram definidas as seguintes questões de pesquisa: Q1: Em faculdades na área de TIC com uma porcentagem maior de professoras, há mais estudantes mulheres? Q2: Em faculdades na área de TIC com uma porcentagem maior de professoras, há uma evasão menor entre as estudantes mulheres?

A questão Q1 foi respondida na seção 5.1, em que é possível notar por meio do gráfico produzido que, apesar da significância estatística ser baixa, existe uma tendência indicando que a maior presença feminina no corpo docente resulta em uma maior porcentagem de mulheres nos cursos de TIC, visto que há uma correlação positiva entre as duas variáveis. Já a questão Q2, respondida na seção 5.2 pela Figura 6, demonstra que há uma correlação positiva entre o aumento da porcentagem de mulheres no corpo docente e a porcentagem de estudantes não evadidas nesses cursos. Similarmente, a Figura 5 aponta para a diminuição da porcentagem de estudantes evadidas à medida que a porcentagem de professoras mulheres aumenta. No entanto, em ambas as questões, não foi possível determinar uma significância estatística que aponte que há uma causalidade nas correlações encontradas, portanto, é necessário a continuação dos estudos com mais dados, sejam eles qualitativos ou quantitativos.

Como sugestões de trabalhos futuros há a inclusão de mais dados para a pesquisa, de modo a produzir novas análises entre professoras e estudantes. Há também a possibilidade de ampliar o escopo dos dados, analisando não só dentro de cursos de TIC, como também cursos das outras áreas de STEM, ou considerando os dados de todos os cursos

do Brasil, independentemente da área, para observar as tendências encontradas em grande escala. Também sugere-se uma pesquisa qualitativa com as professoras das universidades selecionadas neste artigo, para entender se elas percebem e acreditam na importância que a docente mulher tem na retenção feminina em cursos de TIC.

## 7. Agradecimentos

Agradecemos o apoio do Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) 308395/2020-4, Fundação de Amparo à Pesquisa e Inovação do Estado de Santa Catarina (FAPESC) Nº 027/2020 Apoio a Infraestrutura para Grupos de Pesquisa da UDESC TO n° 2021TR795 e Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES) - Código de Financiamento 001.
