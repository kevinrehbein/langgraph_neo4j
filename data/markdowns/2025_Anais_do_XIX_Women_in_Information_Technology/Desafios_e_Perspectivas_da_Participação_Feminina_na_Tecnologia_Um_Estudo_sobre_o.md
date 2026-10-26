# Desafios e Perspectivas da Participação Feminina na Tecnologia: Um Estudo sobre o Programa OxeTech

Lais S. Almeida, Geymerson S. Ramos, Raquel S. Cabral, Eliana S. Almeida

1Instituto de Computação – Universidade Federal de Alagoas (UFAL) CEP 57.072-900 – Maceió – AL – Brasil

2Faculdade de Medicina — Universidade Federal de Alagoas (FAMED/UFAL) CEP 57.072-900 – Maceió – AL – Brasil

3Orion Lab – Universidade Federal de Alagoas (UFAL) CEP 57.022-230 – Maceió – AL – Brasil

4Inria, INSA Lyon – CITI, UR3720

69621 Villeurbanne, França

5Campus Arapiraca – Universidade Federal de Alagoas (UFAL) CEP 57.309-005 – Maceió – AL – Brasil

6Gioconda Lab – Universidade Federal de Alagoas (UFAL) CEP 57.309-005 – Maceió – AL – Brasil

{ lais.almeida,geymerson } @orion.ufal.br

raquel.cabral@arapiraca.ufal.br

eliana.almeida@gmail.com

Abstract. This study analyzes the reach and female participation in the OxeTech program, a state-level initiative for training in Information Technology. Based on the application of statistical methods to over 8500 anonymous records, a significant association was identified between gender and job category, with female underrepresentation in areas such as Development & IT, and overrepresentation in categories such as Marketing & Social Media and Creative & Design. Furthermore, women showed greater adherence to introductory courses, in contrast to the male predominance in more advanced training. These findings highlight the need for public policies focused on foundational training and female engagement in areas of greater technical complexity and leadership, aiming to expand their participation beyond support roles.

Resumo. Este estudo analisa o alcance e a presença feminina no programa OxeTech, uma iniciativa estadual de capacitação em Tecnologia da Informação. A partir da aplicação de métodos estatísticos sobre mais de 8500 registros anônimos, identificou-se uma associação significativa entre gênero e categoria da vaga de trabalho, com sub-representação feminina em áreas como Desenvolvimento & TI, e sobre-representação nas categorias Marketing & Social Media, Criação & Design. Além disso, verificou-se uma maior adesão de mulheres a cursos introdutórios, contrastando com a predominância masculina em formações mais avançadas. Esses achados

evidenciam a necessidade de políticas públicas voltadas à formação de base e ao engajamento feminino em áreas de maior complexidade técnica e liderança, ampliando sua atuação para além dos papéis de apoio.

## 1. Introdução

De acordo com dados da Brasscom [Brasscom 2021], em relatório divulgado em 2021, o défice de profissionais de TI no Brasil deve ultrapassar meio milhão até 2025. Algumas razões que contribuem para essa demanda estão relacionadas à transformação digital, na qual as empresas vêm investindo em tecnologias como Inteligência Artificial Generativa [Baidoo-Anu and Ansah 2023] e Cibersegurança [AlDaajeh et al. 2022], que exigem profissionais qualificados. Além disso, tais profissionais necessitam de adaptação e aprendizado contínuo para se manterem relevantes no mercado de trabalho.

Neste contexto, a UFAL (Universidade Federal de Alagoas), por meio do LaCCAN (Laboratório de Computação Científica e Análise Numérica), propôs em 2021 o Programa OxeTech Lab de Capacitação e Gestão de Laboratórios de Qualificação Técnica em Tecnologia da Informação, com o objetivo de implantar uma estrutura em rede descentralizada de laboratórios em dez municípios do estado de Alagoas, incluindo sua capital, Maceió. Esses laboratórios, implantados em parceria com o governo do estado, configuram um ambiente para a realização de atividades de capacitação em temas relevantes na área de Tecnologia da Informação (TI), suprindo uma necessidade do OxeTech, uma iniciativa governamental de incentivo à geração de empregos e ao desenvolvimento da área de TI no estado.

O OxeTech tem se consolidado como uma iniciativa de sucesso, que oferece capacitação e oportunidades de trabalho. Sua plataforma digital (http://oxetech.al.gov.br) já conta com mais de 8500 registros e continua a crescer. Uma de suas sub-vertentes, o OxeTech Work, oferece bolsas de incentivo aos participantes, que passam a ter vínculo com uma empresa parceira, e ao fim da experiência, caso esta seja bem-sucedida, o bolsista pode ser contratado pela empresa. O publico atendido é diverso, no entanto, observamos uma tendencia desfavorável à participação feminina. Este problema afeta de modo geral a área de TI, e de acordo com dados apresentados na pesquisa “ Women in Technology ” no ano de 2021 [Technology by Page Group 2021], apenas 30% dos cargos de tecnologia na América latina são ocupados por mulheres. No Brasil, esse número não chega a 25% [Technology by Page Group 2021].

Apesar disso, poucas empresas possuem iniciativas para atrair mulheres para cargos de tecnologia. A mesma pesquisa apresenta dados da Unesco indicando que apenas 3 em cada 10 pessoas que escolhem a área de ciência e tecnologia são mulheres. Independentemente das razões para essa baixa participação feminina, o relatório também destaca os benefícios corporativos de uma representação equitativa de gênero na área de TI. Contar com talentos diversos em percepções, capacidades, criatividade e habilidades, refletidos nas diferenças de pensamento entre homens e mulheres, pode contribuir significativamente para a melhoria de processos e para a construção de soluções inovadoras para empresas e para o mercado tecnológico emergente.

Com o objetivo de alcançar um maior público feminino e mitigar a disparidade de gênero no contexto de tecnologias da informação, este estudo avalia a presença feminina no programa OxeTech para compreender como as mulheres estão se posicionando

em relação às suas escolhas na área de TI, bem como os fatores que afetam suas decisões de candidatura no mercado de trabalho. Utilizando dados anonimizados de mais de 8.500 registros da plataforma OxeTech, aplicamos o teste Qui-Quadrado e o V de Cramér [Das et al. 2023, Bergsma 2013], juntamente com uma análise dos resíduos padronizados para sustentar nossas conclusões. Como contribuição, apresentamos uma descrição detalhada de nossa metodologia de análise, baseada em métricas estatísticas, além de sugestões de ações no contexto desse programa governamental para ampliar a participação feminina na área de TI.

## 2. Trabalhos Relacionados

As mulheres são sub-representadas tanto em cursos universitários quanto em oportunidades de trabalho. Um estudo realizado pela organização Deloitte [Fondazione Deloitte 2022] mostra que, apesar de as mulheres se graduarem e receberem mais diplomas em relação aos homens, elas ocupam apenas 25% dos cargos relacionados a STEM ( Science, Technology, Engineering and Mathematics ) na Europa.

No contexto brasileiro, o estudo realizado por Nascimento et al. [Nascimento et al. 2023] mostra que a participação feminina no ensino superior em STEM aumentou de 29.5% para 33.7% entre 2010 e 2019. No entanto, nesse ritmo, seriam necessários 24 anos para se atingir o limite mínimo de paridade (45%) [Nascimento et al. 2023]. Em Alagoas, essa tendência também é observada nos números de participação feminina no OxeTech, com 34% dos registros até 2023 sendo de mulheres. Além disso, nota-se uma sub-representação das mulheres nas oportunidades ofertadas na área de tecnologias da informação, o que motivou a realização deste estudo.

Estudos como o de Avolio et al. [Avolio et al. 2020] explicitam e discutem o que parece ser uma problemática global. O trabalho dos autores analisa e identifica fatores inter-relacionados que afetam a participação das mulheres na ciência ao longo de seus ciclos de vida e em diferentes contextos culturais. O estudo enfatiza a natureza não biológica da sub-representação feminina, destacando influências socioculturais, educacionais e econômicas, interconectadas em diferentes estágios da vida.

Pullman et al. [Pullman 2018] analisam em que medida as disciplinas acadêmicas fomentam ou atenuam a inserção de mulheres em trabalhos não convencionais, como empregos em tempo parcial e temporários, entre recém-formados no Canadá. O artigo compara fatores educacionais, demográficos e relacionados ao mercado de trabalho como explicações para o envolvimento em trabalhos não convencionais no início da carreira. Os resultados mostram que as taxas de trabalho não convencional variam substancialmente entre os diferentes campos de estudo.

De Las Cuevas et al. [de las Cuevas et al. 2022] realizaram um estudo sobre os motivos pelos quais as mulheres optam por não cursar graduações em STEM. Entre as principais conclusões, os resultados confirmam que: i) o número de mulheres em cursos técnicos diminui conforme o nível do curso aumenta; ii) A falta de modelos de referência não é um impedimento para que mulheres se sintam confortáveis na área; iii) ao contrário dos homens, as mulheres não escolhem engenharia, mesmo que tenham boas notas em disciplinas relacionadas a STEM; iv) as mulheres se percebem como menos capazes de cursar uma graduação em engenharia em comparação aos homens. Esses resultados proporcionam uma compreensão mais profunda da disparidade de gênero nos

campos de STEM, especialmente em idades nas quais mulheres e homens decidem seus futuros acadêmicos e profissionais.

Em um estudo realizado por Jiang [Jiang 2021], a disparidade de gênero em ocupações de STEM não pode ser explicada por diferenças de gênero em habilidades ou seleção baseada em competências. Em vez disso, parte da disparidade pode ser atribuída ao fato de as mulheres estarem mais representadas em cursos de STEM menos intensivos em matemática, cujos egressos têm maior probabilidade de encontrar e optar por empregos mais compatíveis fora de STEM. Outra parte pode ser explicada pela preferência feminina por um maior equilíbrio entre trabalho e vida pessoal, bem como pela localização da residência.

Embora grande parte das pesquisas se concentre em entender as causas da sub-representação feminina e do abandono de áreas STEM, é igualmente importante propor soluções para mitigar esses problemas, especialmente considerando as profissionais das novas gerações [Berman and Bourne 2015]. Chang e Milkman [Chang and Milkman 2020] discutem estratégias para melhorar as decisões que promovem a igualdade de gênero em ambientes de trabalho. Já Pantic e ClarkeMidura [Pantic and Clarke-Midura 2023] exploram interações sociais e práticas que apoiam a retenção das mulheres, analisando a perspectiva de aquelas que persistiram em seus cursos de ciência da computação.

Por meio deste estudo, espera-se não apenas enriquecer a discussão sobre o problema de sub-representação feminina, mas também apresentar soluções que melhorem o grau de participação de mulheres nas iniciativas do OxeTech e consequentemente na STEM, aprimorando as politicas de inclusão no estado de Alagoas.

## 3. Metodologia

Nossas análises foram realizadas com dados anonimizados de 8776 pessoas registradas até dezembro de 2023 na plataforma OxeTech, que é uma iniciativa de cunho profissional e educacional do estado de Alagoas para acelerar a capacitação e o protagonismo no setor de tecnologia da informação. Os usuários da plataforma têm acesso às seguintes iniciativas:

1. OxeTech Work: O estado financia a capacitação de alunos em empresas que disponibilizam vagas de trabalho com bolsa de pesquisa e inovação por um período de seis meses. Após o término do treinamento, caso o bolsista seja avaliado com bom desempenho, a empresa deverá assumir o compromisso de integrá-lo ao seu quadro de funcionários, oferecendo um salário no mínimo equivalente ao valor da bolsa, por um período mínimo de um ano.

2. OxeTech Lab: Um subprograma proposto pelo Laboratório de Computação Científica e Análise Numérica da Universidade Federal de Alagoas, cujo propósito é interiorizar e popularizar a ciência, a tecnologia e a inovação por meio de cursos online gratuitos ou presenciais, realizados em espaços modernos e organizados, acompanhados por instrutores bolsistas qualificados para apoiar e contribuir com uma melhor absorção de conhecimento por parte dos alunos.

A Tabela 1 apresenta o percentual de homens e mulheres registrados na plataforma (coluna Registros), inscritos no OxeTech Work (coluna Inscritos OxeTech Work),

candidatos às vagas de trabalho (coluna Candidaturas OxeTech Work) e matriculados em turmas do OxeTech Lab (coluna Alunos OxeTech Lab). Como observado em estudos realizados ao redor do mundo, o percentual de homens registrados é expressivamente maior: 66% em comparação aos 34% de mulheres. As oportunidades oferecidas pelas vertentes OxeTech Work e OxeTech Lab também evidenciam uma disparidade significativa entre os gêneros.

Tabela 1. Distribuiç ão percentual de homens e mulheres registrados na plataforma, a parcela de inscriç ões e candidaturas no OxeTech Work, e o percentual <u>de alunos do OxeTech Lab ate dezembro de 2023.´</u>

||Registros|Inscritos OxeTech Work|Candidaturas OxeTech Work|Alunos OxeTech Lab|
|---|---|---|---|---|
|Homens|66.0%|75.9%|76.2%|69.7%|
|Mulheres|34.0%|24.1%|23.8%|30.3%|

Para analisar, identificar e entender as possíveis causas de tal disparidade, utilizaremos os dados do OxeTech Work e OxeTech Lab, que disponibilizam os seguintes campos para cada pessoa registrada na plataforma: sexo, escolaridade, turmas em que se matriculou no OxeTech Lab, inscrição no OxeTech Work, vagas de trabalho às quais se candidatou, e a categoria das mesmas, que estão divididas nas seguintes grandes áreas de conhecimento: Desenvolvimento & TI; Análise de Dados; Suporte Técnico; Gerência de Projetos; Criação & Design; Marketing & Social Media; e Vendas. Conduziremos nossas análises estatísticas aplicando o teste Qui-Quadrado para avaliar a existência de relação entre gênero e categorias de vagas de trabalho, o V de Cramér para verificar a força dessa relação e a análise dos resíduos padronizados para entender quais categorias exercem maior influência entre homens e mulheres.

Adicionalmente, para as categorias de maior influência, geramos a distribuição das turmas mais frequentes entre os gêneros para identificar preferências e o perfil dos candidatos em relação às vagas de trabalhos desejadas. As subseções seguintes detalham a aplicação do teste Qui-Quadrado, V de Cramér, e análise de resíduos padronizados.

### 3.1. Teste Qui-Quadrado e V de Cramér

A Tabela 2 apresenta a contagem de candidaturas em ofertas de trabalho, agregadas por categoria, no OxeTech Work. O número de candidaturas masculinas supera o de femininas em todas as categorias, mas a diferença é expressivamente maior na categoria Desenvolvimento & TI. Para entender as causas dessa desproporção, investigamos a relação entre gênero e categoria de emprego por meio do teste Qui-Quadrado de Independência e do V de Cramér. O primeiro teste avalia a existência de uma relação entre gênero e categoria de emprego, indicando se a distribuição de homens e mulheres entre as categorias é aleatória ou não. O V de Cramér, por sua vez, nos informa o quão forte é essa relação, caso ela exista.

Considerando os dados da Tabela 2 e a Equação (1) da estatística Qui-Quadrado, avaliamos as seguintes hipóteses: a hipótese nula H 0, que afirma que não há relação entre gênero e categoria de emprego, e a hipótese alternativa H 1, que sugere que existe uma relação entre gênero e categoria de emprego. O número de linhas r = 8 e o número de colunas c = 2 correspondem, respectivamente, às categorias de trabalho e aos gêneros

Tabela 2. Número de candidaturas de homens e mulheres para vagas de trabalho do OxeTech Work em diferentes categorias.

|Área|Feminino (F)|Masculino (M)|
|---|---|---|
|Desenvolvimento & TI|578|3148|
|Marketing & Social Media|203|362|
| Suporte Técnico|184|774|
| Criação & Design|103|264|
| Gerência de Projetos|142|489|
| Vendas|54|170|
|Análise de Dados|23|77|
|Outros|44|134|

dos candidatos apresentados na Tabela 2. A frequência observada em cada célula é representada por Oij, enquanto a frequência esperada é denotada por Eij. Quanto maior o valor de χ, maior a discrepância entre as frequências observadas e esperadas, indicando possível dependência entre as variáveis.

As frequências esperadas para cada célula Eij, dadas pela Equação (2), são calculadas sob a suposição de independência entre as variáveis, de modo que Ri é a soma total da linha i, Cj corresponde a soma total da coluna j, e N é a soma de todos os valores na tabela.

Com relação ao V de Cramér, definido na Equação (3), é possível verificar a força da relação entre as categorias de trabalho e o gênero dos candidatos. Um valor de V = 0 indica uma associação desprezível, não permitindo qualquer tipo de especulação sobre o gênero dos candidatos, enquanto V = 1 representa uma associação perfeita, nesse caso, conhecer a categoria da vaga de trabalho permitiria determinar o gênero do candidato. Na fórmula, χ representa o valor do teste qui-quadrado, N é o tamanho total da amostra e k é o menor número entre o total de linhas ou colunas da Tabela 2.

### 3.2. Análise de Resíduos Padronizados

A análise de resíduos padronizados é um método estatístico que permite identificar, de maneira mais específica, quais categorias de trabalho contribuem significativamente para a dependência ou independência entre os gêneros. O resíduo padronizado Rij é calculado para cada célula da Tabela 2, conforme a Equação (4). Valores próximos de 0 indicam que o valor observado está de acordo com o esperado. Valores positivos elevados indicam que

a categoria possui mais indivíduos do que o esperado, enquanto valores negativos acentuados indicam que a categoria possui menos indivíduos do que o esperado. Células com |Rij| > 1. 96 indicam diferenças estatisticamente significativas ao nível de 5%, sugerindo associações não aleatórias entre o gênero e a categoria profissional.

## 4. Resultados e Discussão

Os resultados do teste Qui-Quadrado, listados na Tabela 3, indicam que há uma relação estatisticamente significativa entre o gênero dos candidatos e a categoria de emprego à qual se candidatam. O valor da estatística Qui-Quadrado χ = 161. 03 indica que há uma discrepância considerável entre o número de candidaturas recebidas e o esperado para cada gênero em diferentes categorias. Uma vez que o p -valor é extremamente pequeno (1. 95 × 10 ), rejeitamos a hipótese nula ( H 0) de que não há relação entre gênero e categoria profissional.

Tabela 3. Resultados da estatística do Qui-Quadrado ( χ ) e do V de Cramér, considerando um nível de significância de 5%.

|χ|p-valor Graus de|Liberdade|V|
|---|---|---|---|
|161.03|1_.95×10 |7|0.154|

Isso significa que a distribuição das candidaturas entre homens e mulheres não é aleatória, sugerindo que fatores estruturais, culturais ou sociais influenciam a escolha das áreas. No entanto, o V de Cramér (0.154) indica que, embora a relação entre as variáveis seja significativa, sua força é fraca. Isso sugere que o gênero tem alguma influência nas escolhas profissionais, mas não é um fator determinante, e que há outras variáveis que podem afetar essas escolhas.

O mapa de calor dos resíduos padronizados, apresentado na Figura 1, evidencia três categorias com influência estatisticamente significativa ( |Rij| > 1. 96) na distribuição das candidaturas entre homens e mulheres, a saber: Marketing & Social Media, Criação & Design, e Desenvolvimento & TI. Resíduos padronizados positivos indicam que a frequência observada nessa célula foi superior à esperada sob a hipótese de independência entre as variáveis, enquanto valores negativos indicam uma frequência inferior ao valor esperado.

As categorias Marketing & Social Media e Criação & Design apresentam valores de resíduos padronizados positivos para mulheres, _Rij = 8. 68 e Rij = 3. 60, respectivamente, indicando que há mais mulheres do que o esperado nessas categorias. Esse resultado pode estar relacionado a fatores estruturais e sociais, como a maior presença histórica de mulheres nessas áreas e a possível influência de modelos de referência. Em contraste, a categoria Desenvolvimento & TI apresenta um resultado negativo ( Rij = − 5. 79), indicando que as mulheres estão sub-representadas nesse setor.

Esse resultado reforça a persistência da desigualdade de gênero no setor de tecnologia, e revela que a desigualdade de gênero nas candidaturas às vagas de emprego segue

Figura 1. Mapa de calor dos resíduos padronizados, considerando o número de candidaturas de homens (H) e mulheres (F) em diferentes categorias de vagas de trabalho.

padrões globais, onde mulheres estão sub-representadas em áreas STEM. Muitos são os fatores que podem contribuir para essa disparidade, inclusive formação. Na Figura 2, podemos observar os cursos e formações mais procuradas no OxeTech Lab pelos indivíduos que se candidataram nas três categorias discutidas anteriormente.

Na categoria Desenvolvimento & TI, onde as mulheres estão subrepresentadas, observa-se que, após a área de Cibersegurança, os cursos mais procurados por candidatas concentram-se em formações introdutórias, como programação básica em Python e fundamentos de redes. Em contrapartida, o perfil das candidaturas masculinas nessa mesma categoria revela uma demanda maior por cursos de nível mais avançado, voltados ao aprofundamento em diferentes linguagens de programação e ferramentas especializadas.

Figura 2. Distribuiç ão das turmas de interesse para homens e mulheres que aplicaram para vagas OxeTech Work nas categorias Desenvolvimento & TI, Marketing & Social Media, e Criaç ão & Design.

A Figura 3, que contém a proporção de homens e mulheres por categoria de turmas oferecidas no OxeTech Lab, ilustra de maneira clara uma maior presença de mulheres em áreas introdutórias, como Informática Básica e Lógica de Programação. Por outro lado, a participação feminina é significativamente menor em áreas que demandam maior experiência e familiaridade com tecnologia, como Linux para Devs, Git e GitHub, e Arduíno. Esse padrão sugere uma possível relação entre o nível de complexidade dos cursos e a representatividade de gênero, e a possível evasão feminina da área.

Figura 3. Proporç ão de homens e mulheres por categoria de cursos oferecidos no OxeTech Lab.

Esse fenômeno ocorre em todo o mundo nas áreas de STEM, e é conhecido como leaky pipeline, ou, em português, “cano com vazamento”. O termo se refere à perda gradual de mulheres ao longo da trajetória acadêmica e profissional. Essa desigualdade se intensifica em níveis mais avançados, formando gráficos com um padrão em formato de tesoura, nos quais a proporção de mulheres diminui significativamente à medida que se avança em cargos de maior prestígio ou titulação acadêmica e a porcentagem dos homens aumenta. Entre as principais causas apontadas para esse fenômeno está a dificuldade de equilibrar as responsabilidades acadêmicas com as demandas domésticas, como a maternidade, que se torna um problema estrutural pela falta de políticas de apoio.

Para enfrentar esses desafios, é fundamental a adoção de políticas que incentivem tanto a entrada quanto a permanência de mulheres nas áreas de ciência e tecnologia. Entre as estratégias possíveis, destacam-se a implementação de programas educacionais que introduzam conceitos de ciência e tecnologia desde o ensino básico, com abordagens acessíveis e inclusivas; a promoção da visibilidade de mulheres bem-sucedidas nas áreas de STEM; e o enfrentamento de estereótipos de gênero, por meio da reformulação de ideias propagadas desde a infância. No âmbito do mercado de trabalho, podem ser oferecidos incentivos financeiros e oportunidades específicas para mulheres. Além disso, é essencial o estabelecimento de políticas institucionais que promovam a diversidade e combatam o assédio e a discriminação em ambientes acadêmicos e profissionais.

Além disso, é crucial implementar políticas de apoio estruturado, como a oferta

de serviços de cuidados infantis gratuitos ou subsidiados em locais acessíveis, de modo a reduzir significativamente o impacto das responsabilidades familiares sobre a trajetória profissional das mulheres. Também é fundamental assegurar que tanto mães quanto pais tenham acesso a licenças parentais adequadas, permitindo que as mulheres se afastem temporariamente do trabalho sem comprometer suas carreiras a longo prazo.

Para aumentar a participação e a retenção de mulheres em STEM, é fundamental adotar uma abordagem abrangente que contemple desde a educação básica até as políticas institucionais voltadas a profissionais em estágios mais avançados da carreira. A implementação de iniciativas que incentivem o ingresso, ofereçam suporte ao longo da trajetória e promovam ambientes mais flexíveis e inclusivos é essencial para superar as barreiras que historicamente afastam as mulheres dessas áreas. Um exemplo inspirador de iniciativa nacional nesse sentido é a criação da primeira Maratona Feminina de Programação do Brasil, realizada em 2023, que buscou ampliar a participação de mulheres e pessoas não-binárias na computação, especialmente no ensino superior. A iniciativa foi motivada por mudanças nas regras da Maratona de Programação da SBC, que passou a reservar vagas para equipes com participação feminina [Nunes et al. 2024].

## 5. Conclusão e Trabalhos Futuros

Este trabalho apresentou um estudo do público alcançado pelo programa OxeTech, com ênfase na presença feminina nas iniciativas de Tecnologia da Informação oferecidas no estado de Alagoas. Conduzimos nossos estudos com o auxílio de métodos estatísticos, aplicados a mais de 8500 registros anônimos da plataforma OxeTech. Resultados-chave mostram que: i) a relação entre homens e mulheres no programa OxeTech se assemelha à média mundial, de modo que 34% dos registrados na plataforma são mulheres; ii) na busca por oportunidades de mercado, existe uma relação entre o gênero dos candidatos e a categoria da vaga de trabalho; iii) as mulheres estão sub-representadas nas candidaturas de trabalho na categoria Desenvolvimento & TI, e apresentam sobre-representação nas categorias Marketing & Social Media, e Criação & Design; iv) entre os inscritos no OxeTech Lab, observa-se uma maior presença feminina em formações introdutórias, como Informática Básica e Lógica de Programação. Por outro lado, a participação de mulheres é significativamente menor em áreas que demandam maior experiência e familiaridade com tecnologia.

Essas observações indicam que é fundamental construir mecanismos que despertem o interesse e ampliem a participação feminina nas políticas de capacitação em tecnologias da informação oferecidas pelo estado, de modo que as mulheres sejam incentivadas a buscar formações além da informática básica. Também é necessário promover a participação ativa de mulheres em áreas de protagonismo profissional, a fim de equilibrar a distribuição entre papéis de apoio e posições de liderança no setor de tecnologias da informação. Como trabalhos futuros, estenderemos nossas análises por meio da verificação e identificação de correlações relacionadas ao engajamento feminino nas políticas da plataforma, considerando fatores econômicos, educacionais e geográficos, sob as perspectivas rural e urbana nos diferentes municípios do estado. Refletir sobre a representatividade feminina em programas como o OxeTech é corroborar a ideia de que a presença de talentos diversos no ambiente corporativo, refletida nas diferentes formas de pensar entre homens e mulheres, pode representar um diferencial estratégico na criação de soluções inovadoras para um mercado tecnológico em constante evolução.

## Agradecimentos

O presente trabalho foi realizado com apoio da Fundação de Amparo à Pesquisa do Estado de Alagoas (FAPEAL), e da Secretaria de Estado da Ciência, Tecnologia e Inovação de Alagoas (SECTI-AL).
