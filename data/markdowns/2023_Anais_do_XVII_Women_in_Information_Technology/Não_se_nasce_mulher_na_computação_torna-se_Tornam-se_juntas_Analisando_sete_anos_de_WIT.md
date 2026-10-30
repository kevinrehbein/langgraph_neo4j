# Não se nasce mulher na computação, torna-se. Tornam-se juntas! Analisando sete anos de WIT.

Luiz Paulo Carvalho, Silas Lima Filho, Michele A. Brandão, Jonice Oliveira, Flávia Maria Santoro, Mônica Ferreira da Silva

1UFRJ – Rio de Janeiro, RJ – Brasil

2IFMG/UFMG – Belo Horizonte, MG – Brasil

3UERJ – Rio de Janeiro, RJ – Brasil

luiz.paulo.carvalho@ppgi.ufrj.br, silaslfilho@ppgi.ufrj.br

michele.brandao@ifmg.edu.br, jonice@dcc.ufrj.br,

flavia@ime.uerj.br, mfsilvamail@gmail.com

Abstract. CSBC integrate Brazilian computing and drives the direction of the area in the country. In one of its base events, WIT, gender topics and computing meet. The analysis of the last 7 years of WIT shows something rare in CSBC events: an absolute and proportional amount of authorship by women in accordance with the dialectical agenda of the event. WIT presents cohesion, recurrence and collaboration among its community, with a predominance of institutions outside the Southeast region, and publications where we perceive an emphasis on education and on solving problems faced by Brazilian women.

Resumo. O CSBC integra a computação brasileira e trata dos rumos da área no país. Em um de seus eventos-base, WIT, questões de gênero e computação se encontram. A análise dos últimos 7 anos de WIT expõe algo raro nos eventos do CSBC: uma quantidade absoluta e proporcional de autoria de mulheres em conformidade com a agenda dialética do evento. WIT apresenta coesão, reincidência e colaboração entre sua comunidade, com predominância de instituições fora da região Sudeste, e publicações onde percebemos a ênfase em educação e na solução de problemas enfrentados pelas brasileiras.

## 1. Introdução

Em 2023 o workshop Woman in Technology (Mulheres na Tecnologia) (WIT) alcança sua décima sétima edição, e se apresenta:

> “O WIT – Women in Information Technology está em sua décima sétima edição, sendo realizado desde 2007 como uma iniciativa da SBC para discutir os assuntos relacionados a questões de gênero e a Tecnologia de Informação (TI) no Brasil – histórias de sucesso, políticas de incentivo e formas de engajamento e atração de jovens, especialmente mulheres, para as carreiras associadas à TI. Organizado na forma de apresentação de artigos, palestras convidadas e painéis, o workshop é centrado em debater problemas relacionados à mulher e ao seu acesso à TI, tanto do ponto de vista de mercado de trabalho quanto de inclusão e alfabetização digital. Os temas abordados se concentram na necessidade de educar, recrutar e treinar mulheres, como uma política estratégica para o desenvolvimento e competitividade nacional e regional.”

> 1https://csbc.sbc.org.br/2023/wit/ [acesso 04-04-2023]

O WIT é o primeiro evento-base no Congresso da Socidade Brasileira de Computação (CSBC) que trata de um fenômeno primariamente não-técnico. Um dos fatores que distinguem esse evento é o seu foco em um aspecto social, cultural e histórico exterior aos aspectos técnicos computacionais em si: a questão de gênero na computação, sendo um aspecto intrínseco à Computação. O WIT trata de um fenômeno computacional não-técnico, que agenciado pode trazer melhorias, vantagens ou benefícios à computação como um todo, enquanto uma instituição social [Lakatos e Marconi 2019]. O evento, através de sua comunidade, estrutura, formaliza e registra o panorama das mulheres na computação no Brasil, tanto por meio de suas publicações, como pelos respectivos dados e metadados associados em materialidade, autores, instituições e regiões.

A motivação central e primária deste trabalho é analítico-descritiva e tem o objetivo de apresentar uma análise descritiva baseada em Análise de Redes Sociais (ARS) e estatística sobre os dados e os metadados de publicações do WIT (2016 – 2022) através de suas publicações, envolvendo dados diversos disponíveis, possíveis e válidos. À esta categoria de pesquisas é facultada a ausência de perguntas de pesquisa ou hipótese [Marconi e Lakatos 2017], com ênfase nas informações e conhecimentos gerados; expomos o panorama de uma década de WIT, compondo uma contribuição meta-científica descritiva do cenário de educação e computação brasileiro.

Considerando as dinâmicas científicas tradicionais, percebemos um avanço da ciência ancorado nas publicações e comunicações científicas formais [Agassi 2008]. Apesar do WIT iniciar sua operação em 2007, sua chamada de trabalhos tradicional ocorreu em 2016, ponto do qual inicia nossa análise. Neste presente trabalho apresentamos uma visão materialista através de outras dimensões além das publicações, e seus conteúdos [Latour 1987, Lefèvre 2005], com uma ênfase metacientífica [Ioannidis et al. 2015, Ioannidis 2018] por uma abordagem analítico-descritiva [Marconi e Lakatos 2017, Wazlawick 2014]. Analisamos sete dimensões: autoria, sexo, instituição/filiação, geolocalização institucional, idioma e resumos + palavras-chave.

Alguns trabalhos similares analisam comunidades e espaços acadêmicocientíficos brasileiros sob uma perspectiva meta-científica [Ioannidis 2018], como [Lobato et al. 2021] e [Digiampietri et al. 2017] sobre o Workshop Brazilian Social Network Analysis and Mining (BraSNAM); [Barbosa et al. 2017] sobre o Simpósio Brasileiro sobre Fatores Humanos em Sistemas Computacionais (IHC-Br); ou [Kauer e Moreira 2013] sobre a evolução dos tópicos de interesse no Simpósio Brasileiro de Banco de Dados (SBBD). O exame sobre si, envolvendo análises, avaliações e percepções formais e estruturadas; permite que rede(s) ou comunidade(s) amadureçam, tomem decisões baseadas em evidências e se identifiquem objetivamente [Ioannidis et al. 2015].

Cabe considerar as publicações meta-científicas do WIT sobre o próprio WIT [Bordin et al. 2021, Bordin et al. 2022, Maximino et al. 2022] ou sobre outros eventos acadêmico-científicos em computação [Êrica Carmo et al. 2021, Lorens et al. 2020]. Em uma busca breve pelos anos de 2020, 2021 e 2022 já notamos diversos trabalhos com

> 2Neste trabalho, consideramos apenas o WIT, enquanto um espaço acadêmico científico. Reconhecemos igualmente a importância do projeto Meninas Digitais, associado ao WIT, acessível em: https: //meninas.sbc.org.br/ [acesso 04-04-2023]

> 3Utilizamos o termo considerando as pessoas autoras. Para síntese de espaço e por costume científico, optamos pelo uso do termo “autores”, sem desvalorizar “autoras” ou “pessoas autoras”.

esta natureza crítica e de auto-exame, reforçando um aspecto de maturidade e consciência próprias. Por restrição de espaço, nos limitamos a indicá-los e agenciá-los ativamente. Diferente de todos estes, aqui cobrimos os sete anos de WIT e trazemos uma perspetiva ampla em ARS, inédita até então.

O trabalho está estruturado da seguinte forma, a Seção 2 expõe o método, materiais e conceitos essenciais; a Seção 3 apresenta os resultados; e a Seção 4 encaminha as considerações finais.

## 2. Método, recursos, fontes de dados e conceitos

A Figura 1 expõe o método deste trabalho. Coletamos dados disponíveis e possíveis para análise presentes no CSBCSet [Lima Filho et al. 2023], um conjunto de dados representando publicações de 2013 a 2022 do Congresso da Sociedade Brasileira de Computação (CSBC), com diversos dados e metadados. As análises, individuais ou combinadas, partem de dados dos atributos: Ano, Evento, Edição, Titulo, Pessoa autora, Sexo, Instituição, Localização, Idioma, Resumo, Palavras-chave. O CSBCSet traz dados sobre diversos eventos, para as análises neste presente trabalho utilizamos o sub-conjunto de dados “WIT” no atributo Evento.

Figura 1. Etapas da metodologia aplicada neste trabalho.

A partir do método, utilizamos os seguintes sistemas computacionais: NetworkX e Gephi, gratuitos e abertos, usados para criação, manipulação e estudo de estruturas, dinâmicas e funções de redes complexas; (iii) Microsoft Excel, versão comercial, e Google Sheets, gratuito, usados para tabelas e planilhas para estruturação, armazenagem e compartilhamento de dados, com funcionalidades aritméticas e estatísticas, representação gráfica de dados e combinações complexas. Utilizamos as funcionalidades gratuitas do sistema online WordClouds para geração das nuvens de palavras.

Em relação à etapa de análise, objetivo primário deste trabalho, realizamos análises quantitativas e estatísticas gerais e conduzimos métodos e abordagens em ARS [Tabassum et al. 2018]. Em ambos os casos, o WIT foi tratado como um todo e cada ano separadamente. Pelo excesso de informações geradas, e para melhor visualização, disponibilizamos os artefatos gerados online.

Algumas definições e conceitos de ARS são fundamentais ao decorrer deste trabalho [Tabassum et al. 2018]: Componente gigante é um sub-grafo da rede principal com a maior quantidade de nós conectados e sua medida é importante para mostrar o quão coesiva ou separada uma rede é; coeficiente de agrupamento representa a tendência de um nó formar uma comunidade, ou seja, a tendência dos vizinhos de um nó se conectarem

> 4https://zenodo.org/record/7977462 [acesso 04-04-2023]

> 5https://networkx.org/ – https://gephi.org/ – https://en.wikipedia.org/ wiki/Spreadsheet – https://www.wordclouds.com/ [acesso 04-04-2023]

> 6https://4658.short.gy/CSBC_ARS_2023 [acesso 04-04-2023]

uns aos outros; o diâmetro é o menor caminho entre dois nós com a maior distância na rede; densidade é a proporção de conexões possíveis na rede em relação às existentes; e, finalmente, um clique consiste de um sub-grafo completo na rede, no qual todos os nós estão conectados uns aos outros.

### 2.1. Aspectos éticos

Extraímos esta discussão de [Carvalho et al. 2023c], pela semelhança e aplicação do CSBCSet. Manter os nomes das pessoas autoras ou seguir com anonimato foi um dilema ético que nos acometeu. Moralmente, é ausente uma justificativa, fundamentação ou base que objetivamente determine um anonimato, pelas diretrizes institucionais governamentais que regem a ética em pesquisa brasileira [Brasil 2016] ou questões éticas gerais de pesquisa [ANPEd 2019, Bos 2020, London 2022]. Pois lidamos com dados abertos; dados de promoção e publicidade de atividade-fim; sem qualquer dado pessoal sensível ou potencialmente prejudicial ou consequencialmente negativo às partes; consiste de uma pesquisa secundária que trata especificamente de dados meta-científicos; por fim, é ausente de qualquer juízo moral ou de valor primário associado aos dados.

Eticamente debatemos uma série de possíveis consequências negativas ou prejudiciais materiais e concretas, além da ética relativista (e.g., “não quero” ou “não gosto”), e fomos incapazes de pontuar justificativas morais significativas o bastante para seguir com o anonimato. Adicionalmente, pessoas autoras podem utilizar destes dados ou informações para sua vantagem, e.g., em memoriais de promoção de carreira.

## 3. Resultados e discussão

Nesta seção apresentamos as análises quantitativas (Seção 3.1), gerais e centralizadas em cada um dos atributos-chave; e as análises baseadas em ARS (Seção 3.2) da colaboração entre pesquisadores e instituições.

### 3.1. Análises quantitativas gerais

Nesta seção apresentamos as análises quantitativas gerais, aritméticas ou estatísticas, combinando os dados e informações sobre o WIT presentes no CSBCSet [Lima Filho et al. 2023], de suas publicações entre 2016 – 2022, excluídas comunicações como abertura, prefácios, mensagens da coordenação, dentre outros.

Como primeiro atributo e pela essência do evento, iniciamos pela análise de sexo (seções c e d da Tabela 1), no WIT ocorre um fenômeno inteiramente exclusivo e distinto do restante do CSBC [Carvalho et al. 2023c]: em todas as edições e anos a quantidade absoluta e proporcional de autoria de mulheres supera a de homens. Nenhum homem é autor primário de publicações no WIT 2022. Em nenhuma edição a quantidade de autoria de homens superou 20%; e a quantidade de autoria de mulheres não foi inferior a 75%.

Considerado o restante do CSBC [Carvalho et al. 2023c], este fenômeno é único. Analisando as autorias de uma década dos eventos mais longevos do CSBC

> 7Estamos conscientes sobre a diferença entre sexo e gênero. Esta é uma limitação de abordagens envolvendo dados mecanicamente e estatisticamente rotulados devido ao volume como do CSBCSet, i.e., sem que os autores envolvidos anunciem seu próprio sexo. Ademais, este é um dado significativo à investigação do envolvimento de mulheres na computação brasileira [Ribeiro et al. 2020, Santana e Braga 2020].

[Carvalho et al. 2023c], em nenhum ano, de nenhuma edição e de nenhum evento a quantidade de autoria das mulheres supera a de homens.Isto é, reforça a agenda dialética proposta pelo WIT. O mais próximo de um empate ocorre no Workshop de Educação sobre Computação (WEI) e no WPerformance em 2021, no qual a quantidades de autorias primárias empata.

Intensificando o cenário, quanto “mais técnica” a natureza do evento, menor a quantidade de mulheres enquanto autorias mais prolíficas nas dez primeiras posições [Carvalho et al. 2023a, Carvalho et al. 2023b, Carvalho et al. 2023a]. De maneira inusitada ou até inesperada para quem desconhece o cenário do WIT e apenas observando estes quantitativos, pode ser estranho perceber que um dos autores mais prolíficos no WIT é um homem, Cristiano Maciel envolvido em 14 autorias. Pareado com Aletéia Araújo, também em 14 autorias; seguidos por Maristela Holanda com 13; Sílvia Amélia Bim com 12; e Karen Ribeiro com 11.

Logo após o Cristiano Maciel, seguem 17 mulheres, até Adriano Braga, na 19ª posição. Então mesmo que um homem esteja “no pódio quantitativo mais alto”, logo depois todas as posições mais significativas são de mulheres, sendo também um feito raro comparado aos demais eventos do CSBC [Carvalho et al. 2023c].

Partindo para análise de autorias/pessoas autoras, a Tabela 1 expõe os resultados das publicações e suas autorias no conjunto (a). Há uma distribuição esparsa da quantidade de autores por publicação, principalmente em 2021 em uma relação de ≈ 5 para 1; no restante este valor é de ≈ 4 para 1.

Se considerarmos 10% de todas as publicações ( ≈ 23) como um valor estável para os anais, e 10% deste valor ( ≈ 2) como um valor estável de variância, variando entre 21 e 25, percebemos que o WIT é um evento instável no quantitativos de publicações por ano. Mesmo assim, em todos os anos os valores superaram o teto desta margem, e.g., excessivamente em 2021 com 48 publicações. A análise dos dados disponíveis encaminha à uma percepção tendenciosa à uma quantidade de aceites crescente. Fomos incapazes de encontrar os dados de submissão e aceite, o que nos limita a esta análise simples.

Tabela 1. Análises quantitativas gerais de publicações, sexo e idioma

||(a) Pub|licações|(d) I|dioma das|publ|icações|(b) |Autores(t|odos) |por sexo|(c) |Autores(p|rimári|os) por sexo|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Ano|Por autor (todos)|Por autor (único)|pt-br|Qtd. %|en|Qtd. %|M|Qtd. %|F|Qtd. %|M|Qtd. %|F|Qtd. %|
|2016|105|25|25|100%|0|0%|14|13%|87|83%|1|4%|23|92%|
|2017|109|28|26|93%|2|7%|16|15%|85|78%|4|14%|23|82%|
|2018|113|28|25|89%|3|11%|21|19%|88|78%|1|4%|26|93%|
|2019|117|31|30|97%|1|3%|16|14%|97|83%|1|3%|29|94%|
|2020|177|42|42|100%|0|0%|26|15%|144|81%|5|12%|35|83%|
|2021|241|48|48|100%|0|0%|24|10%|207|86%|1|2%|45|94%|
|2022|136|30|29|97%|1|3%|14|10%|118|87%|0|0%|28|93%|
|Geral|998|232|225|97%|7|3%|131|13%|826|83%|13|6%|209|90%|

 Alguns dos dados deste atributo constam como “-” (desconhecidos); o somatório pode não alcançar 100%.

Em relação à quantidade de autorias por publicação e ano, 545 ( ≈ 80%) apresentam apenas uma autoria (i.e., publicaram apenas um trabalho, seja como autor individual ou em colaboração); 82 ( ≈ 12%), duas autorias; 15 ( ≈ 2%), três autorias; 16 ( ≈ 2%), quatro autorias; o somatório das demais é de ≈ 4%. Diversos trabalhos no WIT apresentam cinco ou mais autorias, fenômeno divergente ao CSBC [Carvalho et al. 2023c]. O WIT

tem a característica de apresentar muitos autores com muitas autorias, indicando colaboração entre sua comunidade.

O grafo na Figura 2 expõe o componente gigante acumulado de 2016 – 2022 no WIT. A cor das arestas serve para, sem ordem ou associação específica, diferenciar os anos de ocorrência. Analisando em conjunto com a Figura 3 notamos dois grandes agrupamentos, um conduzido por Sílvia Amélia Bim e outro por Aletéia Araújo. Cada um com quantidades significativas de autorias. Entretanto, pelo excesso de colaborações e parcerias, inclusive com maior diâmetro, o componente de Sílvia Amélia Bim se destaca. Por outro lado, o componente de Aletéia Araújo tem maior densidade em autorias, i.e., mais publicações com mais autores combinados entre si.

A Figura 3 e as métricas de ARS para colaboração indicam que, quando se trata de colaboração, Maristela Holanda e Sílvia Amélia Bim superam Cristiano Maciel e Aletéia Araújo, esta ocupando a terceira posição em grau de colaboração. Cristiano Maciel, neste quesito, apresenta um grau bem menor, alocando-o na sétima posição, i.e., apesar do maior quantitativo em autorias, as colaborações são mais concentradas e menos diversas.

Figura 2. Componente gigante do WIT 2016 – 2022

Figura 3. Grafo de colaboração e co-autorias em 7 anos de WIT, 2016 – 2022

A maioria das publicações do WIT apresenta três autores, 58 ( ≈ 25%). Há uma variância entre um extremo com as autorias individuais ( ≈ 2,5%), até 14 autores, em 2 publicações ( ≈ 1%), maior quantidade observada. Como se percebe pela distribuição de publicações e autores na Tabela 1, diversas publicações tem muitos autores, onde observamos 12 publicações ( ≈ 5%) com 8 autores e 14 ( ≈ 6%) com 7 autores.

Sobre a análise de idiomas, português brasileiro é o idioma significativamente dominante do WIT. O idioma das publicações, e seu desdobramento político, é objeto de discussão acadêmico-científica na computação brasileira [Carvalho et al. 2022, Mendonça 2021], e podemos afirmar que o WIT enfatiza uma comunicação nacional e orientada àqueles que se comunicam em português (brasileiro ou não). Este comportamento é esperado, pela imanência do fenômeno primário estudado no WIT, fortemente orientado às brasileiras e ao Brasil.

Representamos as relações da análise de instituições/filiações como um grafo, exposto na Figura 4. Os nós representam as instituições e o tamanho o respectivo grau, i.e., relevância quantitativa; e as arestas representam as relações entre instituições e a largura a relevância quantitativa dessa interação. Diferente da análise de autorias, pela Figura 2, aqui fica explícita as fortes colaborações da UTFPR e UFMT. Um dos eixos está concentrado no Distrito Federal (DF) e Minas Gerais (MG), e o outro espalhado por todas as regiões do país.

Apesar do componente composto por PUCPR, UP, Tech Ladies e UFSCar ter quatro autores e cada um com apenas uma publicação, comparativamente esta é uma colaboração relevante pelas métricas, mesmo que concentrada.

A Tabela 2 sintetiza os resultados das instituições/filiações com publicações que apresentam 24 ou mais autorias. Por exemplo, a UFSC publicou em 4 anos distintos e com mais ocorrências (36) do que a UNIPAMPA (35), que publicou em 7 anos distintos. Como um comportamento atípico, 3 instituições apresentaram autores afiliados presentes em todas as edições do WIT (UnB, UTFPR, UFMT). Mesmo que a UnB colabore com poucas instituições, mantém a consistência e qualidade de ocorrências.

Percebemos um fenômeno atípico e inusitado ao analisar a Figura 4 e a Tabela 2, apesar da UFC ter a terceira maior quantidade de autorias, empatada com a segunda (UTFPR) com 57; todas as suas publicações são de colaborações internas e com coautorias muito similares.

O ano de 2021 apresenta um valor atípico em relação à quantidade total de instituições participantes (49). Este fenômeno pode ter sido causado pela realização do evento na modalidade online, devido à pandemia de COVID-19 e restrições sanitárias e sua análise pode compor um potencial trabalho futuro neste sentido.

Figura 4. Grafo de colaboração entre instituições dos autores

A análise de geolocalização institucional traz um resultado destoante das análises anteriores: MG é o local com a maior quantidade de autorias (83, 8,32%). Apesar das colaborações serem poucas e de cada instituição apresentar pouca representatividade quantitativa (e.g., PUC Minas, IFMG, CEFET-MG, UFMG), em conjunto superam em 1

Tabela 2. Análises de instituições com 24 ou mais autorias

||Qtd.|2016|2017|2018|2019|2020|2021|2022|Total|
|---|---|---|---|---|---|---|---|---|---|
|UnB|7|4|11|13|3|3|24|22|80|
|UTFPR|7|15|10|3|5|9|6|9|57|
|UFC|5|0|0|6|12|19|15|5|57|
|UFPB|6|6|10|19|9|6|2|0|52|
|UFAM|6|7|10|7|3|4|21|0|52|
|UFMT|7|7|4|8|16|4|2|9|50|
|UFSC|4|22|0|0|0|4|3|7|36|
|UNIPAMPA|6|2|3|0|8|9|8|5|35|
|IF GOIANO|5|0|4|0|5|8|6|8|31|
|UFBA|6|4|9|3|1|7|3|0|27|
|UFPA|3|0|0|0|0|10|9|5|24|
|UFAL|3|0|0|0|0|8|9|7|24|

o Paraná (PR), encabeçado pela UTFPR. O PR em 1 supera o DF, encabeçado pela UnB. Logo após, Rio Grande do Sul (75, 7,52%), Paraíba (74) e Ceará (73). O Ceará apresenta todas as suas autorias institucionalmente auto-contidas, IFCE e UFC, sem nenhuma colaboração externa, desta forma ausentes da Figura 4.

Como característica de geolocalização desviante do padrão, as 12 primeiras instituições com maior quantidade de autorias estão fora da região Sudeste. Desta maneira, todas as regiões brasileiras são contempladas pela UFAM (Norte), UnB e UFMT (CentroOeste), UTFPR (Sul) e UFC (Nordeste). Como supracitado, mesmo que MG seja o local mais representativo, é impacto de suas colaborações.

Por outro lado, considerando as regiões e UFs analisadas, as UFs sem ocorrência de nenhuma autoria encontram-se majoritariamente na região Norte, sendo elas AC, RO, RR, TO; seguida pelo Nordeste, PI e MA. Esta informação pode estar estratégica para políticas de parceria e colaboração ou análises críticas.

Para contextualização do conteúdo das publicações, analisamos os resumos e palavras-chave. A Figura 5 expõe a nuvem de palavras após tradução para português brasileiro e tratamento de termos vazios (e.g., artigos), insignificantes (e.g., verbos vagos) ou descartáveis (e.g., termos que isolados perdem significado). Estavam disponíveis palavras-chave de 2019 – 2022. Como a nuvem de palavras de resumos ficou similar à de palavras-chave, seguimos com a de resumos, mais completa e consistente.

Notamos que os termos seguem a natureza epistêmica do evento, com ênfase em mulheres, meninas, feminina, gênero. Há forte ênfase em educação e termos desta área, com cursos, estudantes, médio (de ensino médio) e ensino. Ambas categorias semânticas estão de acordo com o WIT e sua proposta primária.

### 3.2. Análise da Rede Social do WIT

Para realizar as análises temporais sobre as interações de co-autoria do WIT, utilizamos as métricas de número de nós, número de arestas, densidade, diâmetro, tamanho do componente gigante, tamanho e número máximo de cliques e coeficiente de agrupamento.

Pela quantidade de nós (autores) e arestas (autoria) ao longo dos anos, podemos ver que é uma comunidade que cresce continuamente. Entretanto, a conexão entre os autores não é tão forte, o que é de se esperar em comunidades muito grandes ou em

Figura 5. Nuvem de palavras dos resumos do WIT, 2016 – 2022

desenvolvimento. Isto pode ser visto pelas métricas referentes à densidade do grafo e número de cliques do grafo. Globalmente, a rede não é “densa”, ou seja, o número de conexões diretas entre os autores não é grande. Grande parte das colaborações são feitas por grupos com alto grau de colaboração interna, mas não tão fortemente conectados entre si. O alto número de cliques no grafo e a pouca força da componente gigante mostram indícios disso. A Figura 5 também ilustra essa característica.

A componente gigante representa a “saúde” da comunidade, exposto graficamente na Figura 2, mostrando como os seus membros estão ligados direta ou indiretamente. Ligações diretas ou indiretas melhoram o fluxo de informação e conhecimento. Os valores mostram que a componente gigante tem se tornado estável, com um tamanho modesto ao longo dos anos se comparado ao número de autores. O nível de interação direta entre os autores não é grande (mostrado pela baixa densidade do grafo e da componente gigante). Observando a evolução da componente gigante, em 2022 houve um aumento considerável de sua densidade. Isto pode indicar que, apesar de estável, os membros pertencentes à componente gigante colaboraram mais entre si no último ano, diminuindo distâncias.

Apesar das baixas conexões diretas, há muitas conexões indiretas. Ou seja, há grandes chances de se alcançar um membro rapidamente, através de poucos intermediários (“amigos dos amigos”). O baixo diâmetro e o alto coeficiente de agrupamento do grafo, mostram indícios desta característica. Talvez este efeito tenha ajudado o número de novas arestas no último ano, apesar do número de autores ter diminuído.

## 4. Considerações finais

Neste trabalho apresentamos análises quantitativas gerais e ARS sobre o WIT em sua totalidade temporal, através de suas publicações, dados e metadados. O WIT é um dos eventos tematicamente mais disruptivos e necessários da computação brasileira contemporânea, e através de suas dinâmicas podemos montar parte do panorama da agenda de gênero na computação brasileira, gerando informações e conhecimentos e contribuindo meta-cientificamente com o amadurecimento, memória e cultura do cenário. Desconhecemos trabalhos similares ou fielmente próximos a este, em magnitude de abrangência, completude ou profundidade. Os dados, informações e redes aqui apresentados podem ser explorados para planejar o futuro do WIT, e.g., alcançar seus objetivos.

Apesar de indicarmos a ausência de juízo moral, precisamos anunciar um complemento ético sobre este tópico. Reforçamos a agenda de inclusão, incentivo e manutenção

<u>Tabela 3. Métricas da rede de coautoria de uma década do WIT.</u>

|Métricas|2016|2017|2018|2019|2020|2021|2022|
|---|---|---|---|---|---|---|---|
|Diametro|2|2|2|3|3|2|2|
|DensidadeGrafo|0,050|0,039|0,04|0,038|0,028|0,0298|0,0371|
|DensidadeCompGigante|0,439|0,666|0,454|0,576|0,323|0,632|0,730|
|TamAbsolutoCompGigante|12|9|11|13|15|17|13|
|TamRelativoCompGigante|0,146|0,097|0,111|0,128|0,096|0,0805|0,105|
|NumMaxCliquesCompGigante|4|2|3|4|4|3|3|
|TamMaxCliquesCompGigante|5|7|5|9|6|11|8|
|NumMaxCliquesGrafo|22|27|27|29|37|43|30|
|TamMaxCliquesGrafo|7|7|8|9|9|14|8|
|CoefAgrupamnentoCompGigante|0,887|0,952|0,903|0,902|0,915|0,901|0,877|
|CoefAgrupamnentoGrafo|0,887|0,884|0,893|0,888|0,913|0,924|0,881|
|NumNosCompGigante|12|9|11|13|15|17|13|
|NumNosGrafo|83|93|100|102|157|212|124|
|NumArestasCompGigante|29|24|25|45|34|86|57|
|NumArestasGrafo|173|169|201|200|350|668|283|

de mulheres na computação, sendo nossa intenção central e única descrever e analisar a realidade já concretizada, material. Um aumento da presença de mulheres em edições futuras deve ser uma consequência primária do incentivo e promoção das mulheres no âmbito científico da computação, consequencial.

Em suma, pelos valores basilares da ética científica [London 2022, Marconi e Lakatos 2017], publicações não devem ser aceitas com base no sexo dos autores envolvidos, em primeira autoria ou colaboração, para “fazer um malabarismo” com estes dados. Devemos promover um aumento concreto da quantidade de mulheres agindo neste contexto, atualmente bastante deficitária, para potencialmente alavancar, através de uma abordagem moralmente positiva, o aumento deste quantitativo, como consequência e não princípio. Isto é, a intenção e objetivo primários do WIT são de suma-importância na direção ao panorama estrutural de equidade de gênero na computação, através de um avanço moral positivo [Vázquez 2018].

Além das contribuições analítico descritivas aqui apresentadas, limitações e ameaças à validade são pertinentes [Wazlawick 2014, Marconi e Lakatos 2017]. Devido à limitação de espaço, alguns dos objetos resultantes de análises gráficas foram omitidos e podem ser acessados e apreciados com melhor qualidade no repositório complementar, online (indicado na Seção 2). Este trabalho se limita às análises e métricas realizadas, sendo que outras constituem potenciais trabalhos futuros, quantitativas ou qualitativas, por dimensões ou perspectivas variadas, e.g., outras abordagens ou métricas de ARS.

## 5. Agradecimentos

Este trabalho foi realizado com apoio da CAPES – Brasil – Código de Financiamento 001; e parcialmente pelo programa Oracle for Research (número do prêmio CPQ-2160239).

## Referências**

- [Agassi 2008] Agassi, J. (2008). Science and its History: A Reassessment of the Historiography of Science. Boston Studies in the Philosophy and History of Science №253. Springer, 1st edition.

- [ANPEd 2019] ANPEd (2019). Ética e pesquisa em educação: subsídios – volume 1. volume 1. ANPEd, Rio de Janeiro, RJ.

- [Barbosa et al. 2017] Barbosa, S., Silveira, M., e Gasparini, I. (2017). What publications metadata tell us about the evolution of a scientific community: the case of the brazilian human–computer interaction conference series. Scientometrics, 110(14):275–300.

- [Bordin et al. 2021] Bordin, A., Ferrão, I., e Branco, K. (2021). Women in technology: Uma análise bibliométrica dos últimos cinco anos. In Anais do XV Women in Information Technology, pp. 250–259, Porto Alegre, RS, Brasil. SBC.

- [Bordin et al. 2022] Bordin, A., Frigo, L., Laurindo, S., Ereno, L., e Souza, A. (2022). Uma análise das citações do women in technology (wit). In Anais do XVI Women in Information Technology, pp. 157–166, Porto Alegre, RS, Brasil. SBC.

- [Bos 2020] Bos, J. (2020). Research Ethics for Students in the Social Sciences. Springer Cham, 1st edition.

- [Brasil 2016] Brasil (2016). Ministério da saúde. RESOLUÇÃO Nº 510, DE 07 DE ABRIL DE 2016.

- [Carvalho et al. 2023a] Carvalho, L. P., Lima Filho, S., Brandão, M. A., Oliveira, J., Santoro, F. M., e da Silva, M. F. (2023a). A computação toda, em todo lugar, ao mesmo tempo. Analisando uma década de SBCUP. In Anais do XV SBCUP, Porto Alegre, RS, Brasil.

- [Carvalho et al. 2023b] Carvalho, L. P., Lima Filho, S., Brandão, M. A., Oliveira, J., Santoro, F. M., e da Silva, M. F. (2023b). Avante e a todo vapor, analisando uma década de WPerformance e desempenho computacional no CSBC. In Anais do XXIII WPerformance, Porto Alegre, RS, Brasil.

- [Carvalho et al. 2023c] Carvalho, L. P., Lima Filho, S., Brandão, M. A., Oliveira, J., Santoro, F. M., e da Silva, M. F. (2023c). Uma década de interações entre eventos e pesquisadores do CSBC: Um estudo meta-científico. In Anais do XII BraSNAM, Porto Alegre, RS, Brasil.

- [Carvalho et al. 2022] Carvalho, L. P., Suzano, J. A., Santoro, F. M., e Oliveira, J. (2022). A meta-scientific broad panorama of ethical aspects in the Brazilian IHC. Journal on Interactive Systems, 13(1):105–126.

- [Digiampietri et al. 2017] Digiampietri, L., Mugnaini, R., Pérez-Alcázar, J., Delgado, K., Tuesta, E., e Mena-Chalco, J. (2017). Análise da evolução, impacto e formação de redes nos cinco anos do brasnam. In Anais do VI BraSNAM, Porto Alegre, RS, Brasil. SBC.

- [Ioannidis et al. 2015] Ioannidis, J., Fanelli, D., Dunne, D., e Goodman, S. (2015). Metaresearch: Evaluation and improvement of research methods and practices. PLoS biology, 13(10).

- [Ioannidis 2018] Ioannidis, J. P. A. (2018). Meta-research: Why research on research matters. PLoS Biol, 16(3).

- [Kauer e Moreira 2013] Kauer, A. U. e Moreira, V. P. (2013). Evolução dos temas de interesse do sbbd ao longo dos anos. In SBBD (Short Papers), pp. 25–1.

- [Lakatos e Marconi 2019] Lakatos, E. M. e Marconi, M. (2019). Sociologia Geral. Atlas, 8th edition.

- [Latour 1987] Latour, B. (1987). Science in action: How to follow scientists and engineers through society. Harvard university press.

- [Lefèvre 2005] Lefèvre, W. (2005). Science as Labor. Perspectives on Science, 13(2):194– 225.

- [Lima Filho et al. 2023] Lima Filho, S., Carvalho, L. P., Suzano, J., Brandão, M., Oliveira, J., e Santoro, F. M. (2023). CSBCSet: Um conjunto de dados para uma década de CSBC, seus eventos e publicações. In Anais do XII BraSNAM, Porto Alegre, RS, Brasil.

- [Lobato et al. 2021] Lobato, F., Sousa, G., e Jr., A. J. (2021). Brasnam em perspectiva: uma análise da sua trajetória até os 10 anos de existência. In Anais do X BraSNAM, pp. 217–228, Porto Alegre, RS, Brasil. SBC.

- [London 2022] London, A. J. (2022). For the Common Good: Philosophical Foundations of Research Ethics. Oxford University Press, 1st edition.

- [Lorens et al. 2020] Lorens, A. L., Botelho, J., Moura, A. F., Duarte, B., e Moro, M. (2020). Participação feminina em comitês de programa de simpósios da computação. In Anais do XIV Women in Information Technology, pp. 90–99, Porto Alegre, RS, Brasil. SBC.

- [Marconi e Lakatos 2017] Marconi, M. d. A. e Lakatos, E. M. (2017). Fundamentos de Metodologia Científica. Atlas, São Paulo, SP, 8ª edition.

- [Maximino et al. 2022] Maximino, G., Santos, I., e Mota, M. (2022). Mulheres na ciência: Um panorama das publicações no wit. In Anais do XVI Women in Information Technology, pp. 77–87, Porto Alegre, RS, Brasil. SBC.

- [Mendonça 2021] Mendonça, N. (2021). Abertura e Internacionalização do SBES: Um Oximoro Irreconciliável? In Anais do I Workshop de Práticas de Ciência Aberta para Engenharia de Software, pp. 49–51, Porto Alegre, RS, Brasil. SBC.

- [Ribeiro et al. 2020] Ribeiro, K. S. F. M., Maciel, C., e S. Bim, M. A. (2020). Gênero e tecnologias. In Maciel, C. e Viterbo, J., editors, Computação e sociedade: a profissão - volume 1, pp. 104–140. EdUFMT Digital, Mato Grosso, Brasil.

- [Santana e Braga 2020] Santana, T. e Braga, A. (2020). Uma análise cienciométrica das publicações do congresso da sociedade brasileira de computação na perspectiva das mulheres na computação. In Anais do XIV WIT, pp. 279–283, Porto Alegre, RS, Brasil. SBC.

- [Tabassum et al. 2018] Tabassum, S., Pereira, F. S. F., Fernandes, S., e Gama, J. (2018). Social network analysis: An overview. WIREs Data Mining and Knowledge Discovery, 8(5):e1256.

- [Vázquez 2018] Vázquez, A. S. (2018). Ética. Civilização Brasileira, 39th edition.

- [Wazlawick 2014] Wazlawick, R. S. (2014). Metodologia de Pesquisa para Ciência da Computação. Elsevier, São Paulo, SP, 2ª edition.

- [Êrica Carmo et al. 2021] Êrica Carmo, Souza, E., Schuelter, A. F., Silveira, M., Barbosa, S., Schroeder, R., e Gasparini, I. (2021). Panorama sobre participação das mulheres no ihc. In Anais do XV Women in Information Technology, pp. 151–160, Porto Alegre, RS, Brasil. SBC.
