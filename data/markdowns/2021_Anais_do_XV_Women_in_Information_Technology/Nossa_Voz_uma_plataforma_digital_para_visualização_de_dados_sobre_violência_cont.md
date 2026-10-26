# Nossa Voz: uma plataforma digital para visualização de dados sobre violência contra a mulher no Brasil

Dynnah Hanna Max P. G. da Silva, Alana Marques de Morais, Aline Marques de Morais

1Instituto Federal de Educação, Ciência e Tecnologia da Paraíba - Campus João Pessoa

(IFPB)

2UNIESP Centro Universitário – Cabedelo-Paraíba

`dynnah.silva@academico.ifpb.edu.br, {alanamm.prof,`

àlinemm.prof}@gmail.com`

Abstract. Brazil fights against a huge challenge when we mention gender inequality. It is noticeable that some figures released by violence monitoring surveys become alarming. Therefore, this article aims to present results of the development of a system that allows a more intuitive visualization of data from open databases on the problematic violence against women in Brazil, giving a special focus to the state of Paraíba.

Resumo. O Brasil enfrenta um grande desafio quando colocamos em evidência a desigualdade de gênero e é perceptível que alguns números divulgados por pesquisas de monitoramento de violência se tornam alarmantes. Sendo assim, este artigo procura apresentar resultados do desenvolvimento de uma plataforma que permite uma visualização mais intuitiva dos dados de bases abertas sobre a problemática violência contra a mulher no Brasil, dando um enfoque especial ao estado da Paraíba.

## 1. Introdução

A violência é um fenômeno social que atinge indivíduos e populações, tanto global quanto localmente, no público e no privado, estando seu conceito em constante mutação, uma vez que várias atitudes e comportamentos passaram a ser considerados como formas de violência ao longo dos anos [JESUS, 2014]. De acordo com a Convenção de Belém do Pará [1994], define-se como violência contra a mulher qualquer conduta, de ação ou omissão, baseada no gênero, que cause morte, dano ou sofrimento físico, sexual ou psicológico à mulher, no âmbito público ou privado

Dados da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD) de 2018 [IBGE, 2020] apontam que as mulheres representam 51,7% dos brasileiros. Mesmo com um percentual quantitativo maior, as mulheres são consideradas minoria e por isso, existem consequências claras de como a violência contra a mulher reflete na persona feminina para a sociedade. Os dados de análise muitas vezes são desencontrados e nem sempre atualizados. Outro desafio é lidar com a subnotificação causada por uma espécie de "pacto de silêncio", pelo qual as mulheres vítimas da violência não denunciam, e algumas vezes até mesmo protegem seus agressores. No sentido de entender melhor os dados ou minerar melhor as informações já catalogadas, a Computação é uma grande aliada nesta interpretação.

Desse modo, o presente artigo discute os resultados do planejamento e desenvolvimento de uma plataforma online que tem como objetivo apresentar de forma mais intuitiva o panorama geral sobre violência contra a mulher no Brasil e na Paraíba.

## 2. Referencial Teórico

O Women in Information Technology (WIT), que é uma iniciativa da Sociedade Brasileira de Computação (SBC) para discutir os assuntos relacionados a questões de gênero e a Tecnologia de Informação já destacou em edições anteriores uma série de trabalhos que lidam com análises e soluções para a problemática da violência contra a mulher sob diversas perspectivas, entre elas: assédios no transporte público [DE MOURA e DE MELO, 2017], os machismos diários [MARINO et. al, 2017] e aplicações para defesa de mulheres em situação de perigo [DE FREITAS et. al, 2020].

O presente trabalho tem o intuito de colaborar nesses esforços e construir uma ferramenta online que ajude a comunidade diante de uma temática tão complexa. Apesar de existirem algumas plataformas que exploram o tema, a maioria trabalha com relatórios estáticos e infográficos para discutir o assunto [LABCIDADE, 2021; MAPA DA VIOLÊNCIA CONTRA MULHER, 2021]. Um trabalho que faz uma análise interessante é o Mapa da Violência de Gênero [2021] da Fundação Alvina, mas ele se restringe aos dados de parte do país e não contém dados do estado da Paraíba, por exemplo.

Levando isso em consideração, o grupo conversou com membros da Polícia Civil do Estado da Paraíba e alguns integrantes de ONGs (Organizações Não-Governamentais) a fim de entender os desafios na coleta e análise de tais dados. Ambas as conversas destacaram que questões relacionadas ao sigilo das informações são muito mais sérias do que qualquer outro cenário de análise de dados, pois é possível com uma exposição inadequada colocar em risco a vida de mulheres.

Por isso, o presente estudo utilizou dados de diversos tipos de crimes contra a mulher. Assim, o projeto executou técnicas estatísticas para observação e análise dos resultados. Além disso, também foi empregado ao estudo a Ciência de Dados que agrupa a utilização de técnicas desenvolvidas a partir de máquinas de conhecimentos, reconhecimento de padrões, dados estatísticos, banco de dados e estratégias de visualização para que seja possível realizar a extração de conhecimentos relevantes a partir de grandes bases de dados [FÁVERO, 2015].

## 3. Metodologia

Considerando o objetivo do estudo, é possível classificar a presente pesquisa como exploratória, pois objetiva proporcionar maior familiaridade com o problema, tornandoa explícita ou construindo hipóteses sobre o problema. A abordagem de pesquisa adotada é Quali-quantitativa e os principais procedimentos técnicos utilizados nesta pesquisa são: Pesquisa Bibliográfica, Surveys, Estudo de Caso e Pesquisa Participante. Do ponto de vista de construção, o projeto foi desenvolvido de acordo com as etapas a seguir:

- de dados abertos que cumpriam com a necessidade do projeto. Foram utilizados dados do DATASUS e dados da Secretaria de Segurança do Estado da Paraíba.

- os dados foram acessados, pré-processados e tratados. Nesta etapa, foi iniciado a

aplicação da técnica de Data Analytics para filtrar aquilo que é considerado relevante para os objetivos da pesquisa.

- disponibilizada a visualização de dados para o público-alvo. É importante ressaltar que o objetivo não é só que a sociedade como um todo visualize os dados, mas que isso possa apontar direções para o governo e ONGs que façam trabalho voluntário para mulheres vítimas de violência.

- tipos de gráficos e indicadores, foi executada a construção dos painéis pela equipe. Durante essa etapa, o desenvolvimento foi dividido em front-end e back-end.

- nesta fase do desenvolvimento.

- testes e estudaram estratégias para disponibilizar gratuitamente a plataforma.

### 3.1 Base de Dados

A coleta de informações do estudo relacionadas ao panorama do Brasil foi obtida no site DATASUS, configurando como uma fonte secundária que, segundo Mattar et. al [2014], se caracteriza por disponibilizar dados para consulta após já ter ocorrido uma coleta, análise, tratamento e tabulação prévia. Os dados coletados contemplam os registros entre os anos de 2009 e 2018. Já para a coleta de informações relacionadas ao estado da Paraíba, foi obtida por meio de uma parceria com a Secretaria de Segurança do Estado da Paraíba dados que já representam um panorama da pandemia e do ano de 2020.

### 3.2 Ferramentas

A plataforma proposta tem o objetivo de ser acessível por meio de uma aplicação web e relatar os casos de violência e a gravidade desse assunto com implementações usando tecnologias Node.js para o back-end e React.js para o front-end.

## 4. Resultados

Após a etapa de análises das bases de dados abertas e seleção de quais informações seriam pertinentes para serem exibidas ao usuário final, o resultado foi a plataforma online denominada “Nossa Voz”, cujo principal intuito é evidenciar e esclarecer dados de violência contra a mulher no Brasil. A interface principal da plataforma é ilustrada pela Figura 1. O nome da plataforma foi escolhido baseado em uma discussão que envolvia o fato de que quando mulheres se unem em prol de algo (principalmente atualmente com denúncias sendo expostas em rede social), existe um maior alcance e visibilidade. A plataforma pode ser acessada gratuitamente pelo endereço <u>https://nossavoz.netlify.app/.</u>

As seções introdutórias da ferramenta têm o propósito de situar o usuário sobre a gravidade do problema descrito pelos gráficos. Os diferentes gráficos foram construídos para serem facilmente lidos e interpretados. Um exemplo dessa estratégia foi o uso de mapas como acontecem em outras iniciativas (Figura 2).

Os dados coletados foram categorizados em dois grandes grupos de análise, as análises nacionais e a análise do estado da Paraíba, pois a ferramenta pode ser útil para a Secretaria de Segurança da Paraíba, entre as análises se destacam: ocorrências dos tipos de violência, etnia mais afetada, agrupamento de casos por município (quando analisados os dados da

PB) e faixa etária mais afetada.

Figura 1. Página inicial da plataforma

Figura 2. Dispersão dos casos

no território brasileiro

Durante a apresentação dos dados, alguns tipos de visualizações foram construídos, com a predominância dos gráficos de setores e histogramas. Um exemplo foi observado na seção “Ocorrências dos Tipos de Violência” em que foi definido que um gráfico de setor seria o mais adequado (Figura 3). Neste exemplo, de acordo com a interação do usuário com o gráfico, o tipo de violência e o quantitativo de casos vai se modificando. Por outro lado, a Figura 4 exibe um outro tipo de gráfico muito utilizado em estudos comparativos e pode ser útil para análises globais entre estados do Brasil ou cidades da Paraíba.

Figura 3. Exemplo de gráfico de setor

Figura 4. Exemplo de histograma

Com relação aos dados analisados, alguns panoramas merecem destaque, por exemplo, o número de casos de violência contra mulher só na cidade de João Pessoa-PB em 2020 (1253 casos) foi maior do que a média de casos registrados no estado entre 2009 e 2018 (859 casos), de acordo com os dados do DATASUS.

Segundo os dados, o tipo de violência predominante é a física seguida da psicológica. Além disso, não há uma etnia em que os casos sejam mais concentrados no Brasil. Outro ponto interessante de mencionar é que os casos de violência na Paraíba são mais corriqueiros em mulheres abaixo dos 45 anos. Uma razão pode estar relacionada às denúncias feitas por mulheres mais jovens.

## 5. Considerações Finais

Apesar da relevância do assunto discutido e identificado, é possível perceber, por meio dos dados obtidos, a diferença em como o assunto era tratado em anos anteriores para a atualidade. Educar e elucidar sobre a temática traz luz a uma sociedade com preconceitos ainda enraizados, esses mesmos preconceitos inclusive dificultam denúncias e andamento em casos de violência.

Como próximas etapas, o trabalho pretende inserir dentro da ferramenta uma opção de denúncia, como também parcerias diretas com ONGs e talvez com a secretaria de segurança do estado da Paraíba. Além disso, é planejado a inclusão de gráficos que se alimentem de modelos de Aprendizado de Máquina para predizer panoramas para que ONGs e Estado possam traçar ações. Além disso, o trabalho pretende realizar uma análise de usabilidade da ferramenta, pois a ferramenta precisa ser clara e intuitiva.
