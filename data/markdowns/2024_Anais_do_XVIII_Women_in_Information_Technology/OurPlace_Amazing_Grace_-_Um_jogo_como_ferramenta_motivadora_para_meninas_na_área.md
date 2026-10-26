# OurPlace: Amazing Grace - Um jogo como ferramenta motivadora para meninas na área de STEM

Paula Y. Nizer, Isabel Ap. Duarte,

Carolina Paula de Almeida, Sandra Mara Guse Scós Venske

1 Departamento de Ciência da Computacão (DECOMP)

Universidade Estadual do Centro Oeste (UNICENTRO) Alameda Elio Antonio Dalla Vecchia, 838 – Vila Carli – CEP 85040-167 Guarapuava, PR – Brasil

{ paulaynizer,isabel.duarteeh } @gmail.com, { carol,ssvenske } @unicentro.br

Abstract. In STEM (Science, Technology, Engineering, and Mathematics) fields, female participation is still small compared to male participation. However, it is important to recognize the significant role of women who have contributed to the history of these fields. Among these prominent figures is Grace Hopper, recognized as the coder of the first compiler. This study focused on the development of a game called OurPlace: Amazing Grace, which highlights the importance of women in STEM and aims to encourage more girls to consider these fields of study. The game aims to stimulate logical reasoning through mini puzzles while narrating events from Grace Hopper’s life.

Resumo. Em áreas STEM (Science, Technology, Engineering and Mathematics), a participação feminina ainda é pequena em comparação com a masculina. No entanto, é importante reconhecer o papel significativo das mulheres que têm contribuído para a história destas áreas. Entre essas figuras proeminentes está Grace Hopper, reconhecida como a codificadora do primeiro compilador. Este estudo concentrou-se no desenvolvimento de um jogo, chamado OurPlace: Amazing Grace, que destaca a importância das mulheres na STEM e busca incentivar mais meninas a considerarem essas áreas de estudo. O jogo visa estimular o raciocínio lógico por meio de mini quebra-cabeças, ao mesmo tempo em que narra eventos da vida de Grace Hopper.

## 1. Introdução

A paisagem acadêmica atual na área de STEM ( Science, Technology, Engineering and Mathematics ) apresenta uma marcante discrepância entre os gêneros masculino e feminino. De acordo com dados estatísticos do [IBGE 2024], a menor representatividade das mulheres em cursos de graduação ocorre naqueles relacionados à Computação e Tecnologias da Informação e Comunicação (TIC), totalizando apenas 15,0%. Este número também é inferior ao registrado em 2012, que foi de 17,5%. Uma das principais dificuldades enfrentadas pelas mulheres na área está associada à significativa taxa de evasão nos últimos anos. As causas subjacentes a esse afastamento são multifacetadas, envolvendo questões culturais, históricas, sociais e até mesmo aspectos psicológicos. No entanto, uma razão mais direta é evidente: as meninas na área STEM não se sentem devidamente representadas [Morais and Morais 2020].

Diante desse contexto, é evidente a necessidade imperativa de promover a inclusão das mulheres nas áreas tecnológicas. Neste sentido, a Organização das Nações Unidas para a Educação, a Ciência e a Cultura (UNESCO), agência especializada das Nações Unidas (ONU) possui uma recente iniciativa, denominada #EDUCASTEM2030, para reverter a desigualdade de acesso nas áreas STEM enfrentada pelas meninas/mulheres [UNESCO 2022]. A aprendizagem por meio de jogos digitais está entre as estratégias abordadas pelo #EDUCASTEM2030, sendo uma abordagem promissora para alcançar o objetivo do projeto.

Conforme proposto por [De Carvalho 2015], a Aprendizagem Baseada em Jogos (GBL de Game-Based Learning ) é uma metodologia pedagógica que tem foco na concepção, desenvolvimento, uso e aplicação de jogos na educação e na formação. A concepção de [Santos et al. 2021] complementa essa perspectiva, destacando que o ensino por meio de jogos tem o potencial de envolver os alunos em uma experiência de aprendizagem única. Assim, essa estratégia pode ser utilizada para promover a aprendizagem de maneira mais divertida e envolvente, além de aumentar a visibilidade de temas importantes.

Neste trabalho foi desenvolvido um jogo 2D, denominado OurPlace: Amazing Grace, destinado a dispositivos móveis e computadores pessoais no estilo de jogo Point and Click Adventure. Essa categoria de jogos, conforme descrito por [Vraneˇsevi´c 2014], enfoca o diálogo e a resolução de quebra-cabeças, avançando na narrativa por meio de interações de apontar e clicar na tela. O enredo do jogo foi inspirado na vida de Grace Hopper, reconhecida como a inventora do primeiro compilador e do termo bug. Portanto, o jogo apresenta desafios e elementos que refletem as situações enfrentadas por Grace ao longo de sua vida.

O principal objetivo deste trabalho foi utilizar a aprendizagem baseada em jogos como uma ferramenta, por meio da plataforma Unity, para promover a participação das mulheres nas áreas de STEM e aumentar o conhecimento sobre modelos femininos nesta área. Isso foi alcançado ao longo do jogo, o qual narra a história de uma figura feminina proeminente, enquanto estimula o pensamento lógico por meio de uma abordagem lúdica.

O restante deste artigo está organizado como segue. Na Seção 2, são apresentados os conceitos necessários para entendimento do trabalho, bem como projetos similares existentes. Na Seção 3, detalhes sobre o processo de criação do jogo são explorados, englobando enredo, modelagem e implementação. Os resultados e suas implicações são debatidos na Seção 4. As conclusões e apontamentos para trabalhos futuros são apresentados na Seção 5.

## 2. Fundamentação Teórica

Esta seção define os principais conceitos necessários para o desenvolvimento deste trabalho. Inicialmente, são apresentados os conceitos de aprendizagem baseada em jogos, incluindo o estilo de jogo point and click adventure (Seção 2.1). Em seguida, a vida de Grace Hopper é brevemente apresentada (Seção 2.2). Por último, são tratados alguns trabalhos correlatos na Seção 2.3.

### 2.1. Aprendizagem baseada em jogos

De acordo com [Pivec et al. 2003], a maioria dos pesquisadores conceitua a aprendizagem como uma construção multidimensional de habilidades de aprendizado, resultados de aprendizagem cognitiva, como conhecimento procedimental, declarativo e estratégico, e atitudes. O modelo de aprendizagem baseado em jogos é usado na educação formal com muito sucesso, especialmente em treinamentos militares, de medicina, físicos, entre outros.

De acordo com [De Carvalho 2015], a Aprendizagem Baseada em Jogos (GBL - Game-Based Learning ) é uma metodologia pedagógica centrada na criação, desenvolvimento, uso e aplicação de jogos na educação e formação. A visão apresentada por [Santos et al. 2021] complementa essa perspectiva, enfatizando que o ensino por meio de jogos possui o potencial de envolver os alunos em uma experiência de aprendizagem única. Dessa forma, essa estratégia pode ser utilizada para tornar o aprendizado mais divertido e envolvente, além de aumentar a visibilidade de temas importantes.

No entanto, apesar do reconhecimento do potencial dos jogos na educação, é importante destacar a disparidade entre o interesse dos alunos por videogames e sua disposição para atividades escolares tradicionais. [Prensky 2003] ressalta essa diferença e destaca a necessidade dos educadores de capitalizarem a motivação intrínseca proporcionada pelos jogos, adaptando suas práticas pedagógicas para engajar os alunos. Para que a gamificação seja realmente efetiva, isto é, aplicar mecanismos de jogos para motivar e ensinar de forma lúdica, é necessário considerar os princípios da teoria da aprendizagem e os fundamentos do design de jogos [Jan L. Plass and Kinzer 2015].

Existem diversos estilos de jogos. Neste trabalho foi aplicado o estilo point and click adventure. De acordo com [Vraneˇsevi´c 2014], jogos point and click adventure são focados no diálogo e na resolução de quebra-cabeças em que o progresso do jogo se dá apontando e clicando. Jogos desse gênero funcionam bem no contexto de aprendizagem baseada em jogos uma vez que dependem da capacidade do jogador em resolver quebracabeças interagindo com o cenário para avançar no jogo [Pérez-Colado et al. 2019]. Quebra-cabeças, no contexto deste trabalho, são pequenos desafios de raciocínio lógico.

Outros estudos referem-se a jogos, em geral, como uma ferramenta de ensino promissora e uma estratégia favorável para destacar personalidades femininas nas ciências [Silva et al. 2021] [Angeli et al. 2020] [Lopes et al. 2023] [Vinhal and Odakura 2023], considerando a crescente diversidade de mídias aplicadas ao lazer e à aprendizagem, com um propósito lúdico [Milson et al. 2020]. Portanto, a vida de Grace Hopper será abordada aqui, por meio de um jogo do tipo point and click adventure.

### 2.2. Grace Hopper

Grace Murray Hopper nasceu em 9 de dezembro de 1906 na cidade de Nova York e é uma figura de referência devido às suas significativas contribuições para o universo da programação. Dentre elas estão a criação do conceito de biblioteca, o desenvolvimento do primeiro compilador da história, a criação da linguagem de programação Flow-Matic, sua participação na criação da linguagem COBOL e seu trabalho na programação da série de computadores Mark II [Morais and Morais 2020].

Além de realizações notáveis, Grace Hopper também é conhecida por popularizar o termo bug. Enquanto trabalhava no computador Harvard Mark II, Hopper descobriu

um problema no sistema que foi causado por um inseto que ficou preso em um dos relés. Ela e sua equipe removeram o inseto e anotaram o incidente em um livro de registro, com a anotação “ first actual case of bug being found ”[Gürer 2002]. Desde então, o termo bug tornou-se uma palavra comum na programação, referindo-se a um erro ou falha no sistema. Grace Hopper também usou o termo debugging para se referir ao processo de encontrar e corrigir erros em um programa [Beyer 2009].

### 2.3. Trabalhos Correlatos

Nesta seção, são discutidos alguns trabalhos que abordam jogos com temáticas voltadas para mulheres nas ciências, visando promover o conhecimento sobre figuras importantes na área e incentivar a participação feminina em STEM.

- Computasseia [Alencar et al. 2019] este trabalho sugere a utilização de um jogo de cartas impresso como meio de promover o conhecimento sobre a história da computação. Esta abordagem não requer conhecimento prévio e oferece uma maneira lúdica e educativa de explorar o tema, tornando-o acessível para pessoas de diferentes idades e níveis de conhecimento.

- Personalities [de Oliveira et al. 2019] este jogo de cartas impressas visa destacar personalidades menos conhecidas na área de computação, como Hedy Lamarr e Ada Lovelace, enquanto promove discussões sobre questões de gênero. Requer conhecimento prévio sobre o tema do jogo e oferece uma plataforma para debates e reflexões sobre a presença feminina na computação.

- Quem Sou Eu (Elas na Ciência) [Milson et al. 2020] corresponde a um site com um quiz destinado a promover o conhecimento sobre mulheres importantes na ciência. O jogo é interativo e exige algum conhecimento prévio para responder às perguntas, mas oferece uma forma envolvente de aprendizado e incentivo à participação feminina na área. O jogo utiliza as linguagens HTML, CSS e JavaScript.

- Ajudando Marie (Elas na Ciência) [Milson et al. 2020] outro projeto baseado em um website, “Ajudando Marie” busca ensinar sobre a história de uma importante cientista, servindo como uma fonte de inspiração para o público. O jogo precisa de acesso à Internet e foi disponibilizado no formato de website. No desenvolvimento foram utilizadas as linguagens HTML, CSS e JavaScript.

- Jogo da Memória (Elas na Ciência) [Milson et al. 2020] esse jogo de memória online foi projetado para transmitir conhecimentos sobre seis mulheres importantes para a computação: Ada Lovelace, Carol Shaw, Frances Allen, Grace Hopper, Jean Sammet, Mary Kenneth Keller. Requer acesso à Internet e foi desenvolvido utilizando as linguagens HTML, CSS e JavaScript.

- Mundo Bit Byte [Briceño et al. 2021] é um jogo para dispositivos móveis projetado para disseminar conhecimento sobre mulheres na computação e estimular meninas do ensino fundamental e médio a considerarem carreiras na área de tecnologia. Não exige conhecimento prévio, nem acesso à Internet, sendo desenvolvido na plataforma Unity.

- Peg.Ada [Vinhal and Odakura 2023] é um jogo com o propósito de educar as meninas com relação à importância da proteção de sua privacidade e segurança online, orientando-as sobre ética e segurança digital com exemplos de como lidar com determinadas situações na Internet. O Peg.Ada não exige conhecimento prévio, porém requer acesso à Internet, sendo desenvolvido na plataforma Unity.

O OurPlace: Amazing Grace se distingue dos jogos descritos nesta seção, principalmente, devido ao seu gênero de jogo, o point and click adventure. Além disso, destaca-se por não requerer conhecimento prévio do assunto e por ser desenvolvido para computadores e para dispositivos móveis. Seu objetivo central é ilustrar a relevância das mulheres na computação por meio da narrativa de Grace Hopper, ao mesmo tempo em que busca estimular a participação feminina em cursos relacionados à área da computação.

## 3. Desenvolvimento

Esta seção retrata o processo de desenvolvimento do jogo OurPlace: Amazing Grace desde a descrição e modelagem até a criação dos elementos gráficos e implementação.

Neste trabalho foi utilizada a Unity [Alves 2019] como ferramenta de desenvolvimento principal. A escolha se deu devido a sua capacidade de desenvolver jogos 2D e 3D com qualidade gráfica, tanto para ambientes desktop (Windows, MacOS ou Linux) ou dispositivos móveis (Android). A Unity é um motor de jogo bastante difundido tanto pelos recursos oferecidos, os quais facilitam a criação de jogos, quanto por empregar a linguagem de programação C#.

Para a elaboração dos elementos de design, foi utilizado o aplicativo Canva. Ele foi escolhido devido à sua interface intuitiva e à vasta gama de recursos para a criação de gráficos e elementos visuais. Além disso, o Canva oferece uma variedade de modelos pré-fabricados que podem ser adaptados para as necessidades específicas do jogo. O Photoshop foi usado para edição de imagens com recursos para ajuste de cores, composição de imagens e criação de efeitos visuais e o Leonardo.ai para criação de uma das personagens do jogo. Sua capacidade de gerar arte de forma rápida utilizando inteligência artificial permitiu criar a personagem principal do jogo de forma automatizada, economizando tempo e recursos durante o processo de desenvolvimento. Como editor de código-fonte foi usado o Visual Studio Code.

### 3.1. Descrição

O jogo foi desenvolvido para incentivar o ingresso feminino em carreiras STEM destacando a história de Grace Hopper, uma personalidade importante para a área. O jogo é sequencial e possui o formato point and click com diversos quebra-cabeças a serem resolvidos.

O OurPlace: Amazing Grace possui uma introdução a qual mostra uma menina chamada Ana, como personagem principal, no momento de decisão sobre qual curso superior escolher. Porém, o jogo em si começa quando a menina dorme e sonha. Neste momento, inicia-se a primeira fase que se passa no quarto de infância de Grace. O contexto remete ao fato de Grace, quando menina, ter desmontado diversos despertadores para verificar o seu funcionamento. Esta fase consiste em um caça-objetos das peças do despertador camufladas no cenário, bem como dois quebra-cabeças.

A segunda fase se relaciona com o trabalho de Grace Hopper no Mark II e a origem do termo bug. Dessa forma, no cenário de uma sala de computadores, o jogador

> 2www.canva.com

> 3www.adobe.com/br/products/photoshop

> 4leonardo.ai

> 5www.code.visualstudio.com

deve ajudar Grace a resolver o enigma que fará o computador voltar a funcionar. Ao final de cada fase, o jogo oferece uma explicação da relação do cenário com a vida de Grace Hopper. A modelagem do jogo e sua jogabilidade são apresentadas a seguir.

### 3.2. Jogabilidade

Para definição da modelagem e da jogabilidade, foram utilizados fluxogramas. Esta técnica permite representar graficamente a lógica de um programa. Os símbolos podem variar ligeiramente, porém devem indicar com clareza e precisão o raciocínio e operações envolvidas [Velloso 2017].

A Figura 1 mostra o fluxograma geral do jogo. Esse fluxograma retrata toda estrutura do jogo desde a tela inicial até sua finalização. O jogo possui duas fases representadas nas partes cinzas da figura. Antes de iniciar a primeira fase, o jogo conta com uma introdução, em que ocorre a narrativa sobre uma menina chamada Ana que está decidindo o curso de sua graduação. Ela está tendo dificuldades em realizar essa escolha e quando vai dormir, sonha com Grace Hopper. Nesse sonho, a menina recebe uma missão de Grace para encontrar as peças de um despertador em seu quarto de quando criança, iniciando a fase 1. Nesta fase o jogador deve cumprir a missão e montar o despertador para prosseguir com o jogo. Quando a fase é concluída, Grace explica brevemente a relação do despertador com a sua história e se dá início à segunda fase.

A segunda fase se passa no cenário de uma sala de computadores para representar o trabalho de Grace no computador Mark II. Nessa sala, existem computadores que não estão funcionando e o objetivo é que o jogador encontre uma forma de consertá-los. Para isso deve resolver um quebra-cabeça relacionado aos botões do computador, que devem ser girado de maneira a formar a palavra-chave “ DEBUG ”. Dessa forma, uma parte do computador se abre e o próximo desfio do jogador é encontrar um inseto escondido no seu interior. Ao retirar o inseto, ou bug, os computadores voltam a funcionar concluindo a segunda fase. Por fim, após uma explicação de Grace sobre o termo bug, o sonho acaba e o jogo é concluído com a inscrição de Ana para o curso de Ciência da Computação.

### 3.3. Criação de Elementos Gráficos

Para o desenvolvimento dos elementos gráficos do jogo foi empregada a ferramenta Canva. Nesta ferramenta foram utilizadas algumas imagens prontas disponíveis mas, de modo geral, foram criados novos elementos por meio de edição de imagens, formas e desenhos. Para o desenvolvimento da personagem Grace Hopper foi utilizado o Photoshop e para a menina Ana, a personagem principal, foi utilizada a ferramenta Leonardo.ai.

A Figura 2 mostra as duas personagens criadas como elementos gráficos do jogo, Grace Hopper e Ana, uma menina comum que irá prestar vestibular. Para criação da menina Ana foi utilizada a ferramenta Leonardo.ai que gerou a imagem por meio de inteligência artificial. Para a geração de imagens nessa ferramenta são utilizados os chamados prompts, frases contendo a descrição da imagem que o usuário deseja gerar. A ferramenta possui limitações e não é completamente assertiva. Por isso, foram necessárias algumas tentativas para que a imagem da menina fosse gerada adequadamente.

Figura 1. Fluxograma geral do jogo proposto.

Figura 2. Elementos gráficos do jogo proposto: Grace Hopper (à esquerda) e Ana (à direita), a personagem principal.

### 3.4. Implementação

A implementação deste trabalho foi realizada na Unity Editor, um ambiente de desenvolvimento da Unity, no qual as interfaces e a mecânica do jogo foram criadas, unindo os

elementos gráficos e os scripts escritos na linguagem de programação C#. Esses scripts, desenvolvidos utilizando o editor de código Visual Studio Code, desempenham um papel de integração e interação entre os elementos gráficos. Eles controlam desde o clique do jogador até a lógica do jogo, a detecção de colisões e, até mesmo, a animação. Os scripts atuam como a base do jogo, moldando como os elementos visuais se comportam e respondem às ações dos jogadores.

## 4. Resultados e Discussões

Nesta seção são apresentadas as principais telas do jogo. A telas do jogo podem ser dividas em quatro tipos: i) tela de menu, com as configurações de controle do jogo; ii) telas de narrativa, onde ocorrem os diálogos e não necessitam de interação ativa do jogador; iii) telas jogáveis, onde ocorre a ação efetiva do jogador; e iv) telas finais. A tela de menu permite a inicialização do jogo e é apresentada na Figura 3. Nela é possível ativar ou desativar o áudio, começar o jogo ( PLAY ) ou sair do jogo.

Figura 3. Tela inicial do jogo OurPlace: Amazing Grace.

As telas de narrativas são responsáveis por contar a história do jogo. Nelas são exibidas caixas de textos. Ao jogador, neste tipo de tela, cabe apenas ler e seguir para a próxima caixa de texto. A Figura 4 mostra uma das telas de narrativas.

Figura 4. Exemplo de tela de narrativa do jogo proposto.

As telas jogáveis se referem às fases do jogo em que o jogador deve explorar o ambiente e completar os quebra-cabeças. As cenas principais são o cenário da primeira fase, o quarto de Grace Hopper, apresentado na Figura 5, e o cenário da segunda fase, uma sala de computadores, como mostra a Figura 6.

Figura 5. Cenário da primeira fase do jogo proposto.

Figura 6. Cenário da segunda fase do jogo proposto.

Por fim, após a conclusão das duas fases do jogo, a tela de inscrição representa o processo pelo qual o jogador passa até se matricular no curso de ciência da computação, servindo como uma analogia visual para a finalização do jogo. Todos os elementos utilizados na imagem final foram selecionados e montados a partir do Canva, como mostra a Figura 7.

O jogo desenvolvido apresenta uma interface visualmente atraente, com elementos gráficos significativos ao tema tratado por ele. Além disso, a jogabilidade permite o aprendizado de fatos relacionados à vida e à carreira Grace Hopper de forma lúdica e inspiradora. O jogo possui como principal fragilidade a baixa adaptabilidade a diferentes níveis de habilidades. Como pontos fortes podem ser destacados os cenários com alta qualidade gráfica, interações estimulantes e informativas, além da flexibilidade de plataformas em que ele pode ser executado ( desktop e dispositivos móveis).

Figura 7. Telas de fechamento do jogo proposto.

## 5. Conclusões e Trabalhos Futuros

Este trabalho realizou estudos sobre o desenvolvimento de jogos, utilizando a aprendizagem baseada em jogos como estratégia para promover representatividade e incentivar o interesse de meninas em áreas de estudo relacionadas às ciências exatas e tecnologias. Como resultado, foi criado um jogo 2D no estilo point and click adventure, inspirado na história de uma figura importante da computação, Grace Hopper.

O jogo desenvolvido servirá como ferramenta de incentivo para meninas e está disponível publicamente para dispositivos Android na Play Store. Além disso, pretendese realizar testes com diferentes públicos para avaliação das interfaces e jogabilidade do projeto, bem como mensurar seus efeitos na questão de representatividade feminina na computação.

Como perspectivas para desenvolvimentos posteriores, considera-se a implementação de elementos de aleatoriedade nos quebra-cabeças. Atualmente, os desafios são estáticos, o que pode limitar o interesse dos jogadores em revisitar o jogo. No entanto, ao introduzir a aleatoriedade nos quebra-cabeças, os jogadores poderiam desfrutar de novas experiências a cada partida, aumentando assim a re-jogabilidade. Além disso, seria interessante explorar a adição de novas fases com desafios distintos, relacionados não apenas à vida de Grace Hopper, mas também a outras figuras importantes das ciências.

## 6. Agradecimentos

O trabalho contou com o apoio da Fundação Araucária e da UNICENTRO. As autoras agradecem à Fundação Araucária pelo apoio financeiro proporcionado por meio da bolsa de pesquisa PIBIC (Programa Institucional de Bolsas de Iniciação Científica) durante a realização deste estudo, e à UNICENTRO (Universidade Estadual do Centro Oeste - Campus Cedeteg) pelo suporte contínuo.

> 6https://play.google.com/store/apps/details?id=com.paulaynizer.AmazingGrace

> 7https://www3.unicentro.br/
