# Mulheres na Pós-graduação nas Areas de Exatas: Um Estudo de Caso na Universidade de Brasília

Thayanna Klysnney Moreira Nunes, Aleteia Araujo, Maristela Holanda

1Departamento de Ciência da Computação, Universidade de Brasília

thayannaklysnney@gmail.com, aleteia@unb.br, mholanda@unb.br

Resumo. As áreas relacionadas às Ciências Exatas têm uma baixa representatividade de mulheres. No nível de mestrado e doutorado, a literatura apresenta que existe uma lacuna de diversidade de gênero. Esta é a realidade da área da Computação, que integra a grande área das Ciências Exatas. Desta forma, este artigo aborda a questão de pesquisa: Como está a representatividade feminina nas áreas de Ciências Exatas e da Terra na Universidade de Brasília (UnB)? Para responder esta pergunta foram utilizados os dados abertos e a definição de área Ciências Extasa e da Terra (CET) da CAPES. Como resultado foi possível constatar que Computação é a área das CET com o menor número de mulheres proporcionalmente nos cursos de mestrado e doutorado da UnB.

Abstract. In the Exact Science areas, women are a group with little representation in universities. This problem occurs at both masters and doctoral levels. A lack of gender diversity is reported in the Exact Science areas in general, and in particular in Computing. Thus, this paper has the research question: How is gender diversity in the Exact Science areas at the University of Brasília (UnB)?; We used CAPES open data and its definition of Exact and Earth Sciences (CET) to answer this question. As a result, it was possible to verify that Computing is the area of CET with the lowest number of women proportionally in the masters and doctoral levels at the UnB.

## 1. Introdução

De acordo com a Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES), em 2020, as mulheres representam 53% dos bolsistas de mestrado e doutorado no Brasil. As mulheres também ocupam 53% das matrículas (195 mil das 364) em cursos de pós-graduação autorizados pela CAPES [Gov.br 2020]. Em [Monard and Monteiro 2015] tem-se que as mulheres no mestrado se tornaram maioria em 1998 e no doutorado em 2007. A predominância feminina, no entanto, não é vista em todas as áreas do conhecimento, pois elas se destacam nas áreas de Ciências da Saúde e na Linguística, Letras e Artes. Na grande área de Ciências Exatas e da Terra (CET), foco deste artigo, as mulheres têm menor representatividade. A grande área CET na CAPES é composta pelas seguintes áreas do conhecimento [CAPES 2020b]: Astronomia/Física, Ciência da Computação, Geociências, Matemática/Probabilidade e Estatística e Química.

Na Universidade de Brasília (UnB), em 2019, o número de alunas nos programas de pós-graduação stricto sensu, de mestrado e doutorado acadêmicos, era maior do que o número de alunos. Porém, quando se analisa apenas os programas de pósgraduação do Departamento de Ciência da Computação desta universidade, a porcentagem de alunas nos níveis de mestrado e doutorado é menos de 20% no mesmo ano

[Holanda and de Araújo 2019]. Neste contexto, este artigo busca responder a questão de pesquisa: Como está a diversidade de gênero nas áreas de Ciências Exatas na UnB? Para responder esta questão de pesquisa foi utilizada a metodologia baseada em análise de dados a partir dos dados abertos da CAPES, e a visualização dos dados foi implementada com a linguagem R.

Este artigo está estruturado com as seguintes seções: Seção 2 na qual os trabalhos relacionados são apresentados; Seção 3 descreve as etapas para o desenvolvimento do artigo; Seção 4 apresenta e analisa os resultados; Seção 5 discute as questões de pesquisa deste artigo; e por fim, a Seção 6 expõe as conclusões e os trabalhos futuros.

## 2. Trabalhos Relacionados

Nos últimos anos o tema pós-graduação e diversidade de gênero no Brasil tem sido discutido na literatura. Em [Moreira and Velho 2010] analisa-se a inserção das mulheres nos cursos de pós-graduação stricto sensu desenvolvidos pelo Instituto Nacional de Pesquisas Espaciais (INPE). Em [Monard and Monteiro 2015] é apresentado um panaroma geral da representatividade feminina em pesquisa na plataforma Lattes. Em [Holanda and de Araújo 2019] é feito um estudo de gênero na pós-graduação no Departamento de Ciência da Computação da UnB. Em [Carvalho et al. 2020] o objetivo foi esclarecer a situação quantitativa das mulheres no Programa de Pós-graduação em Informática (PPGI) na UFRJ.

Assim, diferentemente dos artigos apresentados anteriormente, este artigo apresenta uma análise da grande área de Ciências Exatas e da Terra da CAPES em relação à questão de diversidade de gênero na pós-graduação na UnB.

## 3. Metodologia

Esta pesquisa foi desenvolvida em cinco etapas: Coleta dos Dados, Seleção dos Dados, Limpeza dos Dados, Visualização dos Dados e Análise dos Dados. A primeira etapa, Coleta de Dados, foi realizada a partir de download dos arquivos no formato CSV ( Comma-Separated Values ) da plataforma de dados abertos da CAPES [CAPES 2020a]. Os arquivos coletados foram da área de CET, de 2007 a 2017, da UnB. Assim sendo, foram extraídos dez arquivos, um para cada ano. O intervalo de dez anos foi escolhido para fazer uma análise com no minímo dois ciclos de formação de discentes, já que o doutorado tem uma duração, aproximadamente, de quatro anos. A segunda etapa foi a Seleção dos Dados, os quais foram: sexo do discente (tp ~~s~~ exo ~~d~~ iscente); grau acadêmico, mestrado ou doutorado (ds ~~g~~ rau ~~a~~ cademico ~~d~~ iscente); situação discente (nm ~~s~~ ituacao ~~d~~ iscente); entidade de ensino, sigla da instituição de ensino (sg ~~e~~ ntidade ~~e~~ nsino); área de conhecimento (nm ~~g~~ rande ~~a~~ rea ~~c~~ onhecimento); ano de referência da coleta (ano ~~b~~ ase). Para a terceira etapa, Limpeza dos Dados, foram verificados problemas com dados acentuados e valores inválidos, por meio de um programa em Python. Na fase de Visualização dos Dados foi implementado um programa na Linguagem R para geração dos gráficos, a biblioteca ggplot() com a propriedade facet. Dentre os gráficos analisados, este apresentou o melhor resultado em termos de visualização das informações pesquisadas neste artigo. Por fim, foi realizada a fase de Análise de Dados que é apresentada em detalhes nas seções seguintes.

## 4. Resultados

A Figura 1 apresenta os dados de todas as áreas de CET do mestrado dividida por sexo e área de conhecimento. Na Astronomia e Física (AstrFis) o ano com menor número de mulheres foi o de 2009 (16%) com quatro discentes do sexo feminino e 21 do sexo masculino, e o ano com o maior número de mulheres foi em 2012 com 16 (30,18%) discentes. Na Ciência da Computação (CiencComp), os anos com a menor representação feminina foi 2009 que teve apenas uma (3,84%) discente, e o ano com a maior representatividade feminina foi o de 2011 com nove (16,98%) discentes. Na Geociência o ano com o menor número de mulheres foi o de 2007 com 20 (50%) discentes, neste ano também tiveram 20 homens, e o ano com o maior número de mulheres foi 2017 com 48 (40%) discentes. Na Matemática e Probabilidade e Estatística (MatProbEst) o ano com o menor número de mulheres foi 2009 com 9 (20%) discentes. Já em 2014 foi o ano que teve o maior número de mulheres, no total eram 25 (50%) discentes. Na Química o ano com o menor número de mulheres foi 2009, com oito (27,58% ) discentes do sexo feminino, e o ano com o maior número de mulheres foi em 2012 com 42 (44,68%) mulheres.

Fig. 1. Discentes de Mestrado em CET por Ano na UnB.

No geral, no mestrado acadêmico, o ano de 2012 foi o ano com o maior número de mulheres, somando 113 discentes. Destas 113 discentes, somente seis eram da Ciência da Computação, 5,3% das discentes. O ano de 2009 é o ano com o menor número de mulheres, pois neste ano houve 62 discentes. Destas discentes somente uma (1,61%) era da Ciência da Computação. Não existe um padrão de crescimento entre os anos na representatividade feminina nas áreas de CET. Já os discentes do sexo masculino desde 2014 ocorre um crescimento no número, foram de 168 discentes para 221, um aumento de aproximadamente 31,5%, aumentando gradativamente a cada ano.

A Figura 2 apresenta os dados de todas as áreas de CET do doutorado. Na Astronomia e Física (AstrFis) os anos com o menor número de mulheres foram 2008 (9,09%) e 2009 (11,11%). O ano com mais mulheres foi 2016 com 26 (33,76%) discentes. Na Ciência da Computação (CiencComp) os anos com menor representatividade foram 2010 (28,57%), 2011 (15,38%) e 2016 (5%) e o ano com a maior representatividade femi-

Fig. 2. Discentes de Doutorado em CET por Ano na UnB.

nina foi 2017 com cinco (11,37%) discentes. Na Geociência o ano com o menor número de mulheres foi de 2007 com 11 (31,43%) discentes, e o ano com o maior número de mulheres foi o de 2017 com 42 (37,5%) discentes. Na Matemática e Probabilidade e Estatística (MatProbEst) o ano com o menor número de mulheres foi de 2007 com 10 (29,42%) discentes, e o ano com maior número de mulheres foi 2010 com 18 (43,90%) discentes. Na Química os anos com o menor número de mulheres foram 2007 (46,42%) e 2008 (39,39%) e o ano com maior número de mulheres foi 2016 com 38 (50,66%) mulheres.

No doutorado, o ano com mais mulheres (2017) teve 120 discentes, dessas apenas cinco eram de Ciência da Computação. O ano com o menor número de mulheres foi de 2007, porém, nem todas as áreas do CET tinham doutorado nesta universidade, por exemplo, o doutorado da Ciência da Computação só iniciou em 2010. A partir de 2010, o ano com o menor número de mulheres foi o de 2012. Neste ano haviam 64 discentes mulheres, destas discentes somente três eram de Ciência da Computação. Contudo, no doutorado é possível notar uma crescente de alunas desde 2012. Em 2012 eram 64 discentes e em 2017, 120 discentes, um aumento de mais de 100%. Já os alunos do sexo masculino o ano com mais alunos foi 2017 e estão crescendo desde 2015.

## 5. Discussões

De maneira geral, a mulher tem uma menor representatividade em todas as áreas da CET quando somados os discentes de pós-graduação dos níveis de mestrado e doutorado acadêmicos. Porém, a diversidade de gênero nas áreas da CET tem grandes variações. A área de Química, no nível de doutorado, em 2016 teve mais mulheres do que homens. As áreas de Computação e, Astronomia e Física tiveram a menor representatividade feminina. A área da Matemática e Probabilidade e Estatística chegou a ter aproximadamente 42,56% de discentes do sexo feminino no nível do mestrado. A Geociência também tem menos mulheres do que homens em programas de pós-graduação, porém, no doutorado, é possível observar que tem uma tendência de crescimento do número

de mulheres a partir de 2015. Por fim, no mestrado, o maior número de mulheres está concentrado nas áreas de Geociência e Química, e o menor número está nas áreas de Astronomia e Física, e Ciência da Computação. No Doutorado não é diferente, ou seja, a maior representatividade feminina é nas áreas de Geociência e Química, e a menor nas áreas de Ciência da Computação, e Astronomia e Física.

## 6. Conclusões

Este trabalho apresentou uma análise dos dados da pós-graduação em CET da UnB. Na grande área do conhecimento de Ciência Exatas e da Terra na CAPES, há uma baixa representatividade feminina. O programa de Química teve a menor diferença entre o número de discentes do sexo feminino e masculino, mesmo assim, em todos os anos teve mais homens na pós-graduação em Química do que mulheres. A área de Computação a- presentou o menor número de mulheres em relação às outras áreas da CET. Os programas da pós-graduação, mestrado e doutorado acadêmicos, de Computação aumentaram bastante o número de vagas, porém o número de mulheres ficou basicamente estável, menos de 10 alunas por ano.

Para trabalhos futuros pretende-se estender este estudo para todas as universidades do Brasil utilizando os dados públicos abertos da CAPES, analisar o corpo docente do programas, e fazer predições da representatividade feminina, tanto no mestrado, quanto no doutorado.

## 7. Agradecimentos

Ao Conselho Nacional de Desenvolvimento Científico e Tecnólogico (CNPq): Processo 442789/2018-1 Edital Chamada CNPq-MCTIC No 31/2018 - Meninas nas Ciências Exatas, Engenharias e Computação, e Processo 440806/2019-4, Edital 05/2019, Linha 2 Ações de intervenção em escolas básicas com foco em ciência. Agradecemos também a Fundação de Apoio a Pesquisa do Distrito Federal (FAP-DF) no Edital DPG/UnB 05/2018 Programa de Bolsa de Pós-doutorado no Exterior FAP/DF.
