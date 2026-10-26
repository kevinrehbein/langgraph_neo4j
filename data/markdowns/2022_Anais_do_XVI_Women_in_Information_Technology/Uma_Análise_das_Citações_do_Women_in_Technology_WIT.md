# Uma Análise das Citações do Women in Technology (WIT)

Andréa Sabedra Bordin, Luciana Bolan Frigo, Suelen Laurindo, Luiza Castilho Ereno, Ana Carolina da Silveira de Souza

1Universidade Federal de Santa Catarina (UFSC) Campus Araranguá – Santa Catarina, Brasil.

{ andrea.bordin,luciana.frigo } @ufsc.br

{ suelen.m.laurindo,erenoluiza,anacsilveirasouza } @gmail.com

Abstract. This article provides an analysis of citations from the six years of the Workshop Women in Technology (WIT) to identify the most prestigious articles, the main bibliometric indicators and the citation network knowledge flow. The process was carried out through the collection, extraction and analysis of the articles cited in the event. The results reveal that most of the cited documents were published in events and specifically in the WIT. The most prestigious article addresses the “Programa Meninas Digitais”. The citation network is loosely connected and has six isolated components. The analysis results can support decision-making, both for researchers and event organizing committe.

Resumo. Este artigo provê uma análise das citações dos seis anos do Workshop Women in Techcnology (WIT) com o intuito de identificar os artigos com maior prestígio, os principais indicadores bibliométricos e o fluxo de conhecimento da rede de citações. O processo foi realizado por meio da coleta, extração e análise dos artigos citados no evento. A análise revela que a maioria dos documentos citados foram publicados em eventos e mais especificamente no WIT. O artigo com mais prestígio aborda o Programa Meninas Digitais. A rede de citação é fracamente conectada e possui 6 componentes isolados. Os resultados dessa análise podem subsidiar tomadas de decisão, tanto para pesquisadores, como para a organização do evento.

## 1. Introdução

O desenvolvimento da ciência como sistema é governado pela produção e fluxo de informação, até que esta se transforme em conhecimento. Dessa forma, pesquisadores devem disseminar o conhecimento científico através das publicações [de Souza Vanz and Caregnato 2003]. Os eventos científicos são um meio de disseminação desse conhecimento, uma vez que de forma democrática abrem chamadas para submissão de artigos, que são avaliados por pares da comunidade científica. No processo de comunicar cientificamente resultados de pesquisa, é importante fazer referências às ideias ou resultados de pesquisas anteriores que inspiram, corroboram ou refutam os argumentos da pesquisa em questão.

A análise do conjunto de citações permite explorar e explicar os interesses de uma comunidade científica, assim como avaliar as contribuições de pesquisadores individuais [Garfield 1979]. Uma das formas de realizar a análise de citações é através de uma rede de

citações, onde as publicações científicas são vértices (nodos) e as citações são as arestas (links) que conectam os nodos.

No Brasil, a comunidade científica interessada na temática “mulheres e tecnologia” vem crescendo e tem, desde 2016, a oportunidade de comunicar experiências e resultados de pesquisa no evento Women in Technology (WIT). O WIT é uma iniciativa da Sociedade Brasileira de Computação (SBC) que visa discutir os assuntos relacionados a questões de gênero e Tecnologia de Informação (TI).

Desde o início da abertura das chamadas, o WIT aceitou 202 artigos. Bordin et al. [Bordin et al. 2021] analisaram os indicadores bibliométricos de produtividade e colaboração científica dos últimos cinco anos do WIT, revelando os autores mais produtivos, os autores e instituições de ensino com laços de colaboração mais frequentes, dentre outros. No entanto, a análise das citações não foi abordada no referido trabalho.

O objetivo deste artigo é apresentar uma análise das citações da produção científica do WIT no período de 2016 a 2021, a fim de identificar: (1) quais artigos mais influenciaram outros artigos; (2) propriedades bibliométricas como as principais fontes e veículos de publicação dos artigos citados; (3) a estrutura intelectual deste campo de pesquisa por meio da análise da rede de citação. Para isso foi realizado um processo de coleta e normalização das referências bibliográficas dos artigos aceitos nesse período. Na sequência alguns indicadores bibliométricos foram calculados e a rede de citação foi criada e analisada através do método de Análise de Rede Sociais (ARS).

Além dessa seção, o artigo está organizado da seguinte forma: na Seção 2 são abordados conceitos de análise de citações; na Seção 3 é descrita a metodologia; os resultados são apresentados e discutidos na Seção 4 e, por fim, as principais contribuições e limitações do trabalho são expostas na Seção 5.

## 2. Análise de Citações

Uma citação, segundo [Reitz 2014], é entendida como uma menção à opinião ou argumento de uma autoridade sobre algum assunto, e nesse sentido, a citação deve, também, indicar o “caminho” para verificação dessa menção à referência bibliográfica. Há uma grande variedade de razões pelas quais um autor escolhe citar um determinado artigo. Pesquisas tem identificado alguns dos principais motivos, incluindo reconhecimento, concordância ou crítica, apresentação de conteúdo associado ou favorecimento a amigos pessoais ou colegas pessoais [White 2011].

Uma cadeia de citações conecta ancestrais e descendentes intelectuais. Essas cadeias nos permitem traçar o rastro da influência intelectual ao longo do tempo através de gerações de pesquisadores e responder a perguntas como “Que ideias e métodos influenciaram este trabalho?” e “Como os estudiosos atuais incorporaram este trabalho em teorias atualizadas?” [Chen et al. 2015]. A análise de citações é uma das ferramentas utilizadas para responder estas e outras perguntas.

Solla Price [de Solla Price 1965] foi um dos pioneiros a reconhecer explicitamente as relações de citação como os blocos de construção de uma rede de artigos científicos a partir dos quais hipóteses e conclusões podem ser tiradas. Eugene Garfield, em seus

trabalhos seminais ([Garfield 1972], [Garfield 1979]), reconheceu que, embora existam alguns problemas com o uso de dados de citação – por exemplo, citação negativa e autocitação, ainda assim a análise de citações é uma ferramenta importante para explorar e explicar os interesses de uma comunidade científica, assim como avaliar as contribuições de pesquisadores individuais.

Como método quantitativo de investigação da ciência, a análise de citações possui o intuito geral de medir o impacto e a visibilidade de determinados autores dentro de uma comunidade científica, verificando quais “escolas” do pensamento vigoram dentro das mesmas. Ela também possibilita a mensuração das fontes de informação utilizadas, como o tipo do documento (artigo em evento, artigo em periódico, livro, relatório, etc), os veículos de publicação (evento X, periódico Y), o idioma do documento, dentre outros. Ao utilizar indicadores como os citados, é possível saber como se dá a comunicação científica de uma área do conhecimento, obtendo-se um “mapeamento” da mesma, descobrindo, por exemplo, teorias e metodologias consolidadas [de Souza Vanz and Caregnato 2003].

Quando um documento cita um documento anterior, o conhecimento flui do trabalho citado para aquele que o cita, criando um vínculo entre eles. Essa relação pode ser representada como uma aresta que conecta dois documentos (vértices). Seguindo essa abordagem, os grafos ou redes de citação podem ser usados para analisar os avanços do conhecimento científico e tecnológico. As redes de citação permitem reconhecer rapidamente as respostas a perguntas como “Quais são os trabalhos mais influentes que inspiraram um determinado artigo?”, “Quando determinada linha de pesquisa foi iniciada?”, dentre outras [Chen et al. 2015].

## 3. Metodologia de pesquisa

Este trabalho foi desenvolvido por meio de três etapas: (1) Coleta de dados, (2) Extração de dados e (3) Análise dos resultados. Essas etapas são detalhadas a seguir:

1. Coleta de dados: os dados que serviram de insumo para as análises foram coletados dos anais do WIT no período compreendido entre 2016 e 2021. Esse período de seis anos contemplou todas as edições do evento com chamada de trabalhos. Foram coletados 202 artigos, sendo 150 artigos curtos e 52 artigos completos. A coleta foi realizada manualmente por meio da biblioteca digital da SBC.

2. Extração de dados: os dados de identificação e referências bibliográficas dos artigos foram extraídos manualmente e organizados em tabelas. Cada artigo recebeu um código único, utilizado sempre que o artigo foi citado. As referências foram normalizadas manualmente. Após a codificação e normalização foram processadas todas as relações entre artigos que citaram outros artigos. Este processo foi realizado de forma automatizada através da implementação de um algoritmo que gerou a rede de citação do evento. A rede de citação consiste no conjunto de artigos que foram citados no WIT (incluindo artigos do próprio WIT), representando os nodos da rede e as relações de citação representando as arestas da rede.

3. Análise: os indicadores gerais das citações foram calculados manualmente por meio de contagens em planilhas. Já os indicadores da rede de citação foram ob-

> 2https://sol.sbc.org.br/index.php/wit

> 3shorturl.at/cdzBR

tidos por meio do software de análise exploratória de dados Gephi. As análises posteriores foram feitas com base nos indicadores obtidos.

## 4. Resultados e Discussão

Os resultados apresentados nesta seção foram divididos em duas partes: indicadores gerais e indicadores de rede de citação. Em indicadores gerais serão apresentados: o número de documentos citados por tipo de fonte de publicação; o número de documentos citados por veículo de publicação, dentro dos principais tipos de fonte de publicação; o número de documentos citados por ano de publicação, o número de artigos do WIT que foram citados classificados por temática. Em indicadores de rede de citação será apresentada a rede gerada, assim como as métricas de grau médio da rede, densidade da rede e os nodos da rede com maior prestígio.

### 4.1. Indicadores Gerais

Como o objeto de estudo desta pesquisa são as citações, fizeram parte da análise todos os documentos que foram citados pelos artigos publicados no WIT. A partir dos 202 artigos publicados ao longo da história do WIT, foram contabilizados 1743 documentos citados. Destaca-se que esse número engloba documentos duplicados, uma vez que alguns documentos foram citados por vários artigos.

A Figura 1 ilustra o percentual de documentos citados por tipo de fonte de publicação. Aqui observa-se que a maior parte dos documentos citados (32,8%) foram publicados em eventos científicos, seguido de artigos publicados em periódicos (22,5%). O conjunto de documentos citados que foram publicados em eventos e periódicos representam um pouco mais 50% dos artigos citados.

Figura 1. Percentual de documentos citados por tipo de fonte de publicaç ão.

A Tabela 1 mostra os três principais veículos de publicação onde os artigos citados foram publicados, classificados pelos dois principais tipos de fonte de publicação (Artigo em Evento e Artigo em Periódico). Na categoria Artigo em Evento, o veículo que aparece com maior frequência é o próprio WIT, com 257 artigos, seguido do Workshop Sobre

Educação em Computação (WEI) com 46 artigos e do Computer On the Beach (COBT) com 45. Na categoria Artigo em Periódico, o Periódico Cadernos Pagu aparece com 35 artigos, o Communications of The ACM com 19 e a Revista Estudos Feministas com 18.

A alta frequência de artigos citados que foram publicados em eventos e periódicos está relacionada com a qualidade das informações encontradas em publicações desta natureza. O aparecimento do WIT como o veículo de 15% dos documentos citados pode estar relacionado a carência de veículos de publicação dentro da temática “mulheres e tecnologia”.

Tabela 1. Número de artigos citados por veículo de publicaç ão.

|Artigo em Evento||
|---|---|
|Women in Information Technology (WIT)|256|
|WorkshopSobre Educação em Computação(WEI)|46|
|Computer On The Beach(COTB)|45|
|Artigo em Periódico||
|Cadernos Pagu|35|
|Communications of The ACM|19|
|Revista Estudos Feministas|18|

Em relação ao ano de publicação dos artigos citados, observa-se na Figura 2 um crescimento a partir de meados da década de 90, tendo um pico no ano de 2016. Entendese que o ano ou período das publicações que serviram de referência para os artigos publicados no WIT tenha sido influenciado pelo crescimento do interesse na temática “mulheres e tecnologia”, assim como pelo início das publicações do próprio WIT no ano de 2016. Uma das hipóteses deste pico de citações em 2016 seria ineditismo no cenário brasileiro de um evento voltado a esta temática, além do incentivo a citação de trabalhos do WIT no próprio evento.

Figura 2. Número de artigos citados por ano de publicaç ão

O idioma principal das publicações citadas é o Português com 74%, seguido do Inglês com 25%. Este maior percentual pode estar relacionado à aderência, no sentido de citar iniciativas ou cenários relacionados à realidade brasileira e, portanto, anteriormente publicados em veículos nacionais.

Os artigos publicados no veículo WIT e citados por artigos do próprio evento representam o maior percentual no conjunto de documentos citados (15%). Assim, considerou-se realizar uma análise das temáticas desses artigos, na qual os artigos publicados no ano de 2021 não foram avaliados, considerando que ainda não foram citados em outros artigos do evento. Para isso, os artigos foram categorizados nas seguintes temáticas, as quais foram definidas a partir da leitura do título e resumo dos artigos:

Gênero e TI, Perfil, História, Relato de Experiência, Causas, Mapeamento, Pesquisa com Egressas de Tecnologia e Informação (TI) e Pesquisa de Interesse em TI.

Considerou-se a categoria Gênero e TI quando o conteúdo dos artigos apresentou um estudo sobre gênero na área de TI; a categoria Perfil, quando os artigos continham um estudo/análise sobre o perfil das mulheres da área de Computação; a categoria História, quando os artigos abordavam a história da trajetória feminina em ciência da computação ou áreas correlatas; para a categoria Relato de Experiência foram considerados os artigos que descreveram uma experiência vivida e que contribuíam na construção de conhecimento; na categoria Causa, consideraram-se os artigos que estudaram os motivos e razões que minimizam a entrada e permanência de mulheres na área de TI; a categoria Mapeamento foi utilizada para classificar artigos que realizaram um estudo mapeando ações sobre mulheres na área de TI; a categoria Pesquisa com Egressas de TI foi utilizada quando os artigos apresentaram uma pesquisa com questionários para egressas dos cursos de TI; e por fim, a categoria Pesquisa de Interesse em TI foi considerada quando os artigos divulgaram resultados de pesquisas realizadas com estudantes ainda no ensino médio, na qual avaliavam o interesse destas em cursar uma graduação na área de TI.

O resultado pode ser observado na Figura 3, a qual ilustra o percentual de artigos citados por temática. Esta análise permite identificar qual categoria recebeu mais citações e consequentemente recebeu mais atenção por parte dos autores do WIT.

Figura 3. Percentual de Citaç ões Recebidas por Temática

Observa-se que a maior parte dos artigos desta análise (53%) pertencem a categoria Relato de Experiência. Entende-se que este resultado esteja relacionado à própria gênese do WIT, idealizado como um veículo para divulgação de experiências de projetos parceiros do Programa Meninas Digitais (PMD). Na sequência, tem-se a categoria Gênero e TI com 11,8 % das citações, que também pode ser justificada pelo principal objetivo do WIT, que é discutir questões de gênero e TI. A categoria Perfil, que aparece com 10,6%, pode indicar uma necessidade da comunidade em conhecer o perfil das mulheres envolvidas que atuam em TI, tanto na academia como na indústria, além de discutir e refletir sobre as possíveis causas da falta de representatividade feminina na área de TI. Trabalhos desta natureza são fundamentais para traçar planos de ação para aumentar a representatividade feminina na área.

Por fim, com exceção da categoria Relato de Experiência, entende-se que todas as demais podem ser englobadas como Pesquisa. Dessa forma, observa-se um percentual também significativo de trabalhos que se preocupam em investigar cientificamente

problemas existentes na temática “Mulheres e Tecnologia”e com isso contribuir para a consolidação desta área de pesquisa no Brasil.

### 4.2. Análise da Rede de Citação

Uma rede de citação é um tipo de rede social, representada por um grafo direcionado, onde os artigos representam os nodos (vértices) da rede e as relações de citação representam as arestas, direcionadas do artigo que citou para o artigo que é citado. Métricas de Análise de Rede Social (ARS) podem ser aplicadas em uma rede de citação para descobrir o nível de conectividade da rede (densidade), o número médio de citações recebidas por artigo (grau médio), os artigos mais influentes da rede (prestígio de grau, prestígio de proximidade, prestígio de rank ), grupos formados por artigo e respectivos artigos citados que não foram citados por nenhum outro artigo da rede (componentes isolados), dentre outros.

A rede de citação original das últimas seis edições do WIT (2016-2021) é composta por 1313 nodos (artigos) e 1739 arestas (relações de citação). Aqui é importante observar que um nodo na rede representa um único documento que pode citar e ser citado várias vezes. Para fins de legibilidade, a rede analisada nesta seção e exibida na Figura 4 não apresenta: a) os artigos do WIT que não foram citados por outros artigos do WIT e cujo conjunto das citações (referências bibliográficas) também não foram citadas mais de 1 vez; b) os documentos citados uma única vez por algum artigo do WIT.

Figura 4. Rede de citaç ão do WIT

De acordo com [Wasserman and Faust 1994], existem alguns níveis possíveis de análise de uma rede. No nível análise global, a rede mostrada na Figura 4 revela que o grau médio da rede (número médio de citações recebidas por artigo) é 2,2. Este grau é considerado baixo, e se deve ao fato de 90 nodos ou artigos (dos quais 47 foram publicados em 2021) não terem recebido nenhuma citação neste escopo de análise. A densidade da rede é 0,006 (onde o valor máximo é 1,0), o que indica uma rede fracamente conectada, que explora pouco as possibilidades de citação dentro do universo de artigos analisados.

Ainda nesta perspectiva de análise global, destaca-se que a rede original possui 7 componentes conectados (subgrafos). Um componente conectado é aquele onde os nodos são conectados por algum caminho, mas desconectados dos demais subgrafos [Wasserman and Faust 1994]. Dos sete componentes, seis estão isolados do maior componente (chamado de componente gigante) e referem-se aos artigos do WIT que não foram citados nenhuma vez e cujos artigos da sua lista de referências também não foram citados por mais nenhum artigo.

A rede de citação permite mostrar de maneira visual as relações de citação ou escolha dos documentos que deram suporte ou refutaram argumentos publicados nos artigos. Essas relações caracterizam o fluxo de conhecimento da temática de pesquisa deste evento e são possíveis de serem reconhecidas na visualização da rede.

Ao analisar o conteúdo dos artigos e respectivas citações destes 6 componentes isolados identificou-se que, embora as temáticas estejam dentro da proposta do evento, elas são bastante pontuais, pouco numerosas e transversais como: LGBTQIA+, violência contra a mulher, população quilombola, robótica e aspectos psicológicos. Desta forma, estes componentes formados por nodos (artigos) ficaram isolados dos demais por não terem citações comuns com os demais artigos publicados no evento.

O nível análise individual considera as propriedades de cada nodo individualmente na rede. Em um grafo direcionado à noção de importância ou influência de um nodo é chamada de prestígio. De acordo com [Wasserman and Faust 1994], o prestígio é quantificado por medidas como o prestígio de grau, denotado pelo grau de entrada ou número de arestas recebidas; o prestígio de proximidade, dado pela média dos caminhos mais curtos de um nodo em relação a todos os nodos do seu domínio de influência (conjunto de nodos que são direta e indiretamente ligados ao nodo); e o prestígio de rank, que mede o prestígio de um nodo levando em conta o prestígio dos nodos ligados a este nodo direta ou indiretamente. De uma certa maneira esta medida descreve quão bem conectado é um nodo em relação a outros nodos bem conectados.

A Tabela 2 exibe os cinco artigos (nodos) com mais prestígio de grau, ou seja, com mais arestas recebidas ou mais citados por outros artigos do WIT. Esses artigos também podem ser visualizados na Figura 4, onde estão destacados, de forma proporcional, pelo tamanho e cor verde do nodo. Pode-se observar que o artigo com maior prestígio (posição 1) possui mais que o dobro de citações do segundo artigo. Esse artigo foi citado pela primeira vez na primeira edição do WIT com chamada de artigos, não sendo, portanto, um artigo publicado no WIT. Ele aborda a história do Programa Meninas Digitais (PMD) e foi usado por muitos artigos como o referencial de base para os projetos parceiros do PMD, sendo a primeira publicação que aborda o programa em língua portuguesa.

Dentre os artigos com mais prestígio, somente um foi publicado no WIT (posição 5). Este artigo aborda o relato de experiência de um projeto que ganhou projeção nacional pelas ações realizadas e premiações conquistadas. Observa-se também que dois artigos publicados no periódico Cadernos Pagu figuram nas lista dos mais prestigiados (posição 2 e 4). O periódico Cadernos Pagu iniciou em 1993 e desde então vem contribuindo para a constituição do campo de estudos de gênero no Brasil. E um veículo do Núcleo de Estudos de Gênero da Unicamp, cujo objetivo é contribuir para a ampliação e o fortalecimento do

campo interdisciplinar de estudos de gênero. O aparecimento da referência ao Programa Meninas Digitais (PMD) (posição 6) não é uma surpresa, uma vez que a chamada de trabalhos do evento teve como principal motivação a existência de um espaço para que os projetos parceiros do PMD pudessem divulgar suas ações e resultados.

Tabela 2. Artigos com maior prestígio

|Posição|Referência do artigo|Prestígio de Grau|
|---|---|---|
|1|Maciel,C., Bim, S. A. (2016) “Programa Meninas Digitais – Ações para divulgar a computação para meninas do ensino médio”, In: Computer on the Beach, 2016, Itajaí – SC. Anais do Computer on the Beach. p. 327-336.|34|
|2|Maia, M. M. (2016). Limites de gênero e presença feminina nos cursos superiores brasileiros do campo da computação. Cadernos Pagu, (46),223-244.|15|
|3|Oliveira, A., Moro, M., Prates, R. (2014) “Perfil Feminino em Computação: Análise Inicial”. Anais do XXII Workshopsobre Educação em Computação,Brasília.|14|
|4|Schwartz, J., Casagrande, L. S., Leszczynski, S. A. C., e Carvalho, M. G. (2006) “Mulheres na informática: quais foram aspioneiras?”,Cadernos Pagu, (27),255-278.|11|
|5|Lauschner, T. et al. (2016). “Cunhantã Digital: programa de incentivo à participação de mulheres da região amazônica na Computação e áreas afins”. In XXXVI Congresso da Sociedade Brasileira de Computação 2016,Porto Alegre, p2656-2660.|10|
|6|SBC (2017). Programa Meninas Digitais da Sociedade Brasileira de Computação. Disponível em_<http://meninasdigitais.sbc.org.br/>.|10|
|7|Santos, C.M., (2018). “Por que as mulheres “desapareceram” dos cursos de computação?” In: Jornal da USP. Publicado em: 7 de março de 2018.|10|

Os três artigos com maior prestígio de grau são também os artigos com maior prestígio de proximidade, com 0,27, 0,19 e 0,12 respectivamente (valores normalizados onde o valor máximo é 1.0). Isso significa que são os mais próximos àqueles que o citaram, assim como àqueles que citaram àqueles que o citaram e assim por diante (domínio de influência). Esses graus de proximidade reforçam a influência desses artigos na estrutura de conhecimento denotada pela rede de citação.

O mesmo ocorre com o prestígio de _rank, com os três artigos de maior prestígio de grau possuindo também os maiores prestígios de rank, com 1.0, 0,47 e 0,28 respectivamente. Destaca-se que essa medida considera também o prestígio dos artigos ligados direta e indiretamente ao artigo em questão. Se muitos artigos de prestígio escolhem (citam) um artigo, então isso deve ter mais peso do que se muitos artigos sem prestígio citassem um artigo.

## 5. Considerações Finais

Considerando os objetivos desta pesquisa, foram identificados os artigos que mais influenciaram os artigos publicados no WIT, os principais indicadores bibliométricos relacionados às citações e a estrutura em rede que denota o fluxo de conhecimento do evento.

O artigo que aborda a história e motivação de criação do Programa Meninas Digitais (PMD) é o que possui o maior prestígio dentre os artigos citados no WIT. Esse resultado é consequência da relevância do artigo para muitos autores que publicaram no evento, uma vez que o PMD foi uma iniciativa pioneira em divulgar a área de Computação para estudantes mulheres e que engajou muitos projetos parceiros nesse objetivo.

Os indicadores gerais revelam principalmente que os autores de artigos do WIT citam mais frequentemente trabalhos publicados em eventos, sendo o próprio WIT um dos eventos mais citados; o período das publicações citadas apresenta um crescimento exponencial na década de 2000 e essas foram escritas predominantemente em língua portuguesa. A análise temática revela que um pouco mais da metade do artigos citados são do tipo Relato de Experiências e que a outra metade são artigos de Pesquisa.

Já os indicadores da rede de citação mostram a existência de uma rede fracamente conectada, evidenciando uma diversidade nas escolhas dos artigos citados. A análise dos componentes isolados propiciou identificar temáticas que são pertinentes ao evento, mas com temas que fazem um recorte específico e que ainda parecem ser pouco explorados.

De uma forma geral, entende-se que os resultados deste estudo forneçam subsídios iniciais para entender o fluxo de conhecimento envolvido no evento. Por consequência, podem permitir, tanto por parte da organização do evento e pelos próprios autores de artigos que citam e são citados, a tomada de decisões variadas. Por exemplo, a identificação de artigos aderentes a temática do evento, mas que possuem pouca ou nenhuma relação a literatura científica do evento, permite: a)explorar novos direcionamentos para os projetos parceiros do Programa Meninas Digitais; b) promover a interdisciplinaridade (troca de conhecimentos) entre grupos/comunidades diferentes que podem contribuir com a temática e que não sejam especificamente da Computação. Outro exemplo é a identificação de autores de artigos influentes, para a colaboração científica, dentre outras possibilidades.

Como ameaça à validade deste trabalho destaca-se a contagem manual de alguns indicadores, que apesar de ter passado por um processo de revisão em várias etapas, pode estar sujeitos a erros. Por outro lado, todo o processo de extração dos dados foi documentado e disponibilizado de forma a propiciar a proveniência dos dados. Recomenda-se interpretar os resultados de prestígio com a devida cautela uma vez que artigos mais antigos têm uma probabilidade maior de serem citados por existirem há mais tempo.
