# Explorando a vida de Hedy Lamarr em um jogo motivacional para meninas em STEM

Paula Y. Nizer, Carolina Paula de Almeida, Sandra Mara Guse Scós Venske

1 Departamento de Ciência da Computacão (DECOMP) Universidade Estadual do Centro Oeste (UNICENTRO) Alameda Elio Antonio Dalla Vecchia, 838 – Vila Carli – CEP 85040-167 Guarapuava, PR – Brasil

paulaynizer@gmail.com, { carol,ssvenske } @unicentro.br

Abstract. This work aims to help reduce the gender gap in technology by highlighting the fundamental role of women in STEM fields. To this end, a 2D pointand-click adventure game was developed, inspired by the life and achievements of Hedy Lamarr, a pioneer in the history of computing. The proposed game, presents puzzles that stimulate logical thinking, while exploring Lamarr’s story and her contribution to Wi-Fi technology. The aim of this work is to help inspire young women to consider the fields of Science, Technology, Engineering and Mathematics (STEM) as a career possibility. The game was developed on the Unity platform for mobile devices.

Resumo. Este trabalho visa ajudar a reduzir a disparidade de gênero na área da tecnologia, destacando o papel fundamental das mulheres nas áreas de STEM.Para isso foi desenvolvido um jogo 2D do tipo Point and Click Adventure, inspirado na vida e realizações de Hedy Lamarr, uma pioneira na história da computação. O jogo proposto apresenta quebra-cabeças que estimulam o raciocínio lógico, enquanto explora a história de Lamarr e sua contribuição relacionada à tecnologia Wi-Fi. O objetivo deste trabalho é ajudar a inspirar jovens mulheres a considerarem as áreas de Ciência, Tecnologia, Engenharias e Matemática (do inglês, STEM) como uma possibilidade de carreira. O jogo foi desenvolvido na plataforma Unity para dispositivos móveis.

## 1. Introdução

São várias as mulheres que tiveram um papel crucial na história das áreas de STEM ( Science, Technology, Engineering, and Mathematics ). Segundo [Morais and Morais 2020], houve um tempo em que o gênero feminino era dominante na área. Entretanto, a partir da metade década de 80 o percentual de mulheres decresceu abruptamente e atualmente é evidente a discrepância de gênero em cursos de STEM, nos quais a presença masculina é predominante. De acordo com o [IBGE 2024], as mulheres representam apenas 15,7% das matrículas em cursos de graduação na área de Computação e Tecnologias da Informação (TIC). Dessa forma, a alta taxa de evasão de mulheres na área de STEM nos últimos anos é um desafio significativo, cujas razões são multifacetadas. Além de questões culturais, históricas e sociais, a falta de representação adequada das mulheres na área contribui para esse cenário, conforme destacado por [Morais and Morais 2020].

Diante da urgente necessidade de promover a inclusão das mulheres nas áreas de STEM, se faz necessário a tomada de medidas com o objetivo de reverter essa situação.

Diante disso, a Organização das Nações Unidas para a Educação, a Ciência e a Cultura (UNESCO), agência especializada das Nações Unidas (ONU), adicionou na agenda de 2030 um projeto chamado #EDUCASTEM2030 com objetivos que vão desde aumentar a conscientização sobre a importância da educação em STEM para meninas e mulheres no Brasil até diminuir a lacuna de gênero em profissões na área de STEM [UNESCO 2022]. Jogos relacionados ao tema são uma das estratégias abordadas neste projeto.

Dessa forma, a aplicação da aprendizagem baseada em jogos emerge como uma estratégia promissora de incentivo para mulheres na área de STEM. Os jogos oferecem um ambiente motivador e envolvente onde os utilizadores “aprendem a jogar, jogando” graças a desafios ajustados ao nível de competência do jogador e a uma realimentação constante [De Carvalho 2015]. A visão complementar de [Santos et al. 2021] ressalta que conhecer ou testar conhecimentos de forma descontraída, motiva e pode potencializar a aprendizagem, ampliando assim as possibilidades de engajamento e inclusão das mulheres nessas áreas. Diversos trabalhos já foram empreendidos nessa direção, como o projeto “Personalities” [de Oliveira et al. 2019] e o jogo de tabuleiro “Computasseia” [Alencar et al. 2019], os quais visam disseminar as narrativas de mulheres notáveis no campo da computação. Adicionalmente, exemplos digitais incluem o questionário interativo “Quem Sou Eu” [Milson et al. 2020] e a plataforma de jogo “Mundo Bit Byte” [Briceño et al. 2021], desenvolvida na plataforma Unity.

No presente estudo é desenvolvido um jogo 2D para dispositivos móveis no estilo Point and Click Adventure, o qual é descrito por [Vraneˇsevi´c 2014] como centrado em diálogos, resolução de quebra-cabeças e interações de apontar e clicar na tela. Inspirado na vida de Hedy Lamarr, pioneira da tecnologia Wi-Fi, o enredo do jogo incorpora desafios e elementos característicos de sua história. O principal objetivo deste trabalho é utilizar o jogo como uma ferramenta, utilizando a plataforma Unity, para promover a participação das mulheres na STEM e estimular a representatividade de forma lúdica.

O artigo está organizado como segue. A Seção 2 apresenta a fundamentação teórica envolvendo conceitos importantes e trabalhos relacionados. A Seção 3 demonstra o desenvolvimento do jogo com sua descrição e modelagem. A Seção 4 apresenta os resultados e, por fim, a Seção 5 descreve algumas considerações finais e trabalhos futuros.

## 2. Fundamentação Teórica

A presente seção define os principais conceitos necessários para o desenvolvimento deste trabalho. Inicialmente, são apresentados os conceitos de aprendizagem baseada em jogos, incluindo o estilo de jogo Point and Click Adventure (Seção 2.1). Em seguida, um pouco da vida de Hedy Lammar é apresentada (Seção 2.2). Por último, são tratados alguns trabalhos correlatos na Seção 2.3.

### 2.1. Aprendizagem baseada em jogos

A Aprendizagem Baseada em Jogos (GBL de Game-Based Learning ) é uma metodologia pedagógica que se possui foco na concepção, desenvolvimento, uso e aplicação de jogos na educação e na formação [De Carvalho 2015]. Para [Santos et al. 2021], o ensino através de jogos tem o potencial de atrair o aluno para uma vivência diferenciada de aprendizagem. Deste modo, essa estratégia pode ser utilizada para promover a aprendizagem de forma lúdica e engajadora, além de aumentar a visibilidade de temas relevantes.

Neste trabalho, optou-se pelo desenvolvimento de um jogo do gênero Point and Click Adventure, que se caracteriza pelo foco no diálogo e na resolução de quebracabeças. Para este estilo de jogo a progressão se dá através da interação com o cenário, apontando e clicando em objetos e personagens [Vraneˇsevi´c 2014]. Segundo [Pérez-Colado et al. 2019], esse estilo de jogo pode ser facilmente incorporado no contexto de aprendizagem baseada em jogos pois sua dinâmica se baseia na habilidade do jogador em solucionar quebra-cabeças (pequenos desafios de raciocínio lógico) através da interação com o ambiente para progredir no jogo.

### 2.2. Hedy Lamarr

Hedwig Eva Maria Kiesler, conhecida como Hedy Lamarr, nasceu em Viena, Austria, em 9 de novembro de 1914. Filha de pais de classe média, ela revelou uma inteligência curiosa desde jovem e uma paixão pela tecnologia, desmontando máquinas para entender seu funcionamento [Morais and Morais 2020].

Apesar de seu sucesso no cinema, Hedy Lamarr também tinha um interesse em invenções e tecnologia. Durante a Segunda Guerra Mundial, ela se concentrou em contribuir para a causa aliada, buscando maneiras de melhorar os torpedos para a marinha. Ela desenvolveu a ideia de salto de frequência, do inglês frequency hopping, um sistema em que as frequências de comunicação mudavam rapidamente, tornando os sinais de rádio mais seguros e difíceis de interceptar [Morais and Morais 2020].

Hedy se uniu ao compositor George Antheil para patentear essa inovação, mas o projeto foi inicialmente rejeitado pela Marinha dos Estados Unidos. No entanto, sua ideia foi posteriormente adotada e se tornou fundamental para tecnologias modernas, como Wi-Fi e Bluetooth. Apesar disso, ela não foi reconhecida e nem financeiramente recompensada por suas contribuições [Morais and Morais 2020].

### 2.3. Trabalhos Correlatos

Nesta seção, será apresentado um quadro comparativo de trabalhos correlatos que abordam jogos com temáticas relacionadas a mulheres nas áreas de ciências exatas. Os jogos mencionados são projetos que buscam promover o conhecimento sobre mulheres importantes na área de ciência e tecnologia e incentivar a participação feminina em cursos relacionados à STEM. Na Tabela 1 são apresentados alguns trabalhos relacionados.

O trabalho Computasseia [Alencar et al. 2019] sugere a utilização de um jogo de cartas impresso como meio de promover o conhecimento sobre a história da computação. Similarmente, Personalities [de Oliveira et al. 2019] é um jogo de cartas impressas que visa destacar personalidades na área de computação enquanto promove discussões sobre questões de gênero.

Outro exemplo é o Mundo Bit Byte [Briceño et al. 2021] é um jogo para dispositivos móveis projetado para disseminar conhecimento sobre mulheres na computação e estimular meninas do ensino fundamental e médio a considerarem carreiras na área de tecnologia, sendo desenvolvido na plataforma Unity. Já o Peg.Ada [Vinhal and Odakura 2023] tem o propósito de educar meninas sobre a importância da proteção de sua privacidade e segurança online, orientando-as sobre ética e segurança digital.

O OurPlace: Hedy Lamarr se distingue dos jogos descritos, principalmente, devido ao seu gênero de jogo, o point and click adventure. Seu objetivo central é ilustrar a relevância das mulheres nas áres de STEM por meio da narrativa de Hedy Lamarr.

|Tabela 1. Trabalhos relacionados.|
|---|

|Jogo|Objetivos|Meios|Tipo|Ferramentas|
|---|---|---|---|---|
|Jogo proposto|Demonstrar a importância das mulheres na área das ciências exatas por meio da história de Hedy Lamarr e incentivar a participação feminina em cursos de STEM.|Mobile Android|Point and click adventure|Unity|
|Computasseia [Alencar et al. 2019]|Promover o conhecimento sobre a história da computação.|Impresso|Cartas|Sem menção|
|Mundo Bit Byte [Briceño et al. 2021]|Difundir conhecimento sobre mulheres da computação para meninas do ensino fundamental e médio visando incentivá-las a considerar cursos relacionados à tecnologia de informação.|Mobile Android|Plataforma|Unity|
|Personalities [de Oliveira et al. 2019]|Divulgar personalidades importantes porém pouco divulgadas na área de computação e discussão degênero.|Impresso|Cartas|–|
|Peg.Ada [Vinhal and Odakura 2023]|Instruir meninas do ensino médio a tomarem cuidado com informações compartilhadas na Internet.|Desktops|Narrativa|Unity|

## 3. Desenvolvimento

O jogo proposto é destinado para plataforma mobile Android e foi desenvolvido utilizando a ferramenta Unity e a linguagem C#. Como editor de Código foi utilizado o Visual Studio Code onde foi feita toda a programação. Para as interfaces gráficas foi utilizada a ferramenta Canva, que permite a desenvolvimento de cenários e elementos gráficos com facilidade. Para criação da personagem Hedy, foi escolhida a ferramenta Leonardo.ia, a qual gera imagens usando inteligência artificial a partir de comando de texto.

> 2unity.com

> 3www.code.visualstudio.com

> 4canva.com

> 5https://leonardo.ai

O jogo visa incentivar o ingresso de meninas em cursos de da área de STEM. Isso se dá por meio do enredo que se baseia na história de Hedy Lamarr, uma importante personalidade feminina da computação. Entre as fontes utilizadas como base e inspiração para criação do enredo e dos quebra cabeças pode-se citar [de Oliveira et al. 2019] e [Morais and Morais 2020].

O jogo se passa em um ambiente fictício que representa a casa de Hedy. Neste ambiente o jogador deve explorar o cenário por meio do clique. O jogo possui um inventário no qual o jogador pode armazenar e utilizar os objetos que coletar. O objetivo final do jogo é despertar Lamarr de um sono profundo, para isso o jogador deve encontrar sete objetos relacionados na vida de Hedy:

1. Partitura: Hedy era pianista e isto foi fundamental em sua invenção do sistema de comunicação por salto de frequência;

2. Coroa de Flores: representa a beleza icônica de Hedy Lamarr. Ela era conhecida por sua aparência deslumbrante e elegante;

3. Maçã: está associada a um curioso boato sobre a influência de Hedy Lamarr na criação da famosa personagem Branca de Neve pela Disney;

4. Caixa de música: Hedy Lamarr desmontou quando criança uma caixa musical para entender seu funcionamento interno. Esse ato reflete a sua engenhosidade e mente inventiva;

5. Calçada da Fama: símbolo do reconhecimento de sua carreira em Hollywood;

6. Ciência: este elemento simboliza o espírito científico e a curiosidade de Hedy Lamarr;

7. Invenção: Hedy desenvolveu um sistema de comunicação por salto de frequência, uma tecnologia revolucionária que foi precursora da tecnologia de comunicação Wi-Fi.

Para encontrar cada um desses elementos o jogador deve resolver os quebracabeças presentes nos cenários. Quando todos os elementos forem encontrados, o jogador recebe uma explicação sobre cada um deles e como se relacionam com a vida de Hedy Lamarr.

### 3.1. Modelagem

As Figuras 1 e 2 apresentam os fluxogramas da modelagem do jogo. Nos fluxogramas são representados o início e fim do jogo, em blocos cinzas, seguido pelo contexto atual do jogo, em rosa. Os blocos brancos representam ações que o jogador deve realizar.

No Fluxograma 1, como mostra a Figura 1, é retratada a parte do jogo em que o jogador deve encontrar os objetos nos cenários. A relação de dependência entre os cenários foi modelada de modo a explicar qual cenário pode ser acessado a partir de qual. Também é representado o cenário em que cada objeto se encontra e a ação do jogo que leva a guardar o objeto encontrado no inventário. Tanto para encontrar os objetos quanto para desbloquear cenários é preciso resolver quebra-cabeças. Por exemplo, a Coroa de Flores se encontra no cenário Jardim, mas para acessá-lo, é preciso desbloqueá-lo no cenário da Sala. Após ser encontrado e clicado, o objeto vai para o inventário.

O Fluxograma 2, apresentado na Figura 2, descreve a sequência de ações finais do jogo, onde o jogador busca despertar Hedy Lamarr de seu sono profundo. O fluxograma

Figura 1. Fluxograma 1 que retrata a tarefa de encontrar objetos no cenário do jogo proposto.

retrata as etapas que ocorrem no Museu, que só podem ser acessadas após desbloqueio de uma passagem secreta a partir da Sala. São sete etapas e cada uma representa a ação de colocar um objeto encontrado ao longo da exploração dos outros cenários no Museu. Para isso, é necessário que o jogador tenha os objetos no inventário, embora não seja necessário possuir todos de uma vez, podendo adicioná-los conforme são encontrados. Cada objeto coletado deve ser colocado em um pilar do Museu de acordo com o desenho correspondente do pilar. Ao adicionar o objeto no lugar correto o jogador recebe uma explicação sobre sua relevância para a história de Hedy Lamarr. Ao reunir todos os objetos, o jogador obtém uma Poção que possibilita acordar Hedy do sono profundo, concluindo o jogo.

## 4. Resultados e Discussões

Esta seção apresenta algumas das telas do jogo desenvolvido. Para o desenvolvimento dos elementos gráficos do jogo foi utilizada a ferramenta Canva e a implementação deste projeto foi realizada na Unity Editor, um ambiente de desenvolvimento da Unity, onde as interfaces e a mecânica do jogo foram criadas, unindo os elementos gráficos e os scripts escritos na linguagem de programação C#. O jogo desenvolvido está disponível para

Figura 2. Fluxograma 2 que retrata a sequência de aç ões finais do jogo.

download em dispositivos Android na Play Store.

Foram escolhidas algumas das telas e cenários, representadas nas Figuras de 3 a 7, para exemplificar o jogo. A tela inicial apresentada na Figura 3 contém o nome do jogo seguido por um botão para iniciar.

O jogo é composto por sete cenários: Museu, Jardim, Laboratório e Sala, sendo que o último se divide em quatro cenários que representam as visões de dentro da Sala. A Figura 4 mostra quatro deles. O inventário, representado pela imagem “c” na Figura 4, é o elemento responsável por armazenar os objetos coletados pelo jogador. Os objetos interativos do cenário vão para uma barra lateral no lado direito da tela, o inventário. Esses objetos ficam disponíveis para que o jogador arraste-os pelo cenário e desencadeie outras ações. Por exemplo, arrastar uma chave até uma porta para destrancá-la.

Para ajudar o jogador a encontrar os objetos necessários existem dicas escondidas

> 6https://play.google.com/store/apps/details?id=com.paulaynizer.OurPlaceHedyLamarr

Figura 3. Tela inicial do jogo desenvolvido.

Figura 4. Telas a), b), c) e d) são exemplos de cenários do jogo proposto e c) mostra o Inventário.

pelo cenário. Uma delas é apresentada na janela de um dos cenários - retratada na Figura 5, e é crucial para desvendar o quebra-cabeça relacionado à Invenção. Ao limpar a mancha que a esconde é revelada a pista escrita, com informações essenciais sobre como posicionar os pontos pretos da Invenção entre as frequências corretas. Um dos objetos mais importantes do jogo é a Invenção. Ela exemplifica um dos quebra-cabeças presentes no jogo e representa o feito de Hedy sobre a tecnologia de salto de frequência. O objeto Invenção (Figura 6) foi feito para representar de forma lúdica a tecnologia de Hedy.

O cenário do Museu, representado pela Figura 7, é onde os objetos coletados durante o jogo serão colocados. Cada um dos 7 objetos que representam a vida de Hedy possui um lugar no museu. O jogador deve descobrir qual o lugar de cada objeto e colocá-lo. Assim, receberá uma explicação de sua importância na história de Hedy Lamarr.

A Figura 8 representa um dos cenários da Sala. Nele é possível notar a personagem Hedy em um sono profundo. E uma das cenas finais do jogo em que o jogador já encontrou os sete objetos, os colocou no Museu e recebeu a poção que se encontra no inventário. Por fim, a poção deve ser entregue a Hedy para despertá-a, concluindo, assim,

Figura 5. Dica da janela para resolver o quebra-cabeça da Invenç ão.

Figura 6. Quebra-cabeças da Invenç ão do jogo proposto.

Figura 7. Museu de Hedy, um dos cenários do jogo proposto.

o jogo. A Figura 9 representa a cena final do jogo, na qual Hedy desperta e agradece ao jogador, contando um pouco de sua história e finalizando o jogo.

Os cenários do jogo desenvolvido são visualmente cativantes e envolventes para os jogadores, os que os incentiva a continuar jogando e aprendendo. O tipo do jogo, Point and Click, permite uma interação ativa dos jogadores com o conteúdo relacionado a vida de Hedy Lamarr, proporcionando uma experiência hands-on que facilita a compreensão e a retenção do conhecimento. Os desafios, representados pelos quebra-cabeças, incentivam

Figura 8. Cena de Hedy em sono profundo.

Figura 9. Cena final do jogo proposto.

os jogadores a pensar criticamente e a resolver problemas de forma criativa.

## 5. Conclusões e Trabalhos Futuros

A aprendizagem baseada em jogos se mostra como uma ferramenta importante na motivação e promoção da representatividade feminina nos campos de STEM. Através do desenvolvimento do jogo é esperado o incentivo às meninas a considerarem cursos e carreiras nesta área.

O jogo desenvolvido neste trabalho, apesar dos objetivos educacionais, possui desafios que incentivam sua jogabilidade. Os quebra-cabeças presente nos cenários possuem a dificuldade de resolução pensada para motivar os jogador e manter seu interesse e divertimento. O inventário e interfaces atrativas são elementos que também contribuem para a jogabilidade e permitem uma melhor experiência para o jogador.

Como trabalhos futuros pode-se mencionar a realização de testes com usuários e a adição de aleatoriedade nos quebra-cabeças para maior interesse dos jogadores. Ademais, poderiam ser adicionadas novas fases, com diferentes desafios relacionados com outras situações da vida de Hedy Lamarr. Também menciona-se a possibilidade de adicionar músicas e efeitos sonoros e permitir a portabilidade para diferentes plataformas.
