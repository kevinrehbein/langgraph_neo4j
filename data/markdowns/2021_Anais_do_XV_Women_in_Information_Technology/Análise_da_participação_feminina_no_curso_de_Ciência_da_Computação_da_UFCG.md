# Análise da participação feminina no curso de Ciência da Computação da UFCG

Beatriz A. de Miranda, Marcella M. S. C. de Almeida, Ivyna R. S. Alves, Lívia M. R. S. Campos

1Departamento de Sistemas e Computação Universidade Federal de Campina Grande (UFCG) Caixa Postal 10.106 – 58.109-970 – Campina Grande – PB – Brasil

{ beatriz.miranda,marcella.almeida } @ccc.ufcg.edu.br

ivyna@copin.ufcg.edu.br, livia@computacao.ufcg.edu.br

Abstract. Despite their great importance for the development of Computer Science, women still have a low participation in undergraduate courses of the area. In order to understand whether these low numbers apply to the Computer Science course at the Federal University of Campina Grande, a descriptive analysis of the data provided by the course department was carried out. From this analysis, it was possible to draw a profile of the female student body and understand aspects related to the rate of admission, completion, dropout, success and performance in subjects with greater retention in the course from the gender perspective, in order to know if gender is a determining factor for success in the course.

Resumo. Apesar de sua importância histórica para o desenvolvimento da Ciência da Computação, as mulheres ainda têm uma baixa participação nos cursos de graduação da área. A fim de entender se e como essas números se aplicam ao curso de Ciência da Computação da Universidade Federal de Campina Grande, foi realizada uma análise descritiva dos dados acadêmicos fornecidos pela instituição. A partir dessa análise foi possível traçar um perfil do corpo discente feminino e compreender aspectos relacionados a taxa de ingresso, conclusão, evasão, sucesso e desempenho nas disciplinas com maior retensão no curso a partir da perspectiva de gênero, de a forma a entender se o sexo é um fator determinante para o sucesso no curso.

## 1. Introdução

Na contramão de cursos superiores tradicionais no Brasil, a exemplo de medicina, engenharia, direito e arquitetura, em que é crescente a participação feminina, na área da computação o número de mulheres tem diminuído ao longo do tempo [Maia 2016]. No período de 2000 a 2013, dentre os mais de 400 mil alunos concluintes em cursos da área pelo país, a presença feminina foi de apenas 17% no total. Esse número tem sido motivo de estudos em torno das possíveis causas para tamanho afastamento das mulheres em relação aos cursos superiores de computação [Santos 2019b][Santos da Silva 2020][Menezes 2021].

No trabalho realizado em [Silva 2017], os discentes acreditam que a falta de eventos e programas de incentivo para maior participação feminina são possíveis causas influenciadoras nos baixos números de mulheres em cursos de computação, reforçando a

necessidade de investimentos em projetos que ampliem o contato de meninas com a tecnologia. Em [Menezes 2021] foi realizada uma revisão sistemática para identificar fatores relacionados a menor presença feminina em cursos de computação. Alguns dos fatores encontrados foram discriminação de gênero, carga horária excessiva, além de dificuldades e reprovações em disciplinas. Ainda nesse trabalho, os autores também citam fatores que atraem e motivam as mulheres nessa área, incluindo: fomento a projetos que apoiem as mulheres na computação, apoio de familiares, disponibilidade de cursos próximos de onde moram, gostar da área e exemplos de outras mulheres.

Uma maior participação de mulheres em computação envolve um esforço para manter as graduandas em cursos superiores na área como também atrair mais mulheres para estes cursos. Considerando esse último ponto, uma iniciativa bem conhecida está ligada a um projeto na Carnegie Mellon University, tendo como um dos resultados o aumento no número de mulheres no programa de Ciência da Computação da universidade, alcançando uma proporção de 50/50, comparado a 8/92 nos anos 90 [Fisher 2002].

Nesse contexto, o grupo Elas@Computação [Elas@Computação 2020a] é uma organização criada no curso de Ciência da Computação da UFCG desde 2017, que tem por objetivo trazer mais mulheres para a área e fixar as atuais graduandas, gerando uma rede de apoio e valorizando o empoderamento das discentes. Uma das iniciativas do grupo foi o projeto Raio-X [Elas@Computação 2020b], voltado para a análise de dados sobre a participação das mulheres no curso da UFCG, onde os primeiros resultados obtidos em 2020 trouxeram análises sobre dados acadêmicos dessas estudantes.

O objetivo deste artigo é apresentar uma análise descritiva de dados acadêmicos sobre a participação de mulheres no curso de Ciência da Computação da UFCG, tomando como base os resultados do projeto Raio-X. Por meio deste, foi possível reforçar alguns pontos já conhecidos, como a baixa participação de mulheres em cursos superiores de computação, mas também mostrar que o sexo pode não ser um fator determinante para o sucesso nesse curso, como demonstram as análises sobre taxa de conclusão, evasão e desempenho nas disciplinas com maior retensão no curso. Acredita-se que o acesso à informação é uma forma de entender melhor um problema nas suas diferentes perspectivas e motivar ações para atuar sobre ele.

O restante deste artigo está organizado da seguinte forma: na Seção 2 é discutida a literatura relacionada, seguida pela metodologia adotada para a análise dos dados acadêmicos do curso de Ciência da Computação da UFCG na Seção 3. Já na Seção 4 são apresentados os resultados da análise dos dados e, por fim, as conclusões na Seção 5.

## 2. Trabalhos Relacionados

Análise de dados sobre a participação de mulheres em cursos superiores em computação e áreas afins é um tema bem discutido na literatura. Em [Santos 2019a], os autores trazem um panorama da atuação feminina na computação através do portal Elas na Computação, apresentando dados do número de ingressantes e concluintes em cursos da área no Brasil, como também resultados de um questionário aplicado online para as cinco regiões do país. O trabalho trouxe contribuições significativas no que diz respeito à centralização de informações acerca do tema, facilitando o acesso e a interpretação dos dados a partir das visualizações gráficas disponíveis.

Em [Marinho 2019] os autores apresentam um estudo descritivo, mas além de

analisar o número de ingressantes e concluintes também consideraram informações sobre a situação acadêmica dos alunos nos cursos de Tecnologia em Sistemas para Internet, bacharelado em Ciência da Computação, bacharelado em Sistemas de Informação e bacharelado em Engenharia de Computação. Os dados analisados foram em relação à permanência, abandono, cancelamento e trancamento. Nesse trabalho pôde-se observar uma similaridade no percentual de alunos de ambos os sexos que permanecem no curso, sendo este de 57%, enquanto o percentual de abandono é maior entre o público feminino, por volta de 30%, em comparação ao do público masculino, em torno de 20%. Em contrapartida, é menor o percentual de mulheres que optam por cancelamento ou trancamento do curso, respectivamente, 10% e menos de 5%, em oposição aos 15% e 5% dos homens.

Outro aspecto trabalhado em cima desse tema refere-se a comparar o desempenho das alunas e dos alunos. Em [Teixeira 2016] é apresentado um estudo sobre concluintes dos cursos de Ciência da Computação, Análise e Desenvolvimento de Sistemas e Sistemas para Internet na Universidade de Passo Fundo. Nessa análise de dados entre 2009 e 2015 foi visto que, com exceção do curso de Análise e Desenvolvimento de Sistemas, onde o rendimento acadêmico das mulheres foi 3,14% inferior, nos demais cursos da área de TI da instituição o desempenho feminino foi superior (em média 2%) ao dos homens. O estudo reforça que, por haver uma média de apenas 13% de mulheres ingressantes nesses cursos, é um resultado expressivo que elas tenham alcançado rendimento superior ao dos homens.

O presente trabalho se assemelha aos demais no que diz respeito à abordagem em torno da análise de ingressantes e concluintes no curso de computação, da situação acadêmica e do desempenho. Seu diferencial se faz em apresentar recortes de diversidade, distribuição de cotas e a taxa de sucesso em disciplinas específicas do curso.

## 3. Metodologia

Esta pesquisa segue uma abordagem quantitativa e descritiva de dados acadêmicos históricos do curso de bacharelado em Ciência da Computaçao da UFCG. Os dados utilizados foram cedidos para fins de pesquisa respeitando o anonimato dos alunos e são provenientes do Controle Acadêmico, que é o sistema de acompanhamento do discente durante a sua jornada acadêmica na universidade, incluindo informações como notas nas disciplinas e informações pessoais de ingresso. Essa análise consistiu em identificar as principais tendências dos dados que possam gerar informações relevantes sobre a participação de mulheres no curso.

Os dados analisados se referem aos períodos letivos de 2006.1 a 2019.2, no caso, 14 anos de curso. Esse período de tempo foi escolhido por conter dados mais completos, permitindo uma análise detalhada das informações. Os dados incluíram nota de ingresso do aluno e o tipo de entrada (cotistas ou não), raça, idade, situação acadêmica e desempenho nas disciplinas da graduação. O processamento dos dados foi feito em Python e as visualizações em R. Para alcançar o objetivo deste trabalho foram elaboradas as seguintes questões de pesquisa:

• Quantas mulheres e homens ingressam no curso?

> 1Não foi considerado os dados de 2020.1 haja vista que, no momento da coleta dos dados, o mesmo havia sido cancelado em decorrência da pandemia do SARS-CoV-2

- Qual o perfil das mulheres que ingressam no curso?

- Qual a situação acadêmica dos homens e mulheres do curso?

- Qual o desempenho de homens e mulheres nas disciplinas do curso?

Na Tabela 1 são descritas as colunas do dataframe ’alunos’, utilizado para analisar a distribuição de raças autodeclaradas, distribuição das cotas de ingresso e idade de ingresso das mulheres, como também a quantidade de ingressantes homens e mulheres e suas situações acadêmicas.

|Nome da coluna|Tipo|Descrição|
|---|---|---|
|periodo ~~i~~ngresso|Float|Períodoque o discente ingressou no curso|
|sexo|String|Sexo do discente|
|tipo ~~r~~eserva ~~v~~agas|Int|Tipo de reserva de vagapara ingresso no curso|
|forma ~~r~~eserva ~~v~~agas|String|Tipo de reserva de vagapara ingresso no curso|
|forma ~~e~~vasao|String|Forma de evasão do discente|
|idade ~~i~~ngresso|Int|Idadeque o discente ingressou no curso|
|nome ~~c~~or|String|Cor autodeclaradapelo discente|
|forma ~~s~~aida|String|Forma de saída do curso|

Tabela 1. Colunas utilizadas no dataframe alunos

A Tabela 2 descreve as colunas do dataframe ’historico ~~a~~ lunos’, utilizado para analisar o desempenho nas disciplinas do curso, através do sucesso nas 20 disciplinas de maior retenção.

|Nome da coluna|Tipo|Descrição|
|---|---|---|
|situacao|String|Situação atual do discente na disciplina|
|nome ~~d~~isciplina|String|Nome da disciplina|
|matricula|Int|Matrícula do discente|
|media ~~g~~eral|Float|Média final do discente em determinada cadeira|
|forma ~~e~~vasao|String|Forma de evasão do discente|

Tabela 2. Colunas utilizadas no dataframe historico ~~a~~ lunos

Para a análise de desempenho foram selecionadas as 20 disciplinas que mais retêm alunos no curso, usando os cálculos propostos em [Nunes 2020] e descritos abaixo:

Onde TR é a taxa de retenção na disciplina, nfalhas é o número de reprovações por nota e/ou por falta e ntentativas é o número de matriculados na disciplina.

A partir das 20 disciplinas com maior retenção foi calculado o sucesso de mulheres e homens. Para gerar o índice de sucesso foram consideradas as seguintes situações para o aluno em cada disciplina: aprovado, reprovado e reprovado por falta. Dessa forma, foi calculado o sucesso a partir da seguinte fórmula [Nunes 2020]:

Onde TXsucesso é a taxa de sucesso na disciplina, naprovados é o número de aprovados na disciplina, nsituacoes é o número de reprovações por nota e/ou por falta e o número de aprovados na disciplina.

## 4. Resultados

O curso de bacharelado em Ciência da Computação da UFCG foi criado em 1976 e iniciou suas atividades em 1977 enquanto Universidade Federal da Paraíba (UFPB), sendo um dos primeiros cursos formadores de profissionais em informática do país. Em 2002 teve origem a Universidade Federal de Campina Grande (UFCG) a partir do desmembramento da UFPB. Atualmente o curso possui em torno de 750 alunos ativos e mais de 1000 alunos graduados. Nesse contexto, segue uma análise sobre a participação de mulheres no curso no período de 2006.1 a 2019.2.

### 4.1. Quantas mulheres e homens ingressam no curso?

Como ilustrado na Figura 1, a maior parte dos ingressantes no curso de Ciência da Computação na UFCG é do sexo masculino. A média de ingressantes homens e mulheres no curso é de 83,74% e 16,26%, respectivamente.

Figura 1. Distribuiç ão de ingressantes em Ciência da Computaç ão na UFCG.

Com a implantação do REUNI em 2007, houve um aumento progressivo no número de vagas ofertadas no curso e atualmente são cerca de 180 vagas por ano. Além disso, de 2007.1 até 2019.2 houve um aumento de 0,8% no número de mulheres ingressantes no curso. Vale ressaltar que nesses dados não constam apenas novos ingressantes na graduação, como também reingressantes.

Considerando a média obtida no ENEM (Exame Nacional do Ensino Médio), que é a principal forma de entrada na UFCG pelos ingressantes no curso, tem-se uma média de 634,97, muito próxima da média das mulheres ingressantes, que é de 634,25.

### 4.2. Qual o perfil das mulheres que ingressam no curso?

O perfil das ingressantes no curso será representado pela raça, faixa etária e uso de cotas.

Figura 2. Distribuiç ão de raças dos ingressantes em Ciência da Computaç ão na UFCG.

Antes de analisar a distribuição de raças dos ingressantes, é importante ressaltar que as raças são autodeclaradas, ou seja, o aluno que deseja ingressar na universidade informa sua raça ou não. Caso seja cotista, a autodeclaração do candidato deve ser submetida à Comissão de Validação da Autodeclaração da UFCG para receber devida comprovação e assim ingressar na universidade a partir da cota racial.

De acordo com a Figura 2, pode-se observar que ao longo dos anos tem ocorrido um maior registro de diversidade de raças, principalmente a partir de 2011, ano em que a UFCG começou a adotar o ENEM como forma de avaliação para a entrada dos alunos. Outro aspecto relevante é que, ao longo do tempo, os ingressantes começaram a declarar as raças, já que a quantidade de “Não declarado” caiu consideravelmente.

No Brasil, a Lei de Cotas [Ministério da Educação 2012] foi aprovada em 2012 e previa que até 2016 todas as instituições federais de ensino superior e técnico deveriam destinar 50% das vagas a estudantes oriundos das escolas públicas. Esse percentual deveria ser dividido da seguinte forma: 25% das vagas para estudantes com renda igual ou inferior a 1,5 salário mínimo e 25% para aqueles com renda igual ou superior a 1,5 salário mínimo. Nessa divisão ainda seria destinado um percentual para pretos, pardos e indígenas, conforme o último Censo Demográfico do Instituto Brasileiro de Geografia e Estatística (IBGE).

Figura 3. Distribuiç ão das cotas utilizadas pelas ingressantes em Ciência da Computaç ão na UFCG.

Considerando o uso de cotas pelas mulheres do curso (vide Figura 3), é possível analisar que a maior parte das cotas utilizadas pelas ingressantes são de “Candidato autodeclarado preto, pardo ou indígena, com renda familiar bruta per capita igual ou inferior a 1,5 salário mínimo que tenha cursado integralmente o ensino médio em escola pública”, com cerca de 35 mulheres utilizando esta cota (36,45%).

Percebe-se então que houve um aumento de vagas oferecidas e da diversidade das discentes, apesar de ainda haver uma maioria branca e parda. Assim, o acesso à universidade cresceu por parte dos estudantes de escolas públicas e de baixa renda, mas segue distante das minorias raciais.

Por fim, considerando a faixa etária das ingressantes, cerca de 57,79% estão na faixa dos 16 a 19 anos, onde 30,45% do total das alunas ingressa no curso com 18 anos. No entanto, também há extremos: idade mínima de ingresso de 16 anos e idade máxima de 39 anos. A Figura 4 representa os resultados encontrados.

Figura 4. Distribuiç ão da faixa etária das mulheres em Ciência da Computaç ão na UFCG.

### 4.3. Qual a situação acadêmica dos homens e mulheres do curso?

A situação acadêmica é a situação atual dos alunos do curso, ou seja, se são graduados, regulares (com o curso em andamento), reingressantes (saíram do curso e retornaram com nova matrícula) ou evadidos (saíram do curso antes de concluí-lo).

Figura 5. Situaç ão acadêmica entre homens e mulheres em Ciência da Computaç ão na UFCG.

De acordo com a Figura 5 a média de evadidos do sexo masculino e feminino é bem próxima, respectivamente, 38,01% e 38,86%. Já o número de graduados homens é maior do que o de mulheres, porém, considerando a quantidade de ingressantes, a proporção de mulheres graduadas é de 21,32% e de homens 21,98%. Assim, tendo em vista que a proporção de estudantes formados no curso é similar entre homens e mulheres, o sexo não se mostra um fator determinante para concluir o curso.

### 4.4. Qual o desempenho de homens e mulheres nas disciplinas do curso?

Para analisar o desempenho, foram consideradas as 20 disciplinas com maior retenção no curso (vide Seção 3).

Na Figura 6 é ilustrada a mediana das notas de homens e mulheres em disciplinas do curso. Foi aplicado o teste estatístico de Wilcoxon para verificar se existiam diferenças significativas ao comparar o desempenho de homens e mulheres nessas disciplinas. De acordo com esse teste, calcula-se o valor de p (p-valor) que mede a evidência contra a hipótese de que não há diferença entre as amostras comparadas, quanto menor (p ¡ α ), maior é a evidência, ou seja, maior a probabilidade que as amostras sejam diferentes.

Observou-se que o desempenho de homens e mulheres nessas disciplinas é diferente na maioria delas, pois em muitas disciplinas o p-valor resultante no teste de hipótese é menor que a taxa de significância ( α ) de 0,05. Também é possível observar que os homens apresentam melhor desempenho na maioria das disciplinas específicas de computação e as mulheres nas disciplinas das áreas de matemática e física, sendo até 25% e 10% melhores, respectivamente. Mesmo assim, vale ressaltar que na metade das disciplinas de computação listadas as mulheres apresentam mediana acima de 7,0.

Figura 6. Classificaç ão do desempenho entre homens e mulheres nas disciplinas em Ciência da Computaç ão na UFCG.

Para completar a análise de desempenho, consideramos a taxa de sucesso (aprovação) entre homens e mulheres nas disciplinas em questão (vide Figura 7).

Na Figura 7 pode-se observar comportamentos parecidos nas curvas dos resultados de sucesso nas disciplinas entre homens e mulheres. A diferença maior está relacionada às disciplinas de matemática e física, como Probabilidade e Estatística, Matemática Discreta e Física Clássica, pois as mulheres possuem uma maior taxa de sucesso nessas disciplinas, como já demonstrado anteriormente com as medianas mais altas do que as dos os homens. Por outro lado, os homens tem maior taxa de sucesso na disciplina de

Figura 7. Classificaç ão do sucesso entre homens e mulheres nas disciplinas em Ciência da Computaç ão na UFCG.

Projeto de Software. Como resultado, tem-se que a taxa de sucesso varia entre 58% e 72% para as mulheres e 64% e 75% para os homens.

## 5. Conclusão

Diante do que foi analisado, pôde-se perceber que no curso de Ciência da Computação da UFCG há uma continuidade do padrão já visto de baixos números da participação feminina em cursos superiores da área. Para que a quantidade de mulheres ingressantes aumente, faz-se necessário o investimento em programas de incentivo e de acesso à tecnologia, o que pode ser reforçado através de grupos como o Elas@Computação.

Por outro lado, os resultados apresentados neste trabalho de que o sexo não é fator determinante para o sucesso na graduação, servem de motivação para as mulheres no curso e geram evidências de que computação não é só para homens, mas também para mulheres, se assim desejarem. Além disso, não deixa de ser um estímulo para a entrada de mais mulheres na área.

Espera-se que, ao trazer novos aspectos para as análises em torno do tema, essa pesquisa possa contribuir para futuras discussões no que diz respeito ao perfil e ao sucesso das mulheres em cursos de computação. Tendo em vista a fomentação desse debate, novos estudos podem ser realizados com maior foco na análise do desempenho dos discentes masculinos e femininos em disciplinas da graduação, podendo-se criar todo o panorama educacional do curso.
