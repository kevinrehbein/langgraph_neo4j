20º Women In Information Technology (WIT 2026): Relatos de Experiência

# Peer mentoring e o ensino de python para mulheres ingressantes na engenharia

Yasmin Cani Viviani [0009-0009-2719-0039], Emanuela da Silva Silveira [00090005-5187-4538], Tatiana Nilson dos Santos² [0000-0003-3389-842X], Eliane Pozzebon¹ [0000-0002-4237-6589]

- 1Laboratório de Tecnologias Computacionais (LabTeC-UFSC) – Universidade Federal de Santa Catarina (UFSC) - Araranguá – SC – Brasil

 - 2 Programa de Pós-graduação em Tecnologias da Informação e Comunicação – Universidade Federal de Santa Catarina - Araranguá - SC - Brasil

{yasmincviviani,emanuss2006}@gmail.com, tatiana.santos@ufsc.br, epozzebon@gmail.com

Abstract. The underrepresentation of women and the high dropout rates in the initial semesters of engineering courses highlight the urgent need for welcoming and technical leveling initiatives. This article presents an experience report of an introductory Python programming course, conceived and taught exclusively by senior female students to freshmen in the Computer Engineering course at the Federal University of Santa Catarina. Based on a peer mentoring approach and the creation of a safe learning space, the project aimed to mitigate imposter syndrome and reduce initial barriers to technology. The methodology involved synchronous meetings with live coding and collaborative debugging practices. The evaluated results demonstrated a significant increase in the technical self-confidence of the new students and the effectiveness of the judgment-free environment.

Resumo. A representação feminina e os altos índices de evasão nos semestres iniciais dos cursos de engenharias evidenciam a urgência de ações de acolhimento e nivelamento técnico. Este artigo apresenta o relato de experiência de um curso introdutório de programação em Python, idealizado e ministrado exclusivamente por alunas veteranas para calouras do curso de Engenharia de Computação da Universidade Federal de Santa Catarina. Fundamentado na abordagem de peer mentoring e na criação de um espaço seguro de aprendizagem, o projeto teve como objetivo mitigar a síndrome da impostora e reduzir as barreiras iniciais no contato com a tecnologia. A metodologia envolveu encontros síncronos com práticas de live coding e depuração conjunta. Os resultados avaliados demonstraram um aumento significativo na autoconfiança técnica das ingressantes e a eficácia do ambiente livre de julgamentos.

## 1. Introdução

O ingresso no ensino superior nas áreas exatas traz, para o público feminino, o desafio do primeiro contato com a programação em turmas majoritariamente masculinas, o que frequentemente desencadeia a síndrome da impostora e culmina na evasão precoce das calouras. Análises abrangentes baseadas no Censo da Educação Superior (Alvim; Bittencourt & Duran, 2024) indicam que a evasão, especialmente nos cursos de computação, atinge níveis críticos e que são agravados por fatores socioculturais, quando se trata do público feminino. Além disso, a disparidade histórica de gênero é constantemente corroborada por análises de dados educacionais em larga escala (Santos; Gallindo & Moreira, 2024).

Nesse contexto, ações de nivelamento técnico aliadas ao acolhimento emocional tornam-se essenciais para alterar as métricas de sobrevivência no curso. Freitas et al. (2024) destacam a urgência de aplicar estratégias de retenção adaptáveis e focadas nas alunas durante os anos iniciais dos cursos de exatas. Reconhecendo essa necessidade, alunas veteranas do curso de Engenharia de Computação da Universidade Federal de Santa Catarina estruturaram um minicurso de python para calouras. A literatura recente confirma que iniciativas exclusivas para mulheres são fundamentais para criar ambientes acolhedores, promovendo o empoderamento feminino na computação e quebrando estereótipos de gênero (Barino et al, 2024).

Diante disso, este artigo apresenta um relato de experiência sobre o planejamento, a execução e os impactos desse curso. O objetivo principal deste trabalho é documentar como a união entre o ensino introdutório de tecnologia e o apoio mútuo feminino pode atuar como um agente transformador. Busca-se demonstrar que iniciativas promovidas de alunas para alunas não apenas facilitam a compreensão de conceitos fundamentais de programação, mas são essenciais para construir o senso de pertencimento, aumentar a autoconfiança e incentivar a permanência das mulheres na engenharia de computação.

## 2. Fundamentação teórica

Para fundamentar a iniciativa deste curso, este relato apoia-se em três pilares principais: a análise da representação feminina nas áreas exatas, a eficácia da mentoria entre pares ( peer mentoring ) como ferramenta de retenção e as abordagens pedagógicas no ensino introdutório de programação.

Historicamente, as áreas de Ciência, Tecnologia, Engenharia e Matemática (STEM) enfrentam uma disparidade de gênero significativa. Na computação, esse cenário é frequentemente explicado pelo conceito de "funil vazado" ( leaky pipeline ), uma metáfora que ilustra como as mulheres abandonam essas áreas em diferentes estágios de sua formação e carreira (Schiebinger, 1999).

A literatura aponta que a evasão nos anos iniciais dos cursos de engenharia está fortemente ligada a fatores socioculturais. O ambiente acadêmico, muitas vezes predominantemente masculino, pode gerar isolamento e o desenvolvimento da chamada "síndrome da impostora", onde as alunas duvidam de sua própria capacidade intelectual e técnica. A falta de modelos inspiracionais ( role models ) e de um ambiente acolhedor transforma as dificuldades normais do aprendizado inicial de lógica em barreiras quase

intransponíveis, justificando a necessidade urgente de ações de acolhimento voltadas para ingressantes (Schiebinger, 1999; Mason, Wolfinger & Goulden, 2013).

Como contraponto a esse isolamento, a peer mentoring surge como uma estratégia pedagógica e de apoio psicossocial altamente eficaz. Essa prática consiste no suporte oferecido por estudantes mais experientes (veteranas) a estudantes iniciantes (calouras). Diferente da relação hierárquica tradicional entre professor e aluno, a mentoria entre pares promove um ambiente de aprendizagem horizontal (Dennehy & Dasgupta, 2017). As veteranas, por já terem vivenciado e superado as mesmas angústias e disciplinas, atuam como exemplos reais de sucesso, fortalecendo o senso de pertencimento das ingressantes. Além disso, essa abordagem cria um "espaço seguro" ( safe space ) para a aprendizagem, onde o medo de errar ou de fazer perguntas é reduzido, favorecendo não apenas a absorção do conteúdo, mas também o desenvolvimento da autoconfiança.

Assim, a peer mentoring, consolida-se como uma das estratégias mais promissoras para reter o público feminino em áreas de exatas. Segundo estudos recentes em programas focados em STEM (Jones & Wendt, 2025) quando as estudantes são expostas a modelos inspiracionais (mentoras) com as quais conseguem se identificar, há um aumento direto na autoeficácia, no senso de pertencimento e, consequentemente, na intenção de concluir a graduação (Dennehy & Dasgupta, 2017).

O primeiro contato com a programação exige uma alta carga cognitiva, o que pode ser desmotivador para iniciantes. Por isso, a escolha da ferramenta de ensino é estratégica. Mapeamentos sistemáticos recentes, como o conduzido por Ferreira et al. (2025), demonstram que a linguagem Python tem sido uma das ferramentas mais adotadas e com maior taxa de sucesso em iniciativas de ensino de programação voltadas para mulheres no Brasil.

A sintaxe amigável e limpa do Python minimiza a preocupação com detalhes estruturais complexos, permitindo que a aluna foque no desenvolvimento do pensamento computacional e da lógica. Segundo Aguiar et al. (2025), o uso dessa linguagem em oficinas práticas reduz a barreira de entrada e facilita a inclusão de meninas na computação. Além disso, relatos de experiência similares, como o de Gonçalves et al. (2024), evidenciam que cursos intensivos de python, quando desenhados especificamente para o público feminino, geram alto engajamento, superam a insegurança técnica inicial e promovem a autoconfiança.

## 3. Procedimentos metodológicos

A execução deste projeto foi estruturada visando não apenas o repasse de conhecimento técnico, mas também a criação de um ambiente de acolhimento e fortalecimento do sentimento de pertencimento das alunas ingressantes. A iniciativa foi organizada por alunas veteranas do curso de Engenharia de Computação, contando com apoio institucional da Universidade Federal de Santa Catarina para utilização da infraestrutura física e laboratorial necessária para a realização das atividades.

A primeira edição do curso ocorreu no primeiro semestre de 2024 e, desde então, o projeto passou a ser ofertado semestralmente. As ministrantes atuaram de forma

- 46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

20º Women In Information Technology (WIT 2026): Relatos de Experiência

voluntária como monitoras e mentoras, sendo responsáveis pelo planejamento pedagógico, elaboração das atividades práticas e acompanhamento individual das participantes.

O público-alvo foi composto exclusivamente por alunas ingressantes (calouras) do curso. A divulgação ocorreu por meio de um momento informal denominado “sequestro”, no qual as estudantes eram convidadas pelas veteranas a conhecer a proposta do projeto e participar das atividades introdutórias de programação em Python.

O curso foi planejado com carga horária total de 30 horas, distribuídas em encontros semanais presenciais de duas horas. As aulas ocorreram no laboratório de informática da Universidade Federal de Santa Catarina, equipado com computadores contendo o ambiente Virtual Studio Code e a linguagem Python na versão mínima 3.12.

Além dos encontros presenciais, foi criado um grupo no WhatsApp exclusivo para participantes e ministrantes. O espaço foi utilizado para compartilhamento de materiais complementares, resolução de dúvidas e fortalecimento da interação entre as estudantes, contribuindo para a construção de uma rede de apoio acadêmico.

### 3.1. Conteúdo programático das aulas

A ementa foi elaborada com foco na transição suave para a lógica de programação. O conteúdo foi distribuído da seguinte forma ao longo dos encontros:

- Encontro 1: introdução à computação, apresentação da linguagem Python, variáveis, tipos de dados básicos (inteiros, strings, floats ), comandos de entrada e saída ( input e print ) e exercícios programáticos.

- Encontro 2: tipo de dado Booleano, operadores lógicos e matemáticos, estruturas condicionais ( if, elif, else ) e exercícios programáticos.

- Encontro 3: estruturas de repetição ( for e while ), manipulação básica de listas e exercícios programáticos.

- Encontro 4: funções de listas, uso de tuplas, aplicações de dicionário e exercícios programáticos.

- Encontro 5: construção de matrizes, instalação da biblioteca Numpy (para uso de elementos matemáticos), manipulação de strings e exercícios programáticos.

- Encontro 6: introdução a funções (reaproveitamento de código) e criação de rotinas, e exercícios programáticos.

- Encontro 7: uso de try except (tratamento de erros), manipulação de arquivos e exercícios programáticos.

- Encontro 8: conceitos de variáveis globais e locais, introdução básica à interface gráfica, instalação da biblioteca Tkinter (uso da interface gráfica), desenvolvimento de um miniprojeto final guiado (calculadora básica) e encerramento, com uma roda de conversa sobre a vivência no curso de Engenharia de Computação.

### 3.2. Estratégia pedagógica

A condução das aulas baseou-se nos princípios de aprendizagem ativa e na peer mentoring. Em vez do formato tradicional de aulas expositivas, adotou-se o modelo de live coding (programação ao vivo), onde as ministrantes desenvolviam o código passo a passo, acompanhadas pelas calouras.

Durante as atividades práticas, as monitoras circulavam pela sala para oferecer suporte individualizado. O aspecto mais importante da estratégia pedagógica foi a garantia de um "espaço seguro" ( safe space ). Desde o primeiro dia, foi enfatizado que não existiam "perguntas óbvias" e que o erro fazia parte natural do processo de desenvolvimento de software, buscando ativamente reduzir a síndrome da impostora entre as ingressantes.

A transição do planejamento para a execução do curso revelou dinâmicas valiosas sobre o comportamento das alunas ingressantes diante dos primeiros desafios na universidade. A vivência prática evidenciou que o ensino de lógica de programação, quando aliado a um ambiente acolhedor, ultrapassa a barreira técnica e atinge a esfera emocional e de permanência no curso.

### 3.3. Estratégia pedagógica

Os dados apresentados neste relato de experiência possuem natureza qualitativa e foram obtidos a partir do acompanhamento ao longo das edições do curso. Inicialmente, durante a roda de conversa realizada no primeiro encontro, buscou-se compreender as percepções iniciais das participantes acerca da programação, suas expectativas em relação ao curso e os sentimentos relacionados ao ingresso em um ambiente majoritariamente masculino.

Ao final de cada edição, foram registradas observações realizadas pelas ministrantes durante as atividades práticas e interações desenvolvidas nos encontros presenciais e no grupo de WhatsApp. Os depoimentos utilizados neste trabalho foram anonimizados, preservando a identidade das participantes, que autorizaram o uso acadêmico de suas falas exclusivamente para fins científicos. A análise dos dados ocorreu de forma descritiva e interpretativa, buscando identificar recorrências relacionadas ao acolhimento, à redução da síndrome da impostora, ao fortalecimento da autoconfiança e ao desenvolvimento do senso de pertencimento.

## 4. Resultados e discussões

Somando as quatro edições já realizadas do curso, registrou-se a participação de 29 alunas ingressantes. A taxa média de permanência nas atividades foi de aproximadamente 75%, índice considerado positivo para iniciativas extracurriculares de programação, frequentemente marcadas por elevados níveis de evasão.

As ausências observadas ao longo das edições estiveram majoritariamente relacionadas à sobreposição com avaliações e atividades obrigatórias da graduação, e

20º Women In Information Technology (WIT 2026): Relatos de Experiência

não à desmotivação em relação ao minicurso. Com base nas observações qualitativas e nas rodas de conversa promovidas ao longo dos encontros, foi possível identificar impactos positivos relacionados tanto ao desenvolvimento técnico quanto ao acolhimento emocional das participantes. A Figura 1 abaixo apresenta o quantitativo de meninas participantes do curso de python em cada semestre de sua edição.

Figura 1. Quantitativo de meninas por curso

### 4.1. Construção de espaço seguro e sentimento de pertencimento

O primeiro encontro foi marcado por uma hesitação natural das calouras. Muitas relataram, informalmente, um sentimento de inadequação por não possuírem nenhum conhecimento prévio em programação — um contraste com a realidade de muitos colegas do gênero masculino que costumam ingressar no curso já com alguma bagagem técnica.

Aluna 1: “Quando entrei na faculdade lembro que fiquei um pouco desconfortável com a quantidade de homens na minha sala, já esperava isso por causa da área escolhida, mas mesmo assim foi um pouco assustador.”

Para quebrar esse gelo, o curso não iniciou imediatamente com linhas de código, como geralmente ocorre nas salas de aula. As ministrantes conduziram uma roda de conversa onde compartilharam suas próprias trajetórias, incluindo reprovações, dificuldades enfrentadas nos semestres iniciais e episódios em que também sentiram a "síndrome da impostora", demonstrando assim que as ministrantes entendiam como as calouras se sentiam naquele momento.

Aluna 2: “Essa experiência me proporcionou romper barreiras sobre lógica e sintaxe de programação, também por consequência me fez compreender mais as aulas de programação da própria graduação.”

Essa vulnerabilidade apresentada por parte das veteranas foi o ponto de virada para estabelecer o safe space. A partir desse momento, observou-se uma mudança na

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

20º Women In Information Technology (WIT 2026): Relatos de Experiência

postura das calouras: o medo de fazer "perguntas consideradas óbvias" diminuiu drasticamente, dando lugar a uma participação ativa e livre de julgamentos.

Aluna 3: “[...] um ambiente seguro e confortável que elas proporcionaram, nos deixando completamente à vontade para perguntar e aprender de forma colaborativa.”

Esses resultados dialogam diretamente com Dennehy e Dasgupta (2017), que apontam a importância da representatividade feminina e da mentoria entre pares para o fortalecimento do sentimento de pertencimento em áreas STEM.

### 4.2. Desenvolvimento de autoconfiança técnica

Do ponto de vista técnico, a curva de aprendizado acompanhou os padrões descritos na literatura de ensino de programação. Nos primeiros encontros, que abordaram variáveis, operadores e comandos de entrada/saída ( print e input ), o engajamento foi alto e a assimilação ocorreu de forma rápida. A sintaxe amigável do Python cumpriu seu papel em não sobrecarregar cognitivamente as iniciantes.

Os formulários de avaliação aplicados ao final do curso indicaram que a maioria das participantes percebeu evolução em sua compreensão de lógica de programação e maior confiança para acompanhar as disciplinas introdutórias da graduação.

Aluna 4: “Por ter sido meu primeiro contato real com a programação, o curso foi fundamental para o desenvolvimento do meu raciocínio lógico.”

No entanto, o nível de complexidade e frustração aumentou significativamente nos encontros que introduziram as estruturas de repetição ( for e while ) e o encapsulamento de lógica em funções. Nesses momentos, a estratégia de live coding somada ao suporte individualizado das monitoras mostrou-se essencial.

Em vez de apenas fornecer a resposta correta, a equipe adotou a prática de depuração ( debugging ) conjunta. As monitoras sentavam-se ao lado das alunas na sala para ajudar a ler as mensagens de erro geradas pelo interpretador, ensinando-as a identificar sozinhas falhas de indentação ou erros de lógica. Isso foi fundamental para desenvolver a autonomia das estudantes.

Esse resultado reforça os achados de Aguiar et al. (2025) e Ferreira et al. (2025), que destacam o potencial do Python como ferramenta introdutória capaz de reduzir barreiras de entrada no ensino de programação para mulheres.

Um dos aspectos mais marcantes da experiência ocorreu nas entrelinhas do curso, durante os intervalos e nos minutos finais das aulas. O ambiente criado para ensinar Python naturalmente se transformou em um fórum de mentoria estudantil. Enquanto os códigos eram compilados, as conversas fluíam para as dúvidas sobre a grade curricular do curso de Engenharia de Computação, como lidar com a carga

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS 20º Women In Information Technology (WIT 2026): Relatos de Experiência

horária de determinadas disciplinas, recomendações de professores e dicas de organização para conciliar a vida acadêmica.

Essa "mentoria invisível" reforçou o pilar da representatividade. As calouras puderam visualizar um futuro possível dentro da universidade através da figura das veteranas, compreendendo que as dificuldades iniciais são etapas naturais da graduação, e não sinais de incapacidade intelectual, gerando um índice cada vez menor de desistência das mulheres no curso.

Aluna 5: “Trocar experiências com as alunas do segundo semestre me deu mais confiança e preparo para lidar com os desafios de um ambiente majoritariamente masculino.”

Esses relatos corroboram a literatura apresentada no referencial teórico, demonstrando que a síndrome da impostora e o isolamento podem ser mitigados através da convivência com role models (modelos inspiracionais) femininos. O curso funcionou como um catalisador de pertencimento.

### 4.3. Impactos bilateriais: o lado das ministrantes

Por fim, é fundamental discutir que os resultados do projeto se estenderam à equipe organizadora. Para as alunas veteranas que atuaram como professoras, a experiência de preparar aulas e acompanhar as atividades proporcionou um aprofundamento técnico e o desenvolvimento de habilidades de liderança e aprimoramento da comunicação interpessoal.

Aluna 6: “O ingresso no curso de Engenharia de Computação é um pouco hostil no início por ser um ambiente majoritariamente masculino, mas poder participar desse curso suavizou esse ingresso. Participar dessa oficina fez com que eu não me sentisse obrigada a saber tudo, pois é difícil programar quando se há zero experiências antes do curso. Ser aluna me fez querer aprender e ser professora me possibilitou acolher mais pessoas com as mesmas dificuldades que eu, o que me permitiu aprender ainda mais sobre Python.”

O desafio de transpor conceitos complexos de lógica para uma linguagem acessível aprimorou a capacidade de comunicação das ministrantes. Além disso, assumir a posição de liderança de uma turma contribuiu para o fortalecimento da autoconfiança profissional das próprias veteranas, comprovando que iniciativas de extensão universitária dessa natureza geram benefícios bilaterais.

Os depoimentos coletados e a evolução na autoconfiança das participantes corroboram as percepções de Barino et al. (2024) e Freitas et al. (2024), demonstrando que a principal barreira para as calouras na computação não é a complexidade intelectual da área, mas a falta de um ambiente de pertencimento.

Aluna 7: “Quando participei como caloura, vi ali um lugar possível de desenvolvimento, sem me sentir pressionada pela sensação de não pertencimento à área. Tendo a oportunidade de estar nos dois lados, ao me tornar uma das mentoras fiz o possível para que as novas calouras se sentissem seguras e confiantes com seu próprio potencial.”

O safe space estabelecido e o suporte das veteranas validaram a eficácia do projeto não apenas como ensino técnico (amparado pela escolha do Python, conforme recomendado por Ferreira et al., 2025), mas como uma política eficaz de retenção e acolhimento estudantil.

A atuação como mentoras permitiu às veteranas consolidar conhecimentos previamente adquiridos e desenvolver competências frequentemente exigidas no mercado de trabalho, como trabalho em equipe, empatia e resolução colaborativa de problemas.

Com o objetivo de sistematizar as principais percepções observadas ao longo das edições do curso, a Tabela 1 apresenta uma síntese comparativa entre os sentimentos e comportamentos relatados pelas participantes no início e ao final das atividades. A organização desses aspectos possibilita visualizar de forma mais objetiva os impactos do minicurso no desenvolvimento da autoconfiança técnica, na redução do medo de errar e no fortalecimento do sentimento de pertencimento das alunas ingressantes.

Tabela 1. Quantitativo de meninas por curso

|Aspecto observado|Percepção inicial|Percepção após o curso|
|---|---|---|
|Confiança em programação|baixa|moderada/alta|
|Medo de errar|elevado|reduzido|
|Participação em aula|tímida|ativa|
|Sentimento de pertencimento|reduzido|ampliado|

## 5. Considerações finais

O presente relato de experiência demonstrou que a idealização e execução de um curso introdutório de Python, focado exclusivamente no público feminino e conduzido por alunas veteranas, atingiu com sucesso seus objetivos pedagógicos e sociais. A iniciativa provou ser uma ferramenta valiosa não apenas para nivelar o conhecimento técnico básico em lógica de programação, mas, fundamentalmente, para atuar como uma rede de apoio nos momentos iniciais do curso de Engenharia de Computacação da Universidade Federal de Santa Catarina.

A adoção da mentoria entre pares ( peer mentoring ) e a manutenção de um ambiente de aprendizagem horizontal e seguro ( safe space ) revelaram-se os grandes

catalisadores do projeto. Ficou evidente que, ao se reconhecerem nas ministrantes, as calouras sentiram-se encorajadas a abandonar a postura de passividade e o medo do erro — fatores frequentemente associados à síndrome da impostora em ambientes de exatas predominantemente masculinos.

O curso transcendeu a sintaxe da linguagem Python, transformando-se em um espaço de acolhimento, troca de vivências acadêmicas e fortalecimento do senso de pertencimento. Ademais, confirmou-se o impacto positivo bilateral da ação, uma vez que as veteranas envolvidas na organização puderam aprimorar suas competências de liderança, comunicação e empatia.

Embora os resultados observados sejam positivos, este trabalho apresenta algumas limitações. Por tratar-se de um relato de experiência com abordagem predominantemente qualitativa, não foi realizado acompanhamento longitudinal das participantes ao longo dos semestres subsequentes da graduação, impossibilitando mensurar diretamente impactos sobre índices de evasão acadêmica.

Além disso, não foi estabelecido grupo de comparação entre estudantes participantes e não participantes da iniciativa. Dessa forma, recomenda-se que trabalhos futuros desenvolvam análises quantitativas mais amplas, incluindo avaliações pré e póscurso e acompanhamento acadêmico continuado das alunas.

Também propõe-se a institucionalização do curso para que seja ofertado regularmente a cada novo ciclo de ingresso universitário. Recomenda-se, ainda, a criação de módulos subsequentes abordando tópicos como Estruturas de Dados ou Ciência de Dados básica, bem como a formação de um grupo de estudos permanente que acompanhe essas alunas ao longo de toda a matriz curricular.

Por fim, espera-se que este relato possa encorajar outras instituições e centros acadêmicos a promoverem ações semelhantes, compreendendo que o investimento na equidade de gênero na tecnologia começa pelo acolhimento de quem acaba de chegar..
