# Mapeamento dos Indices da Desigualdade de Gênero por Unidade da Federação no Brasil

Ana Carolina Cebin Pereira, Karin Satie Komati

1Bacharelado em Sistemas de Informação

2Programa de Pós-graduação em Computação Aplicada (PPComp) Instituto Federal do Espírito Santo (Ifes), Campus Serra, Rodovia ES-010, Km 6,5, Manguinhos, Serra-ES

carolcebin@gmail.com, kkomati@ifes.edu.br

Abstract. Quantitative indicators to measure the gender gap between women and men is an initiative undertaken by international organizations such as the UN and the WEF. Although these indices are multidimensional, in the end, a single value represents one entire country. There are Brazilian proposals for indices to assess gender inequality in each federation unit, such as the INDG and the IMDG. The objective of this work is to develop a website with a choropleth map of the INDG and IMDG indices.

Resumo. Medir quantitativamente o quão desigual é a situação das mulheres em relação aos homens é uma iniciativa empreendida por organizações internacionais, tais como a ONU e o FEM. Embora os índices sejam multidimensionais, ao final, é gerado um único valor para o país inteiro. Há propostas brasileiras de índices de avaliação da desigualdade de gênero por unidade da federação, tais como o INDG e o IMDG. O objetivo deste trabalho é desenvolver um site com um mapa coroplético dos índices INDG e o IMDG.

## 1. Introdução

A igualdade entre homens e mulheres é uma das condições para que o crescimento sustentável de um país se torne realidade e é importante a disponibilização de dados públicos de fontes seguras para que exista difusão de informação. No início da década de 1980, os indicadores econômicos ganham espaço nos debates econômicos mundiais, que discutiam o impacto que as decisões políticas tinham sobre os níveis de pobreza [Carrasco 2012]. Mas foi apenas em 1995, que a ONU introduziu duas novas medidas que consideravam o sexo como uma de suas variáveis no “Relatório de Desenvolvimento Humano”: o GDI (do inglês Gender-related Development Index ) e o GEM (do inglês Gender Empowerment Measure ). No entanto, ambos os índices receberam muitas críticas por não estarem capturando da melhor forma as disparidades por gênero [Bardhan and Klasen 1999].

A UNDP ( United Nations Development Program ) introduziu o GII (do inglês Gender Inequality Index ) no Relatório de Desenvolvimento Humano de 2010. O novo índice é uma medida composta que captura a perda de desempenho devido à desigualdade de gênero usando três dimensões: saúde reprodutiva, empoderamento e participação no mercado de trabalho. O GII não inclui os níveis de renda como componente, que foi um

1https://hdr.undp.org/en/faq-page/gender-inequality-index-gii

dos componentes mais controversos do GDI e do GEM. Também não permite que altos valores em uma dimensão possam compensar um baixo desempenho em outra. Outro índice global e amplamente divulgado de disparidades de gênero é o GGGI (do inglês Global Gender Gap Index ) [WEF 2021], publicado no Global Gender Gap Report. O índice foi introduzido pelo Fórum Econômico Mundial (WEF, do inglês World Economic Forum ) em 2006 e é publicada anualmente desde então.

No entanto, todos os índices globais citados medem um país inteiro. O Brasil é um país continental e existem diferenças entre as várias unidades da federação. Assim, neste trabalho são consideradas duas propostas brasileiras para índices por unidades da federação: o INDG [Cardoso 2012] e o IMDG [Lima et al. 2015]. O objetivo deste trabalho é desenvolver um protótipo de um site com um mapa interativo que mostre os índices INDG e IMDG, de desigualdade de gênero, por unidade da federação. Utilizamos o mapa do tipo coropleto, também conhecido como mapa coroplético, que são mapas que permitem conhecer uma variável usando diferentes cores ou tonalidades em uma determinada região. E uma representação de um mapa temático com uma escala que representa a pro- porcionalidade da variável estatística, que nesse caso são representados pelos índices de desigualdades. Desta forma, espera-se prover uma forma visual rápida, facilitando a compreensão de índices estatísticos complexos para pessoas leigas, além de tornar o acesso aos dados de forma pública e online.

O restante do artigo está dividido em quatro seções. A Seção 2 apresenta os índices INDG e IMDG, de forma mais detalhada. A Seção 3 apresenta os materiais e métodos usados, a Seção 4 apresenta as telas do site com os mapas e a Seção 5 finaliza o artigo com as considerações finais.

## 2. Indices Brasileiros por Unidades da Federação

Esta seção apresenta as propostas dos índices nacionais de desigualdade de gênero por unidade da federação: o INDG [Cardoso 2012] e o IMDG [Lima et al. 2015].

O INDG é uma proposta de Luísa Cardoso Guedes de Souza, na época aluna de graduação da UnB, que foi premiado pelo Conselho Regional de Economia do Distrito Federal (Corecon-DF) em 2012 [CorreioBraziliense 2012]. Luísa propõe a criação do Índice Nacional de Desigualdade de Gênero (INDG) por estado, baseado no GGGI. O GGGI leva em conta quatro critérios, que variam de 0 a 1, sendo 1 indicando que há paridade entre os sexos: (i) diferenças salariais e participação no mercado de trabalho; (ii) acesso à educação e nível de formação educacional; (iii) acesso à saúde e queda de índices de mortalidade; e (iv) participação política e posição em cargos de poder político. O Brasil, em 2021, ficou na posição 93 (dentre 156 países), considerando que em 2006 estava na 67ª posição (dentre 107 países). Em “saúde e sobrevivência” o valor é de 0,98 (1ª posição), tanto em 2006 quanto em 2020, graças ao atendimento público e universal do SUS. A educação melhorou de 0,972 (2006) para 1,0 (2021), saindo da posição 74 para a 37, graças ao ensino que não faz distinção de gênero, público e de excelência existente no Brasil. A dimensão de “Oportunidade e participação econômica” melhorou no valor índice de 0,604 para 0,665, mas caiu na posição no rank, de 63ª para 89ª. O “Empoderamento político” que era de 0,061 (posição 86 em 2006) foi para 0,138 (posição 108 em 2021), uma piora. Cada uma das dimensões é subdividida em várias variáveis com uma metodologia de cálculo associado.

Assim como o GGGI, o INDG é composto por quatro dimensões – economia, educação, política e saúde. A diferença da proposta do INDG é a identificação de fontes de dados nacionais, as dimensões de educação e economia são calculados a partir dos dados governamentais do Pesquisa Nacional por Amostra de Domicílios (PNAD) [IBGE 2022], que são de acesso público. Já saúde é calculado com base nos dados da “Síntese de Indicadores Sociais” de 2010 [IBGE 2010] e “Séries estatísticas e séries históricas”, ambos do IBGE. Quanto à politica, ela usou dados dos sites das várias unidades da federação.

No índice associado à política, área com os menores índices do Brasil, o país teria pontuação com INDG de 0,102. O estado de Santa Catarina aparece mais uma vez em última posição (0,035) e o primeiro lugar também se repete, Rio Grande do Norte (0,404), na época, o RN tinha 2.013 homens e 292 mulheres no poder. No mercado de trabalho, os homens ocupavam cerca de 54,4 milhões de posições no mercado de trabalho, enquanto as mulheres ocupavam 43 milhões. Em média, os homens ganhavam R$ 4,9 por hora a mais que as mulheres em cargos semelhantes.

Posteriormente, em 2016, o trabalho de [Bortoluzzo et al. 2016] usou a metodologia de cálculo de Luísa, com diferenças na dimensão de política. Primeiro, os dados foram coletados de um único site, do Tribunal Superior Eleitoral (TSE), e ao invés de calcular a razão do número de mulheres que ocupam cargos eleitos no congresso nacional com relação ao número de homens, foi considerada a razão do percentual de mulheres eleitas com relação ao número de candidatas sobre o percentual de homens eleitos com relação ao número de candidatos, o que revela a preferência do eleitor também com relação ao gênero.

O trabalho de Lima et al. [Lima et al. 2015] optou pela construção de um índice sintético nomeado de Indice Multidimensional de Desigualdade de Gênero (IMDG). O IMDG é composto por indicadores distribuídos em seis dimensões: educação, renda, trabalho, política, saúde reprodutiva e fatores de proteção. Foram usados dados do Censo Demográfico 2010 do IBGE, do PNAD de 2009, do TSE de 2010, DataSUS de 2010 e dados Diretoria de Pesquisas, Coordenação de População e Indicadores Sociais de 2010 do IBGE (este último foi usado para avaliar a esperança de vida ao nascer). O trabalho concluiu que as unidades federativas apresentam, em geral, os mesmos fatores de desigualdade de gênero, sendo os mais intensos verificados nos âmbitos político, doméstico e atividades econômicas, o que as diferencia é a intensidade com que cada fator se manifesta. Uma análise integrada das dimensões mostra que as mulheres têm maior escolaridade que os homens, mas ainda têm menos chances de emprego formal, menores rendimentos médios e fraca participação na política.

## 3. Materiais e Métodos

Como a proposta do trabalho foi a geração de um mapa interativo, seu desenvolvimento foi realizado em um sistema web em Laravel ( Framework PHP). A decisão por esta ferramenta foi por ser de uso gratuito e em linguagem de uso popular. Em relação à base de dados, escolhemos utilizar um sistema de banco de dados relacional open-source, o PostgreSQL. O modelo é apresentado na Figura 1, em que uma região (regions) é composta por vários estados (states); podem ser cadastrados vários índices (indexes), e cada

> 2https://seriesestatisticas.ibge.gov.br/

> 3https://laravel.com/

índice tem um valor (value) associado a um estado (state ~~i~~ ndexes). Cada estado tem como atributos: o nome (name) e sua sigla (uf).

Figura 1. Modelo relacional da base de dados.

Para popular a base de dados, foi usada uma ferramenta de ETL, o Pentaho. A entrada de dados é uma planilha, onde se existe uma relação entre o estado e o valor de um determinado índice. Assim, é possível que novos índices sejam adicionados, sem a necessidade de compreensão da linguagem SQL. Para a geração dos mapas, foi usado a D3.js, que é uma biblioteca JavaScript de código livre para produzir visualizações de dados interativas e dinâmicas em navegadores da web. O site está no endereço https: //mapa-desigualdade-genero.herokuapp.com/.

## 4. Resultados

Os mapas gerados são apresentados na Figura 2 e na Figura 3, do INDG e do IMDG, respectivamente. A planilha de entrada foram os dados originais dos índices. Nos mapas, há a indicação da escala de valores pela tonalidade da cor vermelha. Como os valores dos índices são próximos, a escala tem como limite inferior o menor valor do índice que está sendo apresentado e como limite superior, o maior valor do índice. Assim, a diferença de cor entre os estados é mais perceptível visualmente quando comparado a uma faixa de valores entre 0 e 1.

Pelo INDG (Figura 2), em 2009, o Brasil obteve 0,71 pontos no geral, conforme trabalho original do INDG. Santa Catarina (0,676), aparece como o estado mais desigual, enquanto Rio Grande do Norte (0,779), como o estado com maior igualdade de acesso. O resultado do trabalho original [Cardoso 2012] mostra que a desigualdade não está ligada a uma menor renda, já que o Rio Grande do Norte tem quase metade (R$ 456,94) da renda per capita de Santa Catarina (R$ 864,51).

O mapa do IMDG apresenta os dados do trabalho original, onde os estados das regiões Sudeste, Centro Oeste e Nordeste estão entre os mais desiguais (Goiás com 0,1566, Minas Gerais com 0,13 e Pernambuco com 0,1298) e os estados do Amapá (0,0373) e Piauí (0,0433) como os mais iguais. Estados das regiões Sudeste, Centro Oeste e Nordeste estão entre os mais desiguais (Goiás com 0,1566, Minas Gerais com 0,13 e Pernambuco com 0,1298) e os estados do Amapá (0,0373) e Piauí (0,0433) como os mais iguais.

> 4https://www.hitachivantara.com/en-us/products/data-management-analytics/ pentaho.html

> 5https://d3js.org/

Figura 2. Tela do sistema com o mapa coroplético do INDG.

Figura 3. Tela do sistema com o mapa coroplético do IMDG.

É interessante observar que índices diferentes resultam em análises e resultados diferentes. As unidades da federação consideradas mais iguais ou mais desiguais foram diferentes conforme o índice avaliado.

## 5. Considerações Finais

Ao final, considera-se que o objetivo de se ter um protótipo de um site com mapas coropléticos que mostram os diferentes índices de desigualdade de gênero por unidade da federação foi alcançado. Para tal, foi necessário compreender as duas propostas nacionais de índices de desigualdade de gênero por unidade da federação, o INDG e o IMDG, bem como o índices globais de desigualdade GGGI em que o INDG foi baseado. Como trabalhos futuros de curto prazo, avaliamos melhorar a interface com o usuário, incluir dados dos índices atualizados por ano, pois foram usados os dados originais do trabalhos que propuseram os índices, incluir mais índices de desigualdade de gênero por unidade da federação, tais como os índices os índices IDS-gen e IDG [Soares 2016]. Como trabalho futuro de longo prazo, a ideia é ampliar o sistema para um framework mais amplo que possa integrar dados com o Mapa de Violência da Mulher, e o mapa dos projetos parceiros das Meninas Digitais, além de fazer parcerias para que os dados possam ser atualizados e mantidos.

> 6https://mapadaviolenciadegenero.com.br/

> 7https://meninas.sbc.org.br/projetos/mapa/

## 6. Agradecimentos

Os autores agradecem ao Ifes pela bolsa de iniciação científica da Ana Carolina. A profª Karin Komati agradece ao CNPq pela Bolsa de Produtividade DT-2 (308432/2020-7) e à FAPES pela concessão de Auxílio Taxa de Pesquisa (nº FAPES 293/2021).
