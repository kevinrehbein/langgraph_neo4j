# Booleanas: Um Jogo de Memória Multiplayer sobre Mulheres Cientistas

Michele L. da Silva 1, Fabrícia Damando Santos 1, Débora da Silva M. Matos 1

1 Curso de Engenharia de Computação - Universidade Estadual do Rio Grande do Sul

(UERGS)

Porto Alegre – RS – Brasil

`{michele-dasilva, fabricia-santos, debora-motta}@uergs.edu.br`

Resumo. O presente trabalho aborda a importância de promover a igualdade de gênero, principalmente na área da computação, por ser uma área majoritariamente masculina, fato que demonstra a necessidade de ações desde a educação básica que incentivem e despertem a presença feminina. Uma das ações realizadas, nessa proposta foi a divulgação de mulheres cientistas utilizando uma ferramenta computacional, em formato de jogo da memória online multiplayer distribuído. O jogo online, composto por 50 cartas de mulheres cientistas, foi desenvolvido com uma arquitetura cliente-servidor, em tempo real, possuindo um sistema de pontuação com ranking. O objetivo com esta proposta é permitir que meninas consigam, a partir do jogo, aprender sobre mulheres e suas carreiras, principalmente, na área das exatas.

Abstract. This paper reports on the importance of promoting gender equality, especially in the field of computing, a predominantly male area, demonstrating the need for actions from basic education onwards that encourage and foster woman participation. One of the actions carried out in this proposal was the dissemination of information about woman scientists using a computational tool in the form of a distributed online multiplayer memory game. The game, composed of 50 cards of woman scientists, was developed with a real-time client-server architecture and features a ranking scoring system. The objective of this proposal is to enable girls to learn, through the game, about women and their careers, especially in the fields of STEM.

## 1. Introdução

Ao analisar os Objetivos de Desenvolvimento Sustentável (ODS) (Nações Unidas do Brasil, 2026), observa-se que as pautas de igualdade de gênero (ODS 5), de redução das desigualdades (ODS 10) e de educação de qualidade (ODS 4) integram o conjunto de metas capazes de promover um desenvolvimento global mais equilibrado e igualitário. Nesse contexto, a busca por equidade também se insere no âmbito das instituições de ensino superior, especialmente nos cursos das áreas de exatas em relação à representatividade feminina.

Embora a participação feminina em STEAM, sigla para Ciência, Tecnologia, Engenharia, Artes e Matemática, tenha aumentado de 29,5% para 33,7% no período entre 2010 e 2019, estima-se que seriam necessários ainda 24 anos para atingir o patamar mínimo de paridade (45%) entre homens e mulheres nessas áreas (Nascimento et al., 2023). Para Nascimento et al. (2023, p.1), “o Ensino Superior em STEM no Brasil ainda apresenta desafios consideráveis de igualdade de gênero que demandam a atenção de diversos atores sociais para melhorarem de forma mais acelerada”.

Dentre as diversas ações desenvolvidas pelo Curso de Engenharia da Computação da Universidade Estadual do Rio Grande do Sul (UERGS), destaca-se o Projeto Include Gurias, que tem como objetivo divulgar a área de STEM com enfoque em despertar o interesse de meninas pela área tecnológica. Para atingir seu propósito, o projeto realiza atividades com alunas da educação básica a fim de promover o desenvolvimento do pensamento computacional, a divulgação científica de mulheres nas áreas de STEM, a realização de oficinas na área de eletrônica, dentre outras.

O projeto possui duas vertentes: uma voltada para meninas da educação básica e outra direcionada às alunas da graduação. No que tange à educação básica, diversas ações têm sido realizadas, incluindo a criação de materiais didáticos, como o Jogo da Memória de Mulheres Cientistas, denominado Booleanas. Trata-se de um jogo da memória, disponibilizado tanto em formato físico, disponível pelo link da bio do instagram do projeto (https://www.instagram.com/include.gurias/ ) e, agora implementado e disponibilizado a partir de uma ferramenta em formato online e distribuído, permitindo jogos com várias pessoas jogadoras. O jogo está disponível para acesso via link: https://booleanas.duckdns.org

O Booleanas foi concebido para ser utilizado por estudantes da educação básica, com o objetivo de destacar o papel das mulheres nas ciências exatas e promover a divulgação científica de cientistas dessa área. As cartas evidenciam às estudantes a possibilidade de trilharem trajetórias semelhantes às das cientistas e pesquisadoras apresentadas, caso assim desejem, atuando como elementos de inspiração e promoção da representatividade. Inicialmente, o jogo existia apenas em formato físico, composto por 50 (cinquenta) cartas, nas quais a face frontal apresenta a imagem da cientista ou personalidade, acompanhada de seu nome e área de atuação, enquanto o verso contém o ano de nascimento e uma breve biografia.

A versão online do jogo amplia significativamente seu potencial de uso, permitindo que várias alunas o utilizem simultaneamente, inclusive a partir de diferentes locais. Essa característica o torna especialmente relevante para a divulgação científica no contexto da educação básica, fase marcada pela formação identitária e pela busca por representatividade. Além disso, o jogo pode ser acessado por qualquer pessoa, extrapolando o ambiente escolar e ampliando seu alcance. Dessa forma, contribui para a promoção da equidade e para o enfrentamento de estereótipos de gênero nas áreas de STEM.

Este trabalho está organizado em seções. Após esta introdução, a Seção 2 apresenta a fundamentação teórica, a Seção 3 descreve os trabalhos relacionados, na Seção 4 são expostos os métodos, a Seção 5 se dedica aos detalhes da implementação, descrição e regras do jogo, e, por fim, a Seção 6 apresenta as considerações finais.

## 2. Fundamentação teórica

Nesta seção, são apresentados os conceitos essenciais que constituem a fundamentação teórica da proposta, destacando-se os conceitos e aspectos técnicos sobre a implementação de jogos multiplayers, gamificação e seu uso na educação.

### 2.1. Jogos Multiplayers na área educacional

Os jogos multiplayers podem ser classificados, de forma geral, em jogos de tempo real e jogos baseados em turnos. Nos jogos em tempo real, os jogadores realizam ações sem uma ordem predefinida, com envio simultâneo de dados. Já nos jogos baseados em turnos, as ações ocorrem de maneira sequencial, de modo que cada participante realiza sua jogada em um momento específico, sendo necessário aguardar a ação do jogador do turno para prosseguir (Cecin; Trinta, 2007).

Segundo Cecin e Trinta (2007), os jogos multiplayers também têm sido utilizados em contextos educacionais. A utilização de jogos como recurso pedagógico busca promover um ensino menos rígido, integrando tecnologias digitais já presentes no cotidiano dos estudantes (Whitton, 2014; Hsiao, 2007). Além disso, os jogos podem contribuir para que os conhecimentos adquiridos não se restrinjam à memória de curto prazo, favorecendo sua consolidação na memória de longo prazo, por meio de estratégias gamificadas que tornam a aprendizagem mais significativa (Alves, 2015).

### 2.2. Aspectos da Arquitetura do Sistema

A arquitetura e topologia de um jogo multiusuário é definida conforme a necessidade de comunicação entre os seus usuários. Há dois modelos principais de topologia: cliente-servidor ou peer-to-peer (Colouris, Dollimore; Kindberg, 2013). No modelo peer-to-peer caraterizada pela arquitetura onde os computadores se conectam diretamente, sem um servidor central. Já no modelo cliente-servidor, o servidor receberá as informações enviadas pelos clientes e, a partir delas, tomará as ações devidas e notificará aos demais jogadores. No jogo desenvolvido neste trabalho, como trata-se de um jogo por turno, o modelo de arquitetura adotado foi o cliente-servidor, em que um nó da rede é designado como servidor do jogo, mantendo o estado do jogo de forma centralizada e assumindo a responsabilidade pela gestão da comunicação entre os jogadores (Cecin; Trinta, 2007).

Em um jogo multiplayer é usual o servidor receber as jogadas dos players e notificá-las aos demais jogadores para que tenham conhecimento das ações de cada jogador. Outro aspecto relevante refere-se à definição da ordem dos turnos. Em jogos multiplayers online, a determinação da sequência em que as ações dos jogadores são processadas é fundamental para assegurar a equidade e a consistência do sistema. Esse mecanismo de ordenação garante que todos os participantes tenham a oportunidade de realizar suas ações em seu respectivo turno, evitando conflitos e prevenindo a invalidação de jogadas decorrentes de execuções concorrentes (Ramos, 2024).

Além de ser um jogo cliente-servidor, o Jogo Booleanas é caracterizado por ser um jogo por turnos, em que cada jogador tem a sua vez para executar a sua ação (jogada). Nesse caso, em uma rodada, cada jogador possui um turno para avançar e, após a sua ação, a decisão da sua jogada é enviada ao servidor que notifica sobre a mesma para todos os demais clientes (jogadores). Para Ramos (2024), os jogos multiplayers em tempo real viabilizam uma forma das pessoas interagirem e sentirem-se parte de uma comunidade. Esse fato é mais um aspecto que torna o Jogo Booleanas interessante para as meninas da educação básica, tanto por conhecerem mais mulheres cientistas da área das exatas e, assim, sentirem-se representadas, bem como, por participarem de uma comunidade de jogos femininos.

Com relação ao sincronismo, o servidor apenas precisa garantir que todos os jogadores recebam a última atualização da jogada do último jogador. Já, referente à latência, nos jogos por turno, é aceitável uma latência maior, no entanto, para a continuidade do jogo, é preciso que as respostas das jogadas sejam entregues em algumas poucas centenas de milissegundos (Cecin; Trinta, 2007).

## 3. Trabalhos Relacionados

Nesta Seção serão apresentados trabalhos que abordam jogos multiplayers e jogos educacionais, principalmente, voltados à igualdade de gênero.

O trabalho desenvolvido por Silvia et al (2024), apesar de apresentar um jogo de memória impresso, se refere exclusivamente a mulheres e suas contribuições para a história da Computação, priorizando uma diversidade de etnias, cores e identidades de gênero. O jogo é

impresso e foi construído sob uma ótica de computação desplugada, em que não há a necessidade de equipamentos eletrônicos e/ou laboratórios para que a ação seja executada. O jogo é composto por 12 (doze) mulheres personalidades femininas e está disponível para ser acessado via Canva, além de estar licenciado por meio da licença Creative Commons. Os autores aplicaram o jogo em sala de aula, para alunas do 3º ano do Ensino Fundamental e os resultados sugerem que os estudantes que participaram, conseguiram estabelecer associações entre as contribuições e as figuras das cientistas, o que indica um processo de aprendizagem e memorização dos feitos destacados no jogo.

O minijogo Bugou foi desenvolvido por Tanaka, Bruschi e Odakura (2025) e apresenta um minijogo que conta a história de Grace Hopper de maneira divertida para um público jovem. O jogo possui dinâmicas simples e busca transmitir um pouco da história e feitos, buscando engajar os jogadores. As autoras relatam que o jogo pode ser aplicado para estudantes do ensino médio e ensino superior. Os resultados mostraram que o minijogo teve muito potencial e contribuiu para que os participantes conhecessem mais sobre a história de Grace Hopper.

Uma outra proposta de jogo foi apresentada por Lucena, Nakamura e Lucena (2025). Neste trabalho foi desenvolvido um jogo para divulgar a história de grandes mulheres da computação. O jogo se propõe a incentivar o interesse pela participação feminina na ciência, catalogando as contribuições de três mulheres importantes para a área da computação, colaborando, desta forma, com o processo de ensino-aprendizagem de crianças e préadolescentes.

Na pesquisa realizada por Santos, Leite e Rabelo (2024) é apresentado o jogo digital educacional Thinking Girl. O objetivo da ferramenta é estimular o interesse pela computação através do Pensamento Computacional, desafiando as usuárias a resolverem problemas de raciocínio lógico sob a orientação de figuras femininas históricas da tecnologia. O jogo é dividido em quatro fases, sendo que cada fase aborda um dos pilares do pensamento computacional, um desafio a ser solucionado e uma personalidade feminina da computação que irá auxiliar o jogador. São apresentadas quatro personalidades femininas. Como o jogo ainda está em desenvolvimento, os autores esperam que, após a aplicação do jogo, as alunas demonstrem uma melhora nas habilidades de Pensamento Computacional e um maior interesse na área de computação.

O jogo denominado Mundo Bit Byte, desenvolvido por (Bricenõ et al., 2021), foi criado por um time de meninas de graduação e ensino médio, cuja temática e enredo são baseados em cinco personalidades femininas da área da Computação. Cada fase do jogo é inspirada na vida de uma dessas mulheres, mostrando as conquistas e outros aspectos relevantes da de cada uma. Além de realizar uma ddivulgação científica de forma lúdica, as pessoas autoras relataram que o jogo despertou o interesse dos jogadores em conhecer mais sobre personalidades femininas na história da computação.

Os projetos supracitados apresentam jogos com objetivos similares ao da proposta desse trabalho. O primeiro trabalho citado foi proposto em formato físico e os demais, em formato digital, todos voltados ao protagonismo feminino na tecnologia. Embora existam iniciativas relevantes, muitos desses jogos ainda são predominantemente utilizados em ambientes desktop, o que reforça a importância do desenvolvimento de ferramentas inovadoras, disponíveis de forma online, acessíveis simultaneamente por múltiplos usuários e em qualquer plataforma, como proposto no jogo deste trabalho.

O Jogo Booleanas permite explorar 50 cientistas da área das Exatas, diferentemente das propostas apresentadas que se limitam a poucas pesquisadoras. Além disso, nenhum dos trabalhos relacionados permite múltiplas jogadoras, que é um grande diferencial da presente proposta já que promove maior engajamento e uma competitividade saudável, oportunizando

uma aprendizagem ativa de forma lúdica e descontráida. Dessa forma, a abordagem da diversidade de gênero em formato de jogos contribui para tornar o ensino na área mais inclusivo e diversificado, especialmente para alunas da educação básica, que já estão familiarizadas com o uso de jogos digitais.

## 4. Materiais e métodos

A proposta aqui apresentada se classifica com relação aos seus objetivos como uma pesquisa descritiva e quanto à natureza é uma pesquisa aplicada ao ensino. A proposta desse trabalho apresenta o desenvolvimento de uma ferramenta online em formato de jogo multiplayer distribuído.

O desenvolvimento do jogo foi realizado em um ambiente composto por um computador pessoal com sistema operacional Windows, utilizando o editor de código Visual Studio Code e seu terminal integrado. Para a implementação da aplicação, foram empregadas tecnologias tanto de frontend quanto de backend. No frontend, utilizou-se o framework React.js, com a linguagem TypeScript, além do Vite como ferramenta de construção e compilação.

No backend, utilizou-se o framework Express, com a linguagem JavaScript, para a construção de um servidor capaz de gerenciar conexões em tempo real, atendendo às demandas da aplicação. Para viabilizar a comunicação em tempo real, foi adotado o protocolo WebSocket, por meio da biblioteca Socket.IO, permitindo a sincronização dos estados do jogo entre clientes e servidor. As imagens do fundo das telas do jogo foram geradas por meio de inteligência artificial generativa, usando o Gemini. Já o design das cartas foi desenvolvido com identidade visual e logo pelas bolsistas do projeto, além de formatação adequada ao tamanho de cartas de baralho.

## 5. Booleanas: Um Jogo de Mulheres Cientistas nas Exatas

O jogo da memória sobre mulheres cientistas da área das exatas, denominado Booleanas, é composto por 50 cartas que representam personalidades femininas dessas áreas. Na dinâmica do jogo, cada par de cartas é formado e pontuado quando a jogadora encontra as duas cartas correspondentes à mesma cientista. Quando a jogadora encontra a carta correspondente, são apresentadas informações sobre a pesquisadora da carta, incluindo sua área de atuação e suas principais contribuições.

A implementação da mecânica do jogo incluiu um modelo de cartas baseado na interface Card, responsável por identificar pares, imagens e textos informativos. Além disso, foi desenvolvido o gerenciamento do estado do jogo, contemplando o embaralhamento das cartas, a seleção, a verificação de pares, o controle de pontuação, o ranqueamento e o fornecimento de feedback sobre acertos e erros. Além disso, foi implementada também a sincronização em rede para o modo multiplayer, na qual o servidor mantém o estado da sala e propaga atualizações, como turnos, cartas viradas e jogadores conectados.

O jogo está disponível para acesso via link: https://booleanas.duckdns.org. A Figura 1 apresenta a tela inicial do jogo, que permite a jogadora criar uma nova sala ou ingressar em uma sala já existente. Ao optar pela criação de uma nova sala, é gerado automaticamente um código que pode ser compartilhado com outras jogadoras. Por outro lado, ao escolher entrar em uma sala em andamento, basta inserir o código correspondente.

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

20º Women In Information Technology (WIT 2026): Ferramentas

Figura 1. Tela inicial

Ao selecionar a opção de criar uma sala, a jogadora é direcionada para uma tela na qual deve inserir seu nome, conforme ilustrado na Figura 2a.

Figura 2. a) Tela de abertura de nova sala, b) Sala com jogo em andamento

Caso a jogadora escolha entrar em um jogo em andamento, a mesma deve ter código da sala para poder jogar e inserir o seu nome. A Figura 2b apresenta a opção de entrar em sala já existente.

A primeira jogadora (host), ao entrar na sala, é identificada como “Jogadora 1”. Nesse momento, a chave da sala é gerada e exibida na parte superior direita da tela, permitindo seu compartilhamento com as demais jogadoras convidadas. Nessa mesma interface, também é possível selecionar a quantidade de cartas desejadas na jogada. A Figura 3 apresenta a tela de seleção da quantidade de cartas do jogo.

Figura 3. Escolha da quantidade de cartas

O jogo é habilitado apenas quando há, no mínimo, duas jogadoras. Ao iniciar a partida, uma mensagem indicando “Jogo iniciado” é exibida as participantes. Na parte superior da interface, é possível visualizar qual jogadora possui o turno, sendo essa informação destacada em rosa. No lado direito da tela, são apresentadas todas as jogadoras participantes, suas respectivas pontuações e a rodada atual do jogo. O nome destacado com um contorno azul na lista de jogadoras indica a responsável pela criação da sala ( host ). Já a jogadora com o nome destacado em rosa indica quem está com a vez de jogar.

Como se trata de um jogo da memória, cujo objetivo é encontrar pares de cartas idênticas de mulheres cientistas, as cartas permanecem inicialmente viradas para baixo, estimulando habilidades como atenção, concentração e raciocínio lógico. Quando duas cartas correspondentes são selecionadas corretamente, ou seja, quando a jogadora da vez encontra um par, é exibida automaticamente uma tela com informações adicionais sobre a cientista, incluindo sua trajetória, contribuições, área de atuação e descobertas relevantes.

A Figura 4 apresenta um exemplo das cartas do jogo, com jogadas diferentes. Nesse caso, destaca-se a matemática Karen Uhlenbeck, reconhecida por ser a primeira mulher a receber o Prêmio Abel, considerado equivalente ao “Nobel” da Matemática, bem como outra tela com várias personalidades femininas mais contemporâneas. Ao acertar o par de cartas, uma outra tela é aberta apresentando detalhes sobre a personalidade feminina.

Figura 4. Telas com exemplo de acerto das cartas

Caso a jogadora não acerte a correspondência das cartas, a vez é repassada para a próxima jogadora, sendo emitidas mensagens em azul, indicando que ela não acertou e quem será a próxima a jogar. Mensagem: “Não é par. Próximo jogador1”. Ao fim de cada rodada, é apresentada a jogadora vencedora, como ilustrado na Figura 5.

- 46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

 - 20º Women In Information Technology (WIT 2026): Ferramentas

Figura 5. Quando uma jogadora vence a rodada

Em caso de empate, são exibidos os nomes das jogadoras que obtiveram a mesma pontuação na rodada, como ilustrado na Figura 6, que neste caso, são as Jogadora1 e Jogadora2.

Figura 6. Caso de empate

Ao final das três rodadas de jogo, é apresentada a jogadora vencedora, bem como a pontuação total de todas as participantes, exibida em formato de lista ordenada de forma ascendente. A Figura 7 ilustra a tela com a mensagem de final do jogo e as devidas pontuações.

Figura 7. Fim do jogo

20º Women In Information Technology (WIT 2026): Ferramentas

Uma situação recorrente em jogos online refere-se à saída de uma jogadora antes do término da partida. Nessa circunstância, por exemplo, caso a Jogadora 2 saia do jogo, sua vez é automaticamente transferida para a próxima participante, no caso, a Jogadora 3. Além disso, é exibida uma mensagem na tela informando a saída da jogadora. O nome da jogadora que deixou a partida permanece na lista de participantes, porém destacado em cinza, indicando sua ausência. Essa jogadora não é removida da lista, pois ainda pode retornar ao jogo, caso a saída tenha ocorrido por falha de conexão. Essa situação está ilustrada na Figura 8.

Figura 8. Tela com avisos e saída de jogadora

A lógica implementada para o cálculo da quantidade de cartas por partida permite sua distribuição ao longo das jogadas, podendo variar o número de cartas de 8 a 50, sendo configurável pela pessoa jogadora, o que permite uma quantidade maior ou menor de cartas a serem apresentadas na jogada. À medidad em que o jogo é estruturado em quantidade de cartas, muda o níveil de dificuldade de memorização em uma forma progressiva.

Sendo assim, o jogo Booleanas permite que várias jogadoras distribuídas fisicamente possam entrar em uma mesma partida. Após a definição da quantidade de cartas desejadas para a partida, as jogadas iniciam e, como é um jogo da memória, a jogadora pontua quando conseguir identificar duas cartas da mesma cientista. A pontuação ocorre em um modelo de ranking, onde os maiores pontos ganham um troféu virtual, o que pode gerar maior engajamento entre as jogadoras. Além disso, o jogo da memória permite que mais cientistas mulheres sejam reconhecidas em um universo ainda tão masculino.

O jogo da memória Booleanas contribui para a educação nas áreas de Exatas e da Computação ao promover a quebra de estereótipos, evidenciando que mulheres foram e continuam sendo protagonistas em teorias, descobertas e inovações. Além disso, incentiva a diversidade ao apresentar referências femininas nessas áreas, especialmente para alunas da educação básica, público em que o projeto tem maior atuação. Ressalta-se que as cartas apresentam tanto mulheres reconhecidas historicamente, como pesquisadoras mais contemporâneas, inclusive brasileiras, dando visibilidade para pesquisadoras em atividade, permitindo que as jogadoras percebam a ciência como uma carreira viável e próxima da sua realidade. A aprendizagem, mediada pela divulgação científica, pode ser realizada de forma lúdica, e ainda ser potencializada pelo uso do jogo, ocorrendo como atividade complementar em contextos escolares. Dessa forma, contribui para a disseminação do conhecimento científico e tecnológico pelas jogadoras ao longo das partidas.

## 6. Considerações finais

A divulgação científica de mulheres das exatas ainda precisa ser desenvolvida e apresentada na educação básica, pois acredita-se que promover o contato das meninas com STEAM desde cedo, além de proporcionar acesso a uma educação de qualidade, também favorece uma melhoria na sua autopercepção em relação às suas capacidades e possiblidades de carreiras. A proposta aqui exposta apresentou um jogo de memória de mulheres das exatas, intitulado por Booleanas, que contribui para auxiliar nessa divulgação científica de forma mais atrativa para meninas da educação básica, fugindo de apresentações em slides e oferecendo uma dinâmica por meio do jogo, oportunizando que essas meninas aprendam e conheças as personalidades femininas de uma forma muito mais atrativa.

O Jogo Booleanas foi desenvolvido com base em uma arquitetura distribuída e multiplayer. O jogo permite a participação simultânea de múltiplas jogadoras em tempo real e a partir de diferentes dispositivos, sendo essa uma das grandes vantagens da proposta em relação a outras disponíveis com o mesmo objetivo. O jogo Booleanas favorece a interação entre as participantes, inclusive por meio de mecanismos de ranqueamento de pontuação. A experiência de aprendizagem mediada pelo jogo promove respostas emocionais, fazendo o uso de elementos de gamificação que contribuem para o aumento da motivação no processo de aprendizagem (Alves, 2015).

Como trabalhos futuros, busca-se realizar testes para validação de todas as funcionalidades do jogo, bem como levá-lo para as escolas e aplicar com turmas das escolas participantes do projeto, buscando obter dados para um relato de experiência das aplicações relizadas, e implementando melhorias de jogabilidade. Além disso, a divulgação científica pode ser realizada pelo corpo docente escolar, podendo o jogo ser usado em formações docentes das secretarias de educação. Ademais, deseja-se ampliar a quantidade de cartas com novas personalidades femininas, possibilitando realizar uma divulgação científica contínua de novas pesquisadoras, principalmente dando a opção de ter cientistas classificadas por suas áreas de atuação. Com relação ao tipo de jogo, pretende-se desenvolver uma nova versão utilizando um framework de jogos de cartas ubíquos como, por exemplo, o framework chamado Tardigrade, o que minimiza desafios de implementação para esse tipo de jogo. O framework permite desenvolver jogos de cartas que permitam interação do real com virtual, o que pode ser bem interessante para ambientes escolares, como olimpíadas, dentre outros.

## Declaração do Uso de Ferramentas de Inteligência Artificial Generativa

No presente trabalho, conforme mencionado na seção de metodologia, foi utilizado o assistente de inteligência artificial Gemini para a geração das imagens de fundo do jogo. Adicionalmente, o ChatGPT foi empregado na revisão textual, especialmente no que se refere aos aspectos gramaticais.
