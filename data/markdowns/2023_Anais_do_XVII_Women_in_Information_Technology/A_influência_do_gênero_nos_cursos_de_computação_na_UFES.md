# A influência do gênero nos cursos de computação na UFES

Rebeca C. de Oliveira, Lucia Catabriga, Eliana Zandonade, Andrea Maria P. Valli, Maria Claudia S. Boeres, Camila Z. Aguiar

- 1Departamento de Informática – Universidade Federal Espírito Santo (UFES) Av. Fernando Ferrari, 514 – Goiabeiras, Vitória – ES, 29075-910 – Brasil

- 2Departamento de Estatística – Universidade Federal Espírito Santo (UFES)

{ rebeca.cecco@edu.ufes.br, luciac@inf.ufes.br, zandonade@ufes.br }

{ avalli@inf.ufes.br, boeres@inf.ufes.br, camila.z.aguiar@ufes.br }

Abstract. The objective of this work is to present, analyze and discuss the distribution of genders in Computer Science and Computer Engineering courses at the Federal University of Espírito Santo (UFES), with the aim of investigating the current low female presence. Studies in the world have verified that there has been a great reversal in genders in computing, previously occupied by women creators of various technologies and programming languages. This reality is repeated at UFES, being measured in this work through data, provided by the university, of students entering courses from 1990 to 2022. The quantitative analysis considered, for each student, the year of admission, age, gender, course and form of evasion. In addition to the descriptive analyses, Pearson’s chi-square statistical tests were performed in order to measure the influence of gender on course completion.

Resumo. O objetivo deste trabalho é apresentar, analisar e discutir a distribuição dos gêneros nos cursos de Ciência da Computação e Engenharia de Computação da Universidade Federal do Espírito Santo (UFES), com o intuito de investigar a baixa presença feminina atual. Estudos no mundo verificaram que houve uma grande inversão nos gêneros na computação, antes ocupada por mulheres criadoras de várias tecnologias e linguagens de programação. Essa realidade se repete na UFES, sendo mensurada nesse trabalho através dos dados, cedidos pela universidade, dos estudantes ingressantes nos cursos de 1990 a 2022. Na análise quantitativa foram considerados, para cada estudante, o ano de ingresso, a idade, o sexo, o curso e a forma de evasão. Além das análises descritivas, testes estatísticos de qui-quadrado de Pearson foram executados com o intuito de mensurar a influência do gênero na conclusão dos cursos.

## 1. Introdução

Desde o início da história da computação, as mulheres desempenham um papel fundamental na evolução, manutenção e inovação desta área [Light 1999,

> 1Neste trabalho, considerou-se que o sexo biológico determina o gênero com o qual o indíviduo se identifica, embora nem sempre seja o caso. Essa simplificação foi adotada devido à falta de dados específicos sobre gênero dos estudantes, e para evitar o uso excessivo dos termos ”sexo”e ”sexo biólogico”

Ignotofsky and Augusto 2017]. Entretanto, mesmo com as relevantes contribuições femininas para a área da Tecnologia da Informação (TI) e outras áreas relacionadas, é surpreendente constatar a proporção reduzida de mulheres matriculadas em cursos de graduação e empregadas no campo da TI, tanto no Brasil quanto em escala global. Várias razões podem contribuir para essa desproporção, como: estereótipos de gênero – originados principalmente após a difusão dos PCs ( Personal Computers ) [Santos 2019]; falta de representação de mulheres na área de tecnologia – tanto na academia quanto no mercado de trabalho[Beaubouef and Zhang 2011]; além da falta de políticas para promover a diversidade e a inclusão. De uma maneira geral, acaba sendo uma questão estrutural da sociedade como um todo.

Diferentemente do que acontece na área da TI, o meio acadêmico está sendo mais ocupado por mulheres. Segundo [Maia 2016], observa-se um crescimento do número de mulheres nos cursos superiores mais tradicionais como direito, medicina e engenharia. Porém, a realidade dos cursos de computação segue o caminho inverso. De acordo com o Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), em 2019, apenas 23,9% dos alunos matriculados em cursos de graduação em computação no Brasil eram mulheres. Esta porcentagem é comparativamente menor do que a média geral de participação feminina em cursos de graduação no país, 39,3%. O menor número de mulheres na computação preocupa a comunidade, consequentemente, o interesse pelo tema vem aumentando, como relata [Bordin et al. 2021] na sua análise bibliométrica dos últimos cinco anos no evento anual organizado pela Sociedade Brasileira de Computação (SBC), Women in Information Technology (WIT).

Como aponta a análise feita em [Maximino et al. 2022] sobre as publicações do WIT entre os anos de 2016 a 2021, a região sudeste ficou em terceiro lugar com 43 publicações. Entretanto, as publicações não estão distribuídas equilibradamente, sendo o estado do Espírito Santo o que menos contribuiu, somando apenas 5 publicações no período, enquanto Minas Gerais foi o estado que mais publicou com 17 artigos no mesmo período. Vale destacar que existem várias análises do contexto brasileiro geral, como as feitas em [Santos et al. 2021] e [Cursino and Martinez 2021], em torno dos motivos pelos quais existe a lacuna feminina na área de TI. No contexto de cursos de computação em instituições de ensino superior, podemos destacar os trabalhos realizados na Universidade Federal de Campina Grande (UFCG) [Miranda et al. 2021] e na Universidade Federal do Rio Grande do Norte (UFRN) [Medeiros and Medeiros 2021]. Como ainda não existe nenhuma análise semelhante às listadas acima no contexto da UFES, percebe-se a importância e a necessidade deste trabalho.

O primeiro passo, para minimizar a lacuna da participação de mulheres na área de computação no estado do Espírito Santo, é identificar a sua existência e entender os motivos pelos quais acontece. Apenas com a observação da conjuntura e do histórico local será possível verificar se o padrão nacional se repete ou se é destoante. Neste contexto, este trabalho tem por objetivo analisar os dados referentes a todos os alunos ingressantes dos cursos de computação da UFES, Ciência da Computação e Engenharia de Computação, de 1990 a 2022 – totalizando 33 anos de funcionamento – com relação a algumas questões de gênero. As principais questões de pesquisa que gostaríamos de responder são: (i)

> 2https://www.gov.br/inep/pt-br

> 3https://csbc.sbc.org.br/2022/wit/

“Qual é a distribuição dos gêneros nos cursos de computação na UFES?”; (ii) “Qual é a distribuição dos gêneros por ano nos cursos de computação na UFES?”; (iii) ”O gênero influencia na forma de evasão dos egressos nos cursos de computação da UFES?”.

Este trabalho está organizado como está descrito a seguir. A Seção 2 trata dos aspectos metodológicos deste trabalho, como as ferramentas e dados utilizados. A Seção 3 contém os resultados obtidos, tendo em vista o escopo das questões de pesquisa descritas anteriormente, e as análises envolvidas. Por último, apresentamos na Seção 4 as conclusões do trabalho.

## 2. Metodologia

Neste trabalho adotamos como estratégia de pesquisa o estudo de caso, com geração de dados a partir de uma base de dados disponibilizada pela Pró-Reitoria de Planejamento e Desenvolvimento Institucional da universidade (PROPLAN). Os dados obtidos foram analisados de forma quantitativa. A base de dados da PROPLAN, contempla todos os alunos que já ingressaram nos cursos de Ciência da Computação (CC) e Engenharia de Computação (EC) da UFES, nos últimos 33 anos de funcionamento. Para a pesquisa consideramos: o ano de ingresso (1990-2022), idade, sexo (F e M), curso (CC ou EC) e a forma de evasão (formado, cursando, reopção de curso, transferência para outra instituição, desistência, desligado ou falecimento). Entende-se por: “Reopção de curso”, o aluno que permanece vinculado à universidade, mas em outro curso; “Transferência para outra instituição”, o aluno que continua no curso, mas em outra instituição; “Desistência”, se refere aos alunos que se desligaram voluntariamente da universidade - esta forma de evasão inclui os estudantes que mudam de instituição e de curso; e “Desligado”, quando o aluno perde o vínculo com a instituição por descumprir algum dos itens do regulamento que são passíveis a jubilação.

O processamento dos dados foi feito utilizando a linguagem de programação Python com auxílio da biblioteca Pandas. As visualizações e análises também feitas em Python utilizando bibliotecas como Numpy, Matplotlib, SciPy e Seaborn. Todo o desenvolvimento foi realizado utilizando o Jupyter Notebook, um software de código aberto, no qual é possível criar documentos (notebooks) com células de código e células contendo textos, equações e até mesmo imagens. O notebook resultante, com todo o código e com as principais análises, está disponível em https: //github.com/ceccoRebeca/mulherescomputacao.

Para a análise dos dados, nos 33 anos de funcionamento dos cursos, estudamos a proporção da distribuição dos gêneros nos cursos e comparamos com o que existe na literatura; consideramos a idade dos estudantes ao ingressar nos cursos de computação da UFES, calculando média, moda, desvio padrão e valores mínimos; obtemos a distribuição da quantidade de alunos com relação ao gênero nos cursos; e estudamos as formas de evasão ocorridas para cada gênero.

> 4https://pandas.org/

> 5https://numpy.org/

> 6https://matplotlib.org/

> 7https://scipy.org/

> 8https://seaborn.org/

> 9https://jupyter.org/

Além disso, foi aplicado o teste qui-quadrado de Pearson [Plackett 1983], geralmente aplicado para avaliar o quão provável é que qualquer diferença observada aconteça ao acaso. Neste trabalho foi utilizado para avaliar a dependência ou independência do gênero em relação ao desfecho do aluno nos cursos de computação. O teste é utilizado considerando a probabilidade de se observar um valor da estatística maior ou igual ao encontrado, denominado, o valor-p. Neste trabalho adotamos o nível de significância de 5%, ou seja, não existe dependência de gênero se o valor-p for maior que 0,05.

## 3. Análise dos Resultados

Nesta seção discutimos a distribuição dos gêneros dos estudantes nos cursos de computação da UFES, em conjunto e separadamente, no período 1990-2022. O foco da análise considera não só o ingresso no curso mas também características do seu desfecho pelos estudantes.

A Tabela 1 apresenta respectivamente as porcentagens de alunos e alunas ingressantes nos cursos de computação da UFES ao longo dos 33 anos de sua existência, nos contextos geral (CC+EC) e específico de cada curso (CC e EC). Observe que a distribuição obtida está em consonância com o que existe na literatura acerca do tema. Por exemplo, porcentagens semelhantes a da Ciência da Computação na UFES foram encontradas em [Cursino and Martinez 2021], que analisou os dados de todos os cursos de TI do Brasil, durante o período de 2009 a 2018. Nestes estudos, foram encontradas porcentagens de 20% no início do período de análise (2009) e de 15% no final (2018), demonstrando um decréscimo no número de ingressos de mulheres nos cursos de TI no Brasil ao longo dos anos analisados. Nos casos geral e do curso de Engenharia de Computação, observamos uma similaridade com os resultados apresentados por [Santos et al. 2021], que analisou os dados do Instituto Nacional de Estudos e Pesquisas Educacionais (INEP) relativos aos cursos de TI no período de 2014 a 2019. Nesse trabalho, a porcentagem de alunas ingressantes nos cursos é de 13,8%, próximo dos valores apresentados na Tab. 1.

Tabela 1. Proporç ão da distribuiç ão de gêneros nos cursos da UFES (1990-2022)

|Curso|Masculino(M)|Feminino(F)|
|---|---|---|
|Geral (CC+EC)|85.82%|14.17%|
|CC|82.45%|16.55%|
|EC|88.16%|11.83%|

A Tabela 2 apresenta informações sobre a idade dos estudantes ao ingressar nos cursos, como a média, desvio padrão e valores mínimos e máximos, considerando todo o período de 33 anos de funcionamento dos cursos de computação na UFES. A tabela mostra para cada gênero, a média em relação a todo o período de existência dos cursos, dos valores calculados por ano. Observe que há uma pequena diferença (menor que 2%) na idade média de ingresso entre os gêneros Feminino e Masculino que, entretanto, não é representativa. O desvio padrão é maior em aproximadamente 2 pontos percentuais para o sexo Masculino em todos os cenários, influenciada em parte pela idade máxima encontrada, que também difere muito da máxima encontrada no sexo Feminino. Observamos assim que a idade não apresentou diferenças significativas, e, portanto, não parece ser um fator que influencia na diferença da proporção de alunos dos diferentes sexos.

Tabela 2. Medidas de tendência central e de dispersão – idade dos ingressantes

|C|Me|dia|S|td|m|in|m|ax|
|---|---|---|---|---|---|---|---|---|
|urso|F|M|F|M|F|M|F|M|
|Geral|19.33|20.07|2.30|3.86|16.5|16.0|34.7|58.2|
|CC|19.40|20.50|2.16|4.42|16.5|16.0|30.3|58.2|
|EC|19.24|19.76|2.46|3.36|16.9|16.5|34.7|49.9|

Os gráficos das Figs. 1 e 2 apresentam, respectivamente, a distribuição anual da quantidade de alunos ingressantes com relação ao gênero (sexos M e F), nos cursos de CC e EC da UFES ao longo dos seus 33 anos de funcionamento. Destaque para o curso de CC (Fig. 1), cuja distribuição mostra que existem dois períodos distintos da participação feminina no curso. Até o ano 2000, existia uma participação mais expressiva de mulheres, depois ocorreu uma queda brusca, seguida de algumas flutuações e chegando em 2022 com uma fraca tendência de crescimento no número de alunas ingressantes. As maiores porcentagens observadas de alunas ingressantes no período analisado, foram nos anos de 1995 a 1997, respectivamente, de 34,1%, 39,5% e 35,0%.

Figura 1. Distribuiç ão por ano no curso de Ciência da Computaç ão da UFES

Vários fatores tem sido veiculados para justificar esse comportamento. Por exemplo, o artigo [Santos 2019], descreveu que um dos possíveis fatores pelo quais a primeira turma de Ciência da Computação na USP – década de 70 – ser majoritariamente de mulheres, residia no fato de sua associação com o curso de Matemática. No contexto da UFES, o curso de CC iniciou suas atividades duas décadas depois (1990), tendo uma forte influência do curso de matemática, que já oferecia uma enfase denominada ”Matemática Aplicada e Computacional”, podendo haver no contexto da UFES uma natural influência.

Outro fator veiculado em diferentes fóruns, que também poderia explicar o maior interesse das mulheres pelo curso de CC na primeira década de funcionamento na UFES, estaria na influência do uso do computador para cálculos e processamento de dados, que no passado – décadas de 50 e 60 – eram atividades associadas à função de secretariado, que normalmente era realizada por mulheres. Portanto, nesse período de 1990 a 2000 ainda haveria uma ligação mais forte da computação com um papel de gênero feminino. Com a criação do PC ( Personal Computer ), estereótipos de gênero surgiram e mudariam o cenário do uso do computador. Assim, com o tempo, essas diferenças entre os gêneros aumentariam. Fato que também podemos observar na UFES, ocorreu uma queda tão brusca na procura feminina pelo curso de CC, que nos anos de 2001 e 2007 apenas homens ingressaram no curso.

Infelizmente, este não é apenas um cenário encontrado na UFES, mas em todo o mundo. Por exemplo, [Thurner et al. 2021] relata que na Alemanha, entre os anos de 2002 a 2015, a porcentagem de alunas no curso de CC era de 12,3%. Já na UFES, no mesmo período, a porcentagem foi de 8,8%. No Brasil, [Medeiros and Medeiros 2021] destaca que a presença de mulheres nos cursos de TI na Universidade Federal do Rio Grande do Norte (UFRN) durante o período de 2014 a 2020 foi de 11,9%, sendo que na UFES, neste mesmo período, foi de 11,8%. Portanto, observamos que as diferenças são relativamente pequenas para realidades bem distintas, sendo nacionais e internacionais.

Figura 2. Distribuiç ão por ano no curso de Engenharia de Computaç ão da UFES

A distribuição da quantidade de alunos no curso de EC da UFES (Fig. 2) apresenta um comportamento diferente ao longo dos 33 anos quando comparado com o curso de CC. Em geral, as porcentagens do número de estudantes do sexo feminino foram menores do que aquelas observadas no curso de CC. Entretanto, não ocorreu em nenhum ano, ao longo dos 33 anos de funcionamento, entradas nulas de mulheres. Um fato interessante

ocorreu no ano de 1997, onde a participação feminina na EC foi muito menor que na CC – apenas 3,12% de mulheres ingressantes. A maior taxa de estudantes do sexo feminino ocorreu no último ano da análise. Em 2022, 37,5% dos ingressantes foram mulheres, sendo que no ano anterior tivemos apenas 4,87% de ingressantes do sexo feminino. No intervalo de 2014 a 2020, a média de estudantes ingressantes do sexo feminino foi de 13,71% no curso de EC, próximo do valor relatado por [Medeiros and Medeiros 2021] na UFRN (11,9%). Para o período de 2006 a 2019, [Miranda et al. 2021] relata que a participação feminina na UFCG foi de 16,26%, enquanto na UFES, no mesmo período, foi de 11,51%. Portanto, como atestado para o curso de CC, universidades de diferentes regiões brasileiras apresentam porcentagens de estudantes do sexo feminino para o curso de EC em patamares também relativamente próximos.

Em linhas gerais, a quantidade de estudantes do sexo feminino nos cursos de computação da UFES não é diferente das realidades brasileiras e internacionais, não fazendo sentido aprofundar a análise dos dados considerando os diferentes gêneros. A seguir, apresentamos análises referentes ao desempenho dos estudantes de computação na UFES, sem efetuar comparações entre os dois sexos, mas entre comportamentos do mesmo sexo.

A Fig. 3 apresenta os desfechos ocorridos, para cada gênero, nos cursos de computação do UFES durante todo o período analisado, utilizando as formas de evasão descritas na Seção 2. De maneira geral podemos observar que, apesar das mulheres ingressarem em menor quantidade, apresentam uma taxa maior de formandos e de forma expressiva, cerca de 6% superior. Mais ainda, a taxa de desligamento das mulheres é expressivamente menor, cerca de 10%. Podemos observar também que os outros desfechos no curso não possuem uma diferença insignificante entre os gêneros. A quantidade de alunos que escolhem a reopção ou transferência não chega a ser expressiva, mas a parcela de desistentes e desligados é alarmante, independentemente do gênero. Aproximadamente 40% dos estudantes do sexo masculino não concluem a graduação, enquanto aproximadamente 32% das estudantes do sexo feminino desistem dos cursos.

A Fig. 4 apresenta o desfecho para cada um dos cursos de computação da UFES, CC (acima) e EC (abaixo), seguindo as formas de evasão já descritas. Como pode ser observado no gráfico para o curso de CC, a superioridade numérica de mulheres formadas está bem evidenciada e na ordem de aproximadamente 20%. O mesmo não ocorre na EC, onde tivemos mais homens formandos, apesar de ser uma diferença pequena. O desligamento dos homens também se mantém superior, em ambos os cursos, em relação ao número de desligamento das mulheres. A diferença entre as proporções também se destaca no curso de CC, com quase o dobro de desligamentos masculinos. Já a desistência feminina foi bem maior na EC do que na CC, sendo superior até mesmo em relação aos desistentes do gênero masculino. Estes comportamentos não se mantêm em relação aos desistentes do curso de CC que foi maior para os estudantes do gênero masculino.

A Tab. 3 apresenta o valor-p dos dados utilizados para gerar os gráficos presentes nas Figs. 3 e 4. Considerando que todos os valores-p são menores que 0,05 podemos afirmar que estatisticamente existe uma dependência para a variável sexo, ou seja, o gênero influencia na conclusão dos cursos de computação na UFES.

Figura 3. Desfechos nos cursos de computaç ão da UFES

Tabela 3. Valor-p da distribuiç ão dos gêneros nos cursos da UFES (90-22)

|Curso|Valor-p|
|---|---|
|Geral|0,0063600|
|CC|0,0000032|
|EC|0,0371000|

## 4. Conclusão

Esse trabalho apresentou a análise de alguns dos dados de todos os alunos dos cursos de computação na UFES entre o período de 1990 a 2022. O principal objetivo foi verificar se o gênero dos alunos está relacionado com a maneira que os mesmos saem da universidade. Além isso, também foram analisadas a distribuição dos gêneros dos ingressantes em cada curso, Ciência e Engenharia de Computação, separadamente e em conjunto, ao longo dos anos.

Apesar da grande quantidade de alunos que não concluem os cursos de graduação analisados, as meninas se sobressaem positivamente, ao se formarem mais e serem menos desligadas em relação aos meninos. E de fato, a conclusão ou não do curso está ligada ao gênero do aluno, como foi apontada pelo teste de qui-quadrado.

É alarmante a quantidade de alunos que não chegam a concluir a graduação independente do gênero e isso deve ser investigado. Apesar de ser esperada, essa alta evasão é prejudicial principalmente para uma instituição federal, haja visto o gasto de dinheiro com os alunos e a alta demanda de profissionais da área no momento. E urgente a investigação e tomada de medidas para mitigar e frear o elevado número de alunos desligados.

Além da dependência de gênero do aluno no desfecho, também foram analisadas

Figura 4. Desfechos por curso na UFES - Ciência da Computaç ão (Acima) - Engenharia de Computaç ão (Abaixo)

as proporções de gênero dos alunos ingressantes. A distribuição encontrada, apesar de terem pequenas variações, está em consonância com o que existe na literatura sobre o tema. As diferenças podem existir por se tratarem de cursos mesmo que correlatos, mas diferentes, tipos de instituições diferentes e até mesmo algum fator regional que pode influenciar incentivando ou desmotivando a participação de meninas.

Portanto, esse trabalho apresenta inicialmente resultados novos ao analisar uma conjuntura nunca analisada, mas também abre as portas para que novas análises sejam realizadas com objetivo de complementar as questões aqui levantadas e discutidas, além de fomentar a discussão da alta evasão nos cursos de computação que é urgente.
