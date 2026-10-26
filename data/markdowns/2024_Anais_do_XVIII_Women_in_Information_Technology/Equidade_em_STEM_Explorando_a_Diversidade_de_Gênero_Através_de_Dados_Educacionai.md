# Equidade em STEM: Explorando a Diversidade de Gênero Através de Dados Educacionais de Avaliações em Larga Escala

Letícia Gabrielle P. B. dos Santos, Erica L. Gallindo, Mário W. L. Moreira

> 1Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE) campus Aracati Rodovia CE-040, Km 137 – Aracati – CE – Brazil

leticiapbs408@gmail.com, { erica.gallindo, mario.wedney } @ifce.edu.br

Abstract. This paper analyzes data from the National High School Examination (ENEM) and the Unified Selection System (SISU) to prove that the non-selection of female candidates in STEM fields is not directly related to their low performance in Mathematics. Data analysis techniques and the Tableau tool were used to perform these analyses and visualize the data. The results indicated that approximately 80% of women would have a minimum score in mathematics to enter STEM courses. Additionally, men had a higher average than women in the mathematics test of the 2021 ENEM in all analyzed scenarios; however, the difference between the averages was small and did not exceed 45 points.

Resumo. Este artigo analisa os dados do Exame Nacional do Ensino Médio (ENEM) e do Sistema de Seleção Unificada (SISU) a fim de provar que a não escolha de candidatas por áreas de STEM não tem relação direta com o baixo desempenho destas em Matemática. Para realizar estas análises foram utilizadas técnicas de análise de dados e a ferramenta Tableau para a visualização destes dados. Os resultados indicaram que aproximadamente 80% das mulheres teriam nota mínima em matemática para ingressarem em cursos de STEM. Além disso, os homens apresentaram uma média maior que as mulheres na prova de matemática do ENEM 2021 em todos os cenários analisados, porém a diferença entre as médias foi pequena, e não ultrapassou os 45 pontos.

## 1. Introdução

Atualmente, as áreas de science, technology, engineering, and mathematics (STEM) são vistas como profissões do futuro, por impulsionarem a inovação e o desenvolvimento sustentável. Apesar destes benefícios, existem barreiras que fazem com que as meninas não optem por uma carreira nessas áreas, aumentando a disparidade de gênero neste universo. Apesar dos esforços para reduzir esta disparidade, ainda existem lacunas na educação e em diferentes níveis de carreiras em STEM que persistem praticamente em todos os países do mundo.

Entre os 17 objetivos de desenvolvimento sustentável da Agenda 2030 da Organização das Nações Unidas (ONU), destaca-se o Objetivo 5, que tem como ideia principal alcançar a igualdade de gênero e empoderamento de mulheres e meninas, dando mais autonomia a estas em qualquer área que desejem atuar. Um relatório da Organização da Nações Unidas para a Educação, a Ciência e a Cultura (Unesco) [UNESCO 2018,

> 1Disponível em: < https://brasil.un.org/pt-br/sdgs/5 >. Acesso em 6 de dez. de 2023.

p. 18] revelou um aumento nas matrículas femininas em todos os níveis de ensino, especialmente na educação superior entre 2000 e 2014, com as mulheres sendo maioria em cursos de graduação e mestrado. No entanto, barreiras socioeconômicas e culturais ainda dificultam a conclusão dos cursos e o acesso a uma educação de qualidade conforme a preferência das mulheres.

Segundo o Instituto Brasileiro de Geografia e Estatística (IBGE), apesar de serem maioria no ensino superior e terem um maior nível de instrução em média, as mulheres enfrentam obstáculos ao ingressar em áreas como ciências exatas e de produção [IBGE 2021]. A predominância masculina nessas áreas indica que, no Brasil, ocorre o mesmo que no restante do mundo, resultando no surgimento de diferenças entre ocupações vistas como femininas e masculinas [Nascimento et al. 2023]. Na América Latina e Caribe, e.g., enquanto as mulheres representam cerca de 70% dos estudantes em educação, saúde e bem-estar, a proporção cai para apenas 32% em matemática e estatística [Bello and Estébanez 2022, p. 16-17].

Para [Macedo et al. 2018], a carência de suporte durante a escola, para a escolha de uma carreira em exatas, influencia negativamente na opção das mulheres para estas áreas. Em [Menezes and Santos 2021], os autores apontam que além dos fatores como a intimidação das meninas, a falta de incentivo da família, a percepção de não habilidades para a área, há ainda o fator falta de afinidade com a Matemática, que influencia fortemente a baixa presença de mulheres nos cursos de computação. Adicionalmente, em [Holanda et al. 2022] e [Noguera et al. 2020], os autores concluíram que no contexto do Exame Nacional do Ensino Médio (ENEM), apesar do desempenho dos homens ser superior ao das mulheres nas provas de exatas, a diferença não é tão acentuada.

Diante desse cenário, exposto na literatura, surge o questionamento, a saber, se houvesse um suporte social robusto impulsionando as mulheres nas disciplinas de STEM, a presença feminina nessas áreas seria mais significativa?

Visando contribuir para esclarecer a indagação posta, este estudo analisa dados do SISU e do ENEM para investigar se, em um contexto de apoio à participação feminina em STEM, as mulheres demonstram habilidades compatíveis para essa área, conforme os critérios dos processos seletivos. Para isso, analisa-se a população de mulheres no SISU para determinar o percentual que poderia se classificar em cursos de STEM se tivessem optado por estes. A abordagem envolve comparar as notas das mulheres que escolheram cursos fora de STEM no SISU com as notas dos últimos ingressantes em cursos de STEM no mesmo local. Também examina-se o desempenho por gênero no ENEM, mostrando que, quando as características socioeconômicas são semelhantes, o desempenho em Matemática de homens e mulheres tende a se igualar, sugerindo que as mulheres têm capacidade para ingressar em áreas de estudo STEM.

Este artigo está estruturado da seguinte maneira. Na Seção 2 são apresentados os trabalhos relacionados ao presente estudo. Na Seção 3, por sua vez, detalha-se a metodologia utilizada para a realização desta pesquisa, e, na Seção 4, são apresentados e analisados os resultados desta pesquisa, seguido de considerações finais acerca do trabalho realizado.

## 2. Trabalhos Relacionados

Estudos recentes abordam fatores sociais e educacionais que afetam a participação das mulheres, além de analisarem iniciativas para promover a equidade de gênero, destacando abordagens específicas a seguir.

Em [Noguera et al. 2020], os autores buscaram entender quais fatores influenciam o desempenho das mulheres no ENEM. Utilizando os dados de 2013 a 2017, disponíveis na base de dados abertos do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), este estudo compararou o desempenho das mulheres e dos homens para verificar se existe disparidade entre estes. As conclusões mostram que os homens apresentaram, de forma discreta, um melhor desempenho com relação as mulheres nas áreas de Matemática e Ciências das Natureza. Já na área de Linguagens e Códigos ambos tiveram resultados equivalentes.

Holanda et al. (2022) apresentaram uma análise sobre o desempenho em Matemática nas provas do ENEM, por gênero [Holanda et al. 2022]. Para a realização desta análise, esta pesquisa utilizou dados dos anos de 2010 a 2019, disponíveis na base de dados abertos do INEP. Como resultado geral, este estudo observou que, independentemente do período, o número de mulheres presentes na prova era maior que o de homens. No entanto, os homens obtiveram, mesmo que discretamente, notas superiores às mulheres em todo o período analisado. Como conclusão, esta pesquisa sugere a importância da investigação do quanto o desempenho das meninas em Matemática pode influenciá-las nas escolhas de cursos nas áreas de Computação.

Em [Gallindo et al. 2021], utilizou-se os dados da Relação Anual de Informações Sociais (RAIS) de 2015 a 2019, do Censo Escolar de 2020 e do Censo de Educação Superior de 2019 para analisar a questão de gênero no mercado da Tecnologia da Informação e Comunicação (TIC). Nele os autores analisaram que pesquisadores em início de carreira em STEM tinham maior propensão a serem mulheres e se a participação feminina em cursos de graduação na área de STEM estava aumentando e se havia maior participação feminina em profissões relacionadas à Tecnologia da Informação (TI), concluindo que entre os anos de 2015 a 2019 a presença feminina nas áreas de pesquisa em STEM diminuiu e em 2019 menos de 15% das matrículas na área de informática e TIC eram de mulheres, e uma baixa participação feminina em profissões ligadas à TI.

## 3. Metodologia

A metodologia deste trabalho foi elaborada baseando-se na seguinte pergunta, a saber, as mulheres possuem desempenho suficiente no ENEM para obterem vagas em cursos de graduação na área de STEM ofertados pelo SISU? Neste sentido, utilizando-se dados de uma edição específica do ENEM e do SISU, esta pesquisa busca comprovar as hipóteses enumeradas a seguir:

Hipótese 1: mulheres que foram aprovadas em cursos não-STEM, seriam aprovadas em cursos STEM, se pleiteassem essas vagas.

Hipótese 2: mulheres e homens com características socioeconômicas similares têm desempenho semelhantes na prova de matemática do ENEM.

Para comprovar essas hipóteses, foram usadas as opções de curso escolhidas pelas mulheres no SISU e o questionário socioeconômico do ENEM preenchido no momento da inscrição. Além disso, o estudo considerou a nota de Matemática do ENEM como referência, uma vez que a literatura aponta a falta de afinidade com essa disciplina como um fator influenciador para as mulheres não ingressarem em áreas de STEM [Menezes and Santos 2021].

### 3.1. Compreensão e domínio do estudo

Nesta fase, uma análise inicial do tema foi feita para definir o escopo do trabalho, com foco em entender a baixa participação de mulheres na área de STEM no Ensino Superior brasileiro. Em seguida, elaborou-se uma proposta que poderia ser confirmada usando dados governamentais, realizando investigações sobre a natureza desses dados. Posteriormente, foi feita uma análise dos dados do ENEM e do SISU para identificar e validar hipóteses que ajudassem a responder à pergunta inicial desta pesquisa.

### 3.2. Obtenção dos dados

Nesta etapa, o foco foi obter os dados necessários e definir o escopo temporal. Além dos dados públicos do ENEM e do SISU, também foi necessário obter dados do sistema e- MEC, Cadastro Nacional de Cursos e Instituições de Educação Superior e a Classificação Internacional Normalizada da Educação Adaptada para Cursos de Graduação e Sequenciais (CINE). Quanto a temporalidade, os dados utilizados foram do ENEM 2021 e da chamada regular do SISU 2022.1, os mais recentes disponíveis. O ENEM 2021 tinha 3.389.832 registros e o SISU 2022.1 tinha 1.054.474 registros. Considerando as duas opções de escolha do candidato no momento de sua inscrição no SISU, foram 2.041.627 registros.

### 3.3. Seleção das perguntas do questionário socioeconômico

Nesta etapa, foram selecionados as perguntas do questionário socioeconômico do ENEM relevantes para este estudo. As perguntas serão listadas a seguir:

- Q001: Até que série seu pai, ou o homem responsável por você, estudou?

- Q002: Até que série sua mãe, ou a mulher responsável por você, estudou?

- Q003: A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).

- Q004: A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).

- Q006: Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)

As respostas às perguntas acima foram utilizadas na definição de perfis que permitissem a comparação entre o desempenho de homens e mulheres, usando como base o desempenho obtido no ENEM. As perguntas deste questionário que são relacionadas a profissão do pais (Q003 e Q004), por abrangerem diversos tipos de profissões, assim

> 2Sistema de fluxo de trabalho e gerenciamento de informações relativas aos processos de regulação, avaliação e supervisão da educação superior no Sistema Federal de Educação

como no questionário socieconômico e estes grupos foram separados em 6, sendo os grupos de 1 a 5 contendo as profissões, e o grupo denominado como “Não sei” para aqueles que desconhecem as profissões dos pais.

### 3.4. Preparação dos dados

Nesta etapa, foi feita a preparação dos dados, para que fossem corrigidas imprecisões, como dados faltantes e valores discrepantes. Para esta pesquisa foram utilizadas as bases de dados pública do SISU, do ENEM e a CINE Brasil para cada curso participante do SISU, visto que na base de dados do SISU, não continha informações sobre as áreas dos cursos de graduação.

Para esta pesquisa utilizar os dados dos cursos escolhidos pelos participantes no SISU, desempenho e respostas ao questionário socioeconômico do ENEM, e a classificação CINE Brasil, foi preciso integrar as três bases de dados em uma única. Então, inicialmente uniu-se as bases de dados do ENEM e do SISU, criando uma chave composta com sexo, notas nas 5 áreas do ENEM e faixa etária. A faixa etária foi calculada a partir da data de nascimento em relação ao ano do ENEM na base do SISU. Após essa junção, 4.794 inscrições foram removidas devido ao campo “Nu Inscricao” estar nulo. Para distinguir os cursos de STEM, foi feita uma segunda junção entre o SISU e o sistema E-MEC usando o atributo “código do curso”. A Figura 1 mostra a combinação das tabelas do SISU 2022.1, ENEM 2021 e E-MEC 2023.

Figura 1. Junç ão das tabelas.

Após a junção, foram agrupados os cursos que faziam ou não parte das áreas de STEM, sendo utilizado o nível hierárquico mais alto da classificação CINE Brasil. As áreas classificadas como “STEM” foram “Ciências Naturais, Matemática e Estatística”, “Computação e Tecnologias da Informação e Comunicação” e “Engenharia, Produção e Construção”, tendo sido as demais classificadas como “não-STEM”.

Para análise de dados neste estudo, selecionou-se uma amostra mais homogênea em termos de faixa etária e perfil. Para isso, aplicaram-se dois filtros na base de dados do ENEM. excluíu-se os treineiros (estudantes que fazem o exame antes do último ano do ensino médio para se familiarizarem com a prova) e focamos na faixa etária de 15 a 18 anos para incluir apenas estudantes em seu ciclo regular de estudos.

Ao fim desta etapa, para a Hipótese 1, analisaram-se 80.936 inscrições de mulheres aprovadas em cursos não-STEM no SISU 2022.1, considerando suas escolhas de primeira e segunda opção. Por outro lado, para a Hipótese 2, após filtrar não-treineiros

e a faixa etária de 15 a 18 anos, analisaram-se 1.164.778 inscrições no ENEM 2021 de ambos os sexos.

Ao final dessa fase, este estudo consolidou os dados resultando em:

- 80.936 inscrições no SISU 2022.1, focando exclusivamente na população feminina aprovada em cursos não-STEM e considerando suas opções tanto na primeira quanto na segunda escolha. Este foi o universo de dados utilizados para avaliar a Hipótese 1 deste estudo; e

- 1.164.778 inscrições do ENEM 2021, após a exclusão de treineiros e restrição dos inscritos da faixa etária de 15 a 18 anos. Este foi o conjunto de dados usado como base para a análise da Hipótese 2.

### 3.5. Análise dos dados

Nesta etapa, esta pesquisa realizou análises exploratórias e criou painéis de visualização na ferramenta de Business Intelligence Tableau. Esta etapa foi importante para a exploração dos dados de forma aprofundada e responder à pergunta central do estudo. Essas análises exploratórias possibilitaram uma avaliação detalhada das variáveis, destacando disparidades e correlações relevantes.

## 4. Resultados e Discussões

Nesta seção, discute-se os resultados das hipóteses formuladas, utilizando dados do SISU, ENEM e e-MEC.

Para análise da Hipótese 1, foram considerados dois cenários. O primeiro, analisou as mulheres que atingiram a nota mínima na prova de Matemática para ingressar em cursos das áreas de STEM. O segundo investigou quantas mulheres obtiveram nota, em Matemática, equivalentes ou superiores à média em cursos dessas áreas. Para a análise da Hipótese 2, comparou-se o desempenho no ENEM de homens e mulheres com características socioeconômicas similares. Um dos resultados principais mostra a disparidade de gênero nas aprovações em cursos de STEM no SISU 2022.1, destacando a importância de pesquisas que abordem essa questão.

Tabela 1. Aprovados em STEM no SISU 2022.1 por gênero.

|Gênero|Aprovados em STEM|Aprovados em STEM(%)|
|---|---|---|
|Masculino|38.473|62%|
|Feminino|23.662|38%|

Como pode ser observado na Tabela 1, Dos 62.135 aprovados em cursos STEM, 62% são homens, evidenciando a baixa representação feminina nessa área. Isso levanta a questão do desempenho das mulheres no ENEM, a saber, será que as mulheres não obtêm notas suficientes para ingressar nesses cursos? Para responder a essa pergunta, este estudo iniciou uma análise do desempenho destas para verificar sua qualificação para cursos STEM.

### 4.1. Análise de desempenho feminino em Matemática das aprovadas em cursos não-STEM

Neste cenário, esta pesquisa analisou se mulheres aprovadas em cursos não-STEM em um município teriam sido aprovadas em cursos STEM no mesmo município onde foram aprovadas inicialmente, utilizando como critério de comparação a nota de Matemática do último candidato aprovado em STEM naquele município como referência. Em resumo, compararam-se as notas de Matemática das mulheres aprovadas em não-STEM para determinar quais teriam sido aprovadas em cursos STEM no SISU 2022.1.

A Tabela 2 a seguir resume os resultados obtidos para esta análise, apresentando a distribuição de 80.936 mulheres aprovadas em cursos não-STEM, considerando as duas opções de escolha de curso disponíveis no SISU.

Tabela 2. Aprovadas para cursos STEM no SISU 2022.1, usando nota mínima.

||Seriam|Não seriam|Não há curso de|
|---|---|---|---|
||aprovadas|aprovadas|STEM no município|
|Inscritas|64.832|5.541|10.563|
|Inscritas(%)|80,1|6,9|13,0|

Das mulheres analisadas nesse grupo, 64.832 (80,10%) atenderiam à nota mínima em Matemática 5.541 (6,85%) não alcançariam a pontuação mínima e as outras 10.563 (13,05%) não poderiam ingressar, uma vez que o município onde foram aprovadas não oferece cursos relacionados à STEM. Isso evidencia que uma parcela significativa de candidatas demonstra potencial em Matemática para ingressar em cursos de STEM. Adicionalmente, observou-se que um número relevante de mulheres não teria a oportunidade de ingressar em cursos de STEM mesmo se desejasse, devido à ausência de tais cursos no município de aprovação inicial.

Uma segunda análise foi conduzida para explorar a possibilidade de acesso de mulheres a cursos STEM no SISU, considerando um cenário hipotético em que as aprovadas em cursos não-STEM optassem por cursos STEM. A análise usou a média das notas de Matemática de todos os candidatos aprovados em cada curso e município, e os resultados estão apresentados na Tabela 3.

Tabela 3. Aprovadas para cursos STEM no SISU 2022.1, usando nota média.

||Seriam|Não seriam|Não há curso de|
|---|---|---|---|
||aprovadas|aprovadas|STEM no município|
|Inscritas|22.274|48.099|10.563|
|Inscritas(%)|27,5|59,5|13,0|

Conforme a Tabela 3, das 80.936 mulheres aprovadas em cursos STEM nas duas opções de escolha de cursos disponíveis no SISU, 22.274 (27,52%) alcançaram ou superaram a pontuação média em Matemática, enquanto 48.099 (59,43%) não seriam aprovadas por estarem abaixo da média. Devido à inexistência de cursos em STEM no município onde foram aprovadas, não foi possível ter um resultado para 10.563 (13,05%).

A análise das inscrições no ENEM 2021, excluindo os treineiros e focando na faixa etária de 15 a 18 anos, mostra que as notas médias de Matemática foram 523,59 para

mulheres e 565,22 para homens. Embora a diferença absoluta entre as notas beneficie os homens, é importante ressaltar que, em termos percentuais, essa disparidade foi inferior a 8%, indo ao encontro das conclusões de [Holanda et al. 2022] e [Noguera et al. 2020].

### 4.2. Análise de desempenho por gênero e escolaridade dos pais

Neste cenário, foram analisados os desempenhos em Matemática de 585.071 participantes do ENEM 2021, com faixa etária de até 18 anos, cujos pais possuíam a mesma escolaridade, divididos por gênero para comparação.

Ao usar a média em Matemática em vez do número de participantes. A Figura 2 mostra que os homens apresentam um melhor desempenho em comparação com as mulheres em todos os níveis de escolaridade dos pais. A maior diferença ocorre quando os pais têm ensino médio completo, com mulheres pontuando 519,99 e homens 555,45, uma diferença de 35,46 pontos. Em contraste, o grupo com menor diferença é o de pais sem ensino fundamental completo, com mulheres pontuando 475,55 e homens 506,87, uma diferença de 31,32 pontos. Isso evidencia um desempenho inferior das mulheres em Matemática, independentemente da escolaridade dos pais.

Figura 2. Desempenho dos participantes com faixa etária 18 anos do ENEM 2021 na prova de Matemática por gênero e escolaridade dos pais.

Na Figura 2 observa-se também que o desempenho dos participantes melhora com o aumento do nível de escolaridade dos pais, especialmente para aqueles cujos pais têm ensino superior completo. Nesse grupo, as mulheres apresentaram a maior média, atingindo 610,11 pontos. O gráfico também sugere que o aumento nas notas conforme a escolaridade dos pais é semelhante entre os gêneros.

### 4.3. Análise de desempenho por gênero e profissão dos pais

A Figura 3 apresenta o desempenho em Matemática dos participantes desta análise. Assim como no item anterior, os homens tiveram um melhor desempenho, com destaque para os participantes que desconheciam a profissão dos pais, onde apresentaram uma maior diferença entre as notas. Nesse grupo, as mulheres tiveram uma média de 483,94 pontos e os homens de 525,16, resultando em uma diferença de 41,22 pontos. Por outro lado, no grupo cujos pais exercem profissões do grupo 1, as mulheres tiveram uma média de 472,84 e os homens de 497,69, resultando em uma diferença de 24,85 pontos. Pode-se observar que o desempenho dos participantes diminuiu entre o grupo que desconhece a profissão dos pais e o que possui pais que exercem profissões do grupo 1. Além disso, a partir do grupo 1, o desempenho aumenta, indicando que quanto maior o nível de escolaridade exigido pela profissão dos pais, melhor o desempenho dos participantes. No mais,

Figura 3. Desempenho dos participantes com faixa etária 18 anos do ENEM 2021 na prova de Matemática, por gênero e profissão dos pais.

as mulheres tiveram a maior média no grupo onde os pais têm profissões pertencentes ao grupo 5. Por fim, é possível notar que tanto a diminuição quanto aumento das médias ocorreram de forma semelhante entre os gêneros.

### 4.4. Análise de desempenho por gênero e renda mensal per capita

A Figura 4 apresenta o desempenho na prova de Matemática dos participantes desta população analisada. Nesta foi observado que os homens superam as mulheres em todas as faixas de renda analisadas no desempenho da prova de Matemática, com destaque para o grupo de renda entre 1 e 3 salários mínimos, onde mulheres obtêm média de 514,36 pontos e homens, 547,85, uma diferença de 33,49 pontos. Já na faixa de renda de até um salário mínimo, mulheres têm média de 478,48 e homens, alcançando uma média de 504,58, apresentando uma diferença de 26,09 pontos.

Evidencia-se que a renda mensal per capita influencia no desempenho dos participantes, pois o grupo que apresenta melhor desempenho possui uma faixa de renda que varia de 12 a 20 salários mínimos, em que as mulheres apresentam melhor desempenho com relação as outras faixas de renda. Além disso, o gráfico mostra que o que o aumento das médias ocorre de maneira parecida nos gêneros feminino e masculino.

Figura 4. Desempenho dos participantes com faixa etária 18 anos do ENEM 2021 na prova de Matemática, por gênero e renda mensal per capita.

### 4.5. Análise de desempenho por gênero e tipo de escola em que concluiu o ensino médio

A Figura 5 mostra o desempenho em Matemática dos participantes analisados. Os homens superaram as mulheres em todas as categorias de escola. No grupo sem especificação do tipo de escola, a diferença média foi mais significativa, com as mulheres obtendo em média 545,49 pontos e os homens 586,78 pontos, uma diferença de 41,29 pontos. Já no grupo de escolas privadas, a menor diferença foi observada, com as mulheres atingindo uma média 594,24 pontos e os homens 630,72 pontos, uma diferença de 36,48 pontos.

Com relação ao desempenho feminino, podemos destacar o grupo com as participantes que frequentaram o Ensino Médio em escolas privadas, em que obtiveram a maior média, sendo 594,24 pontos. Em contraste, as mulheres que frequentaram o Ensino Médio em escolas públicas, obtiveram a menor pontuação média, alcançando 498,59 pontos.

Figura 5. Desempenho dos participantes com faixa etária 18 anos do ENEM 2021 na prova de Matemática, por gênero e tipo de escola em que concluiu o ensino médio.

## 5. Conclusões e Trabalhos Futuros

Este trabalho analisou a performance das mulheres aprovadas em cursos não STEM do SISU 2022.1, buscando evidenciar sua capacidade de ingressar em áreas STEM. Além disso, foi realizada uma comparação dos participantes do ENEM 2021 por gênero em cenários distintos. Os resultados destacam uma disparidade na distribuição de aprovações em cursos STEM, com maior predominância de homens, acentuando a desigualdade de gênero nessas áreas. No contexto de desempenho dos participantes no ENEM 2021 podese concluir que, a diferença de pontuação na média geral na prova de Matemática dos participantes não treineiros, separados por gênero, não ultrapassa 45 pontos.

Além disso, também ficou evidenciado que o nível de escolaridade dos pais, a profissão deles, a renda mensal per capita e o tipo de escola frequentada pelo participante durante o Ensino Médio influenciam significativamente seu desempenho, independentemente do gênero. Pois os grupos com pais com Ensino Superior completo, profissões de alto nível educacional (grupo 5), educação em escolas privadas no Ensino Médio e renda mensal per capita entre 6 e 20 salários mínimos mostraram um melhor desempenho nas provas do ENEM 2021.

Portanto, um suporte social robusto, que poderia incluir medidas para equilibrar essas desigualdades, provavelmente teria um impacto positivo significativo na presença feminina em áreas STEM.

Como trabalhos futuros, pretende-se aplicar este estudo para as bases de dados mais recentes do ENEM e do SISU, para poder comparar os resultados com o passar dos anos. Outra sugestão seria considerar outras disciplinas das áreas de exatas, pois elas também afetam o interesse das mulheres por áreas de STEM.
