# Análise do gênero de pesquisadores em eventos do Congresso da Sociedade Brasileira de Computação

Maria Laura Soares, Anna Paula Silva, Erica Carneiro, Luciana Varjolo, Gustavo Guedes

1CEFET/RJ - Centro Federal de Educação Tecnológica Celso Suckow da Fonseca Av. Maracana, 229 - Rio de Janeiro - RJ - Brasil.

2Unirio - Centro Federal de Educação Tecnológica Celso Suckow da Fonseca Av. Pasteur, 458 - Universidade Federal do Estado do Rio de Janeiro Rio de Janeiro - RJ - Brasil.

maria.laura@aluno.cefet-rj.br, anna.silva@edu.unirio.br

erica.silva@aluno.cefet-rj.br

{ luciana.varjolo, gustavo.guedes } @cefet-rj.br

Abstract. According to IBGE data, women represent 51. 03% of the Brazilian population, but only 23% of the total amount of researchers in the field of Computing. Several social factors appear to be responsible for this gap. To mitigate gender inequality, some actions have emerged to attract women to the IT area. Given this disparity, our study aims to compare gender representation in the authorship of articles published in events of the Congress of the Brazilian Computing Society (CSBC) in the last five years. The results indicate that the authorship of articles in these events is predominantly male, reflecting the gender disparity in the field.

Resumo. Segundo dados do IBGE, as mulheres correspondem a 51, 03% da população brasileira. Apesar disso, apenas 23% do total de pesquisadores na área de Computação são do gênero feminino. Diversos fatores sociais parecem ser responsáveis por essa lacuna, porém algumas ações que visam atrair mulheres para a área de informática vêm surgindo a fim de mitigar essa questão. Diante dessa disparidade, este estudo tem como objetivo comparar a representatividade de gênero na autoria de artigos publicados em eventos do Congresso da Sociedade Brasileira de Computação (CSBC) nos últimos cinco anos. Os resultados indicam que a autoria de artigos nesses eventos é predominantemente masculina, refletindo a disparidade de gênero presente na área.

## 1. Introdução

Os dados do último Censo Demográfico (de 2010) indicaram que as mulheres correspondiam a 51, 03% da população brasileira [IBGE, 2010]. Apesar disso, de acordo com um estudo realizado por Arruda et al. [2009], apenas 23% do total de pesquisadores na área de Computação eram do gênero feminino. Há diversos fatores sociais que contribuem

> 1O Censo Demográfico de 2022 não foi disponibilizado até o envio da versão final deste artigo. Entretanto, a Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua) de 2021 indica que a população brasileira é composta por 51,1% de mulheres e 48,9% de homens [IBGE, 2022].

para essa disparidade, no entanto, estão surgindo iniciativas com o objetivo de atrair mais mulheres para a área da informática como uma tentativa de redução dessa disparidade.

A participação e produtividade de mulheres na área de Ciências Exatas e da Terra tem crescido ao longo dos anos, entretanto a literatura ainda evidencia diferenças no número de trabalhos científicos publicados por homens e mulheres [Tuesta et al., 2019; Santana and Braga, 2020]. A análise efetuada por Tuesta et al. [2019] utilizou dados extraídos da plataforma Lattes para analisar os currículos dos pesquisadores entre os anos de 1966 e 2015. O objetivo desse estudo foi avaliar a produção e participação das mulheres na área de Ciências Exatas e da Terra. Os autores evidenciaram que 66, 86% dos currículos eram de indivíduos do gênero masculino enquanto 33, 14% eram do gênero feminino.

Ao examinar a área de Ciência da Computação, a história da presença feminina remonta aos primórdios da tecnologia da Computação. Pode-se destacar a matemática Ada Lovelace, considerada a primeira programadora de computadores do mundo [Clair, 1985]. No entanto, suas realizações foram amplamente ignoradas durante décadas. Ainda hoje, a falta de representação feminina na Ciência da Computação é uma questão importante, com poucas mulheres ocupando posições de liderança e pouco reconhecimento por suas contribuições. Por exemplo, dados apresentados pela USP [2018] mostram que, na década de setenta, 70% dos discentes do curso de Ciência da Computação eram mulheres. Esses números se mantiveram estáveis até a década de oitenta, período que teve uma queda abrupta na quantidade de meninas matriculadas nos cursos de Ciências Exatas e da Terra. Atualmente, apenas 15% dos discentes são mulheres.

As razões por trás do baixo índice de mulheres atuando na Ciência da Computação são complexas e multifacetadas. Muitas vezes, as mulheres são desencorajadas a seguir uma carreira em Ciência da Computação desde cedo, devido a estereótipos sexuais que sugerem que a tecnologia é um campo “masculino”, conforme apresentado pelos estudos de Cvencek et al. [2011] e Bian et al. [2017].

Além disso, o ambiente de trabalho no campo tecnológico pode ser hostil e sexista, o que pode levar as mulheres a se sentirem desconfortáveis e não valorizadas em suas posições [Reilly et al., 2017; Funk and Parker, 2018]. Portanto, de modo a mitigar esse isolamento e tornar o ambiente mais acolhedor, grupos de mulheres da área de Computação vêm surgindo para inspirar outras a entrarem no ramo ou mesmo dar apoio e representatividade ao grupo. É o caso dos programas Programada [UFRGS, 2018], Meninas Digitais [SBC, 2018] e Brasileiras na NLP [na PLN, 2018].

De forma a evidenciar a escassez de mulheres em pesquisas científicas na área de Ciência da Computação, este artigo traz uma análise comparativa da proporção de gênero na autoria dos trabalhos publicados nos eventos do Congresso da Sociedade Brasileira de Computação (CSBC). O objetivo é analisar a representatividade de mulheres que atuam no campo científico da produção de artigos científicos. Para tanto, foram coletados dados dos últimos cinco anos dos eventos do CSBC. Em seguida, os dados foram analisados por evento e ano, contabilizando o número de autores ( i.e., homens e mulheres) em cada artigo publicado.

As definições de gênero adotadas neste trabalho basearam-se no nome social utilizado pelos autores em suas publicações, uma vez que os dados específicos de gênero

não estão disponibilizados. É importante ressaltar que essa abordagem se limita à identificação de gênero com base no nome utilizado e não abrange todas as possíveis identidades de gênero, uma vez que a concepção de gênero pode ser muito mais ampla do que os rótulos binários representados.

As demais seções estão dispostas da seguinte maneira: na seção 2 são levantados trabalhos semelhantes e relacionados ao tema; na seção 3 são apresentados detalhes sobre a aquisição dos dados e a metodologia para análise; na seção 4 são discutidos os resultados encontrados; por último, a seção 5 apresenta as conclusões, as limitações e a discussão sobre trabalhos futuros.

## 2. Trabalhos relacionados

Os estudos relacionados à participação das mulheres na pesquisa científica têm sido cada vez mais evidenciados na literatura. Geralmente, as mulheres preferem os cursos das grandes áreas apresentadas a seguir, em ordem decrescente de preferência: Ciências Humanas, Ciências da Saúde e Ciências Biológicas, Ciências Exatas e da Terra [Monard and Monteiro, 2015]. Essa preferência traz impactos na falta de representatividade feminina, não só na indústria, como no número de formandas na área de Ciências Exatas e da Terra. Nesse aspecto, diversos estudos surgiram para investigar a razão da baixa representatividade de mulheres na área de Ciências Exatas e da Terra e suas subáreas.

A partir desse panorama, Bian et al. [2017] efetuaram um experimento de estereótipo sexual com 96 crianças de 5 a 7 anos de idade. O estudo se fundamentou no fato de que estereótipos comuns associam habilidades intelectuais de alto nível ( e.g., brilho, genialidade) mais aos homens do que às mulheres. Os autores destacaram que esses estereótipos desencorajam a busca das mulheres por muitas carreiras de prestígio, ou seja, salientando que as mulheres estão sub-representadas em áreas cujos membros valorizam o brilhantismo ( e.g., Física). Os resultados do estudo sugerem uma conclusão preocupante: muitas crianças assimilam a ideia de que o brilhantismo é uma qualidade masculina. Esse estereótipo começa a moldar os interesses das crianças assim que é adquirido e, portanto, provavelmente reduzirá o leque de carreiras que um dia contemplarão.

Nesse aspecto, Tuesta et al. [2019] evidenciaram diferenças significantes no número de trabalhos científicos publicados por homens e mulheres. Em um estudo que utilizou dados da plataforma Lattes, os autores analisaram os currículos de pesquisadores entre os anos de 1966 e 2015. Seu objetivo consistiu em avaliar a produção e participação das mulheres na área de Ciências Exatas e da Terra. Os resultados indicaram que 66, 86% dos currículos compreenderam homens e somente 33, 14% foram mulheres.

O estudo desenvolvido por da Cunha et al. [2020] apresentou uma análise da comunidade acadêmica da Universidade Federal de Tocantins. Segundo os autores, no corpo docente e discente de Engenharia da Computação, a presença feminina foi de apenas 12, 5%, enquanto os homens representaram 87, 4%. O estudo também mostrou a relação de bolsistas de Iniciação Científica nas grandes áreas entre 2016 e 2019. O levantamento dos autores refletiu a grande preferência de mulheres pelas áreas de Humanas, porém curiosamente, apesar da baixa representatividade, o ano de 2016 contabilizou mais mulheres bolsistas do que homens nas áreas de Exatas.

Duarte et al. [2019] fizeram uma análise da participação das mulheres em comitês de programas de simpósios da Sociedade Brasileira de Computação (SBC) ao longo

dos anos 2011 e 2018. Segundo as autoras, 30% dos participantes foram do gênero feminino, com especial destaque para o Simpósio Brasileiro de Informática na Educação (SBIE), que conta com mais de 45% de participantes mulheres. Surpreendentemente, o trabalho apontou que, apesar desses números, a quantidade de mulheres matriculadas em Computação caiu de 16, 3% para 14% no mesmo período. Posteriormente, Lorens et al. [2020] complementaram este trabalho revelando que a presença das mulheres nos comitês de programas dos principais simpósios de computação nacionais e internacionais ocorre em áreas mais interdisciplinares, relacionadas à aplicação da computação ou com aspecto social claro.

Assim como Duarte et al. [2019], Santana and Braga [2020] também observaram que os congressos da Sociedade Brasileira de Computação (SBC) não forneceram informações quanto ao gênero de seus participantes. Análises mostraram que tanto em eventos base quanto satélites, apenas 31% foram mulheres [Santana and Braga, 2020]. Os dados foram levantados entre 2017 e 2019 ressaltando que somente 220 mulheres foram autoras principais para uma relação de 539 homens. A única exceção foi o Women in Information Technology (WIT), com 80 mulheres como primeiras autoras para sete homens. Santana and Braga [2020] ainda acrescentaram que a literatura possui trabalhos que analisaram a participação feminina em alguns eventos da SBC, todavia, até o momento de sua publicação, nenhum deles fez uma análise de todos os eventos da conferência.

O presente artigo se difere dos demais apresentados nessa seção por objetivar a comparação entre o número de autores e autoras em trabalhos de eventos do CSBC. Para isso, foram selecionados os eventos que mantiveram sua ocorrência em todos os anos entre 2018 e 2022.

## 3. Material e métodos

O presente estudo levou em consideração as publicações dos últimos cinco anos dos eventos do Congresso da Sociedade Brasileira de Computação. O primeiro passo foi verificar quais eventos aconteceriam no ano de 2023. No segundo passo, os nomes dos eventos com ocorrência em 2023 foram acessados no SBCOpenLib para aquisição dos anais dos últimos cinco anos. Dessa maneira, foram coletados os anais dos eventos que ocorreram em 2018, 2019, 2020, 2021 e 2022. No terceiro e último passo, os eventos que deixaram de ocorrer em algum desses anos foram descartados. A aquisição dos dados foi realizada manualmente da seguinte maneira: (a) foi criado um um arquivo de planilha Excel (XLSX), que foi compartilhado entre os autores do artigo; (b) foi inserida uma aba no arquivo XLSX para cada um dos eventos; (c) em cada evento ( i.e., aba da planilha), foram inseridos os dados do título do trabalho, tipo da publicação, ano, contagem de autores, contagem de autoras e total (número de autores somado ao número de autoras). Esses dados encontram-se disponíveis na página do grupo de pesquisa Meninas e Mulheres em Computação do CEFET/RJ (http://eic.cefet-rj.br/ mmcomp/csbc2018-2022/).

A Tabela 1 apresenta, em ordem alfabética, os eventos que foram considerados após os passos acima descritos. A primeira, a segunda e a terceira colunas correspondem, respectivamente, à sigla, ao nome e ao tipo do evento, que se distribuem em dois

> 2O acesso aos eventos foi efetuado em https://csbc.sbc.org.br/2023/

> 3https://sol.sbc.org.br/index.php/anais

grandes grupos: Base, com quatro eventos; e Satélite, com oito eventos. A última coluna contabiliza o número de trabalhos publicados em cada evento nos últimos cinco anos.

|Sigla|Nome do evento|Tipo|Qtd|
|---|---|---|---|
|BraSNAM|Brazilian Workshop on Social Network Analysis and Mining|Satélite|103|
|BreSci|Brazilian e-Science Workshop|Satélite|77|
|CTD|Concurso de Teses e Dissertações da SBC|Base|82|
|ENCompIF|Encontro Nacional de Computação dos Institutos Federais|Satélite|82|
|ETC|Encontro de Teoria da Computação|Satélite|145|
|SBCUP|Simpósio Brasileiro de Computação Ubíqua e Pervasiva|Satélite|90|
|SEMISH|Seminário Integrado de Software e Hardware|Base|106|
|WASHES|Anais do VII Workshop sobre Aspectos Sociais, Humanos e Econômicos de Software|Satélite|48|
|WCAMA|Workshop de Computação Aplicada à Gestão do Meio Ambiente e Recursos Naturais|Satélite|82|
|WEI|Workshopsobre Educação em Computação|Base|225|
|WIT|Women in Information Technology|Base|181|
|WPerformance|Workshop em Desempenho de Sistemas Computacionais e de Comunicação|Satélite|93|

Tabela 1. Eventos do CSBC com ocorrência em todos os seguintes anos: 2018, 2019, 2020, 2021, 2022. Quatro eventos são do tipo Base e oito são do tipo Satélite. A primeira e segunda colunas apresentam, respectivamente, sigla e nome do evento, a terceira coluna descreve o tipo do evento e a última coluna contabiliza o número de trabalhos em cada evento.

Assim como os estudos de Duarte et al. [2019] e Santana and Braga [2020], o levantamento efetuado neste trabalho não encontrou informações com relação ao gênero dos autores. Desta forma, foi necessária a rotulação manual, que foi efetuada de maneira que os pesquisadores (autores desse artigo) analisaram cada um dos trabalhos para contabilização dos nomes femininos e masculinos. Cada trabalho foi avaliado por pelo menos dois pesquisadores. As divergências foram verificadas por um terceiro pesquisador. Quando os pesquisadores não conseguiram determinar o gênero dos autores dos trabalhos pelos nomes, foram realizadas consultas na plataforma Lattes e outros sites ( e.g., LinkedIn, Google Scholar, Google).

É interessante ressaltar que houve uma divergência entre os pesquisadores na contagem de um artigo do BraSNAM (de 2018), denominado: ‘Detecção de Posicionamento em Tweets sobre Política no Contexto Brasileiro’. Ao analisar minuciosamente o caso, os pesquisadores perceberam que faltava uma vírgula entre os nomes de um autor e uma autora na página da SBCOpenLib. Da mesma forma, não havia vírgula entre os nomes desses autores no PDF. Ao final, os pesquisadores contabilizaram 4 homens e 1 mulher.

Nesta pesquisa, considerou-se os artigos das seguintes categorias: resumos estendidos, pôsteres, artigos curtos, artigos longos, ensaios, artigos de pesquisa, artigos com relatos de experiência/intervenção, teses de doutorado e dissertações de mestrado; sendo esses dois últimos relacionados ao Concurso de Teses e Dissertações. E importante pontuar que os prefácios não entraram na análise. Ao todo foram contabilizados 1314

trabalhos publicados em todas as conferências analisadas (considerando os últimos cinco anos). Nesse estudo, os gêneros dos autores e autoras foram contabilizados por trabalho e não por evento. Isso significa que autores e autoras que publicaram mais de uma vez no mesmo evento e ano foram contabilizados mais de uma vez. O que esse estudo procura evidenciar é o número de homens e mulheres nos trabalhos.

## 4. Resultados e discussão

Os resultados deste estudo são apresentados, primeiramente, em termos dos artigos publicados nos eventos Base. A Figura 1 ilustra quatro gráficos que representam os números de homens e mulheres nos trabalhos dos seguintes eventos: (a) CTD, (b) SEMISH, (c) WEI e (d) WIT. E possível notar que o CTD, SEMISH e WEI apresentam maior número de homens do que mulheres nos trabalhos. Esse resultado se inverte no WIT, podendo-se evidenciar maior número de mulheres do que de homens. E válido ressaltar que o WIT é um evento direcionado a trabalhos relevantes para mulheres na tecnologia, o que acaba as interessando mais. Um dado relevante sobre o WIT é que, em todos os anos estudados, apenas um trabalho é composto só por homens, no caso, um artigo de 2020 que possui apenas um autor.

Figura 1. Número de homens e mulheres nos trabalhos dos eventos Base do CSBC.

Dentre os eventos que possuem mais trabalhos com autores do gênero masculino ( i.e., CTD, SEMISH e WEI), o WEI é o que traz uma proporção mais equilibrada entre homens e mulheres nos trabalhos. Pode-se notar que a porcentagem de mulheres nos trabalhos esteve sempre abaixo, mas não tão abaixo como nos demais eventos: 2018 (41, 18%), 2019 (28, 73%), 2020 (39, 13%), 2021 (38, 09%) e 2022 (40, 88%). No caso

do CTD, nota-se que no ano de 2021, a porcentagem de mulheres nos trabalhos alcançou o mínimo entre os quatro eventos, totalizando 6, 98%.

É importante discutir em detalhes os resultados encontrados para o CTD (Fig. 1a), em que percebe-se uma disparidade bastante elevada entre ambos os gêneros. Esse evento traz um panorama referente às teses e dissertações desenvolvidas por discentes e seus orientadores de ambos os gêneros. No ano de 2018, foram publicados 19 artigos, cuja composição contou com 39 homens e cinco mulheres. Nos anos seguintes, as publicações passaram a ser segmentadas entre artigos de teses e dissertações, cuja distribuição é apresentada na Tabela 2. Nota-se que a maior parte de discentes e docentes nas dissertações de mestrado são homens e também há evidências de que o número de orientadoras reduziu nos anos de 2021 ( i.e., três mulheres) e 2022 ( i.e., duas mulheres). Com relação às teses de doutorado, o número de discentes é bem homogêneo, alcançando seis discentes por ano. No entanto, nenhuma mulher teve sua tese selecionada para o CTD. Apesar disso, há orientadoras de doutorado em 2019, 2020 e 2021. Essa decrescente participação de mulheres entre os anos de 2020 e 2022 pode estar relacionada ao impacto da pandemia de COVID-19. Estudos mostraram que, nesses anos de pandemia, houve uma diminuição de publicações de mulheres devido à sobrecarga de trabalho [Dunn et al., 2022; Pebdani et al., 2022]. Esse acúmulo de trabalho envolveu as demandas profissionais e as tarefas domésticas, principalmente no caso de mulheres que são mães [Bender et al., 2022].

|Ano|D|issertações|de mestra|do||Teses de|doutorado||
|---|---|---|---|---|---|---|---|---|
||Disc|entes|Doc|entes|Disc|entes|Doc|entes|
||Homens|Mulheres|Homens|Mulheres|Homens|Mulheres|Homens|Mulheres|
|2019|10|0|12|5|6|0|8|1|
|2020|9|1|10*|6|6|0|9|3|
|2021|10|0|14|3|6|0|10|0|
|2022|9|1|14|2|6|0|9|1|

Tabela 2. Distribuiç ão de discentes e docentes nas dissertaç ões de mestrado e teses de doutorado nos anos de 2019, 2020, 2021, 2022. Na tabela, o asterisco representa que embora haja 10 orientadores homens, um docente se encontra em duas dissertaç ões de mestrado.

A Figura 2 apresenta o número de autores e autoras nos trabalhos dos eventos Satélite do CSBC. Em todos os eventos observa-se que há mais homens do que mulheres e essas diferenças são mais expressivas no SBCUP (Fig. 2e) e no WPerformance (Fig. 2h). Embora o número de autores no WASHES seja consideravelmente mais baixo que nos demais (Fig. 2f), este é o evento que apresenta mais equilíbrio entre homens e mulheres em trabalhos, o que pode ser fruto das temáticas relacionadas a aspectos sociais e humanos de softwares, conforme destaca o próprio nome do evento: Workshop sobre Aspectos Sociais, Humanos e Econômicos de Software. Em seguida, o mais equilibrado é o ENCompIF, que traz uma visão do que ocorre nos institutos federais.

Os resultados encontrados nesse trabalho são coerentes com os estudos presentes na literatura científica. O número de mulheres que se inserem na área da Computação é reconhecidamente menor do que o de homens, conforme evidenciado em comitês de programas de simpósios do CSBC [Duarte et al., 2019] e em eventos do CSBC [Santana and Braga, 2020]. Não obstante, ao fazer uma análise do número de homens e mulheres em diversos eventos, encontramos que das 12 conferências analisadas, 11 trouxeram majori-

Figura 2. Número de autores masculinos e femininos nos trabalhos dos eventos Satélite do CSBC.

tariamente homens durante o período examinado. Somente no WIT houve uma maioria feminina. Esse panorama se repetiu em todos os anos estudados, sendo mais evidente nos anos de 2021 e 2022, em que a proporção de mulheres nos trabalhos alcançou 90, 04% e

### 90, 44%, respectivamente.

Esses resultados mostram que ainda há um disparate entre homens e mulheres publicando na área da Computação, mas também revelam que a comunidade científica se interessa pelo tema das mulheres na Tecnologia da Informação. Por exemplo, a edição do WIT em 2021 contou com 48 artigos publicados, só perdendo em número de artigos publicados para o WEI nos anos de 2018 e 2021, que totalizaram 49 e 50 artigos respectivamente. Esse resultado é bastante expressivo, indicando a importância que o tópico proporciona.

## 5. Conclusão

Apesar de seu destaque durante a história da computação, principalmente com Ada Lovelace [Clair, 1985], as Garotas do ENIAC, Frances Allen [Demartini, 2016] e Rosalind Pickard [Picard, 1997], as mulheres não se mantiveram na área devido a fatores sociais que contribuíram para sua falta de representatividade e falta de interesse na área. A ausência de um estímulo ao ingresso feminino em STEM (Ciência, Tecnologia, Engenharia e Matemática) foi decisiva para o quadro de desigualdade de gênero vivenciado nos dias atuais nessas áreas.

A criação dos programas já citados, de organizações como a Anita Borg Institute e a Association for Computing Machinery, bem como outras iniciativas, auxiliaram para o alcance de uma maior visibilidade às mulheres que trabalham no ramo. Ademais, os eventos patrocinados pela SBC, como o WIT, têm fornecido um fórum para a comunidade feminina compartilhar suas ideias e pesquisas.

Apesar dessas ações, nossos resultados mostraram que as taxas de pesquisadoras em Computação ainda são baixas, reafirmando as observações já levantadas na literatura. Dos eventos estudados, apenas o WIT possui mais mulheres do que homens, mostrando a importância desse evento para ampliar a presença feminina no CSBC. Logo, a possibilidade de ver outras mulheres em uma área majoritariamente masculina pode trazer motivação e acolhimento para outras que pensam em seguir na área. Além disso, os experimentos de Bian et al. [2017] apontam que essa rejeição - ou segregação - começa ainda no ensino fundamental, com a falta de estímulo à entrada de meninas na Computação, sugerindo que iniciativas sociais e inclusivas devem ser estendidas e reforçadas ainda em idade escolar e de alfabetização.

Vale destacar que as análises realizadas neste trabalho são baseadas nos nomes dos autores dos artigos dos eventos. Portanto, reconhecemos que a análise de gênero é limitada e não abrange a totalidade. Conscientes dessa limitação, pretendemos abordar essa temática de maneira mais abrangente em trabalhos futuros.
