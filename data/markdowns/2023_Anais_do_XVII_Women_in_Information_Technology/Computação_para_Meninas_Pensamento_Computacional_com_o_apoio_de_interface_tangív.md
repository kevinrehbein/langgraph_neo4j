# Computação para Meninas: Pensamento Computacional com o apoio de interface tangível

Maria Adriana V. Lima, Ana Barbara C. Conti, Ana Julia A. F. Silvério, Ana R. Silvério, Gabriel C. B. S. Amaral, Gabriel C. Freitas, Jhully V. N. Leite, Laura B. Moreira

1Faculdade de Computação - Universidade Federal de Uberlândia (UFU) Uberlândia - MG - Brasil

{ maria.adriana, ana.conti, ana.silverio1, ana.roling, gabriel.amaral, gabrielcouto1, jhully.leite, laura.moreira1 } @ufu.br

Abstract. This article presents an extension project aimed at providing a short course on Computational Thinking to public high school girls. The primary objective is to encourage girls to pursue computing careers and to promote the undergraduate courses in Computer Science offered by the Federal University of Uberlândia. Alongside the unplugged Computational Thinking activities, the use of the Sphero Mini, a programmable robotic sphere, was proposed as a tangible interface for experimentation. The project involved the participation of seven volunteer undergraduate students who contributed for identifying the feasibility of the proposal, creating course content, and serving as monitors during the classes. A total of twenty spots were made available for girls enrolled in the first year of a public high school.

Resumo. Este artigo apresenta um projeto de extensão com o propósito de ofertar um minicurso de Pensamento Computacional voltado às meninas do ensino médio de uma escola pública. O objetivo é incentivar a formação de meninas nas carreiras de computação e divulgar os cursos de graduação em Computação oferecidos pela Universidade Federal de Uberlândia. De forma concorrente às atividades desplugadas de Pensamento Computacional, foi proposto o uso da Sphero Mini, uma esfera robótica programável, como interface tangível de experimentação. O projeto teve a participação de 7 graduandos voluntários que atuaram na identificação da viabilidade da proposta, produção de conteúdo e como monitores. Foram ofertadas 20 vagas para alunas do primeiro ano do ensino médio.

## 1. Introdução

A representação desigual das mulheres nas áreas de Ciência, Tecnologia e Engenharia é um dos desafios atuais em todo o mundo. Um levantamento realizado pela Sociedade Brasileira de Computação (SBC) apontou que o percentual de mulheres concluintes dos cursos de Computação no Brasil decresceu entre os anos de 2001 e 2020, de respectivamente 32,61% para 13,88% [SBC 2020]. No mesmo intervalo, os cursos de Computação em todo o país, considerando todas as modalidades, saltaram de 395 para 2279. A criação e a adoção de políticas públicas que influenciem positivamente alunas do Ensino Médio na escolha de carreiras na área de tecnologia, foi recomendada em [Moreira et al. 2018],

e diversas pesquisas e iniciativas têm sido empreendidas visando o equilíbrio de gênero, como [Medeiros et al. 2022, Souza et al. 2022].

O Grupo #include<girls>, formado por professoras da Faculdade de Computação da Universidade Federal de Uberlândia (FACOM-UFU), vem promovendo esforços para fortalecer a presença feminina em seus cursos. Neste contexto, pretendeu-se viabilizar uma ação extensionista que pudesse ser produzida, avaliada e, posteriormente, replicada para o público feminino de escolas públicas de ensino médio. A ação envolveu palestras e um minicurso de Pensamento Computacional. Dentre os objetivos, podem-se destacar:

- Concepção, execução e avaliação da ação composta de palestras e minicurso de Pensamento Computacional voltado a estudantes meninas do ensino médio;

- Levantamento de material pedagógico de Pensamento Computacional, organização, aplicação e avaliação do aprendizado;

- Experimentação de interfaces tangíveis para apoiar as atividades teóricas; e

- Apresentação de trajetórias bem sucedidas de mulheres na computação e projeção da importância da presença feminina na ciência e inovação tecnológica.

O Pensamento Computacional é uma habilidade fundamental que envolve lógica, algoritmos, padrões, abstração e avaliação [Wing 2006]. O uso de ferramentas de programação, robótica, jogos/simulações e intervenções não digitais têm apoiado o ensino de Pensamento Computacional em diversos contextos educacionais, do ensino fundamental ao médio [Shute et al. 2017, Marotti et al. 2021]. Além dos jogos e exercícios usando lápis/papel, a introdução da programação de interfaces tangíveis permite aumentar a motivação, engajamento, diversificar percepções e experiências, não só na dimensão cognitiva, mas também na dimensão afetiva [Kotsopoulos et al. 2017]. No intuito de experimentar o uso da interface tangível apoiando o ensino de Pensamento Computacional, escolheu-se a Sphero Mini, que pode ser programada para locomover-se em velocidade, tempo e direção determinadas, iluminar-se com diferentes cores e executar programas.

A ação extensionista envolveu um conjunto de professoras, alunas e alunos voluntários da FACOM-UFU, no período de agosto a dezembro de 2021. As palestras e aulas do minicurso aconteceram nas dependências da escola, aos sábados. Foram ofertadas 20 vagas para alunas do primeiro ano do ensino médio de uma escola pública estadual.

## 2. Metodologia

Este trabalho seguiu uma abordagem metodológica qualitativa. Diversos registros sobre o progresso dos participantes nas atividades e relativos às interações com os monitores possibilitaram reunir informações para análise do aprendizado e das competências necessárias ao enfrentamento dos desafios propostos.

Foram planejadas duas palestras: abertura e encerramento. A palestra de abertura, com duração de uma hora, teve como objetivo apresentar o projeto de extensão e destacar as diversas realizações na computação que tiveram mulheres como principais agentes. A palestra final visou, principalmente, a divulgação dos cursos de computação da UFU e das ações do grupo #include<girls>.

As aulas do minicurso de Pensamento Computacional foram estruturadas em dois eixos: ( i ) Teórico: formas utilizadas para representar dados pelos computadores (números binários), algoritmos e métodos computacionais de uso frequente no cotidiano, e ( ii )

Prático com interface tangível: treino de programação com a Sphero Mini para construir formas, movimentos e consolidar o conteúdo abordado.

A Sphero Mini vincula-se a dispositivos móveis e pode ser programada em um aplicativo, denominado Sphero Edu, de três maneiras distintas [SpheroEdu ]:

1. Desenho: tela em branco para desenho livre da trajetória a ser executada.

2. Bloco: linguagem visual com blocos condicionais e de repetição, além daqueles para ativação do motor, sensores e LED.

3. Texto: linguagem JavaScript com apoio de uma JavaScript Wiki para Sphero Mini.

A Tabela 1 retrata conteúdo e sequência definidos para o ensino do Pensamento Computacional, bem como atividades práticas de apoio e experimentação. O planejamento do minicurso envolveu a preparação de 9 aulas, com duração de 1h20min cada, totalizando 12 horas, em que cada aula foi preparada por graduandos voluntários, sob a supervisão de uma professora, utilizando como base o programa definido em [Bell and Vahrenhold 2018].

|Número|Conteúdo Teórico|Programação com a Sphero Mini|
|---|---|---|
|1|Números binários e operações.|Desenho: percursos e movimento.|
|2|Representação de valores: direção,velocidade e tempo.|Blocos: percursos livres. Jogo de Mini Boliche.|
|3|Introdução aos algoritmos: variáveis e fórmulas. Leis de Newton.|Blocos: percurso puxando carga. Jogo de salto em distância.|
|4|Algoritmos: sequência de comandos e seleção.|Blocos: percurso com colisão e mudança de direção. Jogo deping-pong.|
|5|Algoritmos: estruturas de repetição. Sequência de Fibonacci.|Blocos: espiral de Fibonacci.|
|6|Algoritmos: Busca Linear e Binária. Atividade: Batalha naval.|Blocos: formas geométricas.|
|7|Algoritmos: Ordenação. Atividade: Comparandopesos.|Blocos: geração de números aleatóriospara direção e velocidade.|
|8|Algoritmos: Ordenação. Atividade: Dividirpara conquistar.|Blocos: uso de números aleatórios para tempo,direção,velocidade e cor do LED.|
|9|Algoritmos: Redes complexas. Vértices e arcos de ligação.|Blocos: desafio do labirinto.|

Tabela 1. Conteúdo programático do minicurso.

Os roteiros das atividades práticas seguiram a proposta de [Hadfield et al. 2018] e nas primeiras atividades práticas os comandos de rolagem, giro, parada e acendimento do LED foram consolidados para o domínio dos recursos do dispositivo. As práticas seguintes introduziram gradualmente controles lógicos de seleção, repetição, captura de informação de sensores, uso de variáveis e operadores lógicos e matemáticos. A Figura 1 apresenta a esfera utilizada nas atividades do minicurso.

Figura 1. Sphero Mini e vista da parte interna.

A Sphero Mini é composta de rodas internas que conduzem a bola, rolamento para manter as rodas em contato interno com a esfera, processador que combina informações de acelerômetro e giroscópio para precisão nos movimentos, comunicação Bluetooth e LED multicor. Em relação ao funcionamento, a Sphero Mini deve estar pareada a um dispositivo controlador (celular ou tablet) e ser calibrada. Uma pequena luz azul deve ser posicionada, via dispositivo, na direção do usuário programador para fixar a direção 0°, que é a direção inicial (à frente do usuário), para rotação e rolagem. A partir deste momento, a Sphero Mini pode ser programada e ter seu código executado corretamente.

## 3. Preparação e Execução do Minicurso

As atividades do minicurso de Pensamento Computacional se basearam no livro Computer Science Unplugged [Bell et al. 2011] e no material de apoio disponível em [SpheroEdu ]. A preparação das aulas considerou os eixos teórico e prático, e, como exemplo, pode-se destacar a aula 5 correspondente à sequência de Fibonacci. O material didático teórico seguiu a abordagem definida em [Silveira 2020] com as seções: ( i ) a história de Leonardo de Pisa e o problema dos coelhos, ( ii ) aplicações da sequência de Fibonacci, ( iii ) construção da série de números, e ( iv ) propriedades geométricas decorrentes da série. Além destas 4 seções, uma lista de exercícios para fixação do conteúdo integrou o material.

Um roteiro detalhando os passos necessários para a implementação da espiral de Fibonacci foi proposto para a aula prática. Os comandos de fixar velocidade e girar ( speed e spin, respectivamente) foram utilizados para formar quadrantes de movimentos circulares, com ângulo de 90°. O tempo para cada quadrante, trecho da espiral, foi dado pelos números da série de Fibonacci. A Figura 2 mostra a codificação, a espiral, e a proposta de usar uma caneta, presa à um suporte (copo), para traçar a espiral em uma superfície [SpheroEdu ].

Figura 2. Prática da Sequência de Fibonacci. Fonte: [SpheroEdu ].

As demais aulas do minicurso seguiram esta abordagem teórico-prática de forma que os alunos pudessem compreender e experimentar o Pensamento Computacional com atividades mão-na-massa. A Sphero Mini se mostrou uma interface tangível viável tanto para a elaboração das atividades, quanto para a execução. O aplicativo de programação Sphero Edu dispõe também de um robô virtual (Virtual Bot - BETA) para a simulação do código sem o uso da Sphero Mini. Esta opção contempla, entretanto, apenas os comandos básicos de rolagem, e pôde ser utilizada somente nas aulas 1 e 2.

## 4. Avaliação e Resultados

As aulas do minicurso foram ministradas por 7 graduandos voluntários da FACOM-UFU, sendo 5 graduandas e 2 graduandos. O minicurso aconteceu aos sábados e as vagas preenchidas por meninas ficaram aquém dos 40%, ficando as restantes disponibilizadas aos alunos interessados. Esta conduta foi adotada para evitar contratempos e segregação, inadequados ao ambiente escolar.

Um formulário de adesão ao projeto foi confeccionado com questões sobre informações do aluno, perfil, futuro profissional e conhecimento prévio de programação. Nenhuma das alunas tinha experiência prévia em programação, e apenas 2 marcaram a área da tecnologia como carreira profissional pretendida. Apenas 1 assinalou a intenção de cursar Computação no ensino superior. A avaliação do aprendizado no minicurso foi realizada pela aplicação e correção de exercícios e pelo registro de observações dos graduandos voluntários no transcorrer das atividades teóricas e práticas. Ao serem questionados sobre como levariam o Pensamento Computacional para o dia-a-dia, houve respostas como: posso resolver um problema passo a passo e consigo organizar tarefas de forma lógica. Sobre o que mais gostaram de aprender, as respostas foram, em sua maioria, relacionadas com a programação da Sphero Mini, usando celular.

Considerando o fato de apenas uma Sphero Mini estar disponível para a turma por ser um recurso de custo elevado, o plano de atividades práticas considerou o seu compartilhamento, o que reduziu o tempo de uso, e, consequentemente, as possibilidades de teste, refinamento e correção de erros nos códigos desenvolvidos. Ainda, o fato das aulas acontecerem aos sábados, e não serem dias letivos e obrigatórios, contribuiu para ausência e dispersão dos alunos. Apenas 6 estudantes concluíram a ação, sendo 2 meninas e 4 meninos. Conquanto a divulgação do minicurso de Pensamento Computacional tenha tido como atrativo uma interface tangível, a atração de meninas para ações de envolvimento com a tecnologia ainda demanda esforços no sentido de identificar abordagens que alcancem maior engajamento.

## 5. Conclusões e Ações Futuras

A atividade extensionista apresentada neste artigo pretendeu a conjugação de material de aprendizagem, tanto teórico quanto prático de Pensamento Computacional, e proporcionou a participação feminina na experimentação de programação com interface tangível e linguagem de programação visual. A Sphero Mini se mostrou adequada à experimentação dos conceitos iniciais da computação, permitindo a abordagem de conceitos matemáticos e da física de forma exploratória e lúdica.

A maioria dos participantes não tinha conhecimento dos cursos da área de Computação da UFU, e a presente ação ampliou possibilidades de carreiras a serem escolhidas, enfatizando a área tecnológica. Um novo projeto de extensão, visando a continuação das ações expostas neste trabalho, foi aceito, com financiamento de duas bolsas de incentivo para estudantes de graduação, com início no segundo semestre de 2023. A nova proposta prevê a oferta do minicurso para meninas em contraturno, e sua integração com as disciplinas de física e matemática, oportunizando experiências que utilizem a interface tangível com conteúdos ajustados aos temas abordados em sala de aula.

## 6. Agradecimentos

O grupo #include<girls> agradece a Escola Estadual Joaquim Saraiva pela acolhida do projeto e a Pró-Reitoria de Extensão da UFU pelo apoio na ação extensionista.
