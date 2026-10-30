# E aí meninas, qual vai ser? Agora sua carreira o jogo STEAM ParPow pode te ajudar a escolher

Victória Guimarães, Larissa Pessoa, Raquel Folz, Lia Martins, Rosiane de Freitas

1Instituto de Computação – Universidade Federal do Amazonas (UFAM) CEP 69.077-000 – Manaus – AM – Brazil

2Instituto Federal de Educação, Ciência e Tecnologia do Amazonas (IFAM) CEP 69.152-470 – Parintins – AM – Brazil

{ vsg,lsp, raquel.folz,lia.martins,rosiane } @icomp.ufam.edu.br

Resumo. Neste artigo são abordados o desenvolvimento e a aplicação de um jogo de cartas que trabalha conteúdos de STEAM (ciências, tecnologias, engenharias, artes e matemática), cultura regional amazônica e a temática de mulheres em computação. Denominado de ParPow, o jogo é similar a um jogo de cartas muito conhecido (Dobble - Spot it). O desenvolvimento e entendimento do funcionamento do jogo envolve conceitos de geometria espacial, combinatória e algoritmos, e, sua jogabilidade trabalha a percepção visual, agilidade e raciocínio lógico, trabalhando, também, os quatro pilares do pensamento computacional: abstração, reconhecimento de padrão, decomposição e passo-a-passo algorítmico. Além de promover a divulgação de projetos de mulheres em STEAM no Brasil, o ParPow serviu de facilitador para promover o diálogo sobre assuntos de STEAM, principalmente com alunas do ensino médio que estavam na fase de escolha da carreira a seguir. A aplicação, em uma feira de profissões, demonstrou o quão atrativo e envolvente é o jogo e sua adequabilidade para demonstrar conceitos e aplicações interessantes em STEAM.

Abstract. This article discusses the development and application of a card game that works on STEAM content (science, technology, engineering, arts, and mathematics), Amazonian regional culture, and the theme of women in computing. Denominated ParPow, the game is similar to a popular card game (Dobble - Spot it). The development and understanding of how the game works involve concepts of spatial geometry, combinatorics, and algorithms, and its gameplay works on visual perception, agility, and logical reasoning, also working on the four pillars of computational thinking: abstraction, pattern recognition, decomposition, and algorithms. In addition to promoting the dissemination of women’s projects in STEAM in Brazil, ParPow served as a facilitator to promote dialogue on STEAM issues, especially with high school students who were in the phase of choosing the career to follow. The application, at a trade fair, demonstrated how attractive and engaging the game is and its suitability to demonstrate interesting concepts and applications in STEAM.

## 1. Introdução

A presença feminina nos cursos de Computação e STEM em geral ( Science, Technology, Engineering, Mathematics ) tem sido muito discutida nos últimos anos. A desproporcionalidade entre mulheres e homens nestas áreas de conhecimento é considerada evidente na comunidade científica e na profissional em geral. Apesar da maior presença de mulheres no ensino superior, graduação e pós-graduação, as mulheres são mais encontradas em áreas ditas serem mais femininas, como educação e saúde, e, os homens continuam a ser maioria nas ciências exatas, como computação e engenharias [Kemp et al. 2019], [Nakamura et al. 2017]. No Brasil, destaca-se o sucesso de iniciativas de vários grupos e projetos que surgiram no meio acadêmico, representados pelo Programa Meninas Digitais da SBC [Bim 2016], e,na América Latina, pelo LAWC ( Latin American Women in Computing ) do CLEI ( Latin American Center for Computer Studies ). Tais grupos visam despertar o interesse de meninas desde o ensino fundamental até o ensino superior, de modo a incentivá-las a seguir carreira em Computação e TI, com diferentes ações e produção de ferramentas e tecnologias [de Freitas et al. 2020], [de Freitas et al. 2016].

Quando os jovens estão cursando o ensino médio é comum estarem muito indecisos sobre a futura profissão a escolher. No entanto, a orientação vocacional de jovens por meio da realização de feiras de profissões, auxilia no esclarecimento de dúvidas no momento desta escolha [Pantoja 2021]. Em Manaus, estado do Amazonas, é realizada anualmente a Feira Norte do Estudante (FNE), que conta com a programação de palestras sobre profissões e temas diversos, como empreendedorismo e mercado de trabalho, além de testes vocacionais, simulados, sorteios e uma área de exposição, chamada “Salão de Oportunidades”.

Dada a necessidade de apoiar os jovens na escolha da carreira a seguir, aliado ao interesse de envolver mais meninas em carreiras de Computação, como uma das ações do grupo de pesquisa ALGOX (Otimização, Algoritmos e Complexidade Computacional) e projeto Cunhantã Digital, do Instituto de Computação da Universidade Federal do Amazonas (IComp/UFAM), foi elaborado o jogo de cartas “ParPow”, como uma releitura de um jogo conhecido chamado Dobble (ou Spot it ), tendo como foco a temática de mulheres em STEAM. Com isto, foram propostas classes temáticas diferentes, envolvendo: jogos mentais; cultura regional amazônica; projetos de incentivo à mulheres na computação; e, sínbolos representativos de ciência e tecnologias. O jogo ParPow foi exposto no Salão de Oportunidades da FNE, para alunos do ensino médio, com o intuito de disseminar conteúdos teóricos como geometria e combinatória, e estimular habilidades relacionadas ao raciocínio lógico estruturado ou Pensamento Computacional, como abstração, decomposição, reconhecimento de padrão e passo-a-passo algorítmico.

Portanto, o objetivo deste artigo é apresentar o jogo “ParPow” como importante ferramenta no despertar de interesse de alunas do ensino médio para carreiras de Computação e afins, para isto sendo explorado o envolvimento de meninas no desenvolvimento e na aplicação do jogo, em uma feira de profissões. Este trabalho está organizado da seguinte maneira: na Seção 2 são apresentados os fundamentos teóricos do jogo; na Seção 3 são apresentados os trabalhos relacionados; na Seção 4 é abordado o jogo de cartas “ParPow”; na Seção 5 saõ reportados e analisados os resultados do desenvolvimento e aplicação do jogo; e, por fim, na Seção 6 são tecidas as considerações finais.

## 2. Fundamentação teórica

No século XXI, para obter sucesso em suas carreiras na “Era da Informação”, os alunos precisam ter doze habilidades: pensamento crítico, criatividade, colaboração,

comunicação, literacia da informação, literacia de mídias, literacia de tecnologias, flexibilidade, liderança, iniciativa, produtividade e ainda, habilidades sociais [Stauffer 2020]. Essas competências têm como objetivo ajudar os discentes a acompanhar o ritmo da luz dos mercados modernos. Competência, implica saber como mobilizar, integrar e transferir os conhecimentos, recursos e habilidades, num contexto profissional determinado.

A sociedade moderna vive a “era da informação”, onde faz-se necessária uma educação permanente, dinâmica e desafiadora visando o desenvolvimento de habilidades para a obtenção e utilização das informações [Moratori 2003]. O domínio de competências e habilidades da computação que podem ser aplicadas a compreensão de conteúdos de outras áreas da ciência (por exemplo, a Matemática) vem sendo denominado como pensamento computacional (computational thinking). O pensamento computacional, de acordo com Wing [2006] é sustentado por quatro pilares: (1) decomposição - é a capacidade de decompor um problema grande em problemas menores e mais simples de se resolver; (2) reconhecimento de padrões - é a habilidade de perceber similaridades entre diversas situações; (3) abstração - é a habilidade de filtrar apenas as partes importantes do processo, ignorando coisas irrelevantes; e, (4) algoritmo - é a capacidade de juntar os três pilares anteriores, na tentativa de se desenvolver um conjunto de passos para a resolução do problema.

Com uma vasta gama de jogos está cada vez mais difícil não se ver diante de um jogo que não exija um dos quatro pilares para a resolução de problemas apresentados para que o usuário vá adiante. Jeannete M. Wing publicou o artigo “Computional Thinking” [Wing 2006] e definiu algumas características para o pensamento computacional como:

- Conceituar, não programar. Avalia que pensar como cientista da computação é mais do que programar e requer pensar em múltiplos níveis;

- Habilidade fundamental, não mecânica.

- Uma maneira que os humanos, não os computadores pensam. Enfatiza que o pensamento computacional é o modo de resolver problemas pelos humanos, somos nós que tornamos os computadores empolgantes e é a partir de nossa inteligência que conseguimos lidar com problemas que nem pesaríamos em lidar;

- Complementa e combina o pensamento matemático e de engenharia. A ciência da computação se baseia tanto em pensamentos matemáticos como de engenharia, já que sistemas interagem com o mundo real;

- Ideias, não artefatos. O que ficará de importante para sempre vai ser o modo como e os conceitos computacionais que utilizamos para resolução de problemas diariamente e não os produtos em si desenvolvidos; e

- Para todos, em todos os lugares. O pensamento computacional deve ser disponível para todos, vendo a sua grande colaboração que pode surgir em qualquer área.

Nna indústria dos jogos de tabuleiro, o raciocínio lógico é muito explorado e, em muitos casos, de certa forma, o jogador acaba exercendo os quatro pilares do pensamento computacional sem perceber, tornando o jogo mais instigante. Os jogos com temática feminista, assim como nos outros elementos de STEAM-W (( Science, Technology, Engineering, Arts, Mathematics and Women ), vem ganhando cada vez mais espaço nas escolas e atraindo ambos os gêneros com as jogabilidades cada vez mais trabalhadas e consequentemente causando um impacto positivo na disseminação de conteúdo sobre mulheres nestas áreas do conhecimento.

## 3. Trabalhos Relacionados

Existem muitos jogos de raciocínio lógico que embutem mais fortemente aspectos matemáticos e computacionais, e, por outro lado, jogos que trabalham a temática feminina visando o empoderamento de mulheres. Por exemplo, a maioria dos jogos listados na Tabela 1 são conhecidos, sendo alguns jogos de agilidade mental e de reconhecimento de padrões, como os jogos Flanx [Game 2020] e Set [Davis and Maclagan 2003]. Porém, pode-se observar que os jogos com temática feminina, Feminaipes [Vanguardia 2020] e Wonder Women [Foyles 2020], não abrangem aspectos de STEAM. Têm surgido propostas recentes de jogos que cobrem a temática de mulheres em STEAM, como no site “Elas na Ciência” [Milson et al. 2020], que disponibiliza três jogos virtuais: Ajudando Marie, Quem sou Eu e o Jogo da Memória. Todos eles com jogabilidade que envolve a história de mulheres famosas da Ciência e seus feitos.

Tabela 1. Aspectos de STEAM, com temática feminina (STEAM-W) ou não,em diferentes jogos. Fonte: Própria.

|Logo dos Jogos|Jogo|Descrição|Aspectos Feministas|Aspectos Matemáticos Computacionais|
|---|---|---|---|---|
||Flanx|Os jogadores se enfrentam tentando combinar suas cartas para formar o caminho que irá bloquear o outro jogador.|Não possui.|Formas geométricas, reconhecimento de padrões e estratégia algorítmica.|
||Set|Os jogadores devem identificar conjuntos de três símbolos iguais ou diferentes em quatro categorias: cor, número, forma e sombreamento.|Não possui.|Noções de conjunto, formas geométricas e reconhecimento de padrões.|
||Feminaipes|Baralho feminista que é ilustrado apenas com figuras femininas que tenham feito sucesso na Argentina.|Promover a igualdade de gênero e empoderar mulheres e meninas|Não possui.|
||Wonder Women - a Feminist Card Game|Jogo de cartas informativo sobre 44 mulheres cientistas em um jogo de estratégia real e com pulso narrativo no centro.|Promover a igualdade de gênero e empoderar mulheres e meninas.|Não possui.|
||Ajudando Marie|Jogo virtual que tem como personagem principal Marie Curie uma das cientistas mais conhecidas por suas contribuições no ramo da radioatividade.|Promover a igualdade de gênero e empoderar mulheres e meninas.|Não possui.|
||Quem Sou Eu|Jogo virtual onde os jogadores desenvolvem maior conhecimento sobre mulheres que apresentaram vultosa importância na área de ciências.|Promover a igualdade de gênero e empoderar mulheres e meninas.|Não possui.|
||Jogo da Memória|Jogo virtual que passa aos jogadores conhecimentos sobre seis mulheres importantes para a computação.|Promover a igualdade de gênero e empoderar mulheres e meninas.|Não possui.|
||Dobble - Spot It|Jogo de velocidade e observação no qual os jogadores devem identificar dentre oito elementos na carta, o único elemento que se repete na carta de dois ou mais jogadores.|Não possui.|Classificação por conjunto, abstração, algoritmo na construção do jogo e reconhecimento de padrões.|

Um dos jogos que se destaca é o Dobble (ou Spot it ) [De Almeida 2018], possuindo diversos aspectos matemáticos computacionais, O jogo Dobble contém 55 cartas, cada uma delas contendo 8 símbolos, sendo fundamentado através de um princípio matemático que garante haver sempre exatamente um elemento em comum entre duas cartas. Os elementos são agrupados em classes temáticas, mas, sem abordar conteúdos de STEAM e tampouco de STEAM-W. Deste modo, uma releitura deste jogo foi feita, para incluir STEAM-W de modo a se trabalhar tais conteúdos em seu desenvolvimento e sua aplicação, surgindo o jogo ParPow.

## 4. O jogo de cartas ParPow

Nesta seção é abordado o jogo ParPow e os conceitos geométricos e combinatórios necessários para seu entendimento, desenvolvimento e aplicação. O material de referência utilizado é baseado em artigos de divulgação científica de revistas online ou mesmo em textos estruturados sobre o tema em sites da Internet. Esta seção está baseada em alguns destes textos [Sengupta 2020], [Mathenæum 2020], [Polster 2015].

O jogo pode ser modelado por meio de uma estrutura matemática chamada plano projetivo finito. Um plano projetivo é um conjunto de pontos e linhas com os axiomas (premissa considerada necessariamente evidente e verdadeira) vistos na Figura 1(a). E possível criar uma equivalência entre o jogo e um plano projetivo finito, para isso, basta considerar os pontos equivalentes aos símbolos, e, as linhas equivalentes à cartas. As propriedades do plano garantem que todas as cartas tenham a mesma quantidade de símbolos e cada duas cartas tenham exatamente um símbolo em comum. A Figura 1(b) mostra como um baralho de 3 símbolos por carta poderia ser gerado utilizando os conceitos do plano projetivo. Devido às propriedades de um plano projetivo finito, essa equivalência só gera baralhos completos. Isto é, qualquer outro baralho com a mesma quantidade de símbolos por carta pode ser obtido eliminando cartas ou trocando os símbolos associados a cada ponto.

Figura 1. (a) Axiomas de um plano projetivo; (b) Plano projetivo finito de ordem 2 e símbolos por carta do baralho gerado a partir do plano. Fonte: Própria.

Esta teoria, portanto, foi base para a elaboração do jogo ParPow, onde, desde o processo de concepção foi também destacado o desenvolvimento dos pilares do Pensamento computacional, por meio da metodologia design thinking. Na fase de imersão, foi formado o time por alunos da área da computação e de design. Desta forma, realizou-se o questionamento aos alunos da universidade de quais categorias temáticas seriam abordadas no jogo. Determinou-se que as categorias do jogo seriam divididas na temática STEAM-W, projetos de mulheres em ciências exatas, jogos em STEAM, cultura Amazônica e ciência. Já na fase de ideação foram promovidas atividades que gerassem ideias inovadoras como o brainstorming, no qual foram definidas as cores que cada grupo seria representado, e quais elementos fariam parte das categorias do jogo. Durante a fase de prototipação, a equipe se dividiu em duas partes: criação do algoritmo e criação dos ícones. Sendo que, para a criação dos ícones, cada participante da equipe encarregouse de produzir e buscar em bancos de imagens gratuitos os símbolos de cada categoria visto na Tabela 2. Após isso, houve uma nova divisão para a confecção das cartas e da logomarca do jogo que pode ser vista na Figura 2(a).

Tabela 2. Quadro com a definiç ão dos grupos temáticos do ParPow, cores e símbolos pertencentes a cada categoria. Fonte: Própria.

|Categorias dojogo|Símbolos|Cor definidapara categoria|Exemplos de Símbolos|
|---|---|---|---|
|Computação|Notebook, Nuvem, Circuito, Mouse, Sinal Wifi, Sinal USB, Pen Drive, Binário, Impressora, Table.|Cinza.||
|Projetos de mulheres em ciências exatas|Cunhatã Digital, Meninas Digitais, Py Ladies Manaus, LAWC, Manauara Tech, Ei Mana, Bit Girls, Ada Code, Caboclas Kirimbaua Aueté na Ciência,Mulheres na PO.|Manteve-se a cor do logo do projeto com a adição de um fundo rosa para padronização.||
|Jogos em STEAM|Xadrez ( Peão), Dominó, Torre de Hanoi, Sudoku, Cubo Mágico, Quebra Cabeça, Ábaco, Jogo da Velha, Baralho ( ÁS),|Amarelo.||
||Tetris.|||
|Cultura Amazônica|Curupira, Vitória-régia, Boto, Garantido e Caprichoso (boi bumbá), Yara, Guaraná, Canoa,Cocar,Jaraqui,Sauim de Coleira.|Roxo.||
|Educação|Lápis, Régua, Livros, Lápis de cor, Borracha, Tesoura, Mochila, Calculadora, Quadro branco,|Laranja.||
|Ciência|Tubo de ensaio, Molécula, Grafo, Globo Terrestre, Engrenagens, Microscópio, Foguete.|Azul.||

O nome ParPow remete a gíria popular denotada como Pá-Pow que usa uma expressão de onomatopéias (palavras que imitam sons naturais), para indicar algo que ”mostra e bate”, para indicar que durante o jogo, cada jogador deve mostrar sua carta e aquele que identificar o símbolo em comum primeiro ”bate”(indica qual o símbolo em comum e faz o movimento seguinte segundo cada tipo de variação do jogo). A palavra Pá foi substituída por Par, visto que a jogabilidade principal do jogo consiste em encontrar um par (dupla) de símbolos iguais. Durante o estudo do jogo Dobble, percebeu-se que existiam categorias separando os ícones implicitamente para melhorar a jogabilidade e aumentar o nível de dificuldade confundindo o jogador no momento em que deve identificar o símbolo que aparece em ambas as cartas. No entanto, esses grupos são formados por elementos simples e são diferenciados apenas por tons de cor. Em contrapartida, o ParPow possui categorias para tornar a experiência do jogador mais interessante, além de também diferenciar cada classe por cor, como apresentado na Tabela 2.

Deste modo, o ParPow possui um total de 57 símbolos, que são distribuídos em 55 cartas onde cada uma possui 8 destes elementos. A importância de trazer nos símbolos do jogo elementos regionais, projetos de mulheres em ciências exatas, jogos educacionais, objetos da ciência, da computação e educação visa a formação do indivíduo em várias áreas do conhecimento enquanto pratica-se uma atividade lúdica. O conhecimento da cultura local promove a valorização regional, assim como conhecer mais sobre computação, ciência e educação estimula o interesse e instiga a curiosidade sobre os assuntos relacionados. Por fim, a compreensão da existência de projetos que promovem o conhecimento e atividades de mulheres em STEAM, proporciona inspiração, motivação e consequente engajamento.

A teoria envolvida na jogabilidade, garante que há apenas um elemento em comum entre duas cartas quaisquer do baralho, como na Figura 2(b). Esses símbolos não se repetem na mesma carta, porém um mesmo elemento aparece em outras cartas do baralho. Os ícones também apresentam tamanho variado em cada carta, em menor ou maior tamanho, para dificultar sua identificação e assim refinar habilidades mentais visuais.

Figura 2. Cartas do jogo ParPow: (a) verso da carta; (b) par de cartas do jogo, com a identificaç ão do elemento em comum. Fonte: Própria.

## 5. Experimentos e Análise dos Resultados

Antes do dia de exposição, o jogo foi explicado para voluntários que ajudaram na exposição do ParPow. Em reunião, definiu-se disseminar conteúdos relacionados à computação e matemática, garantindo que os voluntários soubessem da importância de tratar assuntos de STEAM-W no jogo, tendo como foco os projetos de mulheres em ciências exatas, para além de gerar curiosidade, empoderar mulheres e meninas, visto que muitas enxergariam como exemplo e possibilidade de carreira.

Além disso, os próprios voluntários, devido a necessidade de expor e explicar o jogo, tiveram impactos positivos ao aprender sua jogabilidade e a relação com os pilares do pensamento computacionais vistos na Figura 4. Ademais, os mesmos aperfeiçoaram ou desenvolveram a capacidade de oratória, uma vez que foi necessário a explicação do jogo para o público do evento, devido isso, estes passaram a possuir mais segurança ao se expor para um público desconhecido ao decorrer dos dias da Feira. Uma grande parte desses voluntários são meninas do Projeto Cunhatã Digital, que durante todo o processo, adquiriram o conhecimento proposto pelo jogo e se tornaram mais confiantes ao se manifestar para outros, levando algum conhecimento, e assim, consequentemente inspirando outras meninas.

O ParPow foi exposto na Feira Norte do Estudante para alunos do ensino médio, como mostrado na Figura 3. O jogo também chamou a atenção de pais, educadores e profissionais da área da computação que visitaram o local onde o jogo estava exposto, fazendo perguntas sobre o desenvolvimento, possíveis aplicações em escolas e até mesmo se o jogo era comercializado. No evento, o objetivo era ensinar a jogabilidade e a compreensão do jogo, onde demonstrou-se as regras e exemplos de pares de figuras para que as cartas se combinem.

Contudo, como os estudantes já estavam cursando o ensino médio, foi feita a explicação da teoria combinatória e da geometria, o que foi entendido de maneira fácil, por ser um assunto já visto na sala de aula. Além disso, o jogo trouxe os quatro pilares do pensamento computacional: reconhecimento de padrões, abstração, decomposição e algoritmo, como é explanado na Figura 4. No decorrer da Feira de Exposição de Profissões para alunos do ensino médio foram realizados torneios do jogo ParPow, a Figura 5 demonstra como foi realizada a dinâmica de execução do jogo.

Durante as dinâmicas, tivemos algumas percepções acerca de dificuldades na jogabilidade em relação a cor, tamanho e dúvida sobre elementos desconhecidos. Por outro lado, após jogar algumas vezes, foi perceptível que a cada partida os alunos compreendiam e aprendiam mais sobre os elementos de acordo com que exerciam os pilares do

Figura 3. Registros feitos no experimento realizado na Feira Norte do Estudante (feira de profissões). Fonte: Própria.

Figura 4. Aplicaç ão dos pilares do Pensamento Computacional no ato de jogar: abstraç ão, decomposiç ão, reconhecimento de padrão e algoritmo. Fonte: Própria.

Figura 5. Fases da dinâmica da execuç ão do ParPow. Fonte: própria.

Figura 6. Percepç ões acerca dos torneios realizados como o jogo ParPow na FNE. Fonte: própria.

pensamento computacional. No decorrer dos torneios a curiosidade dos educandos foi sendo aguçada cada vez mais, e os mesmos faziam as mais diversas perguntas. Todas essas percepções estão mais detalhadas na Figura 6.

No geral, os alunos se divertiram durante as dinâmicas de jogos e grande parte dos estudantes desejaram aprender sobre os projetos de mulheres em ciências exatas exibidos no ParPow e conhecer um pouco sobre a teoria matemática e computacional por trás do jogo. O interessante, também, é que alguns estudantes e pais que conheceram o jogo, perguntaram a possibilidade de aquisição do mesmo. Alguns educadores também se interessaram em adquirir o jogo e aplicar em atividades de ensino de geometria e combinatória.

## 6. Considerações finais

A estratégia de elaboração e aplicação do jogo ParPow com objetivo de estimular meninas para carreiras de Computação e STEAM em geral, demonstrou ser bem sucedida e de enorme potencial. Foi proporcionado um espaço para que jovens estudantes tivessem contato com conteúdos de matemática e computação, através de uma atividade lúdica e um produto tangível concreto, sendo apresentado o quão interessante e diverso pode ser a carreira nestas áreas. O jogo de cartas ParPow utilizado nessa ação foi o primeiro protótipo impresso, sendo observado que alguns ajustes precisam ser feitos, principalmente na forma e nas cores de alguns elementos, para que fiquem mais legíveis. Como as cartas do jogo, e a distribuição dos elementos em cada uma, é feita segundo uma estratégia algorítmica, versões do jogo com um número menor e maior de elementos por carta, bem como variação e adaptação dos símbolos e classes temáticas propostas, estão em desenvolvimento, visando melhorar e ampliar a experiência lúdica como proposta de atração de garotas para carreiras de Computação e STEAM em geral.
