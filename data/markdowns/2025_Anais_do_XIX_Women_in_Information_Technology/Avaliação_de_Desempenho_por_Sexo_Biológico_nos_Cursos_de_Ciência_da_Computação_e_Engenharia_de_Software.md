# Avaliação de Desempenho por Sexo Biológico nos Cursos de Ciência da Computação e Engenharia de Software

Sofia de C. Sato, André Y. S. Okimoto, Yago de J. B. Lobato, João C. N. Nogueira, Guilherme L. de S. e Souza, Ana L. M. dos Santos, Leandro S. G. de Carvalho, Tanara Lauschner, Fabíola G. Nakamura, Eduardo F. Nakamura

1Instituto de Computação (IComp) – Universidade Federal do Amazonas (UFAM) Av. Gen. Rodrigo Octávio, 6200, Coroado I, 69080-900 – Manaus – AM

{ sofia.sato, andre.okimoto, yagobrlobato, joao.nogueira, guilherme.louro, analuciamachado, galvao, tanara, fabiola, nakamura } @icomp.ufam.edu.br

Abstract. The low percentage of women in computing courses raises questions about the performance of the female group in the academic environment. To assess whether students’ gender influences their academic journey, a study used educational indicators and data from the Computer Science (CS) and Software Engineering (SE) courses at the Federal University of Amazonas. The results show that women perform similarly to men and, in some cases, surpass them. For instance, the median female completion rate is 4.2 percentage points higher than the male in CS and 13.3 in SE. This indicates that women are not academically inferior to men and are equally capable of handling these courses and their complexities.

Resumo. O pequeno percentual de mulheres em cursos de computação questiona o desempenho do grupo feminino no ambiente acadêmico. Visando avaliar se o sexo dos estudantes influencia a jornada estudantil, foi proposta uma pesquisa utilizando indicadores educacionais e dados dos cursos de Ciência da Computação (CC) e Engenharia de Software (ES) da Universidade Federal do Amazonas. Os resultados demonstram que as mulheres acompanham o desempenho dos homens e, em alguns casos, os superam. Por exemplo, a mediana da taxa de conclusão feminina é 4,2 pontos percentuais a mais que a masculina para CC e 13,3 para ES. Isso indica que o sexo feminino não é inferior em desempenho comparado ao masculino e é igualmente capacitado para os cursos e suas complexidades.

## 1. Introdução

De acordo com uma pesquisa realizada pela Microsoft em 2017, intitulada “ Why don’t european girls like science or technology? ”, a falta de interesse das mulheres por ciência, tecnologia, engenharia e matemática (STEM) está associada à sensação de inexperiência, à baixa representatividade feminina e à desigualdade nessas áreas [Microsoft News 2017]. Além disso, estudos indicam que as capacidades matemáticas das mulheres são frequentemente subestimadas pela escola e pela família, o que pode levá-las a duvidar de sua aptidão para STEM [Wang and Degol 2017, de las Cuevas et al. 2022]. Nesse contexto, fatores socioculturais, especialmente os estereótipos, aparecem como uma das principais razões para a baixa presença feminina na tecnologia, conforme observado por Olmedo-Torre et al. [2018].

Essa pequena porcentagem de participação pode ser vista na média de discentes do sexo feminino em cursos de Tecnologia da Informação (TI) observados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) no ano de 2019, que chegava a 13, 5%, segundo Santos et al. [2021]. Porém, apesar do número inferior de mulheres na área, o sexo feminino supera a porcentagem de formação em aproximadamente 20% em comparação ao sexo masculino no curso de Ciência da Computação da Universidade Federal do Espírito Santo (UFES) [Oliveira et al. 2023], e supera em 38 pontos percentuais a taxa de conclusão masculina dos cursos de Engenharia de Computação e Sistemas de Informação da Faculdadde de Computação (FACOMP) da Universidade Federal do Pará (UFPA) [Costa et al. 2020]. Nesse sentido, análises deste porte ajudam a verificar se estigmas sociais enraizados nas áreas de tecnologia, que afastam mulheres desse campo, podem ser refutados com o desempenho acadêmico do sexo feminino, rebatendo o discurso, principalmente, da incapacidade de atuação das mulheres na área.

Este trabalho avalia, através de indicadores educacionais, o desempenho acadêmico dos sexos biológicos, feminino e masculino, nos cursos de Ciência da Computação (CC) e Engenharia de Software (ES) da Universidade Federal do Amazonas. Em particular, notou-se que a mediana da taxa de conclusão feminina alcançou uma diferença de até 4,2 pontos percentuais superior à masculina em Ciência da Computação (CC), e até 13,3 pontos percentuais em Engenharia de Software (ES), sendo tais diferenças estatisticamente significantes.

O restante do artigo está estruturado da seguinte maneira: na seção 2, são apresentados trabalhos relacionados; na seção 3, é discutida a proposta de pesquisa do artigo e os indicadores utilizados; a seção 4 aborda a metodologia e os resultados obtidos; e a seção 5 apresenta as considerações finais e trabalhos futuros.

## 2. Trabalhos Relacionados

Sobre os cursos de tecnologia na Universidade Federal de Campina Grande, Miranda et al. [2021] mostram, através de dados acadêmicos, que o sexo não é considerado um fator que influencia o desempenho dos alunos nas disciplinas e na situação acadêmica atual do estudante, como evadido ou concluinte. Também se ressaltou que projetos de incentivo à participação feminina e ao acesso das mulheres à tecnologia são essenciais e devem ser fomentados e investidos. Entretanto, o trabalho poderia abordar sobre a situação acadêmica dos estudantes mais clara e profundamente.

Santos et al. [2024] avaliam dados de cinco projetos do Meninas Digitais. Os resultados indicam que esses projetos incentivaram a permanência e aprimoraram as habilidades das alunas nos cursos de computação, aumentando o rendimento acadêmico e aspectos pessoais, como a confiança. Muitas afirmaram que os projetos também criaram um ambiente acolhedor, salientando a importância de ações como as estudadas e como essas estimulam e contribuem para o desenvolvimento das alunas. Porém, esse artigo poderia salientar o impacto dos projetos no rendimento acadêmico das estudantes.

Silva & Santos [2021] analisam um curso de Engenharia da Computação, e apontam que aspectos quantitativos, como o desempenho dos alunos, não depende de sexo, mas fatores qualitativos são dificuldades proeminentes na jornada acadêmica feminina. Na pesquisa, motivos como baixa representatividade, comportamentos masculinos preconceituosos por alunos e professores e falta de apoio foram algumas das considerações

citadas. Um ponto positivo do artigo foi a abordagem qualitativa que proporcionou um olhar sobre aspectos sociais e contastou estigmas impostos ao sexo feminino.

De acordo com Pereira et al. [2020], através de um estudo da participação feminina nos cursos Técnico em Informática e Ciência da Computação do Instituto Federal de Educação Ciência e Tecnologia do Sudeste de Minas Gerais (IF Sudeste MG), revelou que apesar do baixo número de alunas, essas tem um rendimento acadêmico melhor que os homens para CC. Além disso, por meio de questionário com as estudantes, a pesquisa mostrou que as mulheres apresentam interesse na área e possuem facilidade nas matérias de programação. Dessa forma, o artigo revela que as mulheres tem interesse em tecnologia, e ampla capacidade de exercer no campo, sendo um trabalho positivo para argumentar a favor da presença feminina na área.

Silva et al. [2021] analisam o rendimento escolar do Curso Técnico em Informática para Internet do IF Goiano - Campus Ceres, comparando o desempenho dos sexos nas áreas do conhecimento do curso. A partir dos resultados apresentados, conferiu por testes estatísticos um rendimento acadêmico superior por parte das mulheres em três áreas: matemática, ciências humanas e linguagens e códigos. Porém, em todas o sexo feminino apresentou médias sutilmente superiores. Portanto, o desempenho dos sexos é similar, o que afirma as capacidades das mulheres. A pesquisa traz uma perspectiva relevante, pois as mulheres ainda são uma pequena parcela do campo tecnológico, mesmo apresentando um bom desempenho. Isso valida a existência de desafios na participação feminina.

A tabela 1 apresenta pontos similares entre os artigos relacionados apresentados.

|Artigos|Análise de disciplinas|Projetos de incentivo|Questionários sobre vivências|
|---|---|---|---|
|Miranda et al. [2021]|Observou que o sexo não influenciou no desempenho das disciplinas|Apontou sua importância|Não abordou em foco|
|Santos et al. [2024]|Não abordou em foco|A pesquisa abordou o impacto desses projetos|Observou essas informações e como os projetos as influenciaram|
|Silva & Santos [2021]|Avaliou as disciplinas e constatou que o sexo não influenciou os resultados|Não abordou em foco|Coletou dados qualitativos que apontaram vivências femininas|
|Pereira et al. [2020]|Revelou que as mulheres tem um desempenho melhor e facilidade nas disciplinas|Apontou sua importância|Não abordou em foco|
|Silva et al. [2021]|As alunas tem um rendimento superior em todas as áreas|Não abordou em foco|Não abordou em foco|

Tabela 1. Resumo comparativo dos trabalhos relacionados.

## 3. Proposta

### 3.1. Etapas do Processo de Análise de Indicadores

A figura 1 apresenta a arquitetura da pesquisa. O estudo teve início com os dados fornecidos pela coordenação da instituição, que passaram por um processo de anonimização, seguido de tratamento de inconsistências para evitar impactos nos resultados. Após isso, os dados foram utilizados na coleta dos indicadores educacionais e, posteriormente, os resultados foram representados em gráficos.

Figura 1. Etapas do processo de análise de indicadores.

### 3.2. Indicadores

Para extrair os resultados dos dados, foi necessária a utilização de indicadores educacionais, que consistem em cálculos com variáveis específicas retiradas das informações a serem analisadas. Esses indicadores conseguem medir e traduzir desempenhos acadêmicos por meio de números e, posteriormente, em gráficos, como neste artigo.

Os primeiros indicadores educacionais utilizados são relacionados à situação acadêmica dos alunos nos cursos. O indicador de taxa de evasão mede a saída de alunos não formados dos cursos, isto é, alunos que perdem o vínculo com a universidade de maneira definitiva sem se graduar. A taxa de conclusão expressa o percentual de alunos que saíram com a formação completa. Além desses, existe a taxa de permanência, que observa os alunos que ainda constam como cursando e se estende desde uma permanência dentro do tempo do curso, até uma que ultrapassa o tempo máximo estipulado da graduação.

Para os indicadores de situação acadêmica, existem dois indicadores complementares. O primeiro aborda o tempo de formação dos alunos, verificando se o curso cumpre, normalmente, seu tempo mínimo ou se o ultrapassa. O outro complementar trata de alunos registrados como ativos, porém sem matrícula em disciplinas. Esse indicador identifica alunos considerados “fantasmas” e observa o tempo sem atividade desse grupo. Por fim, o último indicador capta o retrato do desempenho dos alunos por meio do coeficiente de rendimento (CR), para visualizar esse aspecto dos cursos estudados.

## 4. Avaliação

### 4.1. Metodologia

A análise segue uma abordagem quantitativa, com o uso de indicadores educacionais e dados do histórico da instituição fornecidos pela coordenação da mesma. Para a coleta dos indicadores, as informações, que contêm dados pessoais e registros acadêmicos, passaram por um processo de anonimização, a fim de respeitar o anonimato dos alunos e a Lei Geral de Proteção de Dados Pessoais (LGPD). Além disso, os dados passaram por

> 1Lei 13.709/2018, disponível em: www.planalto.gov.br/ccivil_03/ato2015-2018/ 2018/lei/l13709.htm.

um tratamento de inconsistências que poderiam afetar os resultados. A partir dos indicadores educacionais, foi possível avaliar o desempenho dos dois cursos estudados. Essas avaliações foram feitas com base em gráficos traçados com ferramentas da linguagem Python, utilizando as bibliotecas Pandas e Matplotlib, que permitiram uma observação visual dos indicadores. Com os gráficos, hipóteses e ideias sobre os comportamentos apresentados foram consideradas e discutidas.

Para verificar algumas hipóteses, foi utilizado o teste estatístico de Wilcoxon, que compara duas amostras independentes. Os testes se dividiram em dois formatos: o primeiro utilizando grupos de dados diretamente e o segundo a partir das medianas dos grupos, em casos de gráficos de boxplot. Esse método foi empregado em um contexto em que se desejava verificar se um grupo independente tinha valores maiores ou menores que outro a um certo nível de significância, 90% neste artigo. Após os testes, as discussões e hipóteses eram levantadas novamente, com o propósito de examinar se seus resultados e testes eram condizentes ou não.

### 4.2. Resultados

(a) Ciência da Computação. (b) Engenharia de Software.

Figura 2. Taxa de evasão ao longo de 4 anos para turmas de 2011 a 2021.

A figura 2 exibe a taxa de evasão anual dos 4 primeiros anos (ou 8 períodos) das turmas de 2011 a 2021 de ambos os cursos. Para essa taxa, foi realizado o teste de Wilcoxon utilizando as medianas, a fim de observar alguma discrepância entre os valores dos grupos. O teste apontou uma diferença significativa para os dois cursos, sendo um _p-value de 0,0334 para CC e um p-value de 0,0105 para ES. Isso pode ser consequência de um paradigma social que afasta as mulheres da área de exatas e, dessa forma, as poucas que imergem estão mais decididas sobre suas carreiras e objetivos. Além disso, por meio dos gráficos, alguns padrões de comportamento trazem possíveis interpretações, como a evasão feminina ser alta logo no início do curso para ES, ao contrário da masculina, que tende a crescer com o passar do tempo.

Já os gráficos de conclusão da figura 3 utilizam a mesma estrutura, mas exibem a partir do quarto ano, pois é o tempo mínimo de formação. Nesses gráficos o teste de Wilcoxon não apontou uma diferença significativa nos valores das medianas, tendo para CC e ES um p-value de 0,8075. No entanto, a disparidade visual é grande, sendo possível observar que as mulheres concluem, normalmente, mais rápido que os homens. Nessa

Figura 3. Taxa de conclusão ao longo de 8 anos para as turmas de 2011 a 2021. Apresenta a partir do 4 ano.

Figura 4. Tempo de formaç ão das turmas de 2010 a 2021.

perspectiva, é justificável que a taxa de conclusão feminina caia no decorrer dos anos, pois as alunas já se formaram.

A figura 4 exibe a distribuição do tempo de formação das turmas de 2010 a 2021 para ambos os cursos, em que cada valor no eixo x corresponde a uma turma. Nesse contexto, é aparente que o grupo feminino, exceto a incomum turma de 2016 de ES, está mais concentrado na faixa verde (que representa o tempo ideal de formação) ou antes dele, em comparação ao masculino, que é mais disperso e ultrapassa o valor de 12 períodos. Isso reforça a hipótese anterior de que o tempo de formação das mulheres é inferior ao dos homens. Essa rapidez pode estar relacionada, talvez, a um senso de responsabilidade potencialmente maior por parte das mulheres, que tenderiam a amadurecer socialmente mais cedo e, assim, a encarar o ambiente acadêmico com mais seriedade e compromisso.

Por meio das figuras 5 e 6, é evidente que, comparando o percentual de concluintes em relação ao total do sexo da turma, as mulheres se formam mais, apesar de anos excepcionais, como 2017, que não houve formação feminina em ES. Esse comportamento foi averiguado por meio de um teste de Wilcoxon, com as taxas de conclusão das turmas de 2011 a 2021, retiradas dos valores absolutos apresentados acima de cada barra nos gráficos das figuras, que constam com a proporção do número de formados para o de ingressantes correspondente. Esse teste apontou uma diferença significativa para ambos os

Figura 5. Dados dos sexos biológicos das turmas de Ciência da Computaç ão com entrada de 2005 a 2024 em relaç ão ao ano de 2024.

Figura 6. Dados dos sexos biológicos das turmas de Engenharia de Software com entrada de 2011 a 2024 em relaç ão ao ano de 2024.

cursos, com um p-value de 0,0888 para CC e um p-value de 0,0942 para ES.

Essa diferença constatada se evidencia ao observar que, para CC, a mediana da taxa de conclusão das mulheres é de 37,5%, enquanto a dos homens é de 33,3%, com 4,2 pontos percentuais a mais para as mulheres. Já para ES, a discrepância entre os valores é ainda maior, com a mediana da taxa de conclusão feminina sendo 33,3% e a masculina 20%, com o sexo feminino superando em 13,3 pontos percentuais o masculino.

As figuras 5 e 6 também apontam que o ingresso feminino não aumentou significativamente, mas se manteve estável nos últimos anos. Isso pode ser visto no número de ingressantes na razão acima das barras. Ademais, a diferença dos anos análisados entre os cursos se dá pelos dados fornecidos, que se limitavam aos anos observados.

Com base nas figuras 7 e 8, é possível verificar a taxa de permanência dos alunos, que se divide em três categorias. A permanência positiva refere-se aos alunos que cursam há menos tempo que o mínimo do curso (4 anos) e se apresenta em maior número, sendo, para CC, superior para as mulheres. Apesar desse grupo feminino aparentar inconstância nos últimos anos, a queda dessa taxa é consequência de outra taxa positiva, a de conclusão

Figura 7. Taxas de conclusão, taxa de evasão e taxas de permanência divididas em categorias para Ciência da Computaç ão ao longo dos anos (2005 a 2024).

Figura 8. Taxas de conclusão, taxa de evasão e taxas de permanência divididas em categorias para Engenharia de Software ao longo dos anos (2010 a 2024).

(que também pode ser vista por valores absolutos acima das barras) e não de um aumento na permanência negativa apresentada mais à frente. Outra categoria é a permanência que ultrapassou quatro anos cursados, mas ainda está dentro do período estipulado. Para esse grupo, ambos os sexos, nos dois cursos, apresentam uma taxa similar.

Já para o último grupo, a permanência é considerada negativa, pois ultrapassa o tempo máximo estipulado (6 anos). Nessa taxa, os homens superam as mulheres em CC, mas em ES, os sexos permanecem similares. Ademais, é válido salientar que o recente declínio da taxa de permanência após seis anos cursados se deve ao jubilamento realizado em 2024, um desligamento que não ocorria desde o início da pandemia de Covid-19, em 2020. Por consequência, a taxa de evasão aumentou significativamente em 2024.

Como visto nas figuras 7 e 8, os sexos não exibiram diferenças de comportamento expressivas, apesar de as mulheres apresentarem taxas positivas superiores e taxas negativas inferiores às dos homens em CC. Também é importante relembrar que as mulheres são significativamente menores em quantidade, e suas porcentagens são sensíveis, com

mudanças radicais causadas por um baixo número de pessoas. Dessa forma, para investigar a fundo esses comportamentos da permanência, foi pensada uma taxa que capta alunos sem atividade no curso, a fim de complementar a análise.

Figura 9. Taxa de alunos sem se matricular ao longo dos anos (2012 a 2024).

A figura 9 apresenta as taxas de alunos fantasmas e seu valor absoluto acima das barras ao longo dos anos observados no eixo x. Esses alunos são aqueles que constam como cursando, mas não possuem matrículas ativas em disciplinas. Nessa perspectiva, a figura 9 aponta que, para o curso de CC, a taxa de homens ausentes é superior à das mulheres, o que ressalta a discussão sobre a responsabilidade e objetividade feminina. Já para o gráfico de ES, os números são variados e instáveis, mas ainda apresentam uma superioridade masculina nas taxas.

Figura 10. Coeficiente de rendimento ao longo dos anos (2010 a 2024).

Em ambos os cursos presentes na figura 10, é possível identificar uma diferença entre a mediana dos dois grupos, feminino e masculino, em que as mulheres apresentam um CR maior, que continua a aumentar, principalmente após a pandemia de Covid-19.

Isso é evidente para ES, em que o grupo feminino alcançou medianas acima da nota média 5 da universidade a partir de 2020. Para testar essa hipótese, foi utilizado o teste de Wilcoxon com os valores das medianas, que confirmou uma diferença significativa entre os números, com um p-value de 0,0171 para CC e um p-value de 0,0007 para ES.

Com isso, é válido afirmar que as mulheres têm, em sua maioria, um coeficiente de rendimento maior que os homens. Uma possível explicação para essa diferença entre os sexos pode estar na cobrança individual e coletiva sobre os grupos, que talvez seja mais intensa para as mulheres. Elas podem enfrentar, com maior frequência, imposições e expectativas que influenciam a forma como lidam com notas e reprovações. Diante disso, algumas alunas tenderiam a desenvolver um maior senso de obrigação, o que poderia levá-las a serem mais responsáveis e a obter melhores desempenhos acadêmicos.

No entanto, é importante destacar que esse engajamento, ainda que possa estar ligado à cobrança feminina, não se explica apenas por esse fator. Em muitos casos, ele também pode representar uma vantagem das mulheres, que possivelmente encaram o seu entorno com mais dedicação, demonstrando um alto potencial de crescimento individual.

## 5. Considerações finais e trabalhos futuros

Como visto e discutido, a participação feminina, apesar do número reduzido de alunas, é bastante expressiva no desempenho acadêmico dos cursos de Ciência da Computação e Engenharia de Software. Com as avaliações, é evidente que as mulheres evadem menos e se formam mais rapidamente, possuindo, possivelmente, menores taxas de alunas que ultrapassam seis anos de curso ou que se tornam fantasmas. Além disso, ainda que o número de mulheres não tenha apresentado um aumento significativo nos últimos anos, as poucas egressas continuam a demonstrar um bom desempenho, com coeficientes de rendimento superiores aos dos homens. Em relação ao desempenho individual de cada curso, observase uma disparidade entre ambos, mas os fatores que influenciam essa diferença não estão relacionados ao sexo dos estudantes e afetam ambos os grupos. Portanto, é viável concluir que o sexo não influencia negativamente nenhum dos dois grupos. Mesmo que as mulheres lidem com questões sociais que não podem ser enumeradas e que possivelmente dificultam sua trajetória de aprendizado, o sexo feminino não apresenta queda em nenhum dos campos analisados e, na maioria dos casos, exibe números superiores. Esses resultados sugerem que as mulheres presentes possuem plena capacidade de atuar na área de tecnologia e apresentam um grande potencial de crescimento.

Dessa forma, é importante que avaliações como esta continuem a ser realizadas, com o objetivo de evidenciar a capacidade do sexo feminino na tecnologia e desmistificar estigmas e preceitos sociais enraizados. A fim de continuar o estudo realizado neste artigo, é proposta uma investigação do impacto de projetos e programas de incentivo feminino nos cursos de tecnologia, assim como uma pesquisa qualitativa em busca das dificuldades que os estudantes dos cursos estudados enfrentam na jornada acadêmica. Com os resultados, será possível avaliar se ambos os grupos, masculino e feminino, apresentam obstáculos similares ou não em suas experiências, e traçar divergências causadas, talvez, pelo sexo dos estudantes. Esses estudos fortalecem a necessidade de políticas de inclusão e diversidade, e ajudam o ambiente acadêmico a reconhecer pontos para melhorias.

## Agradecimentos

Registramos nossos agradecimentos ao Instituto de Pesquisas Eldorado pelo apoio institucional ao desenvolvimento deste trabalho. Este apoio decorre do Protocolo de Intenções nº 021/2024 – ARII, celebrado entre o Projeto Cunhanta Digital da Universidade Federal do Amazonas (UFAM) e o referido Instituto, cuja colaboração tem sido fundamental para o êxito das atividades realizadas.

Esta pesquisa foi financiada, conforme previsto nos Arts. 21 e 22 do decreto no. 10.521/2020, nos termos da Lei Federal no. 8.387/1991, através do convênio no. 003/2021, firmado entre ICOMP/UFAM, Flextronics da Amazônia Ltda. e Motorola Mobility Comércio de Produtos Eletrônicos Ltda.
