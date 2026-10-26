# Mulheres na Ciência: Um Panorama das Publicações no WIT

Gabriela Souza Maximino, Isadora Mendes dos Santos, Marcelle Pereira Mota

1Faculdade de Computação (FACOMP) Instituto de Ciências Exatas e Naturais (ICEN) Universidade Federal do Pará (UFPA) Rua Augusto Corrêa, 01, Guamá – 66.075-110 – Belém – PA – Brasil

2Programa de Pós-Graduação em Ciência da Computação (PPGCC) Instituto de Ciências Exatas e Naturais (ICEN) Universidade Federal do Pará (UFPA) Rua Augusto Corrêa, 01, Guamá – 66.075-110 – Belém – PA – Brasil

gabriela.maximino@icen.ufpa.br, isadora.mendes@ufra.edu.br, mpmota@ufpa.br

Abstract. Women in Information Technology (WIT) is an event that aims to disseminate studies and projects that encourage female participation in computing. In this sense, this paper seeks to verify the current panorama of the event’s publications, identifying which are the most discussed topics and the regions that publish the most. The analysis of papers published in the last six years (20162021) of WIT was carried out. As a result, it is concluded that there is a predominance of specific topics and an inequality of contribution by regions and states, with the need to encourage thematic and regional diversities.

Resumo. O Women in Information Technology (WIT) é um evento que tem como objetivo disseminar estudos e projetos que incentivam a participação feminina na computação. Nesse sentido, este artigo busca verificar qual o panorama atual das publicações do evento, identificando quais são os temas mais abordados e as regiões que mais publicam pesquisas. Para isso, foi realizada a análise dos artigos publicados nos últimos seis anos (2016-2021) no WIT. Como resultados, conclui-se que há a predominância de certos temas, além de uma desigualdade de contribuição por parte de regiões e estados, havendo a necessidade do fomento às diversidades temática e regional.

## 1. Introdução

O Women in Information Technology (WIT) é uma iniciativa da Sociedade Brasileira de Computação criada em 2007 com o objetivo de discutir assuntos relacionados a questões de gênero e a Tecnologia da Informação no Brasil [CSBC 2021]. O evento reúne os principais estudos e projetos que visam incentivar a participação feminina na computação. Por ser um dos eventos base, ele ocorre anualmente no Congresso da Sociedade Brasileira de Computação (CSBC), que alterna os locais de realização em cada edição. Dessa forma, pessoas de diferentes estados têm a oportunidade de participar e contribuir com o evento.

Os tópicos de interesse para artigos do evento normalmente englobam projetos de extensão e pesquisa, análises de dados sobre mulheres e computação no mercado de trabalho ou nas escolas e faculdades, e ações educacionais de incentivo e apoio às meninas

na computação [CSBC 2021]. Assim, levanta-se o questionamento: “Qual o panorama das publicações feitas no WIT durante os últimos anos?”

Esse questionamento norteou o objetivo do presente trabalho de identificar os temas mais abordados e as regiões e estados que mais publicaram nos últimos seis anos de WIT (2016-2021), pois ao se obter um panorama geral das publicações do evento, fomenta-se o incentivo à maior diversidade de temas e regiões. Diante dos resultados, propõe-se a criação de uma ferramenta web interativa para a visualização dos dados, que, alimentada regularmente, refletirá os cenários com base em novas edições do evento.

Sendo assim, este trabalho é estruturado da seguinte forma: a Seção 2 discorre sobre os trabalhos relacionados; a Seção 3 apresenta a metodologia adotada; a Seção 4 discute os resultados e apresenta a ferramenta proposta; e a Seção 5 sintetiza o trabalho e apresenta as considerações finais.

## 2. Trabalhos Relacionados

Como base para o artigo, foram selecionados alguns trabalhos que realizaram a análise de publicações em eventos com o objetivo de responder a diferentes questões de pesquisa.

O trabalho de [Bordin et al. 2021] realizou a análise bibliométrica dos artigos publicados no WIT durante o período de 2016 a 2020. A análise resultou em dois principais indicadores bibliométricos: os de produtividade e de impacto, como os números de artigos por autor e o número de citações; e os de colaboração científica, como o grau médio de colaboração e os autores que mais colaboram. A partir desses indicadores, foi possível identificar quais foram os artigos mais citados, os autores que mais publicaram no evento, as universidades que possuem o maior número de autores, os autores com maior frequência de coautoria, entre outras informações.

A partir da análise dos trabalhos públicados na 10 edição do WIT, em 2016, [Cesario et al. 2017] fizeram o mapeamento dos projetos de incentivo à participação feminina na computação realizados no Brasil. Foram coletados dados acerca das instituições responsáveis, os estados de origem e as ações realizadas pelos projetos. Como resultados, tem-se a presença de projetos em 8 estados brasileiros, sendo a maioria no Rio Grande do Sul – onde ocorreu o evento em 2016. Além disso, a pesquisa verificou que todas as instituições responsáveis pelos projetos, com exceção de uma, são universidades públicas, e que as principais ações realizadas pelos projetos são oficinas e palestras. Contudo, vale ressaltar que os resultados desse trabalho se limitam à análise dessa única edição do WIT.

Com o objetivo de verificar a presença feminina nas produções científicas da área de ciência da computação, [Santana and Braga 2020] realizaram a análise cienciométrica das publicações do Congresso da Sociedade Brasileira de Computação dos anos de 2017 a 2019. Os resultados apontaram a predominância de autores do sexo masculino, com 69%, em relação a autoras, com 31%. Apesar disso, o estudo revela que mesmo em menor número as mulheres estão presentes como coautoras de 60% dos artigos do evento.

Conforme pode ser observado, os trabalhos de [Bordin et al. 2021] e [Cesario et al. 2017], assim como o presente artigo, realizam a análise das publicações do WIT. Contudo, os três trabalhos divergem quanto ao objetivo e às contribuições para a comunidade. [Bordin et al. 2021] realizaram a análise bibliométrica e descobriram, dentre outras informações, os autores mais produtivos, os autores com laços de colaboração

mais frequentes e as instituições de ensino que mais colaboraram durante os cinco anos analisados. [Cesario et al. 2017] analisaram os artigos de uma edição do WIT e identificaram quais foram os projetos de incentivo às mulheres na computação relatados no evento, os estados onde foram criados, as instituições responsáveis e as ações realizadas.

Enquanto isso, o presente artigo analisou as publicações dos últimos seis anos com o objetivo de identificar os temas mais abordados e as regiões e estados que mais publicaram no evento durante esse período. O trabalho de [Santana and Braga 2020], por sua vez, diverge dos mencionados por realizar uma análise cienciométrica no intuito de verificar a contribuição feminina em produções científicas e por expandir a análise para as publicações de todos os eventos do CSBC, ao invés de focar somente no WIT.

## 3. Metodologia

Para o desenvolvimento deste trabalho foram adotadas as seguintes etapas: (1) definição das questões de pesquisa; (2) coleta de materiais; (3) extração de dados; (4) classificação dos artigos; e (5) análise dos resultados.

A principal pergunta que motivou este trabalho foi “Qual o panorama das publicações feitas no WIT durante os últimos anos?”. Dela, foram derivadas duas questões de pesquisa: QP01: Quais são as regiões e os estados brasileiros que mais publicam no evento? e QP02: Quais os temas mais recorrentes? Para responder a essas questões, foram coletados artigos dos anais do WIT do período de 2016 a 2021. A coleta foi realizada manualmente na biblioteca digital da SBC, contemplando todos os artigos (completos e resumidos). Essa biblioteca foi escolhida como acervo para a pesquisa por centralizar todos os artigos em um único repositório e por esses estarem facilmente acessíveis. Contudo, a biblioteca reúne o conteúdo de apenas seis edições do evento, limitando o período de 2016 a 2021.

Em seguida, alguns dados foram extraídos dos artigos: (1) título; (2) ano de publicação; e (3) filiação dos autores. A partir da filiação, foram depreendidos os locais das publicações e as regiões. No caso de artigos com autores de regiões distintas, foi considerada a região e o local do primeiro autor. Todos esses dados foram armazenados manualmente em uma planilha do Excel.

No intuito de verificar quais são os assuntos mais recorrentes no evento, realizouse uma classificação dos artigos. A partir da leitura dos resumos e da checagem das palavras-chave, 14 temas foram propostos de forma arbitrária, porém de acordo com os tópicos de interesse propostos pelo comitê do evento. Os temas e as respectivas explicações do que cada um abrange são:

1. Acessibilidade: abordam propostas ou realização de atividades acessíveis;

2. Análise de Dados: abordam estudos realizados a partir da coleta e análise de diferentes tipos de dados no intuito de verificar as diferenças de gênero. Por exemplo, artigos que discutem o percentual de mulheres em cursos superiores de computação ou o desempenho de meninas no ENEM;

3. Atividades: os artigos com esse tema abordam projetos e atividades realizadas com meninas de qualquer escolaridade no intuito de atraí-las para a computação, utilizando as mais diversas ferramentas (e.g., oficinas, palestras e jogos); ações

1https://sol.sbc.org.br/index.php/wit/issue/archive

para apoiar a permanência de meninas nos cursos superiores de computação; e resultados e impactos das atividades realizadas;

4. Comunidades de Tecnologia: abordam a criação, a execução, os resultados ou os impactos das comunidades de tecnologia para as mulheres;

5. Diversidade sexual e de gênero: abordam questões relacionadas à população LGBTQIA+ na área da computação;

6. Fatores de Influência: discutem causas e fatores que influenciam ou são obstáculos para determinada ação. Por exemplo, os fatores que influenciam as meninas a escolherem carreiras de computação ou as causas da alta evasão feminina de cursos de computação;

7. Ferramentas: apresentam ferramentas construídas no intuito de auxiliar mulheres e conscientizar a população. Por exemplo, um aplicativo que serve como uma ferramenta de defesa a mais para mulheres e uma plataforma para visualização de dados sobre a violência contra a mulher no Brasil;

8. Gênero Feminino Negro: abordam questões ou estudos relacionados às mulheres negras. Por exemplo, a análise discursiva de duas mulheres negras atuantes do campo de computação;

9. Incentivo a professoras: discutem ações voltadas a docentes de modo a orientálas para incentivar a participação de alunas na computação;

10. Parentalidade: discutem aspectos relacionados a pais, mães e filhos;

11. Perfil de Estudantes, Egressos e Profissionais: discutem o perfil de estudantes, egressos e profissionais da área de computação;

12. Redes sociais: abordam a utilização das redes sociais como meio para propagar iniciativas voltadas ao incentivo de meninas na computação;

13. Representatividade Feminina: discutem a construção identitária das mulheres na computação e a representatividade feminina no meio; e

14. Violência: abordam aspectos relacionados à violência simbólica, em específico ao preconceito relacionado ao gênero na área de tecnologia.

Com base nos temas criados, os artigos foram classificados. Por fim, foram gerados gráficos a partir de contagens na planilha que serviram como base para os resultados.

## 4. Resultados e Discussão

Nos últimos seis anos de WIT, foram publicados 202 artigos. Na Figura 1, é possível visualizar a distribuição de artigos por região ao longo dos anos. Nota-se que o número de trabalhos aceitos no evento foi crescente a cada ano, sendo 25 artigos aceitos em 2016, 28 em 2017 e 2018, 31 em 2019, 42 em 2020 e, no último evento em 2021, 48 artigos. Tal evolução pode estar atribuída, para além da popularização do evento, ao início da admissão de um novo formato de artigo a partir da edição de 2019, que passou a considerar artigos maiores, chamados de completos, além dos curtos, que eram o padrão.

Em termos de contribuições regionais, é possível constatar a partir da Figura 1 uma considerável diversidade no local de origem dos trabalhos. As regiões Nordeste e Sul foram as que mais publicaram no evento, com 50 e 48 artigos, respectivamente. Em seguida, tem-se as regiões Sudeste, com 43, Centro-Oeste, com 37, e Norte, com 22. A região “Externa” na Figura refere-se a locais fora do país. Diante disso, nota-se a baixa contribuição da região Norte para o evento, que está distante 15 artigos da penúltima região que menos publica, o Centro-Oeste.

As contribuições regionais podem estar ligadas ao grau de desenvolvimento econômico de cada região. De acordo com [Melo et al. 2019], a distribuição de recursos voltados à pesquisa no Brasil está relacionada com a capacidade econômica das regiões. Dessa forma, as que mais recebem investimentos em bolsas e no fomento à pesquisa são o Sudeste, Sul, Nordeste, Centro-Oeste e Norte, respectivamente. Tal fato corrobora os dados apresentados anteriomente, uma vez que Nordeste, Sul e Sudeste foram as regiões que mais contribuíram com o WIT, enquanto Centro-Oeste e Norte apresentaram o menor número de publicações. Outro fator que também pode influenciar o grau de contribuição é a quantidade de projetos parceiros do Programa Meninas Digitais da SBC existentes na região. Mais uma vez, as regiões com maiores números de projetos são Sudeste, Nordeste e Sul, enquanto Centro-Oeste e Norte apresentam os menores números.

Analisando cada ano, tem-se que em 2016 a região Sul foi a que obteve mais artigos aceitos no evento. Tal situação pode estar ligada ao fato de que, nesse ano, o CSBC aconteceu em Porto Alegre, Rio Grande do Sul. Isso também ocorreu em 2018 com a região Nordeste: o evento foi sediado em Natal, Rio Grande do Norte, e a região obteve destaque no número de publicações. Por outro lado, em 2017 e 2019, o evento aconteceu em São Paulo e em Belém, respectivamente, e as regiões à que cada cidade pertence foram as que menos contribuíram nesses anos. Já em 2020 e 2021, o evento foi online, o que pode ter influenciado no aumento significativo do número de trabalhos para cada região comparado à edição de 2019, uma vez que questões envolvendo deslocamentos e custos foram mitigadas. Nesse contexto, a região que mais se destacou em termos de aumento do número de contribuições foi o Norte, cujos índices de desenvolvimento econômico e de apoio à pesquisa são os menores.

Figura 1. Número de artigos publicados por região de 2016 a 2021.

Além da análise em nível regional, é interessante verificar a contribuição de cada estado. Na Figura 2 (a), é possível observar o número de trabalhos publicados por estado em 2016. Nota-se que, dos 12 artigos da região Sul, metade foi proveniente de Santa Catarina. No caso do Centro-Oeste, dos 4 artigos, o Mato Grosso foi responsável por 3. Para as regiões Norte e Sudeste, apenas um estado contribuiu com os números. O Nordeste foi a única região em que os trabalhos foram melhores distribuídos entre os 4 estados que publicaram nesse ano.

(a) (b)

Figura 2. Número de Artigos publicados por estado em 2016 e 2017.

Na Figura 2 (b), tem-se a distribuição de artigos em 2017. Dessa vez, o Paraná elaborou 6 dos 9 artigos da região Sul, enquanto Santa Catarina não teve nenhuma participação. No Norte, o Amazonas foi responsável por 4 dos 5 artigos da região. Comparado ao ano anterior, o Nordeste perdeu 2 estados contribuintes, Rio Grande do Norte e Sergipe, e concentrou metade dos seus artigos na Paraíba. Nesse ano, as regiões CentroOeste e Sudeste distribuíram melhor os artigos entre os estados participantes.

Em 2018, a concentração de artigos em alguns estados foi significativa na região Nordeste, conforme ilustrado na Figura 3 (a). O Ceará e a Paraíba elaboraram, cada um, 4 trabalhos para o evento; totalizando 8 dos 11 advindos dessa região. Nas demais regiões, houve um equilíbrio da distribuição de artigos entre os estados que contribuíram. Já em 2019, a concentração ocorreu nas regiões Sul e Sudeste, de acordo com o que pode ser observado na Figura 3 (b). Nesse sentido, o Rio Grande do Sul foi responsável por 5 dos 7 artigos do Sul, enquanto Minas Gerais elaborou, sozinho, 4 dos 9 artigos do Sudeste.

Em 2020, o Pará passou a contribuir mais com os números do Norte, sendo o responsável pelo fortalecimento da participação da região no evento, elaborando 4 dos 6 artigos da região, conforme é mostrado na Figura 4 (a). Ainda assim, configurou-se uma concentração, que também ocorreu nas regiões Centro-Oeste, Nordeste e Sul. Os estados de Goiás, Minas Gerais e Ceará foram os que mais contribuíram na sua respectiva região. Somente o Sul teve a participação de todos os seus estados no evento, conseguindo partilhar quase que igualmente o número de artigos entre eles.

Por fim, pode-se observar na Figura 4 (b) que 2021 – o segundo ano de evento online – foi o ano que teve a melhor distribuição do número de artigos entre os estados contribuintes em cada região. No Norte, os estados do Pará e do Amazonas dividiram igualmente os 6 artigos da região. No Nordeste, Centro-Oeste e Sul houve pouca diferença entre o número de artigos publicados por cada estado participante. A concentração se deu apenas no Sudeste, em que Minas Gerais e São Paulo foram responsáveis por 8 dos 11 artigos da região.

(a) (b)

Figura 3. Número de Artigos publicados por estado em 2018 e 2019.

Diante das figuras apresentadas, é possível notar que alguns estados variaram a sua participação no WIT, publicando mais, menos ou não publicando artigos na edição; contudo, a maioria deles já contribuíram pelo menos uma vez com o evento durante os anos analisados. Uma minoria composta pelos estados do Acre, Roraima, Rondônia, Tocantins, Maranhão e Piauí não publicou durante esse período. Dessa forma, nota-se uma demanda por incentivos que aumentem a participação destes e de outros estados no evento, na tentativa de promover a diversidade regional.

Ao observar o mapa dos projetos parceiros do Meninas Digitais, é possível perceber que os estados que não publicaram durante o período analisado apresentam nenhum ou poucos projetos locais. Acre e Roraima possuem zero projetos, Tocantins, Rondônia e Maranhão possuem um e Piauí possui dois. Sendo assim, acredita-se que uma forma de aumentar a participação desses estados no evento seria incentivar a parceria com instituições de ensino locais para a criação de projetos e para a realização de mais ações voltadas à pesquisa e extensão sobre mulheres na computação.

Além disso, também deve-se levar em conta o nível de desenvolvimento socioeconômico dos estados, visto que para um trabalho ser incluído nos anais do evento é necessário que pelo menos um autor esteja inscrito e presente de forma presencial para a apresentação, os custos de deslocamento e hospedagem – principalmente em um país de grandes dimensões como o Brasil – são fatores que influenciam na participação de certos estados no evento. Sendo assim, a flexibilização dos critérios para a inclusão dos artigos nos anais, como a exigência de que pelo menos um autor inscrito no evento possa apresentar o trabalho de forma presencial ou virtual, desde que esteja presente para tirar dúvidas, é uma maneira de incentivar a maior contribuição desses estados. Tal fato foi comprovado nos eventos online de 2020 e 2021, nos quais o número de contribuições por região e estado aumentou consideravelmente.

(a)

(b)

Figura 4. Número de Artigos publicados por estado em 2020 e 2021.

Com base no exposto, a resposta à QP01 sobre as regiões que mais publicaram tem-se o Nordeste, com 50 artigos, e o Sul, com 48. Já os cinco estados que mais contribuíram foram Rio Grande do Sul, com 19 trabalhos, Paraná, com 18, Minas Gerais, com 17, e Paraíba e Ceará, com 16 e 14 trabalhos.

Para responder á QP02, pode-se observar na Figura 5 o percentual de artigos por tema. O tema Atividades, que abrange projetos e ações realizadas no intuito de incentivar meninas na computação, foi o mais presente durante os seis anos de WIT, com mais da metade do número de artigos (54%). O segundo tema mais recorrente é Análise de Dados, com destaque para os estudos voltados à análise da participação feminina em cursos técnicos ou superiores de computação.

Os Fatores de Influência (7%) e o Perfil de Estudantes, Egressos e Profissionais (5%) foram o terceiro e o quarto tema mais abordado no evento. Os demais variaram entre 1% e 3%, mas ainda assim, apresentam uma baixa ocorrência se comparados aos dois mais presentes. O tema Acessibilidade, por exemplo, só foi abordado em 2 artigos, e ambos abordam o mesmo projeto, de estudantes de computação surdas.

Um panorama dos temas mais abordados por edição do evento é ilustrado na Figura 6. A partir dela, é possível notar uma tendência do aparecimento de novas abordagens a cada ano. Contudo, os números ainda são tímidos, uma vez que os temas de Atividades e Análise de dados têm juntos, em média, 74,3% de participação por edição. Com isso, constata-se uma saturação desses temas: apesar do foco principal do WIT ser divulgar atividades e informações voltadas ao incentivo feminino na computação, já existe um grande acervo de trabalhos voltados para isso. Portanto, é essencial que a comunidade aborde novos desafios no intuito de compartilhar diferentes tipos de conhecimento e manter o evento ainda mais atrativo.

As figuras apresentadas neste trabalho demonstram os dados até o presente mo-

Figura 5. Percentual de artigos por tema.

mento, o que chamou a atenção para a possibilidade de agrupar essas informações em uma visualização mais dinâmica. Isso motivou a criação de uma ferramenta interativa para visualização dos dados que permite a inclusão de informações de edições do evento.

## 5. Considerações Finais

Este trabalho realizou a coleta e a extração de informações de 202 artigos, completos e resumidos, publicados no evento Women in Information Technology realizado pelo Congresso da Sociedade Brasileira de Computação nos anos de 2016 a 2021. As informações extraídas foram o título, ano de publicação e a filiação dos autores, esse último com o objetivo de identificar a origem do artigo. A partir da leitura do resumo e das palavras-chave dos trabalhos, foram criados 14 temas para classificar o assunto abordado em cada um.

Após classificados, foi realizada a análise do número de artigos por região, estado e tema. Essa análise teve como objetivo responder às duas questões de pesquisa propostas, ao que constatou-se que as regiões Nordeste e Sul são ativas no evento, enquanto que a região Norte é a que menos publica. Tal fato pode estar relacionado, dentre outros fatores, aos índices de desenvolvimento econômico e de investimentos à pesquisa da região.

Além disso, no contexto das regiões, tem-se ainda uma concentração de artigos em alguns estados; portanto, nem todos os estados contribuem para o status da sua respectiva região. O Norte, por exemplo, publicou 22 artigos em seis anos de evento, sendo a maioria de responsabilidade dos estados do Pará e Amazonas – estados como Acre, Rondônia, Roraima e Tocantins não publicaram nenhum trabalho durante todo o período. Contudo, observou-se que esses estados possuem nenhum ou poucos projetos parceiros do programa Meninas Digitais, o que pode influenciar tais resultados, além dos fatores socioeconômicos de cada estado.

Com relação aos temas, notou-se que a maioria dos artigos abordam atividades

> 4https://gabrielamaximino.github.io/computacao-para-meninas/

Figura 6. Percentual de artigos por tema por e por ano.

com meninas para atraí-las para a computação. Sendo assim, apesar das diferentes propostas de projetos desse tipo, há a carência de diversidade de temas, pois já há um grande acervo sobre esse assunto, demonstrando ser necessário, o incentivo a novas abordagens.

De modo geral, foi possível observar que, com o evento aceitando mais artigos, mais regiões estão publicando, aumentando a diversidade regional. Isso foi constatado principalmente nos anos de 2020 e 2021, quando o Congresso ocorreu online. Contudo, isso é desigual em termos de contribuições locais, visto que são sempre os mesmos estados que publicam. O mesmo ocorre com os temas: há uma concentração em Atividades e Análise de Dados, sendo necessário o incentivo à maior pluralidade de estados e temas.

É importante ressaltar que a análise realizada contemplou apenas seis edições do evento. Além disso, para a classificação regional apenas a filiação do primeiro autor foi levado em consideração nesse trabalho, o que pode influenciar os resultados.

Por fim, acredita-se que esse trabalho possa fornecer subsídios para incentivar a produção científica em mais estados brasileiros no WIT, e dessa forma, contribuir para que o evento se torne mais diverso em estudos, estratégias e abordagens com ênfase nas mulheres na computação. Como trabalhos futuros, deseja-se realizar a mesma análise contemplando mais edições do evento, como os últimos dez anos, com o objetivo de traçar um panorama mais fiel do evento. Além disso, diferentes aspectos podem ser abordados futuramente, como parcerias entre regiões nas publicações, quais os temas mais abordados por região e quais instituições publicam mais.

## Agradecimentos

Agradecemos à Universidade Federal do Pará que concedeu a bolsa de extensão (PIBEX) para a realização do subprojeto “Computação para Meninas” que faz parte do projeto Meninas PaiD’Eguas.
