# Análise do Desempenho Acadêmico das Alunas Cotistas na Primeira Disciplina de Programação da Universidade de Brasília

Kailany Ketulhe, Maristela Holanda, Alice Lima, Alice Borges, Aleteia Araujo, Carla Castanho, Carla Koike, Roberta B. Oliveira

1Departamento de Ciência da Computação - Universidade de Brasília (UnB) Brasília - DF - Brasil

{ Kailany.gomes,alice.lima,alice.borges } @aluno.unb.br

{ mholanda,aleteia,carlacastanho,ckoike,roberta.oliveira } @unb.br

Abstract. In 2012, Law 12,711, also known as the Quota Law, was applied in all federal higher education institutions in Brazil. It stipulated that 50% of students entering undergraduate courses should come from public schools. Before the quota law, only 20% of students in the Department of Computer Science at the University of Brasília had attended public high schools. At this same University, the dropout rate in computing courses has been consistently high. According to the literature, failing the first course in computer programming impacts significantly on the dropout rate. In this context, this article aims to analyze the academic performance of quota and non-quota students in the Department of Computer Science at University of Brasília in particular, with relation to gender. The results show that the difference is very small between quota male and female students, but there is a big difference between quota and non-quota female students in the four undergraduate courses of the department.

Resumo. A Lei 12.711 de 2012, conhecida como Lei das Cotas, aplicada em todas as instituições de ensino superior federais do Brasil definiu que 50% dos estudantes ingressantes em cursos de graduação deveriam ser oriundos de escolas públicas. Especificamente, no Departamento de Ciência de Computação da Universidade de Brasília, antes desta lei, apenas 20% dos estudantes eram de escola pública. A evasão nos cursos de computação da Universidade de Brasília tem sido elevada, e de acordo com a literatura, um dos pontos de desistência dos estudantes em computação é a reprovação na primeira disciplina de programação. Neste contexto, este artigo tem como objetivo analisar o desempenho acadêmico de alunas cotistas e não cotistas no Departamento de Ciência da Computação da Universidade de Brasília. Os resultados mostram que a diferença é muito pequena entre os alunos e alunas cotistas, porém existe uma grande diferença entre alunas cotistas e não cotistas nos quatro cursos de graduação do referido departamento.

## 1. Introdução

A Universidade de Brasília (UnB) foi a primeira instituição de ensino superior federal brasileiro a adotar um sistema de cotas raciais para ingresso por meio do vestibular, a

partir do segundo semestre de 2004. Anos após, em 2012, o Governo Brasileiro criou a Lei 12.711/2012, que tem como principal característica a reserva de 50% do total de vagas da instituição para estudantes que tenham cursado integralmente o ensino médio em escolas públicas: essas vagas ainda são subdivididas de acordo com o perfil econômico. A lei das cotas aumentou a diversidade de perfil educacional dos alunos que ingressam nos cursos do Departamento de Ciência da Computação da UnB, pois antes da lei de cotas, a entrada de alunos que fizeram o ensino médio em escolas públicas era de aproximadamente 20% apenas.

Como pode ser observado no relatório da ACM ( Association for Computing Machinery ) em [Stephenson et al. 2018], nas instituições americanas, questões que se destacam em relação à retenção dos estudantes em computação envolvem: (1) as dificuldades no primeiro ano do aluno em um curso superior em Computação; (2) a primeira matéria de programação; e (3) a diferença de perfil educacional e a questão da falta de diversidade entre os estudantes de Computação. Especificamente sobre o ensino da primeira linguagem de programação, vários artigos relatam a importância dessa disciplina para a persistência dos estudantes em cursos da Computação, como em [Watson and Li 2014], [Robins 2019], [Luxton-Reilly et al. 2018] e [Becker and Quille 2019].

A falta de diversidade de gênero, no qual o número de estudantes do gênero feminino nos cursos de graduação em Computação é desproporcional ao número de estudantes do gênero masculino, tem sido um tema de pesquisa de muitas instituições em todo o mundo. Tem-se que, no Brasil, entre os anos 2000 e 2013, o número de concluintes dos cursos de Computação do gênero masculino aumentou 98%, enquanto o número de concluintes do gênero feminino diminuiu 8% [Maia 2016]. Na UnB, o número de meninas nos cursos de graduação de Computação é menor do que 20% [Holanda et al. 2017] nos últimos 15 anos.

Neste contexto, este artigo tem como objetivo fazer uma análise de desempenho acadêmico na primeira disciplina de programação para os cursos de computação da UnB das alunas cotistas e não cotistas. O Departamento de Ciência da Computação tem quatro cursos de graduação: Licenciatura em Computação, Ciência da Computação, Engenharia da Computação e Engenharia Mecatrônica. A análise foi realizada com dados entre os anos de 2010 e 2019, fornecidos pela Secretaria de Tecnologia da Informação da UnB e extraídos do sistema acadêmico da instituição.

O restante deste artigo está dividido nas seguintes seções: a Seção 2 apresenta o sistema de cotas na UnB; na Seção 3 são apresentados os trabalhos relacionados; a Seção 4 apresenta a metodologia utilizada para a realização da análise; a Seção 5 apresenta os resultados obtidos; na Seção 6, uma discussão dos resultados é apresentada; e a Seção 7 traz as conclusões e os trabalhos futuros.

## 2. Sistema de Cotas

As cotas raciais são ações afirmativas aplicadas em alguns países, como no Brasil, a fim de diminuir as disparidades econômicas, sociais e educacionais entre pessoas de diferentes etnias raciais. Assim sendo, na UnB o candidato pode concorrer para uma vaga por meio de três sistemas diferentes: Sistema universal com 45% das vagas, sistema de cotas para negros com 5% das vagas e sistema de cotas para escolas públicas com 50% das vagas.

Para concorrer pelo sistemas de cotas para Escolas Públicas, o candidatado deve

ter cursado integralmente o ensino médio em escolas públicas, em cursos regulares ou na modalidade Educação para Jovens e Adultos, ou ter obtido certificado de conclusão do ensino médio por exames nacionais ou estaduais de certificação de competência ou de avaliação de jovens e adultos. No Sistema de Cotas para Escolas Públicas, a reserva de vagas é dividida conforme candidatos:

- Com renda familiar bruta igual ou inferior a 1½ salário mínimo per capita (Baixa Renda);

- Com renda familiar bruta superior a 1½ salário mínimo per capita (Alta Renda);

- Que se declaram pretos, pardos ou indígenas (PPI);

- Que não se declaram pretos, pardos ou indígenas (Não PPI);

- Com deficiência (PCD).

A UnB adotou a política de cotas raciais, reservando 20% das vagas do vestibular para aqueles que se declarassem e fossem considerados pretos por uma banca avaliadora. Essa política teve seu início no segundo semestre de 2004, porém, os primeiros registros de alunas cotistas provenientes das cotas reservadas para pessoas negras indicam que apenas no segundo semestre de 2009 uma aluna negra ingressou no curso de Ciência da Computação e outra aluna negra ingressou em Engenharia Mecatrônica, conforme apresentado na Figura 1.

Figura 1. Entrada de alunas nas cotas por ano.

Também pode-se observar na Figura 1 que a partir do ano 2013, as primeiras alunas cotistas no curso de Licenciatura em Computação: três alunas por meio da cota de Escola Pública-Baixa Renda-PPI e uma aluna pela cota de Escola Pública-Baixa RendaNão PPI. Outro fato importante é o ingresso ascendente das estudantes pelas cotas Escola Pública-Alta Renda-Não PPI e Escola Pública-Alta Renda-PPI, entre 2015 e 2016. Temos registro que a primeira aluna cotista a ingressar em Engenharia da Computação foi no primeiro semestre de 2010 proveniente da cota para negros.

## 3. Trabalhos Relacionados

Na literatura tem alguns trabalhos relacionados ao tema de estudantes cotistas e outros que analisam o desempenho acadêmico de mulheres na computação. Cardoso

em [Cardoso 2008] apresenta que na Universidade de Brasília (UnB), verificou-se que os alunos cotistas obtiveram rendimento substancialmente inferior ao dos alunos do sistema universal, apesar destes evadirem em proporções menores. No artigo [Junior and Ferreira 2014] conclui-se que, em um estudo realizado com alunos da Universidade do Estado do Rio de Janeiro (UERJ), que os cotistas possuem pior rendimento em relação aos não cotistas, e que esta diferença é maior conforme a dificuldade relativa do curso.

Muitos artigos apresentam análise sobre número de estudantes ingressos e formados em cursos de Computação em instituições de ensino superior brasileiras, como por exemplo em [Nakamura et al. 2017], [Sales et al. 2017], [Oliveira et al. 2018] e [Marinho et al. 2019]. Neste cenário, considerando apenas os artigos que apresentam dados de desempenho em termos de nota (desempenho acadêmico), em institutos federais e universidade, em diferentes regiões do Brasil, tem-se: [Holanda et al. 2017], [Bordin et al. 2020], [Marques et al. 2021] e [Silva and Santos 2021].

Contudo, diferentemente dos trabalhos apresentados anteriormente, este artigo apresenta a análise sobre o desempenho das alunas, cotistas e não cotistas, na primeira linguagem de programação, uma disciplina na qual a reprovação pode levar as meninas evadirem dos cursos de Computação. Assim, o bom desempenho nesta disciplina introdutória à área de Computação pode desenhar a perseverança das meninas continuarem na área escolhida ou não. Isso tem uma importância ímpar na expectativa de termos maior diversidade de gênero na área de TIC (Tecnologia da Informação e Comunicação), pois além de trabalharmos nos Ensinos médio e fundamental para atrairmos mais meninas para a área, é fundamental que essas meninas tenham apoio para concluírem seus cursos superiores na Computação.

## 4. Metodologia

A pesquisa realizada neste trabalho foi dividida em etapas. A primeira etapa foi a definição das questões de pesquisa. Em seguida, realizou-se a análise detalhada dos dados. Na etapa de análise de dados, o processo dos dados é descrito nesta seção, e a apresentação dos resultados e a discussão sobre os mesmos na Seção 5.

### 4.1. Questões de Pesquisa

Com o objetivo de investigar o desempenho das alunas cotistas e não cotistas, na primeira disciplina de programação da UnB, foram definidas as seguintes Questões de Pesquisa (QP):

- QP1) Como foi o desempenho geral das alunas (cotistas e não-cotistas) nas disciplinas básicas de programação?

- QP2) Como foi o desempenho das alunas comparado aos alunos nas disciplinas básicas de computação?

Neste contexto, este artigo ao responder as questões de pesquisa citadas acima, pretende evidenciar diferenças entre os grupos e a necessidade de criação de programas específicos para as alunas, cotistas e não-cotistas, na instituição.

### 4.2. Processamento dos Dados

O processamento de dados nesta pesquisa foi dividido nas seguinte etapas [Camilo and Silva 2009]: limpeza, seleção, transformação, análise e a visualização dos

dados. Como informado anteriormente, a análise e a visualização dos dados são etapas que serão apresentadas na Seção 5. Esses dados foram coletados do sistema acadêmico da UnB, que teve a sua liberação por meio do comitê de ética que aprovou o seu uso, parecer número 4.283.719, de 17/09/2020.

A etapa de limpeza dos dados foi desenvolvida por meio da linguagem Python, na qual foram implementados os seguintes filtros para a seleção dos seguintes dados:

- Apenas dados de alunos dos cursos de Engenharia da Computação, Ciência da Computação, Licenciatura da Computação e Engenharia Mecatrônica;

- Dados a partir de 2004 até 2019. Um ponto importante de observação é que a lei das cotas nas universidades federias do Brasil iniciou em 2012, porém, a universidade em questão criou uma resolução própria de cota em 2004;

- Dados apenas da primeira linguagem de programação. Inicialmente, essa disciplina era chamada de Computação Básica (CB) e em 2015, com a mudança do currículo, a disciplina passou a ser nomeada de Algoritmo e Programas de Computadores (APC)

Na etapa da seleção foram considerados quatro atributos: “Curso”, “Tipo de Cota”, “Nome da Disciplina”, “Período de Ingresso no Curso” e “Menção”. Esses atributos são fundamentais para as respostas das questões de pesquisa deste artigo. O atributo Menção diz respeito a sistema de nota típico da universidade, na qual cada menção corresponde a um intervalo de nota, ou seja, SR (0 a 0,9), II (1,0 a 2,9), MI (3,0 a 4,9), MM (5,0 a 6,9), MS (7,0 a 8,9) e SS (9,0 a 10). Para a aprovação o aluno deve ter a menção MM, MS ou SS e frequência maior ou igual a 75%.

Para a etapa de transformação foi utilizada a ferramenta Power BI. Nesta fase houve a necessidade de realizar algumas transformações para a análise, as quais foram: (1) a criação de um atributo novo chamado ano de ingresso, o qual agregou dados do primeiro e segundo semestre de cada ano; e (2) uma coluna foi acrescentada indicando se o aluno é cotista a partir dos tipos de cotas definidos na UnB.

## 5. Respostas às Questões de Pesquisa

### 5.1. QP1) Como foi o desempenho geral das alunas (cotistas e não-cotistas) nas disciplinas básicas de programação?

Para responder à QP2 foram utilizados dados de desempenho das alunas nas disciplinas: Computação Básica e Algoritmo e Programação de Computadores (APC), comparando alunas que concorreram pelo sistema universal consideradas não cotistas e pelas consideradas cotistas. Para facilitar a análise, o cálculo apresentado na Tabela 1 é uma média simples entre número de menções e o número total de alunas de acordo com o sistema de entrada.

Os resultados confirmam que o desempenho geral das alunas não cotistas é superior ao das cotistas nas menções em que o estudante tem aprovação, segundo as métricas da universidade, sendo as seguintes menções: MM, MS e SS. Assim, os resultados mostram que as alunas cotistas tiveram mais menções MI e II (ou seja, menções insuficientes para a aprovação). Ao analisar as menções apenas das alunas aprovadas, nota-se que 72,11% das alunas que ingressam pela cota universal foram aprovadas, enquanto que para as alunas cotistas esse percentual foi de apenas 57,02%, ou seja, um pouco mais do que a metade apenas.

Tabela 1. Tabela de comparaç ão de desempenho entre as alunas.

|Menção|Cotista|Não cotista|
|---|---|---|
|II|26,54%|17,67%|
|MI|15,43%|10,23%|
|MM|24,07%|24,19%|
|MS|22,84%|27,45%|
|SS|11,11%|20,46%|

Para analisar a diferença das médias por menção, a Figura 2 mostra a média das alunas não cotistas, e a Figura 3 para as alunas cotistas. Assim sendo, os dados sugerem que as maiores diferenças estão na menção SS, na qual as alunas não cotistas tiveram um melhor desempenho. Por outro lado, na menção SR (a menor menção possível da UnB, as alunas cotistas tiveram essa atribuição em uma quantidade maior de vezes.

Figura 3. Menç ões das Alunas Cotistas

Para entender melhor se o desempenho das alunas cotistas é o mesmo em todos os quatro cursos de Computação, as Figuras 4a, 4b, 4c e 4d apresentam a distribuição das notas dos cursos de Ciência da Computação, Engenharia da Computação, Engenharia Mecatrônica e Licenciatura da Computação, ainda nas disciplinas de Computação Básica ou APC. As figuras apresentam dados entre os anos de 2010 (barra do topo) e 2019 (barra mais baixa). As cores em roxo representam a aprovação na disciplina (menções MM, MS e SS). A cor laranja representa reprovação (SR, II e MI), a cor cinza representa o trancamento da disciplina e, por fim, a azul clara trancamento geral do semestre.

Alguns pontos de destaque nessas figuras são: Licenciatura de Computação tem um alto índice de reprovação nessa primeira disciplina de programação (a parte laranja é bem maior que a roxa), enquanto nos outros cursos existe uma distribuição maior entre aprovação e reprovação; para o curso de Ciência de Computação houve um aumento do número de aprovação após o ano de 2015, tendo o melhor momento em 2019; no curso de Engenharia da Computação, um destaque para o ano de 2017 no qual as quatro alunas que cursaram a disciplina foram aprovadas; por fim, na Engenharia Mecatrônica, em 2018, nenhuma das 10 alunas foi aprovada na disciplina.

Figura 4. Distribuiç ão das menç ões entre os anos de 2010 e 2019 na primeira linguagem de programaç ão.

### 5.2. QP2) Como foi o desempenho das alunas comparado aos dos alunos na disciplina básica de computação?

Para responder esta questão de pesquisa são apresentados os dados dos estudantes cotistas e não-cotistas por gênero. Para facilitar a análise, os valores apresentados nas próximas tabelas são médias aritméticas entre o número de menções e o número total de estudantes, de acordo com o sistema de entrada e o seu gênero.

Como apresentado na Tabela 2, observa-se que o desempenho das alunas cotistas e os alunos cotistas não tem grande variação, o mesmo acontece com os dados das alunas não cotista e os alunos não cotistas. Os resultados confirmam que o desempenho geral dos estudantes não cotistas é superior ao dos cotistas nas menções em que o estudante tem aprovação, segundo as métricas da universidade. Assim, os estudantes cotistas tiveram o maior número de menções MI e II. Em relação à diferença das médias por menção, os dados mostram que as maiores diferenças estão entre os estudantes em geral cotistas e os estudantes não cotista, no qual os estudantes que ingressaram pelo sistema universal tiveram 20,06% de aprovação na menção, e os demais estudantes tiveram apenas de 11,10% de aprovação com a mesma menção. Ao analisar a menção II, tem-se que dos alunos cotistas 25,59% foram reprovados, em contraposição tem-se apenas 15,80% dos alunos não cotistas.

Como apresentado na Figura 5, existe uma diferença entre desempenho dos estudantes (homens e mulheres) não cotista e cotistas. Porém, quando comparamos as diferenças conclui-se que elas são pequenas, como pode ser notado nas seguintes percentagens: Alunas cotistas, 58,02%; Alunas não cotistas, 62,55%; Alunos cotistas, 72,10 e Alunos não cotistas, 74,06%.

Para entender se tem alguma diferença nesses resultados ao analisar, especifica-

Tabela 2. Tabela de comparaç ão de desempenho entre os alunas e alunos

|Menção|Cotistas(F)|Cotistas(M)|Não Cotistas(F)|Não Cotistas(M)|
|---|---|---|---|---|
|II|26,09%|23,85%|15,00%|12,76%|
|MI|16,31%|13,33%|10,67%|11,71%|
|MM|24,46%|27,25%|26,67%|23,90%|
|MS|22,28%|25,45%|27,33%|33,37%|
|SS|10,86%|10,12%|20,33%|18,26%|

Figura 5. Menç ões por gênero e cota.

mente, um curso de graduação, as tabelas seguintes apresentam os dados dos quatro cursos de computação de maneira separada, sendo a Tabela 3 apresenta os dados dos estudantes do curso de Ciência da Computação; a Tabela 4 os dados da Engenharia da Computação; a Tabela 5 os dados do curso de Licenciatura em Computação; e a Tabela 6 os dados da Engenharia Mecatrônica. Como pode ser observado, em todos os cursos o padrão é o mesmo, a diferença não é maior pela forma de entrada (cotista e não-cotistas) do que por gênero.

Tabela 3. Ciência da Computaç ão.

|Menção|Cotistas(F)|Cotistas(M)|Não Cotistas(F)|Não Cotistas(M)|
|---|---|---|---|---|
|II|24,44%|22,30%|9,23%|9,41%|
|MI|8,89%|13,51%|10,77%|11,86%|
|MM|26,67%|22,97%|24,61%|21,66%|
|MS|24,44%|24,66%|32,31%|32,40%|
|SS|15,56%|16,56%|23,08%|24,67%|

## 6. Discussão dos Resultados

Em relação à QP1, existe uma grande diferença entre o nível de aprovação de alunas cotistas e não cotistas. A inclusão social que trouxe a lei de cota é muito importante para reparar déficits antigos com a sociedade carente, porém é necessário criar programas de apoio para essas alunas no ensino da primeira linguagem de programação. Caso contrário,

Tabela 4. Engenharia de Computaç ão.

|Menção|Cotistas(F)|Cotistas(M)|Não Cotistas(F)|Não Cotistas(M)|
|---|---|---|---|---|
|II|22,23%|25,10%|16,67%|8,35%|
|MI|13,33%|13,72%|12,50%|12,43%|
|MM|22,23%|25,49%|18,05%|23,89%|
|MS|26,66%|24,71%|26,39%|33,20%|
|SS|15,55%|10,98%|26,39%|22,13%|

Tabela 5. Licenciatura em Computaç ão.

|Menção|Cotistas(F)|Cotistas(M)|Não Cotistas(F)|Não Cotistas(M)|
|---|---|---|---|---|
|II|35,71%|26,77%|25,60%|23,89%|
|MI|17,86%|11,61%|14,63%|14,34%|
|MM|21,43%|31,31%|34,17%|28,87%|
|MS|21,43%|27,28%|17,07%|24,26%|
|SS|3,57%|3,03%|8,53%|8,64%|

a lei de cota não atingirá seu verdadeiro potencial de fazer surgir uma sociedade mais justa e igualitária entre raça, gênero e poder econômico.

Por fim, na QP2, os dados apresentam que para a primeira linguagem de programação, o desempenho entre as mulheres e os homens são semelhantes, e a diferença é mais forte pela questão do ingresso de cota e não cota. Desta forma, mais uma vez, é necessário ter programas que possam apoiar as alunas cotistas, tal como um programa de acolhimento das mulheres cotistas em curso de Computação.

Diante do exposto no trabalho, fica evidente a necessidade de ações afirmativas para inclusão de mulheres pretas na computação, apesar da lei existir na instituição entre 2004-2012 (antes da lei federal), apenas uma aluna entrou no sistema de cota racial. Nenhuma aluna entrou nos cursos de Engenharia de Computação e Licenciatura em Computação da UnB.

## 7. Conclusão

Este artigo apresentou uma análise do desempenho acadêmico das alunas cotistas que ingressam nos cursos de Computação na UnB. Com os dados apresentados, ficou evidente que as mulheres e os homens dentro da mesma cota de ingresso têm desempenhos semelhantes na primeira linguagem de programação dos quatro cursos de computação analisados. A maior diferença encontra-se entre os grupos cotistas e não-cotistas.

Acredita-se que os resultados obtidos neste trabalho possam ser utilizados pela instituição na identificação precoce de alunas cotistas com possibilidade de ter menor desempenho na graduação. A identificação destas estudantes pode ajudar no planejamento de estratégias para tentar melhorar o rendimento acadêmico destas alunas.

Como trabalho futuro as autoras deste artigo pretendem fazer uma pesquisa de percepção com as alunas sobre o ensino da primeira linguagem de programação, analisar a relação dos professores das disciplinas e o rendimento escolar, pesquisar a conexão entre as ementas das disciplinas e seus impactos no rendimento dessas alunas, identificar

Tabela 6. Engenharia Mecatrônica.

|Menção|Cotistas(F)|Cotistas(M)|Não Cotistas(F)|ão Cotistas(M)|
|---|---|---|---|---|
|II|25,76%|22,09%|7,43%|8,77%|
|MI|22,73%|14,06%|4,93%|7,97%|
|MM|25,76%|30,92%|28,39%|20,91%|
|MS|18,18%|25,70%|34,56%|44,42%|
|SS|7,57%|7,23%|24,69%|17,93%|

quais fatores anteriores a essa entrada corroboram para essa larga diferença, pesquisar como a modalidade cotista incide diretamente na representatividade feminina na área de Computação. Em seguida, analisar o impacto da reprovação na primeira disciplina de programação na evasão dos cursos de Computação, e iniciar programas de apoio para as alunas cotistas em cursos de Computação na UnB.

## 8. Agradecimentos

As autoras agradecem ao apoio do CNPq (Processos No 440806/2019-4) e ao Programa Meninas Digitais da SBC pela inspiração na inclusão de mais meninas na Computação.
