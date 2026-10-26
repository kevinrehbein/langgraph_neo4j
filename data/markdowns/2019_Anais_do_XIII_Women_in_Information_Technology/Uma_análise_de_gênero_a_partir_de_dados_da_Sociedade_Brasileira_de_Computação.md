# Uma análise de gênero a partir de dados da Sociedade Brasileira de Computação

Karen da Silva Figueiredo Medeiros Ribeiro, Jéssica Azevedo, Cristiano Maciel, Sílvia Amélia Bim

Instituto de Computação¹ e Instituto de Engenharia² – UFMT, Mato Grosso, Brasil

Departamento Acadêmico de Informática³ – UTFPR, Paraná, Brasil

`karen@ic.ufmt.br, jessicaknazevedo@gmail.com, cmaciel@ufmt.br, sabim@utfpr.edu.br`

- Abstract. The Brazilian Society of Computing (SBC) is the main scientific society which brings together students, professors, researchers, professionals and enthusiasts of Computing from Brazil. Then, the present paper aims to present a quantitative analysis of the SBC members, according to their gender, location, type of association and areas of interest in Computing, in order to delineate a national panorama.

- Resumo. A Sociedade Brasileira de Computação (SBC) é uma sociedade científica que reúne estudantes, professores, pesquisadores, profissionais e entusiastas da área de Computação do Brasil. Por se tratar da principal instituição civil que representa a área no país, este artigo tem como objetivo realizar uma análise quantitativa a partir dos dados das pessoas associadas à SBC, segundo gênero, localização, categoria de associação e áreas de interesse na Computação, a fim de traçar um panorama atual da Computação no país.

## 1. Introdução

É impossível não pensar em disponibilidade de dados quando realizamos pesquisas com recorte de gênero. Mesmo a respeito de um tema que é discutido há alguns anos, como a equidade de gênero na Computação, os dados disponíveis sobre o assunto ainda são insuficientes, principalmente no cenário nacional.

Alguns países como Estados Unidos ( National Center for Women & Information Technology ), Reino Unido ( The Women in Tech Council ) e Canadá ( Society for Canadian Women In Science and Technology ) possuem programas que reúnem dados sobre mulheres que trabalham no setor de tecnologia. Entretanto, essa ainda não é a realidade brasileira.

No Brasil, além dos dados de gênero no Ensino Superior divulgados anualmente pelo INEP e compilados para a área de Computação pela Sociedade Brasileira de Computação (SBC); o cenário nacional depende de fontes de pesquisas realizadas isoladamente, como o trabalho de Valentova et al. (2017) que analisa dados do CNPq ou de instituições, e de relatórios de organizações, como o divulgado pela UNESCO em

> 1 www.ncwit.org, www.techuk.org/focus/programmes/women-in-tech, www.scwist.ca

> 2 http://www.sbc.org.br/documentos-da-sbc/category/133-estatisticas

### 2018 sobre o número de mulheres que atuam em programação no Brasil.

A fim de contribuir com o corpo de pesquisas que analisam este tipo de dado no país, este artigo tem como objetivo realizar uma análise quantitativa a partir dos dados das pessoas associadas à SBC com ênfase em gênero, investigando as seguintes categorias: localização, tipo de associação e áreas de interesse na Computação.

A SBC é uma sociedade científica e sem fins lucrativos que reúne estudantes, professores, pesquisadores, profissionais e entusiastas da área de Computação do Brasil. Por se tratar da principal instituição civil que representa a área no país, pretende-se com esta pesquisa, aumentar a compreensão sobre o panorama atual de mulheres que atuam na área. A partir da seção atual, este trabalho divide-se em seções segundo a metodologia da pesquisa, os resultados da análise dos dados e as conclusões.

## 2. Metodologia

Todas as pessoas e instituições associadas à SBC, ao realizarem sua inscrição, devem preencher dados referentes à identificação, localização e de suas áreas de interesse na Computação. Tais dados são armazenados pela SBC para controles administrativos e estatísticos internos. Para a execução desta pesquisa, solicitou-se para a SBC em novembro de 2018 alguns dados referentes ao perfil, localização e interesses de associados e associadas. Foram então disponibilizados dados contendo nome, gênero, estado, categoria de associação e áreas de interesses de 6964 pessoas e instituições sócias, na ocasião. A partir dos dados deste arquivo, foram realizados alguns tratamentos para a análise da presente pesquisa.

As categorias de associação na SBC são: “fundador”, “efetivo”, “honorário”, “estudante” e “institucional”, sendo a última a única categoria aplicada para instituições e não pessoas. Assim, a primeira etapa do tratamento consistiu em definir o dado gênero como “não identificado” para registros da categoria “institucional”.

A segunda etapa consistiu em atribuir o gênero como “feminino” e “masculino”, quando possível, para pessoas associadas nas categorias “fundador”, “efetivo” e “estudante”. Não havia integrantes na categoria honorário e as demais categorias não possuíam dados relativos ao gênero. Para tanto, foi realizado um cruzamento dos dados de nome com perfis nas plataformas Lattes e Researchgate. Optou-se ainda por eliminar um registro de usuário que não possuía o dado de estado, a título de localização.

Tabela 1. Dados Pré e Pós Tratamento

||Feminino (F)|Masculino (M)|Não identificado|Sem informações|Total de registros|
|---|---|---|---|---|---|
|Dados brutos|1467|5280|68|149|6964|
|Dados tratados|1509|5390|64|0|6963|

Os totais de registros por gênero nas etapas de pré e pós tratamentos podem ser visualizados na Tabela 1. Os dados tratados foram analisados quantitativamente, e os resultados são apresentados na seção a seguir.

> 3 https://epocanegocios.globo.com/Economia/noticia/2018/02/apenas-17-dos-programadores-brasileiros - sao-mulheres.html, http://www.unesco.org/new/pt/brasilia/about-this-office/single-view/news/the_inclu sion_of_women_in_science_and_technology_is_the_subj/

> 4 Acesse http://tiny.cc/lf3o6y para obter os dados da SBC completos utilizados nesta pesquisa.

## 3. Análise

Do total de registros da análise, 77,71% são do gênero “masculino”, seguidos por 21,67% do gênero “feminino” e por fim 0.92% de associados institucionais. Considerando somente os registros de pessoas, 78,13% são do gênero “masculino”, seguidos por 21,87% de registros do gênero “feminino”.

A Tabela 2 apresenta os dados de gênero por categoria. A categoria “estudante” compreende estudantes de graduação, pós-graduação, curso técnico, entre outros, sendo esta categoria atribuída a maior parte dos registros, aproximadamente 70,08%. Destas, aproximadamente 21,0% são do gênero feminino, superando os dados mais atuais de 13,95% estudantes do gênero feminino no ensino superior em computação no Brasil [SBC 2017]. A categoria com maior proporcionalidade de pessoas do gênero feminino é a categoria “efetivo”, que compreende todas as pessoas atuantes profissionalmente em Computação ou área afim. E a categoria com menor proporcionalidade do gênero feminino é a categoria “fundador”, que compreende as pessoas que assinaram a ata da assembleia de fundação da SBC ou se inscreveram em até 90 dias após a assembleia e mantém sua associação ativa.

Tabela 2. Categoria de Associação x Gênero

|Categoria|Feminino (F)|Masculino (M)|Razão F/M|Total|
|---|---|---|---|---|
|Efetivo|492|1552|0,317|2044|
|Fundador|2|18|0,111|20|
|Estudante|1015|3820|0,266|4835|
|Total|1509|5390|0,280|6899|

A SBC pré-define 29 áreas de interesse em Computação a serem declaradas por seus associados e associadas no momento da filiação. Estas áreas têm relação direta com as 27 Comissões Especiais da SBC com adição dos interesses "Computação Ubíqua e Pervasiva" e " International Association for Pattern Recognition (IAPR)". As pessoas associadas podem declarar quantos interesses desejarem, podendo inclusive declarar interesse em todas as áreas ou em nenhuma delas.

A Tabela 3 apresenta a distribuição por gênero da quantidade de interesses declarados. Das 6899 pessoas associadas, 3283 (47.58%) não declararam interesse algum e 82 pessoas (1.18%) declararam interesse em todas as áreas. Nota-se que não há diferença significativa na proporção de mulheres que não declararam interesses ou selecionaram todas as áreas.

Tabela 3. Interesses Declarados x Gênero

||Feminino (F)|Masculino (M)|Razão F/M|Total|
|---|---|---|---|---|
|Nenhum interesse|707|2576|0,275|3283|
|Um ou mais interesses|782|2752|0,284|3534|
|Todos os interesses|20|62|0,323|82|
|Total|1509|5390|0,280|6899|

Para analisar as áreas de interesse segundo o gênero, foram calculadas além dos totais, as porcentagens por gênero de pessoas interessadas em cada área e a razão “feminino” / “masculino” de pessoas para cada área. A Tabela 4 apresenta um ranking com as 10 áreas de maior interesse geral. Se considerarmos a distribuição de pessoas associadas do gênero “feminino” e “masculino” pelas áreas de interesse, não

encontramos diferenças significativas. Este fato demonstra que há equilíbrio de gênero nos interesses demonstrados pelos conjuntos de homens e mulheres.

Tabela 4. Ranking de Áreas de Interesses x Gênero

|#|Área de Interesse|Geral|F|M|%F (1509)|%M (5390)|Razão F/M|
|---|---|---|---|---|---|---|---|
|1ª|Inteligência Artificial|1827|370|1457|24,5%|27,0%|0,254|
|2ª|Engenharia de Software|1539|371|1168|24,6%|21,7%|0,318|
|3ª|Informática na Educação|1499|433|1066|28,7%|19,8%|0,406|
|4ª|Linguagens de Programação|1429|270|1159|17,9%|21,5%|0,233|
|5ª|Sistemas de Informação|1384|339|1045|22,5%|19,4%|0,324|
|6ª|Banco de Dados|1247|279|968|18,5%|18,0%|0,288|
|7ª|Redes de Comp. e Sist. Distribuídos|1238|198|1040|13,1%|19,3%|0,190|
|8ª|Inteligência Computacional|1186|219|967|14,5%|17,9%|0,226|
|9ª|Jogos e Entretenimento|1155|276|879|18,3%|16,3%|0,314|
|10ª|InteraçãoHumano Computador|1115|343|772|22,7%|14,3%|0,444|

Tabela 5. Proporção de Mulheres por Área de Interesse

||Área de Interesse|Razão F/M|
|---|---|---|
|T á|Arquitetura de Comp. e Processamento de Alto Desempenho|0,170|
|op 5 reas com |Sistemas Distribuídos|0,183|
|menor roorão de|Concepção de Circuitos Integrados|0,187|
|ppç mulheres|Redes de Comp. e Sistemas Distribuídos|0,190|
||Algoritmos, Combinatória e Otimização|0,208|
||Sistemas de Informação|0,324|
|Top 5 áreas com|Sistemas Multimídia e Hipermídia|0,371|
|maior proporção|Sistemas Colaborativos|0,377|
|de mulheres|Informática na Educação|0,406|
||InteraçãoHumano Computador|0,444|

Entretanto, quando olhamos para a razão “feminino”/“masculino” (ver Tabela 5), é possível notar que as áreas com a menor proporção de mulheres são áreas popularmente conhecidas como “ hard skills ”, enquanto as áreas com maior proporção de mulheres são conhecidas como “ soft skills ” [Hong 2016]. Para verificar se realmente estes resultados são significativos, foi executado o método ANOVA de fator único entre os grupos de maior e menor proporção de mulheres, no qual se alcançou os seguintes valores: f-ratio= 90,01856, p=0,000013. O resultado é significativo quando o valor p é menor que 0,05, ou seja, a diferença da proporção de mulheres nas áreas mais duras é bastante significativa com relação às áreas menos duras da Computação.

Por fim, para a análise da localização das pessoas associadas por gênero, agrupou-se os registros dos estados por região, os resultados são observados na Tabela 6. A região com a maior proporção de pessoas associadas do gênero “feminino” é a região Norte, enquanto há a menor proporção e mulheres no exterior e na região Sudeste do país. Já no quantitativo, nota-se que não há diferença significativa na distribuição por gênero de pessoas associadas à SBC.

> 5 Segundo o método ANOVA de fator único (valores: f-ratio= 0,28463, p=0,60021) o resultado é significativo quando o valor p é menor que 0,05.

> 6 Como no caso anterior, foi aplicado o método ANOVA (valores: f-ratio= 0, p=1).

Tabela 6. Região x Gênero

|Região do País|Feminino|Masculino|Geral|%F (1509)|%M (5390)|%Geral|Razão F/M|
|---|---|---|---|---|---|---|---|
|Sudeste|432|1776|2208|28,63%|32,95%|32%|0,243|
|Nordeste|401|1355|1756|26,57%|25,14%|25,5%|0,296|
|Sul|343|1195|1538|22,73%|22,17%|22,3%|0,287|
|Norte|181|550|731|11,99%|10,20%|10,6%|0,329|
|Centro Oeste|140|442|582|9,28%|8,20%|8,4%|0,317|
|Sem localização|10|59|69|0,66%|1,09%|1%|0,169|
|Exterior|2|13|15|0,13%|0,24%|0,2%|0,154|
|Total|1509|5390|6899|100%|100%|100%|0,280|

## 4. Conclusões

A disponibilização de dados tem sido uma estratégia de muitas organizações e iniciativas, uma vez que, para avançar como sociedade em determinadas áreas, formular projetos e identificar a necessidade de políticas públicas, faz-se necessário o uso de dados. A análise e divulgação dos dados deste artigo é de suma importância para o fomento de ações em prol da equidade de gênero na Computação no Brasil. O presente trabalho analisou sob a ótica de gênero os dados das pessoas associadas à SBC segundo a sua categoria de associação, áreas de interesse na Computação e localização. Dentre os achados, destaca-se o fato das pessoas associadas à SBC terem uma distribuição de gênero equilibrada por localização e áreas de interesse. Isto demonstra que a SBC mostra-se efetiva ao alcançar pessoas, independente do gênero. Também quebra o mito de que mulheres teriam uma disposição natural para interessarem-se mais por determinadas áreas, enquanto homens interessar-se-iam mais por outras. O fato da proporção de mulheres associadas ser maior nas soft skills e menor nas hard skills, denota que, apesar do interesse das mulheres ser equivalente aos interesses dos homens, outros fatores externos (e.g. ambiente, cultura etc.) acabam influenciando para que atuem ou direcionem seu foco à determinadas áreas. A hipótese da influência de fatores externos também vale para a proporção de mulheres por região do país, abrindo campo para investigação e novas pesquisas que considerem fatores culturais, econômicos, sociais etc. destas regiões. Ao permitir o uso de seus dados, sociedades científicas como a SBC, denotam transparência e responsabilidade social. Como sugestão para a própria SBC, seria interessante que o dado de gênero pudesse ser auto-declarável no momento do cadastro dos associados. Assim, seria possível mapear na comunidade não somente o sexo biológico, perpetuando o binarismo de gênero, mas a pluralidade da identidade de gênero de seus associados.
