# Aproximando Meninas da Area de STEM com Iniciação a Robótica

Luiza Castilho Ereno, Ana Carolina Marcelino, Andrea Bordin, Luciana B. Frigo

- 1 Departamento de Computação/DEC, Universidade Federal de Santa Catarina (UFSC) Campus Araranguá - Santa Catarina, Brasil

Abstract. This article describes the development and the experience of robotics workshops for elementary school girls from public and private schools in the [omitted for review] city. The methodology applied is described in this article so the experience can be improved and replicated. Robotics proved to be very motivating for the girls, especially the younger ones, who ended up creating a bond with your developed robots. The girls’ wishes to end each workshop were to take the robot home to elementary school I and to stay in touch with technology with new activities for elementary school II.

Resumo. Este artigo descreve a experiência de desenvolvimento e aplicação de oficinas de robótica para alunas do ensino fundamental de escolas públicas e privadas do município de Araranguá/SC. A metodologia aplicada está descrita neste artigo de modo a ser aprimorada e replicada. A robótica se mostrou uma atividade muito motivadora para as meninas, principalmente para as mais jovens, que acabaram criando um vínculo com seus robôs desenvolvidos. Os desejos das alunas ao final de cada oficina foram de levar o robô para casa, para as crianças do ensino fundamental I e de permanecer em contato com a tecnologia com novas atividades para as do ensino fundamental II.

## 1. Introdução

O aumento da representatividade feminina nas áreas de STEM ( Science, Technology, Engineering, and Mathematics ) tem sido objeto de estudo de diversos projetos no Brasil [Williams 2020, Moro et al. 2022, Araujo et al. 2022] e no mundo [Yabas et al. 2022, Campbell et al. 2022]. A realização de projetos, oficinas e encontros, que tenham como objetivo apresentar a tecnologia de uma maneira mais prática para meninas de ensino fundamental e médio se faz essencial, permitindo que elas conheçam e se sintam mais confortáveis na área de STEM ( Science, Technology, Engineering, and Mathematics ).

A falta de representatividade pode estar ligada aos fatores culturais que afastam as meninas dos itens tecnológicos, desde muito cedo e estimula os meninos através dos brinquedos como carros, aviões, robôs, jogos online e videogames, por exemplo. Martins et al. [Martins et al. 2019] citam em seu artigo alguns fatores que atraem meninas para cursos ligados a tecnologia, como os incentivos vindos de outras mulheres, de projetos que proporcionem um contato prévio com TI e auxiliam a despertar um interesse maior na área.

Com o objetivo de atrair cada vez mais meninas para o universo da tecnologia, e também prestar apoio à aquelas que estão nesse meio como forma de acolhimento, o projeto [oculto para revisão] busca levar a tecnologia em forma de oficinas e atividades

para meninas de ensino fundamental. Em 2022, o projeto ofereceu oficinas básicas de robótica para meninas do ensino fundamental.

O presente trabalho descreve o processo de planejamento e realização das oficinas, com o intuito de compartilhar as experiências, apresentando um guia da sequência de atividades, para que possam ser replicadas e aperfeiçoadas. Este artigo está organizado da seguinte forma: na Seção 2 são apresentados os artigos que fazem uso da robótica em oficinas para o público feminino; na Seção 3 é mostrada a metodologia de trabalho das oficinas; na Seção 4 são apresentados os resultados dos questionários aplicados durante as oficinas e por fim, na Seção 5 são apresentadas as considerações finais.

## 2. Trabalhos Relacionados

Uma das formas de motivar o interesse de meninas pela área de tecnologia é a apresentação da robótica nas escolas. Uma pesquisa na base de artigos SBC-OpenLib (SOL), na qual foram utilizadas as palavras-chave Robótica e Meninas, retornou nove (9) artigos, dos quais apenas sete (7) relatam experiências com robótica para meninas, como mostra a Tabela 1.

|Referência Revista|Ferramenta usada|Faixa etária|Questionário|
|---|---|---|---|
|[Santos et al. 2019]|Kit Arduino Uno R3|Ensino Médio|Não|
|Anais do XXV Workshop de Informática na Escola||||
|[Alexandrino et al. 2021]|LOGO, Scratch, Kits LEGO Mindstorm e Arduino|Ensino médio e superior|Não|
|Anais do Simpósio Brasileiro de Educação em Computação||||
|[Mattos et al. 2015]|Kits Fischertechnik e ROBO TX Explorer|Ensino Médio|Sim|
|Anais do XXIII Workshop sobre Educação em Computação||||
|[Marotti et al. 2021]|Scratch e Robótica (sem mencionar o kit)|11 a 17 anos|Sim|
|Anais do XV Women in Information Technology||||
|[Santos and Filho 2020]|Scratch, S4A e Arduino UNO|Ensino Médio|Não|
|Anais do XIV Women in Information Technology||||
|[Ribeiro et al. 2016]|Scratch e kit LEGO|Ensino Médio|Não|
|Anais do X Women in Information Technology||||
|[dos Santos et al. 2016] Anais do X Women in Information Technology|Visual G e kit LEGO|Ensino Médio|Sim|

Tabela 1. Trabalhos Relacionados

Em relação à escolaridade e faixa etária, observou-se que a maioria dos projetos se destina a meninas do ensino médio, com apenas um (1) projeto incluindo meninas mais novas, do ensino fundamental. Como ferramentas utilizadas percebeu-se a predominância de utilização de kits de robótica do tipo Lego e Arduino.

Das experiências relatadas, apenas 3 (três) aplicaram questionários para as alunas avaliarem suas experiências. Além disso, todas as experiências ofereceram uma única turma que percorreu todas as aulas da oficina ou minicurso até o final do projeto.

## 3. Metodologia

Esta Seção descreve as oficinas de robótica realizadas no segundo semestre de 2022 que ocorreram de forma presencial no laboratório LabTeC na Universidade Federal de Santa Catarina, campus Araranguá, no contexto do Projeto Meninas Digitais - UFSC. As oficinas foram planejadas e executadas por uma equipe formada por duas professoras e seis estudantes, sendo três graduandas de engenharia de computação, dois graduandos de engenharia de computação e uma de tecnologia de informação e comunicação. O processo desenvolvido contempla 9 etapas conforme ilustra a Figura 1.

- Etapa 1: o público-alvo definido para a ação foram alunas do ensino fundamental.

Figura 1. Processo para o Desenvolvimento das Oficinas

- Etapa 2: estimou-se que o tempo para a realização das atividades seria de 2 à 3 horas.

- Etapa 3: nesta experiência foram levados em conta os materiais disponíveis no laboratório e o conhecimento dos integrantes da equipe. O grupo selecionou as seguintes cinco alternativas para serem avaliadas: Scratch, Little Bits, Snap Circuits, Arduino e o Lego Mindstorm EV3. Cada ferramenta foi atribuída a um integrante da equipe, para estudo e avaliação. Cada integrante criou um documento com a descrição da oficina, o objetivo e as atividades propostas. A ideia inicial era realizar as 5 oficinas em uma sequência crescente de dificuldade para um único grupo de estudantes ao longo do ano. No entanto, devido ao período de pandemia, sem atividades presenciais do projeto, identificou-se uma demanda represada para a participação nas oficinas. Dessa forma, optou-se em selecionar apenas uma oficina e replicá-la para vários grupos distintos de alunas, oportunizando o acesso a um número maior de estudantes. Assim, a ferramenta escolhida foi a Lego Mindstorm EV3, pois envolve tanto programação quanto robótica e pode ser facilmente adaptada para públicos com idades diferentes como o que se tem no ensino fundamental. A programação em blocos é mais didática para ini-

> 1https://scratch.mit.edu/

> 2https://classroom.littlebits.com/welcome

> 3https://www.elenco.com/

> 4https://www.arduino.cc/

> 5https://education.lego.com/pt-br/downloads/mindstorms-ev3/software

ciantes, além do fato que os robôs tem um apelo diferenciado e muito motivador entre crianças e adolescentes. Os kits didáticos foram adquiridos ao longo dos mais de 10 anos de existência do projeto, com recursos advindos da inciativa privada e de editais públicos. No momento, o projeto possui apenas recursos para bolsas para as estudantes de graduação.

- Etapa 4: ao pesquisar oficinas ofertadas com a ferramenta, o site da Lego com sugestões de oficinas filtrados por kit e idade foi descoberto. Filtrando por Lego Mindstorm EV3 e por faixa etária do ensino fundamental II, o grupo descobriu 3 planos de aula. O plano de aula escolhido foi ’Treinador de robô’ que é dividido em 7 aulas de dificuldade e duração crescentes. A aula escolhida foi a inicial Movimentos e giros que possui um tutorial para base motriz com imagens indicando as peças a serem usadas e como posicionar cada uma e sugestão de programação em blocos em português que foram usados sem necessidade de adaptação.

- Etapa 5: foram elaborados dois questionários para serem aplicados em cada oficina, o inicial, com quatro questões com o objetivo de saber o contato prévio das estudantes com a robótica, e o final, com oito questões para obter uma avaliação geral da oficina. O objetivo dos questionários foi conhecer o perfil das alunas, suas expectativas, suas dificuldades e melhorias a serem implementadas nas próximas oficinas. Foi elaborado um termo de consentimento para participação da oficina e das pesquisas, assinado pelo responsável de cada estudante. O termo foi enviado para a Secretaria de Educação do Município, que fez a coleta das assinaturas e devolução no dia da realização da oficina.

- Etapa 6: as oficinas foram divulgadas junto à Secretaria de Educação do município e na universidade, com um período de inscrições.

- Etapa 7: os kits foram inspecionados para garantir as peças necessárias para a montagem, assim como o software para a programação foi instalado nos computadores. Por fim, uma apresentação contando um pouco sobre o projeto Meninas Digitais - UFSC foi montada.

- Etapa 8: as oficinas ocorreram no laborário LabTec. No início da oficina as alunas conheceram os objetivos do projeto Meninas Digitais - UFSC e o questionário inicial foi aplicado. Como vieram alunas de escolas diferentes, equipes mistas foram formadas. Cada grupo foi acompanhado de perto por um integrante da equipe de execução do projeto. Durante a oficina foram fornecidas as instruções passo a passo para a montagem dos robôs disponíveis no site da Lego, bem como o acompanhamento da montagem e solução de dúvidas. Cada oficina teve um intervalo para o lanche e, no final, foi aplicado o questionário de avaliação da oficina.

- Etapa 9: ao final de cada oficina, houve uma reunião de retrospectiva com a equipe de execução do projeto, onde foram registrados os aspectos positivos e negativos, visando a melhoria do processo, assim como a análise dos questionários respondidos pelas alunas.

Com o processo de planejamento e execução das oficinas definido, as próximas subseções descrevem a ferramenta escolhida, assim como detalham cada oficina.

> 6https://education.lego.com/pt-br/lessons/ev3-robot-trainer/

> 1-moves-and-turns#plano-de-aula

> 7https://forms.gle/ce7usRcvWo8pKJxJ6

> 8https://forms.gle/1MzyQ29UByNorXHHA

A ferramenta Lego Mindstorm EV3 permite a montagem do hardware e da programação. Desenvolvida visando uma ampla faixa etária, a grande variedade de peças permite a montagem de robôs mais simples até mais avançados, e a programação pode ser feita usando blocos coloridos conforme sua função: motor, sensor, som, visor, ou usando a linguagem de programação C, o ambiente para programação e conexão com o robô é disponibilizado no site da ferramenta e em lojas de aplicativo.

Além disso, conta com uma plataforma digital com planos de aula disponibilizados, permitindo que o usuário busque por séries do ensino fundamental ou médio e assunto da aula. Cada plano de aula tem descrição, tutorial da montagem do hardware, sugestão de programação em blocos, perguntas para serem desenvolvidas pelo professor e desafios.

### 3.1. Primeira Oficina

A primeira oficina foi realizada no dia 07 de outubro de 2022 e o projeto escolhido para ser executado foi a base motriz, que aparece em vários tutoriais para estudantes entre 6º e 8º ano, e é uma base com dois motores que permite que o robô seja programado para movimentação. Esse robô usa o sensor de cor para atuar como um robô seguidor de linha.

Participaram da oficina 19 alunas que foram divididas em 4 grupos de 5 meninas selecionadas aleatoriamente, mesclando meninas de três escolas públicas diferentes. A seleção de forma aletatória, tinha como intuito provocar a comunicação e interação de grupo entre as alunas. Participaram estudantes das escolas EBM Otávio Manoel Anastácio, EBM Jardim das Avenidas e EEB Nova Divinéia. As alunas se inscreveram voluntariamente para participar da oficina e a seleção ficou a cargo da Secretaria de Educação do município. Dentre elas, participaram 3 alunas do 1º ano do Ensino Médio, elas já conheciam o projeto e não tiveram a oportunidade de participar pela pausa das oficinas durante a pandemia, assim foram incluídas nessa primeira oficina.

Durante a execução da oficina, percebeu-se que o tempo estimado para a atividade de montagem do robô foi subestimado, então, apenas a base motriz foi montada, não incluindo o sensor de cor, a programação acabou sendo simplificada com a perda do sensor, sendo apenas a execução de movimentos como ir para frente e para os lados.

Ao explorar a programação, os grupos acabaram de forma espontânea, se desafiando para fazer o robô andar formando quadrados. Essa curiosidade teve início ao explorar livremente os movimentos disponíveis na programação em bloco, já que não houve uma movimentação exigida por parte dos monitores, e também, ao analisar os outros grupos, principalmente suas amigas, indo além do que o pedido e percebendo que também poderiam fazê-lo. Além disso, por conhecerem colegas de outros grupos, elas também se sentiam a vontade em pedir ajuda para suas próprias colegas. Para a aplicação dos questionários, a equipe incentivava as alunas a responderem em seus próprios celulares ou usarem os computadores e tablets disponibilizados pela equipe.

Após a oficina, a equipe do projeto se reuniu para a reunião de retrospectiva para discutir sobre dificuldades observadas pelos próprios integrantes e pelos comentários das alunas. Os principais pontos levantados foram o longo tempo focado na montagem da base motriz, ultrapassando o tempo estimado no site da Lego, que resultou em menos tempo de programação, sendo esta a parte que as alunas mais gostaram. Além disso, foi

percebida a vantagem de se mesclar alunas de diferentes escolas, ao longo da oficina, as integrantes de cada equipe se tornaram mais próximas e socializaram,

Figura 2. Oficina 1

### 3.2. Segunda Oficina

A segunda oficina aconteceu no dia 11 de novembro de 2022. Considerando os aspectos destacados na reunião de retrospectiva realizada ao final da primeira oficina optouse por deixar o robô parcialmente montado. Permitindo as meninas focarem mais na programação e na evolução da montagem de um braço para acoplar um sensor giroscópio.

Participaram da oficina 11 estudantes dos anos finais do EFII que foram divididas em 3 grupos de 4 meninas aleatoriamente, como na primeira oficina. Elas são estudantes das escolas: EBM Almerindo Manoel da Luz e Escola João Matias. O processo de seleção foi diferente da primeira oficina, essas não sabiam sobre o projeto e foram escolhidas pela escola para participar, não sendo de maneira voluntária.

Dado o maior tempo disponível à programação, a oficina foi dividida em 3 momentos, inicialmente os monitores incentivaram os grupos a entender os movimentos básicos e explorarem a rotação, andar para frente, trás e lados. Após essa compreensão, os grupos foram desafiados a fazerem seus robôs se movimentarem formando um quadrado, como todos os grupos alcançaram o desafio antes do tempo estimado, elas foram novamente desafiadas a movimentar o robô num quadrado para o lado oposto. Ao final da oficina, as meninas comentaram sentirem falta da montagem da base motriz.

Figura 3. Oficina 2

### 3.3. Terceira Oficina

A terceira oficina aconteceu no dia 02 de dezembro de 2022. Essa oficina teve um público com menor faixa etária, crianças na faixa dos 7 anos. Por este motivo, a base motriz e o

projeto do robô foi simplificado com menos peças e apenas dois motores. O projeto foi elaborado por um dos alunos de graduação voluntários do projeto. O tutorial dos passos da montagem e sugestão de programação também foi novo.

Participaram da oficina 9 alunas que foram dividas em 3 trios. Dessa vez, por muitas delas já se conhecerem e por serem crianças, decidiu-se que elas poderiam criar seus grupos por afinidade. Todas elas são alunas do 2º e 3º ano do ensino fundamental de escolas particulares da região.

As alunas se mostraram muito curiosas e interessadas na oficina, todas do grupo trabalhavam, e comentavam quando queriam participar mais. Todos os grupos tiveram interesse na parte de sons e imagens transmitidas pelo bloco robô, explorando sons de animais e carinhas que expressavam emoções. Além disso, algumas se mostraram interessadas nos sensores, que não foram explorados durante a oficina.

Figura 4. Oficina 3

## 4. Resultados

Nesta seção são apresentados os resultados levantados a partir do preenchimento de questionários disponibilizados no início e ao final de cada oficina. As respostas do questionário inicial serviram para identificar o perfil e as expectativas das meninas em relação à oficina, enquanto que as respostas do questionário final para analisar as dificuldades, facilidades e possibilidades de utilização da robótica no futuro, além de sugestões para as próximas oficinas.

Primeiramente são apresentados os resultados das duas primeiras oficinas realizadas com meninas do oitavo e nono ano do ensino fundamental e na sequência a oficina realizada com meninas do segundo ano do ensino fundamental.

### 4.1. Oficinas 1 e 2

Das 26 respondentes, apenas uma (1) havia tido contato prévio com a robótica, nenhuma delas havia programado um robô e apenas uma (1) já conhecia Lego Mindstorm EV3. A análise das expectativas em relação à oficina revelou que as expressões ”aprender coisas novas”(8), ”aprender mais sobre robótica”(6), ”aprender sobre tecnologia”(3) apareceram com maior frequência nas respostas.

No questionário final, 92,3% meninas afirmaram que seu interesse em robótica aumentou após a oficina. A Figura 5 mostra as respostas em relação à facilidade de construção do robô enquanto a Figura 6 mostra as respostas sobre a dificuldade da

programação em blocos. Como pode ser observado, três (3) alunas disseram que a oficina foi “muito fácil”, seis (6) consideraram “fácil”, 15 “nem fácil nem difícil” e duas (2) acharam “difícil”. Quanto à programação, 10 definiram como “fácil”, cinco (5) como “difícil”, oito (8) como “nem fácil nem difícil” e três (3) como “muito fácil”.

Figura 5. Facilidade da construç ão do robô

Figura 6. Facilidade de programaç ão do robô

Sobre as dificuldades encontradas durante a oficina, a Figura 7 mostra que 9 meninas não tiveram dificuldade alguma, seis (6) tiveram problemas com a programação, quatro (4) não estavam habituadas a ferramenta, três (3) tiveram dificuldade com a montagem do robô, duas (2) delas informaram que haviam muitas pessoas para poucos robôs e outras duas (2) que o grupo não funcionou bem.

Vinte e cinco alunas respoderam que acham interessante projetos de desenvolvimento de robôs, já que permitem conhecer a área e enxergar uma possibilidade de trabalho futuro. No entanto, ao serem questionadas se elas se imaginam em algum momento de vida trabalhando no desenvolvimento e aplicação de robôs, 19 meninas responderam “talvez” e somente cinco (5) reponderam “sim”.

Por fim, a oficina atingiu complementamente as expectativas de 69,3% alunas e parcialmente de 30,7% alunas. Sobre as sugestões para as proximas oficinas, 4 responderam que deveriam ser disponibilizados mais robôs para montagem e 1 sugeriu ter menos pessoas por grupo.

A análise das questões abertas foi realizada por meio do procedimento de codificação aberta da Teoria Fundamentada em Dados (do inglês, Grounded Theory )[Strauss and Corbin 2008]. Para cada resposta foram identificados os códigos (termos, expressões) mais significativos, que na sequência são analisados em relação à semântica e contabilizados.

Quando questionadas se a construção de robôs pode ajudar no desempenho escolar, as respostas abertas revelaram com maior frequência as expressões ”pode auxiliar na escola”(6) e ”auxilia na concentração”(2).

### 4.2. Oficina 3

Nesta oficina, por causa da idade das meninas, os questionários foram impressos e respondidos no papel para depois serem digitalizados. Além disso, as perguntas foram adaptadas para a faixa etária com a maioria das questões sendo de múltipla escolha. As respostas do questionário inicial indicaram que duas (2) das nove (9) meninas já tinham montado um robô, duas (2) já tinham programado um robô e duas (2) conheciam a plataforma

Figura 7. Dificuldades encontradas durante as oficinas

Lego Mindstorm EV3. Perguntadas sobre como iria ser a oficina, se iriam gostar, todas as meninas responderam positivamente.

Em relação às facilidades e dificuldades, as respostas do formulário final indicaram que três (3) acharam fácil construir o robô e seis (6) acharam ”mais ou menos”fácil construí-lo, quatro (4) tiveram facilidade na programação, uma (1) achou difícil e quatro (4) acharam ”mais ou menos”fácil programar o robô.

Quanto às dificuldade encontradas, cinco (5) não a acharam díficil, duas (2) acharam que foi muito rápida, uma (1) achou a programação difícil e uma (1) não entendia a explicação dos monitores. Todas as nove (9) meninas responderam que oficinas como essa devem ser repetidas, seis (6) tiveram suas expectativas alcançadas e três (3) tiveram suas expectativas parcialmente alcançadas.

Na questão aberta as sugestões mais frequentes foram ”levar o robô para casa”, ”fazer mais robôs”e ”criar robôs que se pareçam com animais”.

## 5. Considerações Finais

A iniciativa descrita neste artigo foi bem aceita pela academia e pelas famílias, destacando-se como as meninas podem ser motivadas a estudar e construir carreiras em STEM. Nas 3 oficinas realizadas no segundo semestre de 2022 com um público 100% feminino observou-se que a maioria delas nunca tinha tido a oportunidade de realizar atividades com kits de robótica, tanto para as alunas da rede de ensino pública quanto privada, independente da faixa etária.

A maioria dos trabalhos relacionados traz ações com foco em alunas do ensino médio. No entanto, ao longo desta experiência, percebeu-se que quanto mais novas as meninas, mais abertas elas estão para explorar a tecnologia e despertar o interesse pela área. Assim, é preciso iniciar o contato com a tecnologia já no ensino fundamental para que as alunas conheçam as oportunidades de carreira na área e minimize o impacto dos estereótipos. Outro aspecto relevante neste tipo de projeto foi o contato com estudantes

mulheres de graduação, onde as meninas podem se espelhar e vislumbrar uma carreira em STEM.

Percebe-se que ainda são escassos o número de relatos de experiência de ensino de robótica para meninas e que relatos como os desta experiência, com a descrição detalhada da metodologia e a disponibilização dos artefatos gerados, sejam importantes para estimular a replicação de mais experiências com foco em meninas. Os custos relacionados aos kits deve ser um fator que dificulta a difusão da ação, existem kits de baixo custo, que normalmente implicam em desenvolvimento da própria equipe. As escolas, por exemplo, dificilmente irão construir seus robôs, o que acaba frestringindo este tipo de ação ao meio universitário/tecnológico.

Como projeto futuro, pretende-se ampliar as estratégias incluindo treinamento para os professores atuarem como multiplicadores de atividades tecnológicas nas escolas e palestras com as famílias, como forma de potencializar os resultados das nossas ações com as meninas.

## 6. Agradecimentos

Agradecemos a PROEX/UFSC pelo apoio e financiamento. Agradecemos a todas as pessoas bolsistas, voluntárias, discentes e docentes, pela dedicação ao projeto.
