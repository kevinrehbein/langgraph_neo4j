# Uma Análise Comparativa do Desempenho em Matemática entre Gêneros nas Provas do ENEM

Maristela Holanda, Amilton L. M. Júnior, Eric Hans M. da Silva, João Laterza, Aleteia Araujo, Carla Castanho, Carla Koike, Roberta B. Oliveira

1Departamento de Ciência da Computação - Universidade de Brasília (UnB) Brasília - DF - Brasil

{ amilton.mendes, eric.hans, laterza22 } @gmail.com

{ mholanda,aleteia,carlacastanho,ckoike,roberta.oliveira } @unb.br

Abstract. In Brazil, scores from the National High School Exam, ENEM, are used to access federal public universities. In addition to the grades, the microdata of this exam has a large set of information about the students enrolled in the tests. This information can be used to carry out various analyses regarding student performance. As in other parts of the world, entry into computer courses by women is much lower than by men. One of the points identified in relation to not choosing the computing course is the supposition that computing needs a lot of mathematics. In this context, this article presents an analysis specifically about mathematics in the ENEM, and the differences between men and women in this test, having as a research question: What is the average grade obtained in the mathematics test by gender, ethnicity, Federative Unit (UF) of residence, disability, marital status and high school completion status? Data analysis was from the years 2010 to 2019, and, due to the large volume of data, the experiment was performed on an Amazon Web Services (AWS) cluster using MongoDB. In all analyses, men scored better than women, but the difference between the scores (men and women) was approximately 10%.

Resumo. No Brasil, são utilizadas as notas do Exame Nacional do Ensino Médio (ENEM) para acesso às universidades públicas federais. Além das notas, os microdados desse exame possuem um grande conjunto de informações dos estudantes inscritos nas provas. Essas informações podem ser utilizadas para a realização de diversas análises a respeito do desempenho dos estudantes. Como em outros lugares do mundo, a entrada em cursos de computação pelas mulheres é bem menor do que a dos homens. Um dos pontos identificados na literatura em relação à não escolha pelo curso de computação, é a questão que computação precisa de muita matemática. Nesse contexto, este artigo apresenta uma análise especificamente sobre a matemática no ENEM, e as diferenças entre homens e mulheres nessa prova, tendo como questão de pesquisa: Qual a nota média obtida na prova de matemática pelos inscritos que estavam presentes por gênero, etnia, Unidade Federativa (UF) de residência, deficiência, estado civil e situação de conclusão do ensino médio? A análise dos dados foi dos anos de 2010 até 2019, pelo grande volume de dados o experimento foi executado em um cluster na Amazon Web Service (AWS) com o banco de dados MongoDB. Como resultado, em todas as análises os homens

tiraram notas melhores que as mulheres, porém a diferença foi pequena entre as notas (homens e mulheres), aproximadamente 10%.

## 1. Introdução

A educação superior, no Brasil, é fornecida tanto por instituições públicas quanto privadas. As instituições públicas, embora sejam gratuitas, não têm vaga disponíveis para todos os interessados, o que resulta em uma alta competição pelas oportunidades disponíveis. Atualmente, o Exame Nacional do Ensino Médio (ENEM) é o principal mecanismo de acesso às universidades federais, avaliando em torno de 6 milhões de candidatos por ano [Santos et al. 2019].

O ENEM é administrado e operado pelo Instituto Nacional de Estudos e Pesquisas Educacionais (INEP), sendo a segunda maior prova nacional do mundo, o primeiro exame é o Gaokao [Weller 2021], realizado na China. Os resultados do exame possibilitam, ainda, o desenvolvimento de estudos e indicadores educacionais. Para isso, o INEP disponibiliza a base pública Microdados do ENEM, contendo diversas informações socioeconômicas dos alunos inscritos no exame [Rodrigues et al. 2019]. Consequentemente, é possível conduzir amplas pesquisas usando esses dados, visto existirem diversas variáveis disponíveis para análise.

O relatório da Sociedade Brasileira de Computação (SBC) sobre a Educação Superior em Computação no Brasil [SBC 2019] apresenta estatísticas relacionadas ao número de cursos da área de computação e os perfis dos ingressantes e concluintes. O relatório analisa dados entre os anos de 2001 e 2019 e mostra que apesar do número total de ingressantes nos cursos de computação apresentar nítido aumento no decorrer dos anos, as ingressantes ainda somam pouco menos de 15% no ano de 2019 e não aumenta na mesma proporção. Da série apresentada, 2008 foi o ano com maior ingresso feminino nos cursos, com 28% de ingressantes do sexo feminino. Ainda em [SBC 2019], o Brasil teve, em média, apenas 19,8% de concluintes do sexo feminino em diferentes cursos de Computação nos anos de 2000 a 2019.

Segundo relatório da Associação Brasileira das Empresas de Tecnologia da Informação e Comunicação [BRASCOM 2020], em 2016 as mulheres representavam 34,1% da força de trabalho em TIC (software, serviços, industria e comércio), mas em 2020 esse número caiu para 32,6%. Entre outros dados apresentados nesse relatório, temos que a participação feminina em 2020 é maior em tarefas administrativas (62%), há baixa disparidade entre gêneros em áreas de marketing e serviços gerais, mas há forte predominância masculina nas funções técnicas (80%) e serviços industriais (73%).

Para tentar entender o motivo da não escolha dos cursos de computação pelas mulheres, artigos como [Macedo et al. 2018], [Menezes 2021], [Holanda et al. 2019] e [Ribeiro and Maciel 2020], apresentam, de diferentes maneiras, fatores que podem influenciar essa escolha, tais como, percepção das meninas que computação é para homens, não apoio da família, falta de estímulo na escola entre outros. Além dos aspectos sociais, e de questões afetivas, também tem a percepção das meninas de que computação precisa de muita matemática [Holanda et al. 2019][Menezes 2021].

Neste contexto, este artigo apresenta uma análise da diferença de desempenho em matemática por gênero nas provas do ENEM de 2010 a 2019, tendo como questão de

pesquisa: Qual a nota média obtida na prova de matemática pelos inscritos que estavam presentes por gênero, etnia, Unidade Federativa (UF) de residência, deficiência, estado civil e situação de conclusão do ensino médio? Para responder a questão de pesquisa foram utilizados os microdados do ENEM entre 2010 e 2019. O banco NoSQL MonogDB foi utilizado por causa do grande volume de dados e os experimentos foram executados em um ambiente em nuvem da Amazon Web Service (AWS).

Este artigo apresenta a seguinte estrutura: a Seção 2 descreve trabalhos relacionados; a metodologia e os experimentos são explorados na Seção 3; a Seção 4 apresenta os resultados obtidos e a Seção 5 uma discussão; e por fim, a conclusão e os trabalhos futuros são expostos na Seção 6.

## 2. Trabalhos Relacionados

Poucas meninas estão optando pela carreira em computação, como mencionado anteriormente. Por essa razão, destaca-se a importância de propostas de ações específicas com o intuito de diminuir essa diferença de gêneros nas áreas que envolvem computação. Portanto, entender quais são os fatores que influenciam nas escolhas de uma graduação é uma questão relevante para a elaboração de tais propostas, e que vem sendo muito abordada na literatura nos últimos anos [Santos et al. 2017, Martins et al. 2019].

[Macedo et al. 2018] realizam um estudo com funcionários e estagiários de uma empresa de tecnologia, com o intuito de identificar as influências mais relevantes que os participantes receberam no momento da decisão por um curso na área de tecnologia. Além disso, os autores verificam se esses fatores são distintos entre profissionais dos sexos masculino e feminino. O estudo identificou mais fatores positivos do que negativos para a escolha da graduação na determinada área, no entanto, isso já era esperando considerando que os participantes são da área. Por outro lado, os homens tiveram menos influência negativa do que as mulheres. Os fatores que destacaram-se na decisão da carreira de acordo com o estudo foram a importância da estabilidade financeira para os homens e a influência negativa da família e amigos para as mulheres.

A importância da família na escolha do curso de graduação e o interesse das meninas pela área de Computação são considerados no trabalho de [Holanda et al. 2017]. Os autores analisam os dados coletados de 3.707 meninas dos ensinos fundamental e médio entre os anos de 2011 e 2014. De acordo com os resultados, a área de Ciências Exatas é a que tem menor interesse quando comparada com as áreas de Saúde e Ciências Humanas. Além disso, poucas meninas demonstraram interesse em fazer algum curso de computação. A partir dos resultados, também é possível observar que a maioria das meninas que pensam em fazer um curso de computação tem a aprovação da família, demonstrando a sua relevância na escolha de um curso superior. [Holanda et al. 2017] também apresentam que o interesse é maior para as alunas do ensino fundamental do que para as alunas do terceiro ano, enfatizando que no ensino médio as alunas já estão com suas decisões tomadas.

Baseando-se na Teoria Sociocognitiva da Carreira (TSCC), [Ribeiro and Maciel 2020] identificam os fatores que influenciam de maneira positiva e negativa a escolha das estudantes do Ensino Médio integrado à Educação Profissional (EMIEP) em Informática pela continuidade da carreira em uma profissão, ou em um curso de graduação em Computação. Os autores relatam que as estudantes citaram

uma maior variedade de fatores negativos, apesar de apontarem uma quantidade maior de fatores positivos para a escolha da continuidade da carreira na área de Computação. Os fatores pessoais somados aos fatores comportamentais apresentam maior influência positiva nas escolhas das estudantes, enquanto que os fatores pessoais têm maior influência negativa. Por outro lado, os fatores ambientais representam influências similares nas escolhas. Analisando os fatores pessoais, os autores apresentam que a maioria dos fatores que influencia positivamente são de estados afetivos, e a maioria dos fatores que influenciam negativamente são de estados cognitivos. No entanto, também há fatores de estados biológicos que influenciam de maneira negativa, tais como, cansaço, estresse e medo.

Também com o objetivo de identificar os fatores relacionados à menor presença das mulheres em cursos na área de Computação no Brasil, [Menezes 2021] realizam um levantamento de publicações relevantes na literatura que abordam tais fatores. De acordo com o levantamento, entre os fatores que interferem e desmotivam a escolha pela Computação estão: (1) intimidação das meninas por achar a Computação uma área masculina e com pouca representatividade feminina; (2) falta de incentivo da família; (3) falta de estímulos na infância ou na escola; (4) carência de conhecimento sobre a área de Computação; (5) percepção de não ter habilidades suficientes para a área e de não ter afinidade com Matemática. Além disso, os autores apresentam as iniciativas utilizadas, de acordo com a literatura, para atrair meninas do ensino médio para a determinada área.

Alguns dos fatores apontados por muitas meninas no Brasil que influenciam de maneira negativa na escolha profissional na área de Computação, de acordo com a literatura, foram a percepção da área ser complexa e a percepção da área estar relacionada com a matemática [Menezes 2021]. Além disso, essas percepções associadas às dificuldades do país no ensino de matemática nas escolas pode contribuir ainda mais pelo desencorajamento das meninas [Holanda et al. 2019]. Os resultados das provas do ENEM, conforme os dados disponibilizados pelo INEP, são utilizados em diversos trabalhos com o objetivo de identificar as causas do desempenho dos estudantes nas provas [Franco et al. 2020, Marcom and Kleinke 2017]. Muitos estudos na literatura abordam a diferença de desempenho entre homens e mulheres em avaliações de matemática. Geralmente, tais estudos apresentam que o desempenho dos homens é predominantemente superior [Chagas 2019].

No estudo de [Noguera et al. 2020], é analisado o desempenho dos participantes do ENEM em relação ao gênero e às áreas de conhecimento das ciências exatas, entre os anos de 2013 a 2017, de acordo com os dados do INEP. Os autores investigam vários fatores de análise para participantes dos sexos feminino e masculino, tais como, região de residência, cor/raça, tipo de escola do ensino médio, renda salarial mensal e notas para cada área das ciências exatas. Em relação ao gênero, os resultados demostram que o desempenho dos homens foi discretamente superior ao das mulheres nas áreas de matemática e ciências da natureza. No entanto, o desempenho de ambos os sexos foi quase equivalente na área de linguagens e códigos.

Diferentemente dos trabalhos apresentados na literatura, as contribuições deste artigo envolvem os seguintes pontos: (1) a utilização de um grande volume de dados públicos do ENEM, de 2010 a 2019, no qual foi implementado um banco de dados no MonogDB, um NoSQL baseado em documento; (2) a análise considera diferentes atributos tais como, etnia, UF, deficiência, estado civil e situação no ensino médio; e (3) a visualização dos dados, a partir de gráficos desenvolvidos em diferentes padrões para contribuir com a análise e a apresentação dos resultados.

## 3. Metodologia

Esta seção apresenta uma descrição sobre o dataset utilizado na pesquisa, o préprocessamento dos dados, a implementação do banco de dados e o ambiente computacional no qual foram realizados os experimentos.

### 3.1. Dataset do ENEM

Os microdados do ENEM são públicos e estão disponíveis em arquivos anuais no portal do INEP. Esta base é considerada uma das mais relevantes para políticas públicas educacionais [Ferreira et al. 2021], com dados consistentes, confiáveis, diversificados e numerosos [Rodrigues et al. 2019]. Trata-se do menor nível de desagregação de dados recolhidos por meio do exame, contendo as provas, os gabaritos, as informações sobre os itens, as notas e o questionário respondido pelos candidatos. Cada arquivo possui cerca de 5 milhões de registros, que correspondem ao número de inscritos no exame, com a quantidade de atributos variando de ano para ano.

Para este estudo foram considerados os dez arquivos mais recentes disponibilizados no portal, compreendendo, portanto, os exames aplicados no período de 2010 a 2019, com aproximadamente 64GB de informações armazenadas. Como resultado, obteve-se uma base de dados com mais de 65,4 milhões de registros e 50 atributos consolidados.

### 3.2. Pré-processamento dos Dados

Antes de iniciar os experimentos, fez-se necessário um pré-processamento dos microdados do ENEM, de modo a consolidar as informações da década selecionada em um único arquivo. Para tanto, os seguintes passos foram adotados:

1. Mapeamento dos atributos comuns na década selecionada;

2. Definição de regras e premissas para a padronização do domínio dos atributos;

3. Consolidação dos dados em um arquivo único.

O pré-processamento dos dados foi efetuado utilizando scripts em python para leitura, ajustes e registros linha por linha, disponíveis em https://github.com/laterza22unb/PPCA2020-02-BDM. Como resultado, os dados foram consolidados em arquivos únicos - totalizando 65.407.978 registros e 50 atributos - nos formatos TSV ( Tab-Separated Values ) e JSON ( JavaScript Object Notation ), os quais foram disponibilizados para carga.

### 3.3. Banco de Dados

Nesta pesquisa foi usado o serviço de banco de dados Amazon DocumentDB que possui uma interface compatível com o MongoDB 4.0. O DocumentDB é uma solução proprietária da AWS, disponibilizada como Database as a Service (DBaaS) e, com

> 1https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/ microdados/enem

> 2https://aws.amazon.com/documentdb/

isso, torna os experimentos mais simples do ponto de vista de configuração inicial e também para escalar horizontalmente o cluster. A modelagem do banco foi baseada em documentos embedded, no quais são colocados todos os atributos na raiz, exceto “CO ~~U~~ F ~~R~~ ESIDENCIA” e “SG ~~U~~ F ~~R~~ ESIDENCIA” que são aninhados dentro do atributo “UF”, como pode ser observado na Figura 1.

#### Figura 1. Modelo de dados.

O MongoDB foi implementado de acordo com a Figura 2, por meio de um cluster com quatro máquinas, no qual a configuração contou com apenas uma instância primária (MongoDB Primary) responsável pela escrita dos dados (cargas, criação e exclusão de índices), e as leituras foram feitas exclusivamente a partir das três réplicas (MongoDB Replica). Os experimentos foram feitos na AWS, região São Paulo (sa-east-1), e as instâncias ficaram distribuídas livremente em 3 regiões de disponibilidade. Para isso, foi configurada uma rede virtual privada isolada somente para a comunicação entre o Client Driver AWS EC2 e o cluster do DocumentDB (MongoDB). O Client Driver AWS EC2 era uma instância t2.medium com 2 vCPUs, 4 GB RAM e sistema operacional Ubuntu 20.04.3 LTS. Todas as instâncias do cluster eram idênticas, ou seja, primárias ou réplicas usaram instância r5.large com 2 vCPUs, 16 GB RAM e rede até 10 Gbps, e EBS com largura de banda de até 4.750 Mbps.

## 4. Resultados

Esta seção apresenta os resultados que tratam a questão de pesquisa deste artigo. Inicialmente, foi efetuada uma sucinta avaliação da população alvo definida - constituída pelos inscritos nos exames do ENEM realizados entre 2010 e 2019, e que estiveram presentes na prova de matemática - o intuito foi avaliar a distribuição dos candidatos e seus respectivos desempenhos na prova. A Figura 3(a) ilustra o total de presentes por ano e gênero,

Figura 2. Topologia implementada do banco MongoDB.

sendo possível observar uma tendência crescente na primeira metade da década com decaimento nos anos seguintes. Independentemente do período, é nítida a predominância das mulheres dentre os presentes na prova, com uma proporção média de 58,5%, como mostra a Figura 3(b).

(a) Total de presentes na prova (b) Proporção de presentes na prova (milhões). (percentual).

Figura 3. Presentes na prova de matemática por ano e gênero.

Desempenho por gênero e ano: os homens alcançando pontuações superiores às das mulheres em todos os anos (Figura 4). A evolução das notas é similar para ambos os gêneros ao longo do período selecionado, com uma queda considerável em 2014 e em 2015. Apesar da diferença na média da prova de matemática ser favorável aos homens em todos os anos, a diferença entre essas pontuações não foi maior do que 10% nos anos analisados.

Desempenho por gênero e etnia: em resposta à primeira questão de pesquisa, foi avaliado o desempenho dos presentes na prova de matemática, considerando o atributo etnia. Como resultado, verificou-se que, inobstante a massiva presença de pardos e pretos na prova, as maiores notas em matemática foram obtidas, em média, por candidatos de cor branca e amarela, como observado na Figura 5, possivelmente como reflexo da desigualdade social presente na sociedade brasileira. Ainda, quanto à questão de gênero, a superioridade masculina nas notas pode ser observada em todas as etnias, bem como a maioridade feminina em termos de participantes, sem variações relevantes.

Desempenho por gênero e residência: para esta questão de pesquisa foram consideradas as Unidades da Federação (UF) de residência dos presentes na prova de ma-

Figura 4. Desempenho na prova de matemática por ano e gênero.

Figura 5. Desempenho na prova de matemática por gênero e etnia.

temática. Na Figura 6(b) nota-se uma maior densidade de residentes nos Estados de São Paulo e Minas Gerais, sendo que em todas as UFs o número de mulheres é superior ao de homens. Seguindo o padrão observado, o rendimento masculino na prova supera o feminino, sem alterações substanciais na proporção ao variar as UFs, como ilustrado na Figura 6(a). Ademais, em linha com os resultados encontrados por [Ferreira et al. 2021], aferiu-se uma concentração das notas médias mais elevadas na região Sudeste, seguida pelas regiões Sul, Centro-Oeste, Nordeste e Norte. A proporção entre mulheres e homens em todas as UFs é semelhante, sendo que sempre há mais mulheres realizando a prova do ENEM em todas as UFs do Brasil. Em quatro estados as mulheres tiveram notas maiores do que 500 pontos, SP (508), SC (508), MG (507) e RJ (504). Ao mesmo tempo, os homens obtiveram notas maiores de 500 em 18 UFs. De toda forma, a diferença nas notas entre os homens e mulheres foi em quase todos os casos menor do que 50 pontos, apenas o Estado do RN teve exatamente 50 pontos.

Desempenho por gênero e outros atributos: mesmo estendendo as análises para atributos como deficiência, estado civil e situação de conclusão do ensino médio, o desempenho masculino continua sendo consistentemente superior ao feminino na prova de matemática do ENEM, como consta nos resultados apresentados na Tabela 1. Em todos os tipos de deficiências analisados, a diferença entre notas de homens e mulheres foi menor de 10%. Em relação ao estado civil, o único caso que ficou maior de 10%, a diferença entre notas ficou em 11%, foi o viúvo(a). Nos casos do ensino médio, nos tipos analisados,

(b) Total de presentes na prova (milhões).

Figura 6. Desempenho na prova de matemática por gênero e UF de residência.

a diferença foi menor que 10%.

## 5. Discussão dos Resultados

Os resultados apresentados na Seção 4 demonstram que os homens tiveram nota maior na prova de matemática comparada com as mulheres, apesar da diferença não ser muito grande. O resultado foi semelhante por todas as análises realizadas (etnia, UF, estado civil, deficiência, e situação no ensino médio). Assim, com isso, algumas questões poderiam ser discutidas:

- Será que é necessário trabalhar as meninas em relação à matemática?

- Será que deve existir essa relação direta entre a matemática e a computação?

- Será que o desempenho pior na matemática justifica o fato das alunas não terem interesse por cursos de computação?

Este artigo não tem respostas para essas questões, mas as autoras acreditam que apresentar esses dados, de 10 anos do ENEM (2010-2019), pode ser um importante tema de debate para a comunidade de computação. Assim, é importante analisarmos o quanto a computação, com tantas áreas de atuação diferentes, ainda precisa (ou não) está rotulada ao ensino da matemática. Além disso, vale a pena um estudo profundo de como a matemática está sendo vista em sala de aula, ou seja, a matemática é passada como uma disciplina prazerosa ou como uma disciplina difícil que apenas os bons alunos se destacam? Em relação ao último ponto, as meninas são incluídas ou excluídas neste subconjunto

Tabela 1. Desempenho na prova de matemática por gênero e demais atributos.

||||Gên |ero ||
|---|---|---|---|---|---|
||Atributo|Masc|ulino|Femi|nino|
|||Nota média|Presentes|Nota média|Presentes|
||Deficit atenção|593,15|17.173|583,20|18.482|
||Dislexia|539,90|5.586|507,73|4.898|
|ia|Sem deficiência|527,39|18.877.812|483,68|26.654.966|
|inci|Baixa visão|489,44|23.986|458,80|28.047|
|iciê|Deficiência física|478,09|47.656|450,81|37.212|
|efi|Cegueira|469,01|4.143|445,55|3.138|
|Di|Deficiência auditiva|465,74|12.240|445,05|14.584|
||Deficiência mental|435,61|6.051|431,99|4.550|
||Surdez|427,11|5.785|416,25|5.623|
|il|Solteiro(a)|529,69|16.602.090|487,71|23.183.612|
|Civ|Não informado|518,76|363.740|474,11|454.767|
|do|Divor./Desq./Separ.|510,07|182.690|456,40|420.061|
|ta|Casad./Moramjuntos|508,13|1.833.327|455,04|2.644.625|
|Es|Viúvo(a)|491,35|11.291|435,97|62.550|
|d.|Concluiu|531,91|10.091.120|483,01|14.149.445|
|Mé|Concluirá no ano|529,34|5.489.687|487,31|7.770.191|
|s. |Concluirá após o ano|520,40|2.717.350|486,10|4.178.618|
|En|Não está cursando|468,24|694.969|438,68|667.357|

dos bons? Como dito, este artigo não tem a intenção de apresentar estas respostas, mas tem a missão de trazer o incômodo da dúvida para que os pesquisadores da área possam investigar esses fatos.

## 6. Conclusão

Este artigo apresentou uma análise sobre o desempenho na prova de matemática das alunas no ENEM, por gênero, etnia, Unidade Federativa (UF) de residência, deficiência, estado civil e situação de conclusão do ensino médio. Como ilustrado, nos anos entre 2010 e 2019, em todas as análises os homens tiraram notas melhores que as mulheres, porém a diferença entre as notas (homens e mulheres) foi de aproximadamente 10% apenas.

Contudo, é importante investigar o quanto esse desempenho das meninas nas provas de matemática podem influenciar, de fato, as suas poucas escolhas pela área de computação. Assim, este artigo deixa alguns pontos de reflexão sobre a relação entre a matemática e a escolha pela atuação profissional na área de Computação.

Para trabalhos futuros, planeja-se desenvolver modelos de regressão para a identificação de quais atributos são mais relevantes para o desempenho na prova de matemática. Em seguida, as pesquisadoras objetivam analisar outras fontes de dados, tais como os dados do Censo da Educação Básica, no intuito de identificar variáveis para a diferença de performance observada.

## 7. Agradecimentos

As autoras agradecem ao apoio do CNPq (Processos No 440806/2019-4) e ao Programa Meninas Digitais da SBC pela inspiração na inclusão de mais meninas na Computação.
