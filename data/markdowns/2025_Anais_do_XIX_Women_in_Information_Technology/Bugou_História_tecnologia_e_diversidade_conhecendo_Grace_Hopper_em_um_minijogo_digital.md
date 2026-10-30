# “Bugou?”: História, tecnologia e diversidade, conhecendo Grace Hopper em um minijogo digital

Ellen Ami Tanaka, Carla Rodrigues Bruschi, Valguima Odakura

1 Faculdade de Ciências Exatas e Tecnologia (FACET) Universidade Federal da Grande Dourados (UFGD) Caixa Postal 533 – 79.804.970 – Dourados – MS – Brasil

{ tanakaellen31, carlabruschi } @gmail.com, valguimaodakura@ufgd.edu.br

Abstract. A participação feminina na Computação e no STEAM (Ciências, Tecnologia, Engenharia, Artes e Matemática) ainda é baixa, agravada pelo apagamento histórico das contribuições das mulheres. Este artigo apresenta um minijogo interativo chamado “Bugou” sobre Grace Hopper, pioneira da Computação, tornando seu legado mais acessível ao público jovem. Com mecânicas simples e envolventes, o jogo promove aprendizado e reflexão sobre a diversidade na tecnologia, buscando aumentar a visibilidade das mulheres na Computação e inspirar novas gerações. O minijogo foi avaliado utilizando um modelo de avaliação de jogos educacionais que mostrou que “Bugou” promove o conhecimento sobre Grace Hopper enquanto diverte.

Resumo. The participation of women in computing and STEAM (Science, Technology, Engineering, Arts and Mathematics) remains low, partly due to the historical erasure of their contributions. This article introduces an interactive minigame named “Bugou” about Grace Hopper, a computing pioneer, making her legacy more accessible to young audiences. Through simple and engaging mechanics, the game fosters learning and reflection on diversity in technology, aiming to increase women’s visibility in computing and inspire future generations. The minigame was evaluated using an educational game evaluation model which showed that “Bugou” promotes knowledge about Grace Hopper while being entertaining.

## 1. Introdução

A história da Computação é comumente associada a figuras masculinas emblemáticas como Alan Turing e Bill Gates, no entanto, o avanço dessa área foi profundamente marcado por contribuições significativas de mulheres, com papéis tão relevantes quanto os de homens. Contudo, muitas dessas figuras permanecem desconhecidas pelo grande público, vítimas de uma exclusão histórica que minimizou seu protagonismo e sendo subvalorizadas no imaginário popular ou bibliograficamente [Louzada et al. 2014, Ambrose et al. 1997]. Esse apagamento contribuiu para o desenvolvimento de um estereótipo de gênero, criando a ideia que a área de Computação é um campo predominantemente masculino, levando ao desestímulo do ingresso de novas gerações de mulheres na área [da USP 2023].

A participação feminina nas áreas de Ciências, Tecnologias, Engenharias e Matemática nos países do G20 é de apenas 22% [Straza 2024]. No Brasil, conforme dados

da terceira edição das Estatísticas de Gênero: indicadores sociais das mulheres (2022) [IBGE 2024], a área com menor presença feminina é a de Ciência da Computação e TI (Tecnologia da Informação). Além de ser baixa, a participação das mulheres nesses cursos diminuiu: de 17,5% em 2012 para 15% em 2022 [INEP 2022]. Diante disso, surge a necessidade de criar meios de promover a história de mulheres pioneiras na área, para valorização de suas contribuições na história da Computação e assim provendo interesse para jovens mulheres ingressarem na área.

Nesse sentido, neste trabalho buscamos colaborar com a valorização da história de mulheres na Computação, destacando as contribuições de Grace Hopper, uma pioneira da tecnologia militar. Através do desenvolvimento de um minijogo interativo, buscamos abordar sua história de maneira lúdica, especialmente para um público mais jovem, apostando em uma abordagem mais divertida, com mecânicas de jogo simples e conteúdos de fácil entendimento, para engajar os jogadores e transmitir um pouco da história e feitos de Hopper.

Ao experimentar a dinâmica do jogo, os participantes não apenas aprendem sobre um marco importante na Computação, mas também são incentivados a refletir sobre a importância da diversidade e do reconhecimento das mulheres na tecnologia. O impacto esperado vai além do simples aprendizado através de uma experiência multifacetada. E instigar reflexões sobre o papel das mulheres na tecnologia e contribuir para a construção de um futuro mais inclusivo e igualitário.

O trabalho segue a seguinte estrutura: a Seção 2 aborda jogos digitais e metodologia para o seu desenvolvimento. Na Seção 3, apresentam-se os trabalhos relacionados. O desenvolvimento do minijogo é detalhado na Seção 4. Resultados obtidos após a avaliação do minijogo são descritos na Seção 5. Por fim, a Seção 6 é dedicada às considerações finais.

## 2. Jogos digitais

Os jogos digitais se tornaram poderosas ferramentas de entretenimento e aprendizado, oferecendo uma experiência interativa e imersiva aos jogadores [Savi and Ulbricht 2008]. Seu desenvolvimento exige um planejamento estruturado, organizado em etapas de concepção, design, programação e testes. No caso de jogos de pequeno porte, um modelo útil de planejamento é o Short Game Design Document (SGDD) de Motta et al. [Motta and Trigueiro 2013]. A estrutura do SGDD é concisa, descrevendo o projeto de forma clara e literal, idealmente em uma única página. Esse formato reduzido permite um desenvolvimento ágil, mantendo o foco nos elementos centrais do projeto.

Além de um planejamento bem estruturado, é fundamental avaliar a eficácia do jogo, especialmente quando o objetivo é educacional. O modelo de avaliação de jogos educacionais de Savi et al., combina quatro frameworks: Modelo de Kirkpatrick (para medir a reação dos jogadores, pela reação e valor percebido), Modelo ARCS de Keller (para avaliar a atenção, relevância, confiança e satisfação dos jogadores com o jogo), Experiência do Usuário (que analisa a imersão, interação social, desafio, diversão, controle e competência) e Taxonomia de Bloom (mede se os jogadores lembram, entendem e aplicam os conceitos do jogo) [Savi et al. 2010].

## 3. Trabalhos relacionados

Antecedentes deste projeto buscaram realizar essa iniciativa de modo a atrair e incentivar mulheres nas áreas de computação/STEAM (acrônimo em inglês para Ciências, Tecnologia, Engenharia, Artes e Matemática). Diferentes abordagens foram desenvolvidas com o objetivo de aumentar a participação feminina nessas áreas, promovendo a visibilidade de mulheres de notáveis contribuições.

No trabalho de Lopes et al. (2023), foi criado um jogo de associação de cartas que tem como objetivo dar visibilidade às histórias de mulheres nas áreas STEAM [Lopes et al. 2023].

No projeto Mundo Bit Byte, desenvolvido para plataformas móveis, foi criado um jogo com o objetivo de divulgar a história de importantes mulheres na Computação. O jogo busca despertar o interesse de meninas do ensino fundamental e médio pela área, incentivando-as a seguir carreiras tecnológicas [Briceno et al. 2021].

De forma similar, no trabalho de Santos e Figueiredo (2016), foi criado o jogo de cartas Computasseia, com o objetivo de promover o ensino da História da Computação e dar visibilidade à importância das mulheres na área [Santos and Figueiredo 2016].

Milson et al. (2020) apresentaram a proposta que envolve a criação de um site que contempla um pouco da história de algumas mulheres e minijogos relacionados a algumas dessas mulheres na ciência [Milson et al. 2020].

Inspirando-se em tais iniciativas, este trabalho busca ampliar o conhecimento sobre o trabalho de mulheres nas áreas STEAM, contribuindo para o movimento de valorização e inclusão feminina. O minijogo seguiu uma proposta semelhante aos desenvolvidos por Briceno et al. (2021) e Lopes et al. (2023), mas foi disponibilizado em formato digital.

## 4. Desenvolvimento do minijogo “Bugou?”

O minijogo “Bugou?” se originou da ideia de transformar a curiosa história do termo bug em um símbolo de conexão entre o reconhecimento e o entretenimento, alinhando dois pontos de maneira simplificada. Projetado para desktops, o minijogo busca apresentar um pedaço da trajetória de Grace Hopper e alguns de seus feitos. Proporciona uma experiência dinâmica, integrando elementos visuais que remetem tanto à criação do termo bug quanto à trajetória de Grace na computação, oferecendo ao jogador conhecimento sobre essa figura tão importante na história da tecnologia [Kidwell 1998].

O minijogo foi construído na ferramenta Game Maker, que tem como linguagem de programação, uma linguagem própria, chamada Game Maker Language (GML). Além dessa ferramenta, existiu as ferramentas de edição de imagem que foram utilizadas para a construção de todas as artes do minijogo, sendo elas: Aseprite e Infinite Painter. E sites para criação e utilização de áudios, como o jsfxr e o pixabay, ambos sites livres para

> 1Game Maker, Disponível em: https://gamemaker.io/pt-BR Acesso em outubro de 2024

> 2Aseprite, Disponível em: https://www.aseprite.org Acesso em outubro de 2024

> 3Infinite Painter, Disponível em: https://www.infinitestudio.art/discover.php Acesso em outubro de 2024

> 4jsfxr, Disponível em: https://sfxr.me/ Acesso em outubro de 2024

> 5pixabay, Disponível em: https://pixabay.com Acesso em outubro de 2024

uso. O minijogo está disponível para ser jogado pelo navegador, no site Ponte.

A concepção inicial do minijogo teve início na elaboração do Short Game Design Document (SGDD), que tem como objetivo descrever elementos importantes do jogo em um único texto corrido. No documento original, foi apresentada a história básica do minijogo, resumindo sua essência. Em seguida, o minijogo foi descrito em um texto corrido, no qual foram realizadas marcações para identificar as áreas do projeto: Arte, Programação e Música, utilizando as cores roxo, azul e amarelo, respectivamente. No decorrer do desenvolvimento, algumas ideias foram ajustadas ou modificadas devido a limitações técnicas e feedback da jogabilidade.

A Figura 1 exibe parte do SGDD criado para o minijogo, que contém a história e o texto corrido. Logo a seguir, na Figura 2, é exibida a tabela que organiza as tarefas de cada área de desenvolvimento.

Figura 1. SGDD do minijogo desenvolvido em homenagem a Grace Hopper.

### 4.1. Jogabilidade

O minijogo consiste em uma mecânica simples: desviar dos obstáculos que vão sendo apresentados na tela e sobreviver o máximo de tempo possível. Ele é inspirado em um famoso subgênero de jogos de tiro, Bullet Hell, na qual a tela fica cheia de inimigos e projéteis. Para o caso do minijogo “Bugou?”, a narrativa segue Grace Hopper que, ao trabalhar nos seus programas, descobre uma falha na qual não compreende. Ao inspecionar melhor a falha do programa, descobre que a falha não se encontra na lógica de seu programa mas no hardware deste. Vendo melhor os componentes de seu computador, Grace vê um bichinho, o bug, dentro da sua máquina e vai tentar tirá-lo. A Figura 3 mostra a tela inicial do minijogo, na qual o bug dorme tranquilamente dentro da máquina de Grace.

Nesse contexto, os inimigos do cenário são representados pela mão de Grace e pelas esferas de eletricidade que circulam pelo ambiente. O jogador controla o bichinho, tentando fugir da mão de Grace e projéteis elétricos dentro do computador. O jogador

> 6“Bugou?” (Site: Ponte Educacional), Disponível em: https://ponteducacional.com.br/projetos/grace/, Acesso em Março de 2025.

Figura 2. Tarefas do SGDD do minijogo desenvolvido em homenagem a Grace Hopper.

Figura 3. Tela inicial do minijogo.

precisa tentar sobreviver naquele cenário o máximo de tempo possível, fazendo disso o objetivo principal desse minijogo.

A Figura 4, mostra a tela principal no minijogo, na qual o bichinho está dentro do cenário, desviando da mão de Grace e dos projéteis elétricos utilizando-se das plataformas. Na Figura 5, mostra a tela final com o tempo máximo do jogador e algumas curiosidades sobre a vida de Grace Hopper, a mulher homenageada no minijogo.

Figura 4. Tela principal com o minijogo em andamento.

Figura 5. Uma das telas finais do minijogo.

A proposta central do minijogo é, de forma divertida, integrar uma pequena parte da história de Grace Hopper, com elementos que designam o ambiente de forma única e fazem com que o jogador lembre dos detalhes mais importantes: o bug e sua correlação com a Grace. O minijogo foi construído com o pensamento inicial de ser levado para um projeto de maior escala, sendo um complemento para conteúdos com maior volume de informações. Apesar de ser simples, ele cumpre o sua proposta central de ser uma ponte entre o conhecimento e a diversão.

## 5. Avaliação e Resultados

Para a avaliação do minijogo, foi utilizado o modelo de avaliação de jogos educacionais de Savi et al. (2010), que analisa a interação dos jogadores com o jogo. Para essa avaliação, foi aplicado um questionário que utiliza uma escala Likert de 5 pontos para medir motivação, experiência e aprendizagem, variando de “discordo fortemente” a “concordo fortemente” [Savi et al. 2010]. A pesquisa foi conduzida por meio de um formulário eletrônico, baseado no modelo de avaliação de jogos educacionais, hospedado no Google Formulários. No total, o formulário contou com 40 questões relacionadas ao minijogo, baseadas no modelo de Savi, uma questão específica sobre o conteúdo do minijogo e uma questão aberta.

O público-alvo do minijogo são estudantes do ensino superior, principalmente aqueles vinculados a cursos da área de Computação. Entretanto, sua aplicação pode ser estendida a alunos do ensino médio, uma vez que o minijogo foi desenvolvido com foco na diversão e no estímulo à aprendizagem de forma leve. Caso haja interesse em aprofundar o tema, o jogo pode ser utilizado em conjunto com materiais de apoio.

Com relação aos procedimentos éticos da pesquisa, os participantes foram informados previamente sobre os objetivos, etapas e possíveis impactos da pesquisa, ressaltando que sua participação seria anônima e voluntária. A coleta de dados ocorreu por meio de um formulário eletrônico anônimo, assegurando a privacidade e a confidencialidade das informações.

Participaram voluntariamente da pesquisa 31 pessoas de identidade anônima. Desses participantes, a média etária é de 21 anos; 71% são estudantes dos cursos de graduação em Engenharia de Computação e Sistemas de Informação da UFGD; 54,8% se identificam com o gênero masculino, 41,9% com o gênero feminino e 3,2% optaram por não

### responder.

As Figuras 6, 7, 8 e 9 são relacionadas à motivação dos jogadores ao jogar o minijogo. No geral, a Figura 6 apresenta os resultados quanto à Atenção dos jogadores, na qual 84,4% acharam o minijogo atraente e 78,1% tiveram a atenção capturada logo de início. Com relação à relevância no minijogo, na Figura 7 é mostrado que 73,1% acharam o minijogo relevante e que o seu conteúdo foi útil.

Figura 6. Questões sobre Motivaç ão - Atenç ão.

Figura 7. Questões sobre Motivaç ão - Relevância.

Na Figura 8, são apresentados os resultados em relação a confiança, onde 80,5% dos jogadores não tiveram experiências negativas quanto a quantidade de informação e sobre o entendimento do material do minijogo. Quanto a satisfação, na Figura 9 é possível observar que 64,1% dos participantes se sentiram bem ao jogar e aprenderam algo surpreendente com o minijogo.

Figura 8. Questões sobre Motivaç ão - Confiança.

Figura 9. Questões sobre Motivaç ão - Satisfaç ão.

Com relação à experiência de usuário, as Figuras 10, 11, 12 e 13 apresentam os resultados quanto à imersão, ao desafio, à habilidade/competência, ao divertimento e ao conhecimento. Na Figura 10 são mostrados os resultados sobre a imersão dos participantes com o minijogo, que proporcionou uma experiência imersiva e engajante, com 87,5% dos jogadores se esforçando por bons resultados e 75% sentindo-se estimulados a aprender.

Figura 10. Questões sobre Experiência do usuário - Imersão.

Nas questões sobre desafio, Figura 11, 78,2% dos usuários sentiram que o minijogo adequadamente desafiador e no geral, 71,3% tiveram uma experiência positiva quanto aos desafios do minijogo, se sentiram motivados e obtiveram melhora em suas habilidades conforme jogavam. Dos participantes, 70% relataram ter se sentido competente e bem sucedido ao jogar o minijogo, como demonstrado na Figura 12.

Figura 11. Questões sobre Experiência do usuário - Desafio.

Figura 12. Questões sobre Experiência do usuário - Habilidade/Competência.

Na Figura 13, é possível observar 71,9% dos participantes afirmando que jogariam novamente e 65,7% gostando de utilizá-lo por bastante tempo. Além disso, 53,2% sentiram desapontamento ao serem interrompidos.

Figura 13. Questões sobre Experiência do usuário - Divertimento.

A Figura 14 apresenta os resultados sobre o conhecimento dos jogadores em relação ao tema do minijogo, onde 78,1% dos jogadores concordam que o minijogo ajudou a lembrar mais informações sobre o tema, ajudou 81,2% a compreender melhor os conceitos apresentados e 62,5% se sentiram mais aptos a aplicar esses conhecimentos.

Figura 14. Questões sobre Conhecimento

Após a avaliação do minijogo, os participantes responderam à pergunta específica: “Você já tinha ouvido falar da Grace Hopper antes do minijogo?”, na qual se revela que 58,1% dos participantes já tinham ouvido falar de Grace Hopper, enquanto 41,9% não a conheciam, mesmo que ela seja uma figura feminina poderosa na Computação.

Por fim, a Figura 15 traz algumas respostas qualitativas para a pergunta: “O que você sabe sobre a Grace Hopper após jogar Bugou?”. Os participantes ampliaram seu conhecimento sobre Grace Hopper, aprenderam sobre sua contribuição para o desenvolvimento da linguagem COBOL, sua participação na Marinha dos EUA, a origem do termo bug e sua importância para a representatividade feminina na tecnologia.

## 6. Considerações finais

Este trabalho descreveu o desenvolvimento do minijogo “Bugou?”, com o objetivo de promover aprendizado e reflexão sobre a diversidade na tecnologia, buscando aumentar a visibilidade das mulheres na Computação e inspirar novas gerações.

A importância do minijogo para a visibilidade das mulheres na Computação foi confirmada pelas avaliações realizadas. Os resultados mostraram que o minijogo tem muito potencial e contribuiu para que os participantes conhecessem mais sobre a história de Grace Hopper, além de gerar muitas ideias para aprimoramentos futuros. Tais resultados mostram a relevância desse tipo de conteúdo e são bastante encorajadores.

Como proposta para trabalhos futuros, pretende-se levar o minijogo para um projeto maior, que envolve a construção de um site próprio com outros minijogos e com

#### Figura 15. Questão: “O que você sabe sobre a Grace Hopper após jogar Bugou?”

mais conteúdos sobre mulheres na Computação. Desta forma, podemos contribuir para aumentar a visibilidade e o conhecimento sobre as mulheres na Computação.
