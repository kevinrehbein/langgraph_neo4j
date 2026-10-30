# Síndrome do Impostor na formação acadêmica de estudantes na área de tecnologia: um estudo exploratório na Universidade Federal do Ceará - Campus Russas

Larissa Miguel Sousa¹, Rosineide Paz¹, Anna Beatriz Marques¹

¹Universidade Federal do Ceará(UFC)-Campus Russas

Russas-CE-Brasil

`larissamiguelsousa@gmail.com, {rfdapaz, beatriz.marques}@ufc.br`

Abstract. This paper aims to investigate whether there is a significant gender difference. For this, a survey was carried out with undergraduate students of Computer Science and Software Engineering courses at the Federal University of Ceará, Campus Russas. For data analysis, the item response theory (IRT) was chosen, a statistical model that can measure a person's abilities by analyzing a set of responses to items (questions) in a test. In this research, the graded response model was used to estimate the latent trait of the research participants and to compare whether there is a significant difference concerning gender. As a result, the analysis shows no significant difference between the averages between female and male students in the research.

Resumo. Este artigo tem como objetivo investigar se há diferença significativa em relação ao gênero. Para isso, foi realizado um survey em alunos e alunas de graduação dos cursos de Ciência da Computação e Engenharia de Software na Universidade Federal do Ceará, Campus Russas. Para análise de dados foi escolhido a teoria de resposta ao item (TRI), um modelo estatístico que é capaz de medir as habilidades de uma pessoa por meio da análise de um conjunto de respostas a itens (perguntas) em um teste. Neste trabalho, o modelo de resposta gradual foi usado para estimar o traço latente dos participantes da pesquisa, a fim de comparar se existe diferença significativa em relação ao gênero. Como resultado, na análise não existe diferença significativa entre as médias entre alunas e alunos da pesquisa.

## 1. Introdução

Segundo Oliveira et al. (2019), a representatividade feminina na área de tecnologia ao longo das décadas desde o uso do computador pessoal ainda é baixa, comparada ao gênero masculino. A maioria das meninas, mesmo apresentando desempenho superior aos meninos durante a fase escolar, optam por não escolher a área de exatas para ingressar no ensino superior. Os estudos do Programa Internacional de Avaliação de Alunos (PISA, 2018) afirmaram que em diversos países do mundo, apenas 5% das meninas optam por carreira nas áreas de Computação e Engenharia.

Segundo Clance (1985), a Síndrome do Impostor é um padrão de repetição, que tem início quando indivíduos têm sentimentos de insegurança, ansiedade, preocupação em relação às tarefas, sejam elas acadêmicas ou profissionais, que possam almejar o sucesso. Com isso, é comum a procrastinação ou a necessidade de se preparar com muita antecedência para as atividades. Porém, quando alcançam o sucesso, sentem que foi devido à sorte ou trabalho árduo que desempenharam sentindo-se assim, impostores e fraudulentos. E assim a cada tarefa um novo ciclo se repete.

Os primeiros estudos na literatura relacionados à Síndrome do Impostor foram feitos por Clance e Imes (1978) que verificaram a existência de uma grande quantidade de mulheres que se consideravam impostoras. Ainda que tivessem sucesso acadêmico e profissional, não acreditavam que eram capazes e dignas de estarem naquelas posições de privilégios. Além disso, acreditavam que suas habilidades, competências e inteligências eram uma farsa, que a qualquer momento seriam descobertas como falsas. Esse é o medo recorrente de pessoas que têm a Síndrome do Impostor.

Estudos mais recentes investigam a Síndrome do Impostor como um problema na área da Ciência da Computação (Rosenstein et al., 2020), verificam se as professoras de cursos de Ciências Contábeis e Administração são acometidas pela Síndrome do Impostor (Ferreira et al., 2018) e exploram a existência da síndrome em estudantes de doutorados sediados nos EUA (Chakraverty, 2022). Os resultados indicam que há uma tendência à predominância da Síndrome do Impostor em mulheres.

Diante da motivação apresentada anteriormente, esta pesquisa tem como objetivo geral: investigar a relação da Síndrome do Impostor com o desenvolvimento acadêmico e profissional do ponto de vista de alunos e alunas de graduação dos cursos de Ciência da Computação e Engenharia de Software na Universidade Federal do Ceará, Campus de Russas, sob uma perspectiva de gênero. Pretende-se investigar a hipótese de que há uma maior presença da Síndrome do Impostor em estudantes do gênero feminino.

## 2. Procedimentos Metodológicos

Esta pesquisa trata-se de um survey, onde as informações foram coletadas diretamente com o grupo de interesse: alunas e alunos que estão cursando a partir do 3º semestre dos cursos de Ciência da Computação e Engenharia de Software da universidade na Universidade Federal do Ceará, Campus Russas. Quanto à escolha do semestre, é para traçarmos um perfil da Síndrome do Impostor diante das experiências que os estudantes tiveram quanto à participação de seleção em projetos de extensão na universidade e estágio na área. O objetivo do survey na pesquisa realizada é obter informações que possam traçar um perfil de estudantes que são acometidas pela Síndrome do Impostor e identificar se há diferença significativa em relação ao gênero.

O questionário apresentou perguntas abertas e fechadas, onde havia o termo e consentimento na introdução do questionário e composto por 26 perguntas, sendo 10 perguntas para traçar o perfil dos participantes e 11 perguntas com foco relacionado ao questionário elaborado por Clance (1985) denominado escala Clance Impostor Phenomenom Scale (CIPS), a qual foi desenvolvida para a detecção de características impostoras, e adaptada de acordo com a pesquisa. A escala de Clance tem como objetivo verificar a ocorrência ou não da Síndrome do Impostor de acordo com itens classificados em escala Likert, de cinco pontos, listados da seguinte forma: 1 (Discordo totalmente); 2 (Discordo em parte); 3 (Nem concordo nem discordo); 4 (Concordo em parte); 5 (Concordo totalmente). Para que possamos entender o nível da Síndrome do Impostor é necessário somar a pontuação dos itens escolhidos no questionário de cada participante. Caso a pontuação seja abaixo de 40 pontos, o participante apresenta baixo nível da Síndrome do Impostor, pontuação entre 41 a 60, o participante apresenta nível

moderado, já entre 61 a 80, possui nível alto da Síndrome do Impostor, sendo a pontuação acima de 80 considerada com elevado nível da Síndrome do Impostor.

Neste trabalho, o modelo de resposta gradual é usado para estimar o traço latente dos participantes da pesquisa, a fim de comparar esses traços por gênero dos respondentes. O modelo foi ajustado usando o pacote mirt do software R (Chalmers, 2012), que disponibiliza métodos para avaliação do ajuste do modelo. Um deles é a raiz quadrada do erro quadrático médio de aproximação (RMSEA, do inglês Steiger–Lind root mean square error of approximation ). Outro índice é o resíduo quadrático médio padronizado (SRMR, do inglês Standardized Root Mean Square Residual ). Finalmente, também pode ser obtido o índice de ajuste comparativo (CFI, do inglês Bentler’s Comparative Fit Index ). Maiores informações sobre essas estatísticas podem ser vistas nos trabalhos de Steiger (1990) e Cai (2014).

## 3. Resultados

### 3.1 Perfil dos participantes

Foram obtidas respostas de 84 estudantes, que consentiram em participar da pesquisa. Os dados obtidos foram tabulados e as análises destes dados foram feitas de forma quantitativa. De acordo com os resultados do questionário, na Figura 1, é apresentado o gênero dos participantes, 48,2% são mulheres, 50,6% são homens e 1,2% é não-binário. Os dados apresentam maior índice do curso de Engenharia de Software. Os participantes que estão cursando Engenharia de Software representam 58,8%, enquanto os participantes que são do curso de Ciência da Computação, representam 41,2%.

Figura 1. Gênero e curso dos respondentes.

### 4.2 Escala de Clance

A segunda parte do trabalho foi relacionada ao questionário elaborado por Clance (1985) denominado escala Clance Impostor Phenomenom Scale (CIPS), a qual foi desenvolvida para a detecção de características impostoras, e adaptada de acordo com a pesquisa. A escala de Clance tem como objetivo verificar a ocorrência ou não da Síndrome do Impostor de acordo com itens classificados em escala Likert, de cinco pontos. A Figura 2 ilustra os níveis de Síndrome do Impostor identificadas na amostra coletada.

Dos participantes do gênero feminino respondentes, notou-se que 7 alunas possuem nível baixo da Síndrome do Impostor, 25 alunas possuem o nível moderado, 8

alunas têm nível alto e apenas 1 aluna tem nível elevado da Síndrome do Impostor. Considerando os resultados expostos, é possível notar que as alunas possuem uma prevalência de nível moderado, correspondendo aproximadamente 48%, ou seja, 25 alunas. Seguido de nível alto e posteriormente de nível baixo. Em relação aos alunos, notamos que a sua maioria também apresenta um nível moderado da Síndrome do Impostor. Sobre os dados do gênero masculino, percebeu-se que 2 alunos possuem nível baixo da Síndrome do Impostor, 26 alunos têm o nível moderado e 14 alunos possuem o nível alto da Síndrome do Impostor. Em relação ao gênero não-binário, o participante possui nível baixo da Síndrome do Impostor.

Figura 2. Níveis da Síndrome do Impostor.

Esses dados corroboram com Clance (1985) e outras pesquisas que afirmam que quanto maior o nível de sucesso, maior o nível da Síndrome do Impostor. Podemos afirmar, que os resultados analisados nesta pesquisa são extremamente próximos as pesquisas de trabalhos relacionados a área de STEM.

### 4.3 Análise dos dados usando o modelo de resposta gradual

As respostas ao instrumento proposto por Clance (1985) foram analisadas utilizando o modelo de resposta gradual da teoria de resposta ao item. Aqui, foi usado o pacote mirt do software R para o ajuste e avaliação do modelo. A fim de proceder o estudo comparativo, foram construídos os gráficos boxplot para os traços latentes encontrados para os respondentes, os quais podem ser vistos na Figura 3.

Pode ser visto nessa figura que os traços latentes foram encontrados entre os valores de -3 até 2. Esses valores foram padronizados para terem média zero e variância 1. Quanto mais próximos os valores estiverem de -3, menos chance o indivíduo tem de apresentar a habilidade investigada, que é a síndrome do impostor. Por outro lado, quanto mais próximo o traço do indivíduo está do valor 3, mais esse indivíduo é propenso a ter a síndrome. Tendo como base os boxplots, é possível notar que o grupo feminino está mais deslocado para o valor 3 que o grupo masculino e não binário. Também é possível notar no gráfico do grupo masculino, que existe um valor discrepante, representado por um asterisco, em que o indivíduo tem seu traço no extremo da distribuição, indicando que esse indivíduo tem fortes evidências de não ter a síndrome.

Figura 3. Gráfico boxplot e gráfico de histograma.

Para verificar o comportamento da distribuição dos traços latentes, o lado direito da Figura 3 mostra os histogramas suavizados e sobrepostos dos traços latentes dos dois grupos, masculinos e femininos. Nessa sobreposição, o leve deslocamento do grupo feminino para o lado do valor 3 pode ser notado.

Para verificar se a diferença encontrada entre as duas distribuições é significativa, foi realizado um teste de hipóteses para comparação das médias dos dois grupos. Nesse teste foi testada a hipótese nula de que as médias são iguais contra a hipótese alternativa de que elas são diferentes. O valor de p para esse teste é de 0,2474, mostrando que, ao nível de 95% de significância, não existe diferença significativa entre as médias, pois a hipótese nula não é rejeitada.

## 4. Considerações finais

Este artigo apresentou uma análise da relação da Síndrome do Impostor entre alunos e alunas de graduação dos cursos de Ciência da Computação e Engenharia de Software na Universidade Federal do Ceará, Campus Russas sob uma perspectiva de gênero.

Com base nos dados analisados, utilizamos a teoria de resposta ao item (TRI) que através de modelos estatísticos é possível medir habilidades de uma pessoa por meio da análise de um determinado conjunto de respostas a itens. No caso da pesquisa foi utilizado a Escala de Clance, onde cada item respondido apresentava características presentes de quem é acometido pela Síndrome do Impostor. Os resultados apresentados através do boxplot e gráfico de histograma indicam que não existe diferença significativa entre as médias, pois a hipótese nula não é rejeitada.

O artigo deixa alguns pontos de reflexão sobre o impacto da Síndrome do Impostor no desempenho acadêmico e profissional de alunos e alunas participantes. A pesquisa também mostra que o gênero masculino também é acometido pela Síndrome do Impostor e contradiz pesquisas anteriores que indicavam maior predominância da síndrome em mulheres. Como trabalhos futuros, podem ser realizadas entrevistas com os participantes para se conhecer as percepções dos mesmos quanto aos motivos e experiências acadêmicas e profissionais que levam a terem a percepção de serem acometidas pela Síndrome do Impostor e como trabalhar de forma que não cause um impacto negativo em suas carreiras acadêmicas e profissionais.

## Agradecimentos

Anna Marques agradece ao apoio financeiro da Fundação Cearense de Apoio ao Desenvolvimento Científico e Tecnológico (FUNCAP) por meio do processo BP5-00197-00016.01.00/22
