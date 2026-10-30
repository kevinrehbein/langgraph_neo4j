# Análise da Participação Feminina nos Cursos de Nível Superior da área de Computação do IFPE

Ana Carolina Barbosa dos Santos, Ellen Patrícia Lopes de Santana, Viviane Cristina Oliveira Aureliano

Instituto Federal de Pernambuco – Campus Jaboatão dos Guararapes Jaboatão dos Guararapes – PE – Brasil

`{acbs6,epls}@discente.ifpe.edu.br,`

`viviane.aureliano@jaboatao.ifpe.edu.br,`

Abstract. Although Brazilian women generally have a higher level of education than men, they still represent a minority in enrollments and job positions in the field of Computing and Information Technology (IT). In this context, this study aims to understand female participation in higher education Computing programs at IFPE through the analysis of microdata from the Higher Education Census provided by INEP. The results indicate that, between 2009 and 2022, the number of female entrants, enrolled students, and graduates was lower than that of men. However, completion rates are low for both genders. It is hoped that this study will contribute to the development of institutional strategies to overcome the challenges identified.

Resumo. Embora as mulheres brasileiras apresentem, em média, um nível de instrução superior ao dos homens, elas ainda representam uma minoria nas matrículas e nas vagas de trabalho na área de Computação e Tecnologia da Informação e Comunicação (TIC). Nesse contexto, este estudo busca compreender a participação feminina nos cursos superiores de Computação do IFPE, por meio da análise dos microdados do Censo da Educação Superior disponibilizados pelo INEP. Os resultados indicam que, entre 2009 e 2022, o número de mulheres ingressantes, matriculadas e concluintes foi inferior ao dos homens. No entanto, as taxas de conclusão são baixas para ambos os gêneros. Espera-se que este trabalho contribua para se pensar em estratégias institucionais que possam superar os desafios encontrados.

## 1. Introdução

As mais recentes estatísticas apresentadas pelo Instituto Brasileiro de Geografia e Estatística (2024) mostram que as mulheres brasileiras possuem nível de instrução maior do que os homens. Na população de pessoas com 25 anos ou mais de idade, 21,3% do total de mulheres possui ensino superior completo em comparação com 16,8% do total de homens. Embora mais mulheres do que homens concluam o ensino superior, quando consideramos somente os cursos da área de Computação e Tecnologias da Informação e Comunicação (TIC) em 2022, as mulheres corresponderam a apenas 15% das concluintes nesses cursos.

Diversos estudos destacam a baixa participação feminina em cursos de Computação e TIC no Brasil e os desafios enfrentados pelas estudantes. Silva e Santos (2021) apontam fatores como preconceito e falta de apoio que impactam negativamente a trajetória acadêmica das mulheres em Engenharia da Computação. Pereira et al. (2021) identificam que, embora alunas de cursos técnicos em informática do Instituto Federal do Sudeste de Minas Gerais (IF Sudeste MG) demonstram afinidade com a área,

poucas optam por seguir no ensino superior. Além disso, no curso de Ciência da Computação da mesma instituição, apenas 14,25% dos ingressantes entre 2007 e 2019 eram mulheres, e menos da metade concluiu o curso. Cursino e Martinez (2021) analisaram o Censo da Educação Superior e observaram que a participação feminina nos cursos de tecnologia caiu de 20% para 15% entre 2009 e 2018. Preocupação que vem sendo levantada anteriormente quando Maia (2016) já alertava para a redução de 8% no número de concluintes mulheres entre 2000 e 2013, reforçando a tendência de queda na presença feminina na área.

Com tão poucas mulheres se formando nos cursos na área de Computação, não é de se surpreender que isso se reflita no mercado de trabalho, onde apenas 20% das vagas nas funções técnicas da área são ocupadas por mulheres (BRASSCOM, 2020). Ter um ambiente de trabalho mais diverso do ponto de vista de gênero traz algumas vantagens. Segundo Herring (2009), a diversidade de gênero no mercado de trabalho está associada ao aumento da receita de vendas, a um número maior de clientes e a maiores lucros.

Diante desse cenário, com o objetivo de analisar a participação feminina nos cursos superiores de Computação do Instituto Federal de Pernambuco (IFPE), utilizamos dados do Censo da Educação Superior, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Para consolidar e visualizar essas informações, empregamos o Power BI, ferramenta de Business Intelligence (BI) amplamente utilizada para análise de dados, que possibilita a criação de painéis interativos e relatórios dinâmicos ( dashboards ). A aplicação do Power BI permitiu explorar dados sobre ingressantes, matriculados e concluintes nos cursos de nível superior de Computação do IFPE, facilitando a identificação de padrões e tendências apresentados pelos dados.

Sendo assim, com este trabalho buscamos responder a seguinte questão de pesquisa: Como tem se dado a participação feminina discente nos cursos de nível superior de Computação do IFPE? Para responder essa questão, analisamos os microdados do Censo da Educação Superior disponibilizados pelo INEP no período compreendido entre 2009 e 2022 tendo o IFPE como foco de estudo. O restante do artigo foi organizado da seguinte maneira: na seção 2 é feita uma revisão da literatura sobre a participação feminina em cursos da área de Computação; na seção 3 é descrita a metodologia adotada no presente trabalho; na seção 4 são apresentados os resultados obtidos; e, por último, na seção 5 são apresentadas as considerações finais.

## 2. Revisão da literatura

Há diversos estudos na literatura que relatam as estatísticas de participação feminina em cursos da área de Computação nas instituições de ensino no Brasil. Silva e Santos (2021) apresentam um estudo sobre o percurso acadêmico feminino em um curso de Engenharia da Computação. Este estudo indica que a baixa representatividade feminina, o comportamento masculino preconceituoso de professores e alunos e a falta de apoio durante o curso são alguns dos fatores que afetam as estudantes mulheres desde o início do curso.

Pereira e co-autoras (2021) realizaram uma análise da participação das mulheres

> 1 Power BI. Disponível em: <https://tinyurl.com/z9tpbctv>. Acesso: 31 mar. 25

nos cursos técnico integrado em Informática e superior em Ciência da Computação do Instituto Federal do Sudeste de Minas Gerais (IF Sudeste MG). Nesse estudo, as autoras concluíram que, embora as mulheres que iniciam um curso técnico integrado na área de informática tenham afinidades com o curso, poucas desejam prosseguir na área em um curso superior. Além disso, no curso de Ciência da Computação do IF Sudeste MG de 2007 a 2019, apenas 14,25% dos ingressantes foram mulheres e pouco menos da metade destas mulheres concluíram o curso.

Marques e colaboradores (2021) chegaram a conclusões semelhantes ao analisar os dados das estudantes de um curso técnico na área de informática no Instituto Federal de São Paulo (IFSP). Os dados apresentados no estudo mostraram que o curso tem maioria de estudantes do sexo feminino no entanto, embora tenham obtido um bom desempenho nas disciplinas técnicas, apenas 31% tinham interesse em continuar na área de exatas em um curso superior.

Miranda e co-autores (2021) analisaram os dados sobre a participação feminina no curso de Ciência da Computação na Universidade Federal de Campina Grande (UFCG) e identificaram que a média de mulheres ingressantes foi pouco mais de 16% do total de ingressantes nesse curso no período de 2006 a 2019. O estudo também mostrou que o desempenho acadêmico e a taxa de formandos foram similares para os estudantes tanto do gênero masculino quanto feminino.

Cursino e Martinez (2021) realizaram uma análise da participação feminina nos dados do Censo da Educação Superior nos cursos da área de tecnologia no período de 2009 a 2018. Foi possível observar nos dados analisados que a porcentagem de mulheres que ingressaram nos cursos da área de tecnologia diminuiu de 20% para 15% ao longo dos anos. Em seu artigo, Maia (2016) já alertava para o baixo número de concluintes mulheres nos cursos de computação, de apenas 17% dos anos de 2000 a 2013. Os dados apresentados também chamam a atenção para o fato de que houve uma queda de 8% no número de concluintes mulheres na área de Computação.

Este artigo busca preencher a lacuna existente na literatura ao investigar a evolução da participação feminina nos cursos de Computação do IFPE, uma temática ainda pouco explorada em estudos anteriores. Embora haja pesquisas sobre a presença feminina na área de Computação em diferentes contextos educacionais, não há análises detalhadas sobre como esse fenômeno se manifesta no IFPE ao longo dos anos. Dessa forma, este estudo contribui para a compreensão desse cenário, fornecendo uma base empírica que pode subsidiar futuras iniciativas voltadas à ampliação da equidade de gênero na área.

## 3. Metodologia

Esta pesquisa apresenta uma análise descritiva dos microdados do Censo da Educação Superior, disponibilizados pelo INEP, no período de 2009 a 2022, com o objetivo de examinar a participação feminina nos cursos superiores de Computação do IFPE. Para isso, os dados foram organizados, visualizados e descritos por meio de gráficos e tabelas. A metodologia adotada, apresentada na Figura 1, foi estruturada em quatro etapas: (1) coleta dos dados; (2) análise preliminar; (3) integração, seleção, limpeza e transformação dos dados; e (4) carregamento dos dados e apresentação dos

resultados.

Figura 1. Metodologia aplicada no presente trabalho.

A etapa 1 de coleta de dados foi realizada por meio do download dos arquivos estruturados disponibilizados pelo Governo Federal na página do Censo da Educação Superior do INEP. Após o download das bases de dados, foi realizada a etapa 2 de análise preliminar dos dados, que compreendeu a validação das informações para verificar sua completude e corrigir possíveis lacunas e/ou anomalias. Esse processo teve como objetivo mitigar erros e garantir a confiabilidade da análise subsequente, conferindo maior rigor à análise realizada. A verificação de consistência incluiu a análise de dados de estudantes matriculados, ingressantes e concluintes, segmentados por idade, gênero, curso, grau acadêmico e unidade de ensino do IFPE.

Antes da fase de integração dos dados na etapa 3, ocorreu a fase de pré-processamento dos dados no Power Query, ferramenta essencial para a depuração dos microdados e a execução eficiente do fluxo de extração, transformação e carregamento (ETL). Embora os microdados disponibilizados pelo INEP apresentassem estrutura pré-definida, foi necessário realizar procedimentos adicionais, como limpeza de campos vazios, remoção de colunas fora do escopo da pesquisa e filtragem para manter apenas registros relativos ao IFPE. Em sequência, os dados referentes ao período de 2009 a 2022 foram integrados em uma única base consolidada. A amostra inicial continha aproximadamente 103 milhões de registros de matrículas, 41 milhões de ingressantes e 15 milhões de concluintes em instituições de ensino superior em todo o país. Após o refinamento, restaram 4.205 matrículas, 2.061 ingressantes e 137 concluintes nos cursos de Computação ofertados pelo IFPE, que constituíram o grupo analisado neste estudo.

Após o refinamento dos dados na etapa 3, eles foram salvos no Power Query e em seguida iniciou-se a etapa 4 com a atividade de carregamento dos dados no Power BI. Para apresentação dos dados, foram desenvolvidos diversos painéis no Power BI

> 2 Censo da Educação Superior. Disponível em: <https://tinyurl.com/5be6zb83>. Acesso em: 31 mar. 25 3 Power Query. Disponível em: <https://tinyurl.com/9rwu9hjb>. Acesso em: 31 mar. 25

para representar diferentes aspectos da análise que envolve os estudantes ingressantes, os matriculados e os concluintes. Os painéis foram estruturados para oferecer uma visão das tendências educacionais ao longo do período analisado por meio de gráficos, tabelas e mapas, organizando os dados obtidos por gênero, faixa etária, cor/raça, campus do IFPE e curso, possibilitando uma análise mais detalhada conforme as necessidades da pesquisa.

## 4. Resultados

Atualmente, o IFPE é composto por 16 campi de ensino presencial e um campus dedicado à Educação a Distância (EaD). Os cursos superiores da área de Computação estão distribuídos em sete campi presenciais. O Campus Belo Jardim oferece o curso de Bacharelado em Engenharia de Software, enquanto os campi Garanhuns, Jaboatão dos Guararapes, Palmares, Paulista e Recife possuem o Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS). Já o Campus Igarassu oferece o Curso Superior de Tecnologia em Sistemas para Internet (SI). Esses cursos tiveram início em diferentes anos dentro do período analisado. Os dados utilizados na pesquisa abrangem os anos de 2009 a 2022, considerando os cursos, os campi do IFPE e o ano de início de cada curso, conforme apresentado na Tabela 1.

<u>Tabela 1.</u> <u>Lista de cursos, campus analisados e ano de início do curso.</u>

|Curso|Campus|Ano de início|
|---|---|---|
|Bacharelado em Engenharia de Software|Belo Jardim|2019|
||Garanhuns|2019|
|C Si d Tli|Jaboatão dos Guararapes|2020|
|urso uperor e ecnooga em Aáli Dlit d Sit|Palmares|2022|
|nse e esenvovmeno e semas|Paulista|2019|
||Recife|2009|
|Curso Superior de Tecnologia em Sistemaspara Internet|Igarassu|2020|

Os dados obtidos foram categorizados em três grupos: estudantes ingressantes, matriculados e concluintes. Para cada categoria, foram analisadas as variáveis de gênero, faixa etária e cor/raça. A Figura 2 apresenta os resultados referentes ao número de estudantes ingressantes em todos os cursos superiores da área de Computação do IFPE. Os dados desse painel revelam uma discrepância de gênero, com um número significativamente maior de homens ingressantes em comparação com as mulheres ao longo do período analisado.

Ao analisar o gráfico "Ingressantes por Ano" apresentado na Figura 2, observa-se que, de 2009 a 2018, quando apenas o Campus Recife oferecia o curso de ADS, a participação feminina apresentou seu ponto mínimo em 2009, com 5,3%, e seu ponto máximo em 2013, com 24,4%. Com a expansão dos cursos de nível superior entre 2019 e 2022 para os campi Belo Jardim, Garanhuns, Jaboatão dos Guararapes, Palmares, Paulista e Igarassu, a participação feminina foi ampliada, atingindo seu ponto mínimo em 2019 (16,7%) e seu pico máximo em 2021 (30,3%), embora ainda

permaneça menor do que a participação masculina. Ao todo, a média de homens ingressantes é de 81,4% enquanto que a média de mulheres ingressantes é de 18,6%. Além disso, observa-se que a maioria dos ingressantes têm entre 18 e 24 anos e se autodeclara parda. Assim, o perfil predominante dos estudantes ingressantes nos cursos superiores de Computação do IFPE é do gênero masculino, pardo e com idade entre 18 e 24 anos.

Figura 2. Painel com dados para os estudantes ingressantes.

Como ingressam mais homens nos cursos de nível superior de Computação do IFPE do que mulheres, é natural que haja mais estudantes do gênero masculino matriculados do que do gênero feminino, como pode ser observado nos dados do gráfico “Matriculados por Ano” do painel da Figura 3. De 2009 a 2018, com apenas o Campus Recife oferecendo o curso de ADS, a porcentagem de mulheres matriculadas variou, alcançando seu ponto mínimo de 7% em 2009 e seu ponto máximo de 17,8% em 2011, em relação ao total de estudantes matriculados no curso. Com a expansão dos cursos para os outros campi entre 2019 e 2022, houve uma variação na porcentagem de mulheres matriculadas, que teve seu ponto mínimo de 15% em 2019 e seu ponto máximo de 23% em 2021. Ao todo, temos como média de homens matriculados 83,7% e de mulheres matriculadas 16,3%. O perfil predominante dos estudantes permaneceu consistente, sendo composto principalmente por homens, com idades entre 18 e 24 anos, e autodeclarados como pardos.

Analisando com mais detalhes os cursos mais recentes, observa-se que o curso de Engenharia de Software no campus de Belo Jardim, iniciado em 2019, apresenta 30,1% de mulheres ingressantes no total de estudantes do referido Campus. Já o curso de ADS, oferecido em diversos campi, apresenta variações moderadas. A título de exemplo, o campus Recife, que oferta o curso desde 2009, registra 18,7% de mulheres ingressantes, enquanto os campi de Garanhuns e Paulista, ambos iniciados em 2019, apresentam respectivamente 23,9% e 26,3%. Já o curso do campus Jaboatão dos

Guararapes, iniciado em 2020, possui 20% de mulheres ingressantes. Sendo assim, os resultados demonstram valores aproximados entre os campi que ofertam o curso de ADS.

Em resumo, os gráficos “Ingressantes por Ano” e “Matriculados por Ano” dos painéis das Figuras 2 e 3 mostram uma tendência de crescimento no número de estudantes ingressantes e matriculados, especialmente após o início de novos cursos no IFPE entre 2019 e 2022. Esse crescimento ocorreu tanto para homens quanto para mulheres, e, embora o número de homens ingressantes e matriculados ainda seja superior, também se observa uma tendência de aumento na participação percentual das mulheres, especialmente em 2021.

Figura 3. Painel com dados para os estudantes matriculados.

Apesar do aumento no ingresso e no número de matrículas de mulheres, esse crescimento não se reflete em um aumento proporcional nas taxas de conclusão. Os dados revelam um alto índice de evasão, tanto entre os estudantes do gênero masculino quanto do gênero feminino, sendo a situação particularmente mais grave para as mulheres. Isso pode ser verificado nos dados apresentados no gráfico “Concluintes por Ano” no painel da Figura 4. Ao analisar o gráfico, observa-se que a maioria dos estudantes concluintes está concentrada no Campus Recife, uma vez que os cursos nos outros campi começaram apenas entre 2019 e 2022. Nos anos de 2010, 2012, 2014, 2019 e 2022, não houve mulheres concluintes, enquanto homens concluíram o curso em todos os anos do período analisado, de 2010 a 2022. De modo geral, do total de estudantes concluintes, apenas 13,1% eram mulheres, enquanto 86,9% eram homens.

Figura 4. Painel com dados para os estudantes concluintes.

Em uma análise mais detalhada com os dados do Campus Recife, cujo curso de ADS é o mais antigo, podemos fazer o cálculo da taxa de conclusão utilizando as métricas disponíveis nas Figuras 5(a) para os estudantes ingressantes e 5(b) para os estudantes concluintes. Considerando que o curso de ADS do Campus Recife tem uma duração mínima de 3 anos e que dispomos de dados de 2009 a 2022, é possível calcular a taxa de conclusão do campus com base no número de ingressantes de 2009 a 2019 e no número de concluintes de 2009 a 2022. Nesse período, entre os ingressantes de 2009 a 2019, foram 139 mulheres e 654 homens. Já entre os concluintes de 2009 a 2022, temos 18 mulheres e 116 homens. Isso resulta em uma taxa de conclusão de 13% para as mulheres e 17,7% para os homens, considerando o tempo mínimo do curso. Assim, no Campus Recife, no período analisado, as mulheres ingressaram em número inferior e apresentaram uma taxa de conclusão mais baixa em comparação aos homens.

Figura 5. (a) Números de Ingressantes do Campus Recife; (b) Números de Concluintes do Campus Recife.

Por fim, os dados dos estudantes ingressantes, matriculados e concluintes foram consolidados em um mapa de bolhas que indica onde estão concentrados a densidade

> 4 Iremos nos ater apenas ao campus Recife aqui neste trabalho. Para maiores detalhes dos cursos de nível superior em Computação de outros campi do IFPE, acessar os dados em <u>https://tinyurl.com/3semk9m2</u>

geográfica dos estudantes em cada uma das situações. Na Figura 6 é apresentado um exemplo do mapa de bolhas apresentado nos painéis resultantes da análise apresentada neste trabalho.

Figura 6. Painel com mapa de bolhas para os estudantes ingressantes.

## 5. Considerações finais

O objetivo deste trabalho foi responder a seguinte questão de pesquisa: Como tem se dado a participação feminina discente nos cursos de nível superior de Computação do IFPE? Para alcançar esse objetivo, analisamos os microdados do Censo da Educação Superior disponibilizados pelo INEP tendo o IFPE como foco do estudo. Os resultados mostram que o perfil predominante dos estudantes ingressantes e matriculados nos cursos de nível superior de Computação da instituição é composto principalmente por homens, com idades entre 18 e 24 anos, e autodeclarados como pardos. Embora a participação feminina ainda seja menor do que a masculina, ela vem sendo ampliada principalmente após o início dos cursos superiores em outros campi, além do campus Recife. Essa participação feminina teve seus máximos em 2021 quando tivemos 30,2% de mulheres ingressantes e em 2022 quando tivemos 23% de mulheres matriculadas nos cursos de nível superior em Computação no IFPE. Os dados encontrados para os cursos de nível superior de Computação do IFPE para os ingressantes estão alinhados com os trabalhos de Pereira e co-autoras (2021) e Miranda e co-autores (2021).

Apesar do aumento no ingresso e no número de matrículas de mulheres, esse crescimento não se reflete em um aumento proporcional nas taxas de conclusão. Nos anos de 2010, 2012, 2014, 2019 e 2022, não houve mulheres concluintes, enquanto homens concluíram o curso em todos os anos do período analisado, de 2010 a 2022. Os resultados indicam que, do total de concluintes, apenas 13,1% eram mulheres, enquanto 86,9% eram homens. No entanto, ao analisar isoladamente os dados do Campus Recife, onde se concentra a maior parte dos concluintes, observa-se que as taxas de conclusão

são baixas para ambos os gêneros, sendo de 13% para as mulheres e 17,7% para os homens. Ainda assim, as mulheres ingressaram em menor número e apresentaram uma taxa de conclusão inferior à dos homens.

Os resultados deste estudo contribuem para uma compreensão mais ampla sobre a participação feminina nos cursos superiores de Computação do IFPE, preenchendo uma lacuna existente. Espera-se que os achados sirvam de base para reflexões institucionais e reforcem a necessidade da adoção de estratégias que promovam o ingresso, a permanência e a conclusão de mulheres nesses cursos. Por fim, considerando as baixas taxas de conclusão para estudantes de ambos os gêneros, é fundamental que as ações voltadas à permanência e ao sucesso acadêmico sejam direcionadas a todos os estudantes da área de Computação da instituição.

## Agradecimentos

As autoras gostariam de agradecer ao Programa Institucional de Iniciação Científica (PIBIC) do IFPE, em especial ao Campus Jaboatão dos Guararapes, por fornecer o suporte financeiro necessário para as bolsas concedidas no projeto de Iniciação Científica que resultou neste trabalho.
