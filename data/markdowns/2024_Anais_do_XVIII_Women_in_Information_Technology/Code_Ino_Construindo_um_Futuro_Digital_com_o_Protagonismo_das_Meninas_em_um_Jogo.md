# Code.Ino: Construindo um Futuro Digital com o Protagonismo das Meninas em um Jogo para Programação

Bianca P. Castro, Hanani E. F. Soares,

Thamires P. S. Schiavini, Maristela Holanda, Aleteia Araujo

1 Universidade de Brasília (UnB), Brasília - DF

{castro.bianca, thamires.pontes, hanani.emanuelle}@aluno.unb.br

{aleteia, maholanda}@unb.br

Abstract. This paper highlights the importance of understanding programming logic, regardless of the paradigm used. It introduces a digital game, Code.Ino, developed by undergraduate students in computing-related courses, designed to teach Arduino programming in a playful way. The game aims to help learners understand Arduino components and programming structure through distinct phases. It was designed to be used by girls and boys, but the game’s leading role is given to women, emphasizing that programming is also a girl’s thing. The results indicated success in awakening girls’ interest in the subject with representation.

Resumo. Este artigo destaca a importância da compreensão da lógica de programação, independentemente do paradigma utilizado. Ele introduz um jogo digital Code.Ino, desenvolvido por alunas de graduação em cursos relacionados à Computação, projetado para ensinar programação em Arduino de forma lúdica. O jogo visa auxiliar no aprendizado dos componentes do Arduino e na estrutura de programação por meio de fases distintas. Ele foi projetado para ser usado por meninas e meninos, mas o protagonismo do jogo é dado às mulheres, enfatizando que programação também é coisa de menina. Os resultados indicaram sucesso em despertar o interesse das meninas pelo assunto com a representatividade.

## 1. Introdução

Diversos pesquisadores apoiam o ensino de programação nas escolas como uma forma de adquirir fluência digital e habilidades de projeto [Medeiros et al. 2020, Silva and Falcão 2020, Garcêz and Oliveira 2022]. Autores como Resnick, criadores da linguagem Scratch, argumentam que a programação não se resume a habilidades técnicas, mas também inclui a capacidade de criar e desenvolver novas tecnologias [Resnick et al. 2009].

Os jogos educacionais são destacados como ferramentas motivacionais no processo de ensino-aprendizagem em programação, proporcionando um ambiente lúdico e interativo para os alunos [Garcêz and Oliveira 2022]. O uso do Arduino, uma plataforma de prototipagem eletrônica open-source, é mencionado como uma forma eficaz de introduzir conceitos de programação e hardware [Uzunca and Jansen 2016].

Assim, levando-se em conta os esforços de proporcionar um ensino eficaz e engajador para as estudantes do Ensino Básico, as autoras deste trabalho desenvolveram um

jogo chamado Code.Ino. Logo, o objetivo deste trabalho é apresentar a concepção e o desenvolvimento do jogo digital educacional Code.Ino, cuja utilização pretende apoiar o processo de ensino-aprendizagem de programação por meio de Arduino. A equipe desenvolvedora do jogo Code.Ino é formada só por mulheres, as quais projetaram um jogo para ser usado por meninas e meninos, mas cujo protagonismo do jogo é dado às mulheres. Este jogo deve permitir que o estudante possa conhecer os conceitos envolvidos, tanto na parte de hardware quanto na parte de software do Arduino.

O artigo está estruturado, além desta introdução, em mais quatro seções. A Seção 2 detalha a fundamentação teórica desta proposta. A Seção 3 apresenta o jogo Code.Ino e os detalhes do seu desenvolvimento. A Seção 4 descreve a avaliação do jogo, feita com mais de 50 jogadores. Por fim, a Seção 5 conclui o artigo com as considerações finais e os trabalhos futuros.

## 2. Contextualização

Programar é fundamental para construir algoritmos, sequências de passos que transformam entradas em saídas [Thomas H. Cormen 2002]. O ensino de lógica de programação pode ser desafiador sem a metodologia adequada, mas métodos educacionais lúdicos são recursos facilitadores [Silva and Falcão 2020].

O Arduino, uma plataforma de microcontrolador de código aberto, tem ganhado popularidade devido à sua facilidade de uso e natureza aberta, permitindo a realização de "computação física". O Arduino Uno, uma das placas populares da família, oferece diversas portas de E/S para conexão com dispositivos externos, sendo uma ferramenta introdutória para aprender a programar em C++ adaptado para a plataforma [de Medeiros and Wünsch 2019].

## 3. Jogo Code.Ino

O Code.Ino é um jogo digital educativo, desenvolvido para a plataforma mobile. O objetivo principal é ser uma ferramenta auxiliadora no processo de ensino-aprendizado de programação em Arduino para alunos do ensino médio e fundamental. Assim, a proposta é que o jogador aprenda, em cada fase do jogo, de maneira criativa e lúdica, os componentes de uma placa de Arduino e a lógica envolvida no processamento dos dados. Na última fase do jogo, o jogador deve ser capaz de implementar um projeto completo a partir dos conhecimentos obtidos ao longo das fases. Como consequência, espera-se que o jogo Code.Ino, ao ser usado como ferramenta de apoio nas aulas de programação, otimize o processo de ensino-aprendizado de programação nas escolas de ensino básico.

O jogo tem sido desenvolvido por uma equipe de mulheres universitárias, por meio da engine Unity e da linguagem C. Assim, com o jogo Code.Ino, o jogador aprenderá a lógica de programação e o básico da linguagem C++, que é a linguagem usada no Arduino. Para que o jogador aprenda, de maneira lúdica, os conceitos relacionados ao hardware e ao software do Arduino, especialmente sobre programação e seus componentes, o jogo foi estruturado em dez fases. Cada fase busca ensinar um componente relacionado ao Arduino. Após o ensino de cada componente, há um mini jogo usado para avaliar o nível de conhecimento adquirido pelo usuário, mediante o que lhe foi ensinado. A Figura 1 apresenta a tela inicial do jogo Code.Ino.

Figura 1. Tela inicial e menu do Jogo Code.Ino.

Figura 2. Lado direito da sala.

Figura 3. Lado esquerdo da sala.

O jogo acontece em um ambiente escolar. Ele começa com a personagem Ame, da Figura 4, indo para sua escola e descobrindo um projeto de robótica chamado Meninas.comp. Assim, a personagem Ame entra no projeto em sua escola, como uma atividade extracurricular, para aprender mais sobre robótica e programação em Arduino. O usuário pode fazer com que a personagem Ame ande pela sala, e, dependendo do caminho que ela faz, aparecem opções de interações dela com objetos ou com os demais personagens. Assim, o jogo vai direcionando a personagem para uma nova fase.

A personagem principal se une a um projeto de computação na Universidade de Brasília, sob a orientação da professora Carla, conhecida como Carlona. Ela fica impressionada ao ver várias meninas envolvidas em programação no laboratório. No primeiro dia, expressa sua surpresa e alegria ao encontrar tantas meninas ativas na área de TIC (Tecnologia da Informação e Comunicação). Após conhecer as novas amigas, a personagem principal inicia a sua aventura pelo mundo do Arduino. Assim, a cada componente, personagem ou item que ela interagir, fará com que ela seja levada para outra parte do jogo, proporcionando um lúdico e interessante aprendizado sobre hardware, software, e componentes eletrônicos. Após finalizar as fases, Ame é desafiada a fazer um projeto completo com Arduino, que utilize os componentes estudados nas fases anteriores. O jogo está disponível para download para os dispositivos com Android.

O jogo acontece todo em uma sala de aula, com uma disposição diferente do convencional. De um lado, há mesas e cadeiras, conforme mostrado na Figura 2; enquanto do outro lado há balcões com computadores, como evidenciado na Figura 3. Em cada fase do

Figura 4. Ame (mascote do Meninas.comp) e a personagem do jogo.

Figura 5. Tela das fases do jogo.

jogo, um elemento do Arduino é introduzido, junto com componentes relacionados à sua programação. Desse modo, em cada fase são abordados os componentes: hardware, software, resistores, LEDs, protoboards, botões, chaves, sensores, motores, displays, ponte H e módulos de comunicação. Após completar cada fase, a personagem enfrenta um desafio que inclui um questionário sobre os elementos estudados. Ao alcançar uma pontuação de 3 ou mais, ela avança para a próxima fase ativando um jumper na tela de fases, que conecta à fase seguinte. A Figura 5 mostra todas as fases do jogo Code.Ino em sequência

## 4. Metodologia

A metodologia empregada no jogo foi elaborada para garantir uma aprendizagem lúdica e dinâmica, na qual o jogador pode utilizar sua curiosidade e criatividade para assimilar conceitos de programação, especialmente, voltados para o Arduino. O jogo foi desenvolvido para garantir a mobilidade do jogador, possibilitando seu uso tanto em ambiente escolar quanto em casa. Assim, o jogo pode ser baixado no celular e jogado de maneira offline. Ao iniciar o jogo, existe um botão para aprender como jogar. A Figura 6 apresenta o tutorial do jogo. A metodologia de ensino-aprendizagem aplicada no jogo foi estruturada em dez fases. Dessas dez fases, as nove primeiras foram estruturadas internamente em duas etapas diferentes para promover uma aprendizagem abrangente e progressiva. A décima fase é diferenciada das anteriores para consolidar o conhecimento adquirido ao longo do jogo Code.Ino.

As nove primeiras fases são divididas em duas etapas cada uma: a primeira etapa introduz os conceitos teóricos relevantes por meio de interações com os personagens do jogo, fornecendo fundamentos e princípios a serem aplicados. O jogador também tem acesso a materiais de estudo, como textos explicativos e imagens ilustrativas, conforme apresentado na Figura 7. Já na segunda etapa, o jogador é direcionado para um quiz prático, o qual pode ser visto na Figura 8, realizado em um computador dentro do ambiente virtual do jogo. Esse quiz serve como avaliação para verificar a compreensão e a retenção dos conhecimentos teóricos adquiridos na primeira etapa. Ao obter um número mínimo de acertos no quiz, conforme apresentado na Figura 9, o jogador pode avançar para a próxima fase do jogo (conforme apresentado na Figura 5), mantendo assim o progresso na aprendizagem de programação com Arduino.

Na décima e última fase, o jogo Code.Ino oferecerá um novo tipo de desafio ao jogador. Em vez de seguir o padrão das nove etapas anteriores, esta fase se concentrará em ensinar ao jogador como utilizar outras ferramentas online relacionadas ao Arduino para desenvolver um projeto a partir do zero. Nesta fase especial, o jogador será guiado por meio de diferentes ferramentas online disponíveis para programação e desenvolvimento com Arduino, incluindo o aprendizado sobre softwares de simulação, ambientes de desenvolvimento integrado (IDEs) online, plataformas de prototipagem virtual, entre outros recursos relevantes.

## 5. Resultados Preliminares

Para uma avaliação preliminar da versão demo do jogo Code.Ino, realizou-se uma pesquisa via formulário online. O objetivo foi obter uma análise crítica sobre a jogabilidade e a proposta de um jogo para ensinar programação em Arduino. A versão demo do jogo foi avaliada por 55 pessoas em um período de 14 dias. Os respondentes tinham idades

Figura 6. Tela de tutorial.

Figura 7. Diálogo da aula.

Figura 8. Quiz da Fase 2.

Figura 9. Resultado do Quiz.

entre 11 e 63 anos. Dentre esses, 63, 8% identificaram-se como mulheres cis, 34, 0% como homens cis e 2,2% como homens trans. Em relação à escolaridade dos respondentes, 51, 9% estão no Ensino Fundamental, 33, 3% no Ensino Médio e 14, 8% já possuem graduação.

Com o intuito de identificar se o jogo deveria ser direcionado para um grupo específico de jogadores, perguntou-se: “Se o jogo é destinado a um tipo de público específico?” Dentre os respondentes, 70, 2% responderam que “sim” e o restante disse “não”. Para os que responderam sim, foi questionado: “Para quem o jogo foi desenvolvido?” A maioria disse que o jogo era para iniciantes em programação e estudantes. Em relação à percepção dos jogadores quanto ao protagonismo das meninas no jogo, perguntou-se: “O que você achou da personagem principal ser uma menina?” Neste caso, 87, 2% dos estudantes afirmaram que foi algo muito bom, e 12, 8% disseram que foi bom. Além disso, perguntou-se como eles se sentiram jogando com uma personagem feminina. As meninas responderam que gostaram muito, achando importante e se sentiram representadas; já os rapazes, em sua maioria, acharam tranquilo e interessante. A pesquisa também avaliou o fato de ter um jogo digital para ensinar Arduino. Neste caso, 76, 7% dos estudantes afirmaram ser muito bom, e 23, 3% disseram ser bom. Além disso, foi perguntado o que eles acharam de como o jogo foi organizado. As respostas foram positivas, pois a grande maioria (92, 3%) afirmou que achou o jogo muito bom.

## 6. Conclusão

Este artigo apresentou o jogo digital Code.Ino, que é um jogo desenvolvido por um grupo de mulheres universitárias que fazem parte do projeto Meninas.comp. O objetivo principal é ensinar, de forma lúdica e divertida, o Arduino e a programação em C++, que é uma linguagem utilizada no Arduino. O jogo é baseado na ideia de ativar, a cada fase, a curiosidade das pessoas em conhecer um pouco mais sobre o mundo da tecnologia. Assim, como trabalho futuro, planeja-se que as fases implementadas tenham mais mini desafios que servem para treinos e tenham som.

## Agradecimentos

As autoras agradecem a todas e todos que fizeram (e fazem) parte da história do Projeto Meninas.comp, especialmente, aos que participaram da avaliação do jogo Code.Ino. As autoras BPC e HEFS agradecem à FAP-DF pelas bolsas de PIBITI. AA agradece ao CNPq e CAPES - Código de Financiamento 001.
