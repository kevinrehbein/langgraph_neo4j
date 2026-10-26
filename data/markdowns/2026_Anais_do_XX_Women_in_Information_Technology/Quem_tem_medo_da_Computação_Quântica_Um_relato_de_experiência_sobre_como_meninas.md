# Quem tem medo da Computação Quântica? Um relato de experiência sobre como meninas reagem ao estudo de

# conceitos básicos da área

Anna Luisa F. Costa 1, 3, Estela M. Batista 1, 3, Rodrigo dos S. Miranda, João Marcos A. M. Ramos 1, 3, Thais Regina de M. B. Silva 1, 3, Fabrício A. Silva 1, 3 e Linnyer B. Ruiz Aylon 2, 3

1Instituto de Ciências Exatas e Tecnológicas – Universidade Federal de Viçosa (UFV) Campus Florestal – Florestal – MG – Brasil

2Universidade Estadual de Maringá (UEM) – Maringá – PR – Brasil

3Manna Team

{anna.l.costa, estela.batista, rodrigo.d.miranda, joao.m.ramos}@ufv.br

{thais.braga, fabricio.asilva}@ufv.br

lbruiz@uem.br

Abstract. Quantum computing is one of the emerging fields of science that has been gaining increasing theoretical and practical importance. Mastering its concepts will soon become a competitive advantage in the STEM (Science, Technology, Engineering and Mathematics) market. This article presents an experience report on the implementation of a bootcamp and a game about quantum computing for high school students. The perception of the girls regarding the topic was analyzed, evaluating differences in relation to the boys and to what they already think about STEM in general. The results showed that there is a general interest in the subject. However, unlike the boys, the female students need a safe environment and female role models in order to feel motivated.

Resumo. A computação quântica é uma das áreas emergentes da ciência que vem adquirindo crescente importância teórica e prática. Dominar seus conceitos, em breve, será um diferencial competitivo no mercado de STEM (Science, Technology, Engineering and Mathematics). Este artigo apresenta um relato de experiência sobre a aplicação de um bootcamp e um jogo sobre computação quântica para alunos do ensino médio. Foi analisada a percepção das meninas quanto ao assunto, avaliando diferenças em relação aos meninos e ao que elas já pensam sobre STEM de modo geral. Os resultados mostraram que existe interesse geral pelo tema. Porém, ao contrário dos meninos, as alunas precisam de um ambiente seguro e de referências femininas para se sentirem motivadas.

## 1. Introdução

A Computação Quântica é um campo emergente da ciência e da engenharia da computação que aproveita propriedades únicas da mecânica quântica para resolver problemas além da capacidade até mesmo dos computadores clássicos mais poderosos

[Nielsen and Chuang 2000]. A área tem estado tão presente no cotidiano que a UNESCO declarou 2025 como o Ano Internacional da Ciência e Tecnologia Quântica (IYQ) iyq. Além disso, estima-se que a Computação Quântica (CQ) já tenha movimentado cerca de 1,2 bilhão de dólares em nível mundial [Laignel 2025].

Os computadores baseados nessa tecnologia operam sob conceitos novos e complexos, tais como Superposição, Emaranhamento, Decoerência e Interferência [IBM 2026], que precisam ser compreendidos pela comunidade da área de computação. Em particular, é ideal que estudantes de cursos relacionados já sejam introduzidos a esses conceitos, de maneira que possam se preparar para um potencial novo mercado de trabalho. A partir disso, soluções lúdicas têm sido apresentadas na literatura para auxiliar nessa explicação. Nesse contexto, o grupo Manna Team, da Universidade Federal de Viçosa - Campus Florestal (UFV – Campus Florestal) criou o jogo QuantumFlip, que introduz conceitos sobre portas lógicas quânticas e o bit quântico de forma lúdica.

Ao realizar dinâmicas voltadas à temática da CQ para a aplicação do QuantumFlip junto à estudantes de nível médio/técnico e superior da UFV – Campus Florestal, verificou-se uma baixa participação feminina. Diante desse cenário, esta pesquisa traz um relato de experiência da aplicação de uma oficina sobre o ensino de conceitos básicos de CQ por meio do QuantumFlip para alunos do primeiro e segundo ano do curso técnico em informática vinculado à CEDAF (Central de Ensino e Desenvolvimento Agrário de Florestal), realizada com o objetivo de responder às seguintes questões:

- QP1. Existe um contraste entre a visão das estudantes sobre o ecossistema STEM e a atratividade que manifestam pela Computação Quântica?;

- QP2. Existem diferenças entre as percepções feminina e masculina em relação a CQ?;

- QP3. O jogo desenvolvido pelo grupo de pesquisa, quando aplicado de forma a transmitir segurança para as alunas, conseguiria despertar nelas um maior interesse pela CQ?

Essa temática mostra-se ainda mais importante sob a ótica de que atualmente, segundo o IBGE, as mulheres ocupam apenas 15,7% das matrículas em cursos de graduação voltados à Computação e Tecnologias da Informação e Comunicação (TIC) [IBGE 2024]. Este cenário pode se tornar ainda mais desafiador se considerarmos, em um futuro próximo, uma ampla adoção da CQ, sem que meninas e mulheres tenham se preparado tão bem quanto os homens para dominá-la.

O restante do artigo está organizado da seguinte forma: a Seção 2 discute os trabalhos relacionados; a Seção 3 detalha a metodologia de coleta dos relatos de experiência; a Seção 4 descreve os resultados; e, por fim, a Seção 5 apresenta as conclusões e as perspectivas para trabalhos futuros.

## 2. Trabalhos Relacionados

A literatura aponta que a transição entre o Ensino Fundamental e o Médio constitui um período crítico para a manutenção do interesse feminino em áreas tecnológicas. Em [Ferreira 2023], observa-se que o interesse de alunas por temas de exatas diminui progressivamente ao longo das séries escolares, fenômeno associado à presença de ‘violência simbólica"e à influência de modelos parentais tradicionais na construção de expectativas de carreira.

Para além disso, estudos como [Medeiros et al. 2022, Silva et al. 2023] indicam que as barreiras enfrentadas pelas estudantes vão além do ambiente escolar, envolvendo fatores familiares, sociais e estruturais. Destacam-se a ausência de referências femininas na ciência, o baixo senso de pertencimento e, em contextos de vulnerabilidade, a limitação de acesso a recursos básicos, como computadores.

Diante desse cenário, iniciativas educacionais recreativas têm sido exploradas como estratégias para ampliar o engajamento e o interesse de jovens pela área de novas tecnologias. Trabalhos como Qubit: The Game [Escanez-Exposito et al. 2023] e Entanglion [Weisz et al. 2018] destacam-se por apresentarem abordagens voltadas à introdução de conceitos de Computação Quântica por meio de dinâmicas lúdicas. No entanto, apesar de suas contribuições no âmbito educacional, essas iniciativas não evidenciam um recorte específico quanto à participação feminina ou à promoção de ambientes inclusivos, diferindo, nesse aspecto, da proposta adotada neste trabalho.

Baseado nos resultados dessas pesquisas e na compreensão das dificuldades encontradas por alunas em disciplinas das áreas de exatas, de maneira similar, este trabalho busca entender se existe relação entre a não participação em atividades relacionadas à temática de computação quântica e a falta de atratividade pelas áreas da tecnologia. Além disso, busca-se verificar se o jogo QuantumFlip, quando aplicado de forma a transmitir segurança para as alunas, conseguiria despertar nelas um maior interesse.

## 3. Metodologia

O estudo em questão caracteriza-se como um relato de experiência utilizando procedimentos quantitativos, estruturado a partir do diagnóstico realizado em atividades anteriores relacionadas à Computação Quântica, organizadas pelo Projeto Manna Team, que apresentaram baixos níveis de adesão feminina.

Os eventos relatados dividem-se entre uma Mostra de Profissões, realizada anualmente pela UFV – Campus Florestal, registrando uma participação de 47 estudantes em um estande sobre o jogo QuantumFlip, dos quais apenas 25% eram do gênero feminino; um minicurso sobre Computação Quântica, aplicado na Semana da Computação da CEDAF, que contou com 18 participantes e uma adesão feminina de apenas 5,9%; e, por fim, um workshop sobre CQ organizado também pelo projeto Manna Team, também na Universidade UFV – Campus Florestal, o qual obteve participação de 26,9% de meninas entre os 28 presentes.

Com o intuito de compreender melhor o porquê da baixa adesão feminina observada em todas as ocasiões mencionadas, formulou-se uma nova oficina sobre CQ com aplicação do QuantumFlip. Formulou-se também um formulário de pesquisa, cujas perguntas consideraram aspectos relacionados à percepção das estudantes sobre as áreas STEM, assim como o seu interesse específico pela CQ. A análise buscou identificar se a confiança e a predisposição manifestadas em relação às ciências exatas se mantêm constantes no campo da CQ, investigando como a ludicidade do jogo pode atuar como ferramenta de engajamento e segurança em ambientes de aprendizagem.

Este trabalho utilizou como ferramenta principal para a coleta de dados a observação de eventos e a aplicação de formulários. O processo iniciou-se com a elaboração dos questionários, que foram impressos para preenchimento físico pelas alunas durante a

oficina. Optou-se por formulários em papel e por uma coleta de dados realizada de forma anônima, a fim de garantir a participação de todas as estudantes, uma vez que o acesso à Internet ou a dispositivos eletrônicos não era garantido. O questionário contou com 17 perguntas, discursivas e objetivas, com o intuito de caracterizar o perfil das alunas, bem como suas percepções e interesse em relação à Computação Quântica.

Para a organização da oficina, foram realizadas reuniões estratégicas para definir os conteúdos introdutórios de Computação Quântica e as atividades lúdicas aplicadas. A programação foi estruturada em dois momentos complementares: uma etapa teórica, voltada aos fundamentos da Computação Quântica, e uma etapa prática, dedicada à aplicação do QuantumFlip e de outros jogos relacionados ao tema. Essa divisão buscou proporcionar às estudantes o embasamento necessário para uma transição gradual entre teoria e prática.

## 4. Relatos de Experiência

A oficina foi realizada no dia 25 de fevereiro de 2026, no Laboratório de Informática da Universidade UFV – Campus Florestal, junto às turmas do 1 e 2 ano do curso técnico em Informática da CEDAF, compostas por estudantes do ensino médio integrado. O grupo era formado por 38 alunos no total, sendo 9 meninas, 28 meninos e uma pessoa que optou por não se identificar. A faixa etária dos participantes variava entre 14 e 16 anos, com média aproximada de 15 anos. Em relação à equipe organizadora do evento, esta foi composta por cinco bolsistas e voluntários do Projeto Manna Team, sendo três mulheres e dois homens.

Os formulários físicos de coleta de dados foram distribuídos antes do início das atividades, garantindo tempo adequado para o preenchimento. É necessário ressaltar que, para essa pesquisa, embora os questionários destinados às meninas contivessem perguntas específicas sobre atratividade e barreiras de gênero na área, essa distinção não foi explicitada ao grupo, a fim de preservar o sentimento de segurança das estudantes e assegurar um preenchimento natural e integrado à dinâmica do evento.

### 4.1. Workshop: Do Bit ao Qubit

O Workshop foi conduzido por dois integrantes do Projeto citado, os quais se dividiram na explicação teórica da temática. O objetivo da apresentação era introduzir uma base conceitual introdutória sobre os princípios da Computação Quântica, assim como os aspectos históricos que descrevem a evolução dessa tecnologia. Este momento estruturou-se em quatro blocos principais, formulados para garantir o nivelamento técnico e o engajamento das participantes:

- Aplicação de questões de pré-teste: Momento inicial voltado para despertar o diálogo entre os estudantes e os organizadores, levantando questionamentos acerca do possível conhecimento prévio dos alunos em relação à Computação Quântica. Além disso, aplicou-se um questionário de verdadeiro ou falso relacionado à temática para a coleta de dados, com o objetivo de mensurar, posteriormente, a assimilação dos conteúdos sobre o tema.

- Contextualização Histórica e Representatividade: Apresentação do resumo cronológico da evolução da computação clássica e quântica, desde a mecânica até

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

- 20º Women In Information Technology (WIT 2026): Relatos de Experiência

a eletrônica. Neste momento, destacou-se a participação feminina, ressaltando que o termo “computador” era originalmente a designação das mulheres que realizavam cálculos complexos, e que a máquina herdou este nome em homenagem a esse trabalho [Fritz 1996].

- Fundamentação Conceitual: Apresentação teórica sobre os conceitos fundamentais da Computação Quântica. Foram explicados o funcionamento do qubit, bem como as portas lógicas quânticas e os fenômenos de superposição e emaranhamento, buscando atrelar esses tópicos a exemplos simples do cotidiano.

- Avaliação de Pós-teste: Neste momento, reaplicou-se as questões iniciais relacionadas à Computação Quântica, com o intuito de levantar dados e verificar a absorção dos conteúdos por parte dos participantes.

### 4.2. Atividades Práticas

Ao finalizar o processo de fundamentação teórica, a oficina avançou para a etapa de experimentação prática. Nesse contexto, a aplicação dos jogos foi estruturada de modo que os participantes pudessem consolidar e praticar os conceitos assimilados na etapa anterior. Para isso, os estudantes foram divididos em grupos, de maneira a facilitar a rotação entre os jogos aplicados. Nesse momento, foram aplicados, ao todo, quatro jogos relacionados à Computação Quântica, destacando-se o QuantumFlip, um jogo de cartas pensado e desenvolvido pela equipe.

Durante essa etapa, os participantes foram incentivados a interagir ativamente com as dinâmicas propostas, explorando conceitos fundamentais da Computação Quântica por meio de abordagens lúdicas e colaborativas. A Figura 1 apresenta as fotos descritivas do evento, sendo a primeira fotografia referente à etapa expositiva da palestra, enquanto as duas imagens subsequentes registram a aplicação do QuantumFlip e a interação desenvolvida entre as organizadoras do evento com as participantes. Ao final desse processo, foram distribuídos entre os participantes formulários para a avaliação dos jogos, de forma que esses dados fossem coletados e posteriormente analisados.

Figura 1. Etapas da oficina de Computação Quântica, incluindo a exposição teórica e a aplicação do jogo QuantumFlip.

## 5. Resultados

Nesta seção, os principais resultados obtidos por meio dos formulários e da observação da condução da oficina são apresentados e analisados. A amostra, composta integralmente pelos estudantes participantes da oficina relatada, apresenta um perfil jovem que se

revela fundamental para a análise, visto que esses alunos se encontram em uma fase de exploração vocacional e de consolidação de percepções sobre carreiras tecnológicas.

Para facilitar a compreensão da análise, os dados foram organizados em três subseções: a Subseção 5.1 aborda a relação entre a percepção sobre STEM e o interesse pela CQ; a Subseção 5.2 compara os perfis feminino e masculino, buscando identificar diferenças de percepção; e a Subseção 5.3 discute a eficácia do jogo lúdico aliado a uma estratégia acolhedora como ferramenta de engajamento e segurança para as estudantes.

### 5.1. Percepção Feminina: STEM versus Computação Quântica

Às perguntas iniciais abordadas no formulário tinham como objetivo mapear o perfil de interesse e o repertório inicial das participantes em relação às áreas de STEM e, especificamente, à Computação Quântica. A Figura 2, no que diz respeito à imagem 2.b), apresenta níveis moderados e altos de interesse das alunas por disciplinas de Matemática e Física, sugerindo que a baixa adesão feminina detectada em eventos anteriores não decorre, necessariamente, de uma rejeição às ciências exatas. Por outro lado, os resultados sobre o questionamento 2.a), apresentam baixos níveis em relação ao conhecimento prévio acerca da temática, com 60% das participantes afirmando ‘apenas conhecer o nome’, indicando que, o distanciamento inicial pode ser justificado à falta de exposição prévia ao tema.

(a) Conhecimento prévio sobre CQ.

(b) Preferencia por Disciplinas STEM.

Figura 2. Resultado das perguntas presentes no pré-formulário.

O desconhecimento por parte das alunas em relação às tecnologias quânticas, como indicam os dados, não se traduz, necessariamente, em desinteresse. Os percentuais apresentados na Figura 3 corroboram para esse ponto, uma vez que, as perguntas 3.a) e 3.b) revelam uma predisposição positiva de curiosidade em relação à área, com níveis moderados e altos de expressividade sobre a vontade de aprender conceitos de tecnologias quânticas por meio de metodologias lúdicas, assim como a intenção de participar de eventos relacionados à Computação Quântica. Dessa forma, esses levantamentos sugerem que a aplicação de ferramentas lúdicas, quando estruturada para transmitir segurança e acolhimento, atuam como instrumentos de engajamento e interesse.

Ao analisar a perspectiva de carreira das estudantes em STEM na Figura 4, observa-se uma divisão exata, enquanto metade da amostra considera provável seguir uma carreira em exatas, os outros 50% manifestam indiferença. Os dados em questão sugerem um contraste em relação ao interesse das participantes sobre temas relacionados à Computação Quântica, uma vez que, a inclinação pela atividade quântica supera a própria certeza profissional. Vale ressaltar que tal incerteza associada ao futuro profissional,

Figura 3. Resultado das perguntas presentes no pré-formulário.

pode estar relacionado com a faixa etária das alunas, que por estarem no primeiro ano do Ensino Médio, vivenciam um período de transição e descobertas.

Figura 4. Resultado da pergunta “Você considera seguir uma carreira na área de ciências exatas no futuro?”

Outro aspecto destacado nos questionamentos levantados no formulário foi o sentimento de pertencimento na área STEM. Ao analisar a Figura 5, observa-se que os estereótipos de gênero consolidados nas áreas das ciências exatas refletem-se na percepção das estudantes sobre a Computação Quântica. Aproximadamente 50% da amostra feminina relatou sentir-se “nada” ou “pouco” representada nas carreiras dessa área, enquanto 40% ainda enxergam essas disciplinas como domínios majoritariamente masculinos. Os resultados apresentados estão de acordo com a literatura, que aponta a baixa adesão de meninas às áreas STEM devido à falta de modelos de referência [Morais and Morais 2020].

Figura 5. Resultado das perguntas presentes no pré-formulário.

A lacuna destacada pelos dados da Figura 5, revela-se como uma busca por espaços seguros no aprendizado de tecnologias quânticas emergentes. Tal constatação, baseia-se nas informações levantadas através das perguntas relacionadas aos aspectos necessários para tornar o ambiente atrativo e seguro para o público feminino. Dessa forma,

20º Women In Information Technology (WIT 2026): Relatos de Experiência

ao serem questionadas sobre o que as deixaria mais confortáveis para aprender Quântica, apenas 22,2% declararam não ter preferência de ambiente. Em contrapartida, uma parcela significativa (33,3%) apontou a necessidade de ambientes com maior presença feminina ou atividades conduzidas por mulheres. Tais resultados, encontrados na Figura 6 sugerem que, para esse público, a transição para áreas de alta complexidade técnica, como a Quântica, está intrinsecamente ligada à construção de uma rede de segurança emocional e representatividade.

Figura 6. Resultado da pergunta “Se depender do ambiente, o que te deixaria mais confortável para participar de eventos sobre Computação Quântica? (MÚLTIPLA ESCOLHA)”

### 5.2. Perspectiva Comparativa de Gênero na Percepção da Computação Quântica

Com o intuito de analisar um possível contraste em relação as visões do público feminino e masculino acerca da Computação Quântica, observou-se também as respostas dos meninos sobre o interesse na temática assim como o nível de conhecimento prévio relacionado as novas tecnologias quânticas. A Figura 7 apresenta os resultados de tais questionamentos, reforçando à Computação Quântica como um campo de interesse latente. Segundo os dados levantados, aproximadamente 70% apenas ouviram falar sobre a temática, revelando que essa tecnologia ainda é um campo de conhecimento desconhecido para a maioria dos estudantes, uma vez que, uma grande parcela do público feminino também selecionou o mesmo nível de conhecimento prévio.

(a) Conhecimento prévio sobre CQ.

Figura 7. Resultado das perguntas presentes no pré-formulário.

É importante destacar que, embora 75% (Figura 7.b) dos meninos demonstrem forte inclinação para aprender o tema por meio de metodologias lúdicas, aproximadamente 60,7% disseram que talvez participariam de eventos sobre o tema, como exposto na Figura 8.b). Tais resultados, para este contexto, revelam que aplicação de materiais interativos possuem um carácter atrativo em comparação a realização de eventos formais.

Figura 8. Resultado das perguntas presentes no pré-formulário.

Em relação ao espaço de aprendizagem, ao comparar os dados referente a percepção do público feminino com o masculino, notou-se uma grande disparidade. Embora a maioria dos meninos, aproximadamente 60,7% (Figura 8, pergunta a) tenha inicialmente indicado que sua participação dependeria do ambiente, mais de 60% (Figura 9) deles declararam não possuir preferências específicas quanto à composição social ou condução da atividade. De acordo com tais dados, para o contexto deste trabalho, constata-se que, para os meninos o ambiente é um fator passivo de conveniência, contudo, para as meninas ele torna-se um mediador ativo de pertencimento e segurança.

#### Figura 9. Resultado da pergunta “Se depender do ambiente, o que te deixaria mais confortável para participar de eventos sobre Computação Quântica? (MÚLTIPLA ESCOLHA)”

### 5.3. Análise dos Resultados Referentes ao QuantumFlip

Os resultados obtidos após a aplicação do QuantumFlip, apresentados na Figura 10, demonstram-se condizentes com a predisposição inicial das estudantes em relação ao aprendizado sobre Computação Quântica. A expectativa por metodologias interativas, manifestada anteriormente pelas alunas, foi confirmada pela avaliação positiva do jogo, em que 66,6% das participantes classificaram o nível de diversão entre ’bom’ e ’excelente’. Além desses aspectos, cerca de 55,5% do público feminino analisado afirmaram que a atividade auxiliou de, alguma forma, na compreensão de conceitos da tecnologia quântica.

## 6. Considerações Finais e Trabalhos Futuros

Este trabalho apresentou um relato de experiência da aplicação de uma oficina sobre CQ, composta por um workshop e o uso de jogos lúdicos, para estudantes do ensino médio/técnico, conduzido com o objetivo de avaliar o engajamento feminino. Os resultados

Figura 10. Resultado das perguntas presentes no pós-formulário.

obtidos demonstraram a importância da obtenção de dados reais sobre os cenários que possam tornar o engajamento do público feminino na Computação Quântica concreto. Nesse contexto, a análise dos resultados permitiu validar a premissa de que a Computação Quântica, embora percebida como um campo de alta complexidade, pode se tornar um interesse para as meninas, desde que, a abordagem utilizada traga segurança e conforto para tais.

A principio, observou-se um contraste significativo em relação a visão geral sobre as áreas STEM e o interesse específico pela Computação Quântica. Enquanto a certeza sobre uma carreira em exatas divide as estudantes, o interesse em aprender sobre tecnologias quânticas por meio do lúdico, bem como a participação em eventos sobre essa temática, resultou em um percentual acima dos 60%. Isso demonstra que a resistência à STEM pode não ser um desinteresse pela ciência, mas sim um reflexo de como essas áreas são apresentadas.

Ao comparar as percepções entre os gêneros feminino e masculino, os dados evidenciaram que, embora meninos e meninas partam de um nível similar de desconhecimento técnico, as disparidades surgem na percepção da importância do ambiente de ensino-aprendizagem. Enquanto os estudantes do sexo masculino demonstram não possuírem preferência em relação ao ambiente e sendo indiferentes à composição do grupo, as meninas sinalizam que o ambiente é um fator decisivo para sua segurança.

Por fim, o jogo QuantumFlip demonstrou certa eficácia no que diz respeito a cultivar o interesse do público feminino pela Computação Quântica. As altas notas de usabilidade e compreensão sugerem que dinâmicas lúdicas podem tornar temas complexos mais acessíveis e atrativos. Contudo, a experiência também revelou que o recurso lúdico, por si só, não é suficiente para garantir a inclusão plena. A demanda de 33,3% das participantes por ambientes com maior presença feminina e lideranças mulheres destaca que a segurança emocional está intrinsecamente ligada à representatividade. Como perspectiva de trabalhos futuros, propõe-se a reaplicação do bootcamp, incorporando os feedbacks das participantes, especialmente quanto à composição da equipe organizadora, visando promover um ambiente mais seguro para o público-alvo e ampliar o interesse pela área.

## Agradecimentos

Agradecimentos ao Manna Team, a Fundação Araucária de Apoio ao Desenvolvimento Científico e Tecnológico do Estado do Paraná (FA) e ao Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) - Brasil (Processo nº 421548/2022-3 e

- 46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

 - 20º Women In Information Technology (WIT 2026): Relatos de Experiência

440447/2024-0) pelo apoio e concessão de bolsas. Ao programa MinasCoders, pelo fomento a pesquisas sobre temáticas de gênero em Computação.

## Uso de Inteligência Artificial

De acordo com o Código de Conduta da SBC, declara-se a utilização de ferramentas como plataformas de Inteligência Artificial generativa ao longo da elaboração deste trabalho. O ChatGPT (OpenAI), foi utilizado para revisão gramatical. Já a ferramenta Gemini (Google) foi utilizada para apoio na identificação preliminar de referências bibliográficas.
