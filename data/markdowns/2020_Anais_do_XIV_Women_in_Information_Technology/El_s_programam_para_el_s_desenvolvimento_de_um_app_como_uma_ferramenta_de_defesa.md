# El@s programam para el@s: desenvolvimento de um app como uma ferramenta de defesa a mais para as mulheres

Rosiane de Freitas, Bruna Mariana F. de Souza, Juliana Magalhães, Júlia Luiza Conceição, Maria Luiza Cordeiro, Matheus Uchôa

1Instituto de Computação – Universidade Federal do Amazonas (UFAM) 69077-000 – Manaus-AM, Brasil

{ rosiane,bruna.mariana,juliana.magalhães,jlslc } @icomp.ufam.edu.br

Abstract. This work addresses a multidisciplinary partnership action between computing and digital and women’s rights, involving OAB-AM and UFAM, through Cunhantã Digital project, for the development of a free and easy-to-use mobile phone application, to be one more form of defense for women in a situation of possible danger or even in real danger. The app SOS El@s sends an SMS message and other information to trusted contacts, as well as automatically opening a call to the police, using external buttons on the cell phone. A mixed team of developers was formed, with an emphasis on the participation of women but also with male students, from 03 undergraduate courses in Computing from UFAM. This action was challenging in many ways, but successful and the application in a Beta version is available for use.

Resumo. Este trabalho aborda uma ação multidisciplinar de parceria entre computação e direitos digitais e das mulheres, envolvendo a OAB-AM e a UFAM, através do projeto Cunhantã Digital, para o desenvolvimento de um aplicativo para telefone celular gratuito e de fácil uso, para ser mais uma forma de defesa para as mulheres em situação de possível perigo ou mesmo em perigo real. O app SOS El@s envia mensagem de SMS e outras informações a contatos de confiança, bem como abre chamada para a polícia automaticamente, isto apenas usando botões externos do aparelho de celular. Foi formada uma equipe mista de desenvolvedores, com ênfase na participação de mulheres mas contando com alunos homens também, de 03 cursos de graduação em Computação da UFAM. A empreitada foi desafiadora em vários aspectos, mas bem sucedida e o aplicativo na versão Beta está disponível para uso.

## 1. Introdução

Estamos vivenciando tempos mundialmente difíceis, com a pandemia da COVID-19 (doença causada pelo novo vírus SARS-COV-2, que se iniciou em 2019). Traçando um paralelo importante sobre a problemática tratada neste trabalho, cabe ressaltar que, em 2018, em um evento da ONU, o secretário-geral António Guterres afirmou que a violência contra as mulheres é uma ”pandemia global” [ONUBR 2018], com mulheres de todas as idades, classes sociais, níveis de escolaridade, opções religiosas e por todo o mundo, sofrendo violência dos mais variados tipos. E que o mundo só vai se orgulhar de ser justo e igualitário quando as mulheres puderem viver livres do medo e da insegurança cotidiana. Tal encontro marcou o lançamento da campanha #HearMeToo (#MeEscuteTambém),

que pede apoio às vítimas de violência de gênero, de modo a garantir que suas vozes e histórias sejam ouvidas, em vez de desacreditadas.

O impressionante neste contexto é que neste momento de pandemia de COVID19, aumentou ainda mais a violência contra mulheres. Em tempos de quarentena ou isolamento social, e a consequente diminuição da violência urbana (assaltos, agressões, etc), entre outras questões, está ocorrendo um aumento da violência doméstica. Mas, é importante ressaltar que a violência contra a mulher não se resolve com o fim deste isolamento social, mas sim com a desconstrução da masculinidade clássica e da desigualdade de gênero, além de políticas sociais e de renda.

Este é o cenário também do Brasil, que apresenta altos índices de violência contra as mulheres. Em 2017 foram registrados 4. 473 homicídios dolosos de mulheres (um aumento de 6, 5% em relação a 2016). E em grande parte, a violência que ocorre nos lares sequer são notificadas. Segundo o 12 Anuário Brasileiro de Segurança Pública de 2018 [FBSP 2018], o número de estupros no Brasil cresceu 8, 4% de 2016 a 2017, passando de 54. 968 para 60. 018 casos registrados. Isso significa que ocorreram cerca de seis estupros de uma mulher brasileira a cada dia. E nos casos de violência explícita, muitas vezes a mulher não tem alternativas para uma reação rápida, segura e efetiva.

Neste contexto, este trabalho relata uma parceria interinstitucional entre a academia e a justiça, buscando auxiliar no preenchimento desta lacuna, e tendo o propósito de desenvolver um aplicativo de apoio à defesa da mulher. Como fruto inicial da parceria, uma versão Beta do aplicativo foi lançada em março deste ano em um evento da OAB-AM, em mais uma contribuição do projeto Cunhantã Digital em concordância com o Programa Meninas Digitais da SBC [Maciel and Bim 2017].

O restante deste artigo está estruturado como segue. Na Seção 2, há uma descrição sobre o projeto do aplicativo SOS El@s como um todo, as funcionalidades desenvolvidas e a metodologia aplicada, com destaque para a formação da equipe de desenvolvimento responsável pelo aplicativo, as dificuldades encontradas e como foram solucionadas. Na Seção 4, são tecidas as considerações finais, com uma análise de aspectos envolvendo equipe, gênero, habilidades, complexidade de desenvolvimento, adequabilidade de uso da ferramenta e benefícios de uso, pontuando a boa repercurssão obtida na mídia local e as futuras ações e funcionalidades.

## 2. O aplicativo SOS El@s para a defesa da mulher

O SOS El@s é um aplicativo para telefone celular gratuito e de fácil uso, desenvolvido para ser mais uma forma de defesa para as mulheres em situação de possível perigo ou mesmo em perigo real. Projetado em dois níveis, primeiramente é apresentado um pequeno manual de uso, para em seguida se cadastrar os contatos de confiança da mulher (marido, filhos, amigos, etc). Após isto, pode-se sair do aplicativo e usá-lo normalmente para outros fins. Em situação de possível perigo basta apertar o botão de volume por 2 segundos e uma mensagem de socorro, sua geolocalização e fotos frontal e traseira são enviadas para os contatos de confiança cadastrados. E se a situação for de perigo real, além de apertar o botão de volume por 2s, deve-se agitar o celular que, uma chamada telefônica à polícia (190) é ativada. No aplicativo também pode-se ainda consultar informações sobre violência contra mulher, lei Maria da Penha, lei da Importunação Sexual, lei do Feminicídio e consultar uma lista de telefones e endereços úteis. Uma equipe

de desenvolvedores formada por alunos dos 03 cursos de Computação da UFAM (Ciência da Computação, Engenharia de Software e Engenharia da Computação) participaram do desenvolvimento da versão Beta do aplicativo, disponível para sistemas Android (e posteriormente para IOS também). Muitos desafios foram enfrentados, principalmente o prazo curtíssimo para ser gerada uma versão do app para o início de março, bem como a complexidade intrínseca das funcionalidades desejadas e tecnologias envolvidas, principalmente relativo ao uso de botões externos do app para outros fins, que dispara eventos para o app em background executar ações, envolvendo código nativo, e se configuram em características avançadas no desenvolvimento de aplicativos móveis.

Este aplicativo é fruto de uma parceria iniciada entre comissões da OAB-AM e a UFAM, através do projeto Cunhantã Digital, voltado para envolver mulheres em áreas de computação e STEAM (Science, Technology, Engineering, Arts and Mathematics) em geral, promovendo a atuação, fomentando a representatividade e liderança, e gerando conteúdo e ferramentas para a sociedade.

### 2.1. O projeto e a Equipe DEV

Devido ao prazo curto estabelecido para a entrega e apresentação de uma versão Beta do aplicativo, ocorreu que o desenvolvimento seguiu principios da metodologia ágil, dirigido a funcionalidade (Feature Driven Development - FDD), evidenciando principalmente a colaboração entre as pessoas da equipe mista, visto que poucos possuiam alguma experiência em desenvolvimento mobile. Além disso, a gerência dos problemas e complexidades de projeto utilizou a decomposição baseada em funcionalidades, seguida pela integração dos incrementos de software, e também utilizou-se a comunicação de detalhes técnicas usando formas verbais e texto.

A equipe do aplicativo SOS El@s foi composta por oito pessoas, sendo que sete delas são alunos da UFAM, em cursos e períodos diversificados, como apresenta a Tabela 1. A equipe foi composta em sua maioria por mulheres e contou com a supervisão da professora Rosiane de Freitas, onde poucos dos integrantes tinham experiência em desenvolvimento de aplicativos móveis. A dedicação e esforço da equipe para adquirir o conhecimento necessário resultou em muito aprendizado para todos, principalmente para os que ainda não possuíam experiência prévia.

Tabela 1. Perfil da equipe de desenvimento do app SOS El@s, segundo o curso de formaç ão,período, gênero e habilidades trabalhadas.

|Alunos|Curso|Período|Função no desenvolvimento|
|---|---|---|---|
|Aluna 1|Curso xx|3 Período|Construção de telas do APP|
|Aluno 2|Curso yy|6Período|Funcionalidades do APP|
|Aluna 3|Curso zz|5Período|Funcionalidades do APP e telas|
|Aluna 4|Curso xx|1Período|Funcionalidades do APP|
|Aluno 5|Curso zz|1Período|Funcionalidades do APP|
|Aluno 6|Curso zz|1Período|Funcionalidades do APP|
|Aluna 7|Aluna em transferência|—|Construção de telas do APP|
|Aluno 8|Curso yy|1Período|Funcionalidades do APP|

A maioria dos integrantes da equipe não se conhecia antes do desenvolvimento do aplicativo, entretanto, após a primeira reunião todos tiveram uma boa interação o que

os possibilitou também vivenciar o trabalho em equipe e um ambiente real de elaboração de um aplicativo mobile. Muitos enfrentaram desafios em suas funções devido a falta de experiência com a criação de aplicação mobile, contudo, conseguiram compartilhar bem o conhecimento que cada um tinha, facilitando a aprendizagem de cada um. Com o aplicativo SOS El@s todos ganharam experiência tanto em elaborar uma aplicação mobile como em experienciar um cenário real de uma equipe de desenvolvimento.

Nas Figuras 1 e 2 são apresentadas as telas do aplicativo SOS El@s, conforme descrição geral dada antes. Na Figura 1 são apresentadas telas representativas do app SOS El@s: tela de splash; tela principal do guia de uso; tela principal do cadastro; e, tela da aba sobre nós. Na Figura 2 são apresentadas informações gerais sobre leis voltadas ao combate à violência contra a mulher, como Lei Maria da Penha, da Importunação Sexual e do Feminicídio, bem como informações e telefones de contato importantes.

Figura 1. Algumas telas representativas do aplicativo SOS El@s, voltado para ser uma ferramenta a mais de auxílio à defesa da mulher.

Figura 2. Telas de informaç ão sobre auxílio da justiça, na forma de leis, como proceder e aç ões a tomar em caso de violência sofrida por mulheres.

## 3. Análise dos resultados e considerações finais

Fazendo uma breve análise sobre o aplicativo SOS El@s desenvolvido, ressalta-se que um dos pontos fortes foi a formação da equipe DEV, um grupo heterogêneo, onde se mesclou a experiência de alunos veteranos com a motivação e vontade de aprender de alunos calouros ou nos primeiros períodos de cursos de computação. Também ressalta-se que alunos de 3 diferentes cursos participaram, e com a predominância (mas não exclusividade) de mulheres. O processo de aprendizagem da equipe foi um dos pontos altos, com o cumprimento de prazos e desafios de conceitos e tecnologias envolvidos. Sobre aspectos computacionais e tecnológicos, ressalta-se que o aplicativo é de alta complexidade, exigindo um conhecimento avançado para suas principais funcionalidades (em suma, acionamento de botões externos do aparelho de celular, para ativar o app desligado ou em background, e assim avisar contatos de segurança ou ligar para a polícia, em um segundo

nível). Sobre aspectos de funcionalidade, ressalta-se de que não é preciso entrar no sistema para solicitar socorro, o que é um grande diferencial sobre os aplicativos existentes (e mesmo os que indicam possuir o mesmo tipo de funcionamento, ou não estão disponíveis na lojas públicas de aplicativos ou quando estão, não funcionam adequadamente). Cabe ressaltar que para aparelhos Samsung S8 ou mais e Apple IOS 11 ou superior, já existe um sistema de registro de contatos e envio de SMS e geolocalização, mas, o app SOS El@s proposto é mais democrático no sentido de poder ser usado em qualquer sistema e aparelho de celular (uma grande vantagem para o público-alvo, de mulheres de baixa renda e da base da pirâmide de níveis sociais, que são as mais expostas a situação de violência de gênero). Mas ainda assim, o aplicativo proposto envia outras informações aos contatos (como rastreamento, fotos e áudio), bem como possui um segundo nível de socorro, que consiste em, ao chacoalhar o aparelho, se abre uma chamada direto para o 190, número da Polícia. Na Figura 3 é apresentado um quadro comparativo entre o app SOS El@s e similares.

As ações do projeto SOS El@s, com a composição de uma equipe pouco experiente e em pouco tempo contribuem no combate à violência com consequente ferramenta democrática e de uso simples, para a defesa da mulher em situação de risco. O retorno foi imediato e o impacto na sociedade muito positivo, com covites para diversos espaços na mídia aberta. Em andamento, estão os ajustes e testes sistemáticos na versão Beta para uma maior consistência entre versões, bem como para disponibilização em outras plataformas.

Figura 3. Quadro comparativo entre o app SOS El@s e outros apps similares.
