# Análise do comportamento social das estudantes nas turma do curso técnico em Informática de uma Instituição Pública Federal de Ensino utilizando Redes Complexas

Vitória Calonga dos Santos, Nathalia G. Teixeira, Kalel Baião M. Pereira, Phelipe Oliveira Teixeira, João Gabriel Rocha Silva

1Instituto Federal de Mato Grosso - Pontes e Lacerda Caixa Postal 99 – 78.250-000 – Pontes e Lacerda – MT – Brasil

{ vitoria.calonga,nathalia.teixeira } @estudante.ifmt.edu.br

{ kalel.baiao,phelipe.teixeira } @estudante.ifmt.edu.br joao.gabriel@ifmt.edu.br

Abstract. Despite having a prominent brand and historical significance in the field of computer science, women are a minority in various aspects of computing, including among students in technical, undergraduate, and graduate programs in the field of information technology. Understanding the reasons behind this phenomenon and seeking strategies to mitigate the situation are issues of great interest and necessity within the scientific community. In this regard, this study examines the friendship networks of the six classes in the Technical Course in Computer Science at the Federal Institute of Mato Grosso, Campus Pontes e Lacerda - Fronteira Oeste, aiming to understand how female students establish their relationships and behave within these classes. Complex network technology was used to obtain the friendship networks of the classes. The results indicate that women are a minority in all analyzed classes, and their behaviors suggest tendencies towards female groupings in the majority of the classes.

Resumo. Ainda que com grande marca e importância histórica na área de informática, as mulheres são minoria em diversos âmbitos da computação, inclusive entre as discentes dos cursos técnicos, de graduação e pós-graduação da área de tecnologia da informação. Compreender os motivos pelos quais esse fenômeno acontece e buscar estratégias para mitigar a situação são problemas de alto interesse e necessidade da comunidade científica. Nesse sentido, neste trabalho desenvolvemos redes de amizades das 6 turmas do curso técnico em informática no Instituto Federal do Mato Grosso Campus Pontes e Lacerda - Fronteira Oeste buscando compreender como as estudantes estabelecem suas relações e se portam nas turmas. Para obtenção das redes de amizade das turmas a tecnologia de redes complexas foi utilizada. Resultados apontam que as mulheres são minoria em número em todas as turmas analisadas e seus comportamentos apontam tendências de agrupamentos femininos, na maioria das turmas.

## 1. Introdução

O desenvolvimento que a tecnologia apresenta no cenário atual é evidente[da Costa and Bergamaschi 1981]. Porém, é de conhecimento geral que

desde o início a computação é androcêntrica, mesmo a figura feminina tendo grande importância histórica.[Rago 1998], dados apontam que apenas 13, 3% das vagas dos cursos presenciais de gradução de computação são ocupadas por mulheres[IBGE 2021], o que corrobora os obstáculos na carreira profissional das mulheres, além de inibir as que almejam ingressar em ramos tecnológicos [Lima 2013], salientando que embora as mulheres atuem em áreas tipicamente masculinas, tão pouco possuem a visibilidade merecida [Santana et al. 2009].

Em vista disso, sabendo que as instituições de ensino técnico são uma das portas de entrada para a vida profissional e construção do perfil técnico [Pinto 2016], [Pereira et al. 2020], pode-se considerar que a relação que um aluno possui com terceiros nesse meio é uma ferramenta eficaz para retratar seu perfil e captar fenômenos que podem caracterizar o contexto em que as mulheres de determinada academia estão inseridas.

A procura de uma ferramenta capaz de possibilitar a visualização explícita das relações que os alunos do curso técnico de informática do Instituto Federal do Mato Grosso Campus Pontes e Lacerda - Fronteira Oeste (IFMT) possuem entre si, destacase a abordagem das propriedades das Redes Complexas [Concatto et al. 2020].

Percebe-se, que os elementos podem ser a representação de pessoas e as arestas, ou as ligações que esses elementos possuem são capazes de retratar as relação e interações que os sujeitos apresentam dentro de uma comunidade ou sala de aula por exemplo[Metz et al. 2007]. Dessa forma, o objetivo deste trabalho é desenvolver e analisar, com foco no gênero, as redes de amizades dos estudantes do IFMT utilizando redes complexas assim como o modelo de [Bianch 2021].

Por meio de um questionário aplicado às turmas envolvidas na pesquisa, foi possível desenvolver as redes de amizade. Resultados indicam a presença maior de homens no curso de informática, além da propensão das meninas em se agregarem. Portanto, as análises exercidas nos auxiliaram a esclarecer o comportamento das mulheres em um contexto tradicionalmente masculino.

## 2. Materiais e Métodos

Etapa I: Na primeira etapa desenvolvemos um questionário com o intuito de obter as informações sobre os estudantes do curso técnico em Informática do IFMT acerca de suas amizades, cada estudante poderia marcar de 1 até 5 amigos da turma, e perguntas relacionadas a saber sobre o gênero e quem seriam os integrantes do grupo, como: Qual o seu gênero e selecione de um até cinco amigos da turma.

O questionário foi aplicado nas 6 turmas do curso Técnico em Informática Integrado ao Ensino Médio do IFMT, sendo duas turmas de cada ano do ensino médio. Ao todo obtivemos 158 respostas dos estudantes, vale ressaltar que, mesmo que os alunos se identifiquem, seus dados são tratados no anonimato e codificados para que se mantenham anônimos.

Etapa II: Seguidamente da aplicação do questionário, os dados foram codificados para geração das redes de amizade utilizando a tecnologia das redes complexas. Nesse modelo, os estudantes são representados pelos vértices e as relações de amizade pelas arestas. Para detecção de agrupamentos dentro das turmas, o algoritmo de [Blondel et al. 2008] foi utilizado devido sua credibilidade na comunidade científica.

Nessa etapa, utilizamos a linguagem de programação Python e a biblioteca Igraph.

Etapa III: Por fim, utilizamos de visualização gráfica para analisar a forma organizacional de cada uma das turmas e das comunidades focando na compreensão do posicionamento das meninas. E assim, responder as seguintes questões de pesquisa:

1. Qual a proporção de gênero feminino no curso de informática do IFMT?

2. Como são as amizades e interações das estudantes femininas nas turmas de Informática?

## 3. Respostas às questões de Pesquisa

### 3.1. Qual a proporção de gênero feminino no curso de informática do IFMT?

A Figura 1 apresenta a proporção, por gênero, entre os estudantes que responderam o questionário. Nesse sentido, observamos a predominância de estudantes do gênero masculino na instituição, em números absolutos, 99 respondentes se identificaram como gênero masculino, 57 com o gênero feminino e 2 estudantes declararam não identificação com nenhum dos dois gêneros, optando pela marcação Não-Binário.

Figura 1. Proporç ão por gênero dos estudantes envolvidos na pesquisa

Como podemos observar, o IFMT repete proporções de meninas menores que a de meninos assim como o trabalho de [Pereira et al. 2020]. Na instituição analisada, os estudantes que se identificam como gênero feminino correspondem a apenas 36% do total de alunos no curso que responderam o questionário.

### 3.2. Como são as amizades e interações das estudantes femininas nas turmas de Informática?

As Figuras 2 (a) e 2 (b) são redes complexas que retratam a distribuição dos estudantes na sala de aula em relação às suas amizades, eles estão representados pelos vértices: meninos em azul-escuro, meninas em rosa e pessoas que optaram por não responder em azul-claro. Um conjunto de vértices próximos formam uma comunidade, área colorida ao redor dos vértices, que foram valorados de acordo com suas respectivas cores.

Analisando a Figura 2 (a), referente a turma do 1º Informática Matutino, percebemos que há tendências de agrupamento: as meninas possuem propensão a ter amizades femininas, pois apesar de estarem presentes em quase todas as comunidades ( 5 munidade Rosa contém apenas meninas, além disso, está um pouco afastada das demais

Figura 2. Redes de amizade em comunidades das turmas dos 1ºs anos do IFMT

comunidades, apresentando somente duas ligações com estudantes pertencentes a outras comunidades; os meninos tendem a ter mais amizades masculinas, visto que a comunidade Vermelha – maior comunidade – é composta somente por meninos e a comunidade Verde possui apenas 1 menina.

Observando a Figura 2 (b), referente a turma do 1º Informática Vespertino, percebemos uma leve exclusão entre as comunidades, na qual a comunidade Amarela está um pouco afastada das demais; observamos também que na comunidade Azul, as mulheres tendem a se agruparem.

(a) Rede de amizade em comunidades do 2º ano do período matutino

Figura 3. Redes de amizade em comunidades das turmas dos 2ºs anos do IFMT

Averiguando a Figura 3 (a), referente a turma do 2º Informática Matutino, observamos que há grandes tendências de agrupamento: Os meninos se agrupam de forma muito intensa, pois metade das comunidades (Azul-claro, Verde, Amarela) são formadas exclusivamente por meninos e a comunidade Vermelha possui apenas 2 meninas e uma pessoa que se identificou como não-binário representado na cor amarela, além disso, essas 4 comunidades possuem muitas ligações entre si, quase se sobrepondo, e estão fortemente ligadas com os meninos da comunidade Azul; As meninas tendem a se agruparem também, pois a comunidade Rosa é composta apenas por figuras femininas e está um pouco afastada das demais comunidades, além disso, a comunidade Azul-escuro é composta em sua maioria por figuras femininas que estão se agrupando. Portanto, acredita-se que, nessa turma, ambos os gêneros tendem a se agruparem de forma muito intensa.

Considerando a figura 3 (b), referente a turma do 2º Informática Vespertino, percebeu-se que há tendências de agrupamento: As meninas tendem a ter amizades femininas, pois a comunidade Vermelha é composta em sua maioria por figuras femininas

e elas se agrupam de forma singela dentro da própria comunidade; os meninos tendem a ter mais amizades masculinas, pois 2 comunidades (Amarela e Azul) possuem apenas figuras masculinas e a comunidade Verde possui apenas 2 figuras femininas.

(a) Rede de amizade em comunidades do 3º ano do período matutino

(b) Rede de amizade em comunidades do 3º ano do período vespertino

Figura 4. Redes de amizade em comunidades das turmas dos 3ºs anos do IFMT

Avaliando a Figura 4 (a), percebemos que há pequenas tendências de agrupamento: As meninas tendem, de forma tênue, a ter amizades femininas, pois a comunidade Verde é composta, em sua maioria, por meninas contendo apenas 2 meninos; tal comportamento também é observado nos meninos, devido a comunidade azul conter apenas 1 figura feminina. No entanto, vale ressaltar que, apesar das pequenas tendências agrupamentos, existem muitas ligações entre diversos estudantes de diferentes comunidades, independente do gênero. Acreditamos que esse fenômeno é causado pelo fato do número absolutos de estudantes por gênero nessa turma ser parecido.

Explorando a Figura 4 (b), percebemos que há uma tendência de agrupamento: Os meninos tendem a ter amizades Masculinas, pois a comunidade Verde é composta, em sua maioria, por meninos contendo apenas 1 menina, já a comunidade vermelha é composta por diversas meninas, tendo 2 meninos e 1 não-binário, representado por meio da cor amarela.

Após investigar todos os gráficos e redes, visualizamos que as turmas com maior discrepância no número de estudantes por gênero possuem maiores tendências de agrupamento; e turmas com um número menor de estudantes por gênero possuem menos tendências de agrupamento e suas comunidades possuem mais ligações entre si.

## 4. Considerações Finais e Trabalhos Futuros

Neste artigo foram apresentados dados e redes de amizades das turmas do curso técnico de Informática integrado ao ensino médio do IFMT. Por meio disso, promovemos análises sobre os estudantes das turmas analisadas em questões de gênero.

Após analisar os dados destas turmas, resultados indicam que a maioria das mulheres preferem estar no âmbito de outras mulheres. Portanto, visto que na instituição onde o questionário foi aplicado não há nenhum evento ou debates que visam discutir a visibilidade feminina na computação, é possível promover esses meios para sanar esse problema. Como trabalhos futuros desenvolveremos relações entre gênero, classe social e cor no intuito de entender a pluralidade dessas mulheres e se, em condições de raça e cor, o modelo de acolhimento se estabelece e se existe alguma característica que define o comportamento social das estudantes.
