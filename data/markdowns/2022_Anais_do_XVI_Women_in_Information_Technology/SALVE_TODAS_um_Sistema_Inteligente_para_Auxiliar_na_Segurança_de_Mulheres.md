# SALVE TODAS: um Sistema Inteligente para Auxiliar na Segurança de Mulheres

Maria Fernanda C. Ribeiro, Monica M. Pereira

Programa de Pós-Graduação de Sistemas e Computação – Universidade Federal do Rio Grande do Norte (UFRN) – Natal – RN - Brasil

fernanda.cabral.037@ufrn.edu.br, monica.pereira@ufrn.br

Abstract. This article presents the SAVE HER System, a project that aims to assist in the safety of women through the combination of machine learning techniques, the development of an electronic device and an application aimed at detecting risk situations and triggering a distress message. The device has different sensors whose data will be analyzed by a neural network capable of recognizing situations in which the woman is in danger and triggering the SOS message automatically. The distress message can also be sent manually via a button to be pressed by the user. When the danger is identified, the application signals the distress call and shares the location of the woman to be rescued with her safety contacts.

Resumo. O artigo apresenta o Sistema SALVE TODAS, cujo objetivo é auxiliar na segurança de mulheres através da implementação de técnicas de aprendizado de máquina em conjunto com a construção de um dispositivo eletrônico e de um aplicativo voltados para a detecção de situações de risco e para o disparo de uma mensagem de pedido de socorro. O dispositivo conta com diferentes sensores cujos dados serão analisados por uma rede neural capaz de reconhecer situações em que a mulher se encontra em perigo e disparar a mensagem de SOS automaticamente. A mensagem também pode ser enviada manualmente por meio de um botão. Ao ser identificado o perigo, o aplicativo envia o SOS e compartilha a localização da mulher com seus contatos de segurança.

## 1. Introdução

A discussão acerca da violência contra a mulher tem ganhado maior destaque no Brasil desde a vigência da Lei Maria da Penha em Setembro de 2006 [Lei no 11.340, 2006] e, posteriormente, com a previsão do feminicídio como circunstância qualificadora do crime de homicídio na Lei no 13.104 de Março de 2015 [Lei no 13.104, 2015]. Tratar deste tema se mostra mais relevante que nunca, em especial com o aumento dos casos de feminicídio desde o início do período de isolamento social imposto pela pandemia do Covid-19, no começo de 2020 [Fórum Brasileiro de Segurança Pública (FBSP), 2020]. Estes dados mais recentes evidenciam uma necessidade antiga e ainda não superada de se pensar no desenvolvimento de mecanismos e soluções voltados para o enfrentamento à violência de gênero não somente nas esferas legislativa e social, mas também na área das tecnologias da informação, como é o proposto neste projeto.

Todos os anos diversos órgãos e observatórios publicam estudos sobre os índices de violência contra a mulher. Os dados que já eram alarmantes nos anos anteriores à pandemia, como as taxas de um caso de estupro a cada 8 minutos e um caso de

violência doméstica a cada 2 minutos [FBSP, 2019], se agravaram com as medidas de distanciamento social e maior permanência em casa [FBSP, 2020]. O Brasil, no ano de 2020 quando comparado ao ano de 2019, apresentou um aumento de 1,5% e 1,9%, respectivamente, nos casos de homicídio doloso com vítimas do sexo feminino e de feminicídio. Em contrapartida, os registros oficiais de queixa quanto à lesão corporal dolosa, ameaças e estupro diminuíram consideravelmente - 9,9%, 15,8% e 22,2%, respectivamente. Uma análise mais profunda a respeito destes dados não aponta necessariamente para a diminuição absoluta dos casos de violência contra a mulher, mas sim para os obstáculos que as mulheres precisam enfrentar para efetuar a denúncia, uma vez que, como bem explica o Anuário Brasileiro de Segurança Pública [FBSP, 2020, p.39], “as dificuldades enfrentadas pelas mulheres para realizar a denúncia não foi fruto apenas de medos e receios pessoais, mas principalmente da ausência de medidas de enfrentamento adotadas pelo governo para auxiliá-las”. Além disso, o Anuário destaca a necessidade de investimentos em serviços online de atendimento às mulheres em situação de risco como uma das principais recomendações da Organização das Nações Unidas (ONU) Mulheres no enfrentamento à violência de gênero [FBSP, 2020].

Assim sendo, o Sistema SALVE TODAS tem como objetivo auxiliar na segurança das mulheres por meio de um sistema inteligente composto por hardware e software. O SALVE TODAS deve atuar como uma ferramenta capaz de identificar quando a usuária se encontra em uma situação de risco e também de emitir um pedido de socorro contendo a geolocalização da mulher em perigo para uma lista de contatos cadastrados e/ou para a polícia, além de apresentar informações oficiais sobre como identificar a violência contra a mulher e a quais instâncias locais recorrer caso necessário. Para identificar as situações de risco, o sistema conta com três elementos: um dispositivo eletrônico com sensores que captam informações de movimentos corporais, sinais vitais e geolocalização da usuária; um mecanismo de detecção que utiliza uma rede neural artificial para analisar as informações captadas e identificar a situação; e um aplicativo de smartphone para acesso da usuária que poderá obter as informações básicas sobre violência contra a mulher e acionar manualmente um botão de SOS, além de ser o responsável pelo envio da mensagem de socorro com a sua geolocalização para a lista de contatos salvos. Finalmente, este artigo descreve o Sistema e apresenta seu estado atual que consiste em um protótipo de mesa e um aplicativo para dispositivo móvel.

## 2. Conceitos Relacionados

O presente trabalho abrange três tópicos de investigação principais, são eles: a violência contra mulher, que motivou o desenvolvimento deste projeto; os sistemas embarcados, que compõem o dispositivo eletrônico; e o aprendizado de máquina, responsável pela análise dos dados dos sensores do dispositivo e capaz de classificar quando a usuária se encontra numa possível situação de risco. Esta seção irá apresentar alguns conceitos fundamentais relacionados aos tópicos de investigação deste trabalho.

### 2.1. Violência Contra a Mulher

A violência contra mulher pode ser entendida como qualquer ato, seja na esfera pública ou na privada, que resulte em sofrimento ou dano moral, patrimonial, físico, sexual ou psicológico e até mesmo na morte de mulheres. Além disso, este tipo de violência é voltado para um grupo específico, no qual o gênero da vítima é o principal fator motivador do crime, ou seja, os atos de violência são cometidos contra mulheres,

expressamente por serem mulheres.

Não se pode falar de violência contra mulher sem abordar a violência doméstica, as duas estão intrinsecamente relacionadas uma vez que em 89,9% dos casos de feminicídio no Brasil o crime foi cometido pelo companheiro ou ex-companheiro da vítima [FBSP, 2020].

A violência doméstica apresenta diversas facetas, porém nota-se a recorrência de ciclos onde a gravidade das agressões vai aumentando gradativamente, podendo culminar no feminicídio. O termo 'Ciclo da Violência' foi usado pela primeira vez pela psicóloga estadunidense Leonore Walker em 1979 e apresenta três fases bem definidas: aumento da tensão, ataque violento e calmaria [Walker, 2009]. Ao longo do ciclo a mulher vê a agressividade do parceiro aumentar, até culminar na agressão física de fato, que é então seguida por uma fase de calmaria onde o parceiro (e agressor) pede desculpas e faz promessas de não repetir tais atos [Walker, 2009].

No que diz respeito a medidas legais de coibição da violência contra mulher, o Brasil apresenta a Lei Maria da Penha e a chamada Lei do Feminicídio. A Lei Maria da Penha visa a criação de “mecanismos para coibir a violência doméstica e familiar contra a mulher” [Lei no 11.340, “Capítulo I - Disposições Gerais”, 2006]. Já a Lei do Feminicídio descreve o crime como o homicídio “contra a mulher por razões da condição do sexo feminino […] quando o crime envolve: I - violência doméstica e familiar; II - menosprezo ou discriminação à condição de mulher” [Lei no 13.104, 2015], além de “prever o feminicídio como circunstância qualificadora do crime de homicídio, e […] incluir o feminicídio no rol dos crimes hediondos” [Lei no 13.104, 2015].

### 2.2. Sistemas Embarcados

Um Sistema Embarcado (SE) pode ser entendido de maneira simplificada como “um sistema computacional que faz parte de um sistema maior e implementa alguns dos requerimentos deste sistema” [IEEE..., 1990, p. 30]. Um ponto chave na sua definição é o fato de que os SEs não são programados pelo usuário final, mas sim projetados para controlar uma ou algumas funções específicas [Steve, 2003]. Além disso, os Sistemas Embarcados são caracterizados por apresentarem restrições de recursos e precisarem, em muitas das vezes, atender a requisitos específicos, como por exemplo exigências de resposta em tempo real e/ou limitações de tamanho, preço, etc. [Berger, 2002].

Um dos principais pontos envolvidos no desenvolvimento de um projeto de Sistemas Embarcados é a escolha de uma metodologia adequada, conforme ressaltado por Marilyn Wolf (2008). No projeto do Sistema SALVE TODAS foi adotada uma combinação de duas metodologias: a Metodologia Baseada em Níveis de Abstração Top-down, na qual o projeto se inicia com uma ideia geral das características almejadas para o sistema (um alto nível de abstração) e vai sendo refinada sucessivamente até atingir um nível intermediário de abstração onde foi então aplicada a Metodologia de Projeto Baseada em Plataforma, na qual é definido o fluxo de desenvolvimento do sistema sobre uma plataforma base.

Para o projeto do SALVE TODAS as principais características visam atender a restrições de tamanho, peso, preço e bateria. Mesmo o SALVE TODAS sendo um protótipo de bancada, o seu projeto foi pensado de modo a buscar componentes de tamanho e peso reduzidos, de baixo custo e de baixo consumo de energia. Além disso, o projeto prevê uma série de requisitos funcionais listados na Seção 4.

### 2.3. Aprendizado de Máquina

De acordo com as autoras e os autores Faceli, Lorena, Gama e de Carvalho (2011), o Aprendizado de Máquina (AM) pode ser compreendido como a capacidade de melhorar o desempenho na execução de alguma atividade a partir de análise de experiências anteriores e bem sucedidas de resolução de problemas. Essas experiências anteriores podem ser entendidas como dados de entrada e saída que, uma vez em quantidade suficiente e abrangendo o escopo do objeto de estudo, permite que o algoritmo crie autonomamente predições sobre a temática em questão [Faceli et al. 2011].

Existem diversos paradigmas de aprendizado nos quais os modelos de AM podem se basear, sendo a sua escolha ditada pelas exigências do projeto em questão. O adotado neste projeto é um sistema de Aprendizado Supervisionado de classificação através da técnica de Redes Neurais Artificiais. O termo ‘supervisionado’ indica que cada objeto do conjunto de treinamento possui valores conhecidos de entrada e de saída [Faceli et al., 2011]. Redes Neurais Artificiais (RNA) são um paradigma de AM inspirado no sistema nervoso central de animais, onde os nós, de maneira análoga aos neurônios, se interconectam em camadas e são capazes de computar valores de entrada e retornar valores de saída [Faceli et al., 2011].

Para o Sistema SALVE TODAS foi desenvolvido um modelo de RNA com o objetivo de analisar os dados dos sensores do dispositivo eletrônico a fim de reconhecer padrões da rotina da usuária e poder identificar situações que poderiam representar perigo para ela. A ferramenta utilizada na análise dos dados foi o Waikato Environment for Knowledge Analysis (WEKA) [WEKA,1993].

O software WEKA é alimentado com uma base de treinamento contendo um número suficientemente grande de amostras, as chamadas ‘instâncias’, de valores predefinidos de entrada e saída esperados para a situação problema. As entradas, conhecidas como ‘atributos’, são os critérios a serem analisados. As saídas, ditas ‘classes’, são obtidas após a análise do algoritmo selecionado (RNA, neste trabalho).

## 3. Trabalhos Relacionados

Em se tratando de iniciativas e produtos voltados para a segurança pessoal, existem dispositivos com propostas similares já disponíveis no mercado internacional. Alguns exemplos são o Nimb Ring e o WearSafe.

O Nimb Ring é um anel com um botão que ao ser pressionado envia um pedido de socorro com a localização da usuária para uma lista de contatos cadastrados ou diretamente para a polícia via aplicativo de smartphone [Nimb, 2019].

O WearSafe tem o formato de um broche, que pode ser fixado e escondido entre as vestimentas, e também possui um botão. Quando acionado, ele envia a localização e o pedido de socorro e, além disso, ainda apresenta a opção de gravação de voz, criação de um grupo de bate-papo com os contatos de emergência cadastrados para coordenar a ajuda e um serviço de monitoramento privado terceirizado [Wearsafe, 2021].

Os dispositivos citados acima ainda não estão disponíveis no Brasil e não disponibilizam informações oficiais sobre violência contra a mulher e onde procurar ajuda, além de apresentarem limitações com relação ao aprendizado da rotina da usuária.

No Brasil existem diversos aplicativos para a divulgação de informações oficiais sobre a violência contra a mulher e quais instâncias recorrer no caso de violência, além

de atuar como um canal de denúncia e de pedido de socorro. Alguns exemplos são os aplicativos SOS Mulher dos estados de São Paulo e Amapá e os aplicativos SOS El@s e Nossa Voz, publicados nos últimos dois anos nos Anais do Women in Information Technology.

Os aplicativos SOS Mulher/SP e SOS Mulher/AP foram desenvolvidos, respectivamente, pelo governo do estado de São Paulo e pelo Ministério Público do Estado do Amapá em parceria com a Prefeitura Municipal de Macapá. Ambos são voltados exclusivamente para mulheres que tenha uma medida protetiva concedida pela Justiça. Suas plataformas tem funcionalidades similares: contam com um botão que emite um pedido de ajuda imediato à polícia e/ou contatos de emergência cadastrados e com conteúdos informativos sobre a violência doméstica.

O aplicativo SOS El@s [de Freitas at. al., 2020] é uma iniciativa do projeto Chunhatã Digital da UFMA juntamente com a OAB-AM que tem como objetivo facilitar e democratizar o pedido de socorro de mulheres em situação de violência. O aplicativo permite que a usuária cadastre uma lista de contatos de segurança e envia um SMS com a geolocalização da mulher e foto do momento do acionamento além de ligar automaticamente para a polícia. Já o aplicativo Nossa Voz [Silva et. al., 2021], desenvolvido por estudantes do IFPB e UNIESP/Paraíba, tem como objetivo apresentar os dados atuais de violência doméstica no Brasil de maneira clara e compreensível.

As iniciativas nacionais citadas são limitadas a aplicações para smartphone, de circulação local/estadual e além de nem todos os estados possuírem aplicativos oficiais, alguns ainda são voltados apenas para as mulheres que possuam medidas protetivas em vigor.

Tabela 1. Resumo e Comparação entre os Sistemas

|Funcionalidades|Estr |angeiros|Sistema |s Nacion |ais ||
|---|---|---|---|---|---|---|
||Nimb Ring|WearSafe|SOS Mulher (SP e AP)|SOS El@s|Nossa Voz|SALVE TODAS|
|Botão de Socorro|X|X|X|X|-|X|
|Sensores de Sinais Vitais|X|X|-|-|-|X|
|Geolocalizador|X|X|X|X|-|X|
|Aprendizado de Máquina|-|-|-|-|-|X|
|Aplicativo de_Smartphone_|X|X|X|X|X|X|
|Informações Oficiais|-|-|X|X|X|X|
|Usuárias sem medidas protetivas|X|X|-|X|X|X|
|Disponível no Brasil|-|-|X|X|X|X|

A Tabela 1 mostra de maneira mais explícita as características de cada um dos sistemas citados e compara com as funcionalidades oferecidas pelo SALVE TODAS.

Como pode ser observado, a maioria dos sistemas citados não apresenta sensores de sinais vitais e alarme sonoro, ambos presentes no sistema proposto neste artigo. O maior diferencial do SALVE TODAS está no Aprendizado de Máquina, isto é, o SALVE TODAS é o único dos sistemas listados que se propõe a aplicar técnicas de AM voltadas para o aprendizado da rotina da usuária. Tal funcionalidade é uma vantagem pois permite que o pedido de socorro seja efetuado automaticamente, sem que a usuária precise acionar manualmente o botão de socorro, o que em algumas situações de violência pode se tornar uma tarefa difícil e até mesmo impossível.

> 1 https://www.sosmulher.sp.gov.br/, recuperado em 21 de janeiro, 2021

> 2 https://apps.mpap.mp.br/sosmulher, recuperado em 21 de janeiro, 2021

## 4. Requisitos do Sistema

O SALVE TODAS consiste no protótipo de um sistema de hardware e software voltado para auxiliar na segurança de mulheres. O Sistema foi idealizado para identificar, por meio de Aprendizado de Máquina, situações de risco para a usuária, e então enviar uma mensagem de pedido de socorro para uma lista de contatos de segurança cadastrados. O SALVE TODAS também visa disponibilizar informações oficiais sobre a Lei Maria da Penha e sobre como reconhecer e proceder em casos de violência contra a mulher.

Muito foi pensado, estudado e pesquisado sobre quais elementos deveriam constar no projeto do sistema. Um ponto fundamental da etapa de planejamento foi a troca de experiências e coleta de informações com as pessoas e/ou órgãos e instâncias responsáveis pelos cuidados às mulheres envolvidas na problemática tratada. Assim, a Secretaria Municipal de Políticas Públicas para as Mulheres (SEMUL) foi contatada e, posteriormente, duas reuniões foram realizadas. Os principais objetivos das reuniões eram: buscar mais informações sobre as políticas locais; estabelecer proximidade com os órgãos estatais voltados para o combate à violência contra a mulher; e entender as necessidades que um dispositivo voltado para o enfrentamento a essa violência têm para que o Sistema SALVE TODAS pudesse atuar da melhor forma possível.

A troca de experiências com as representantes da SEMUL foi fundamental e permitiu que os requisitos do Sistema fossem estabelecidos com consistência e de acordo com as necessidades específicas das mulheres.

A seguir estão listados os requisitos de hardware Sistema SALVE TODAS:

- Conter um botão que dispare o pedido de ajuda manualmente;

- Identificar quedas e movimentos bruscos da usuária;

- Monitorar os batimentos cardíacos da usuária;

- Comunicar-se com o aplicativo de smartphone.

Segue abaixo os requisitos do software do Sistema:

- Comunicar-se com o dispositivo eletrônico;

- Ter uma tela de cadastro e login da usuária;

- Possuir um botão para o disparo manual do pedido de ajuda;

- Conter informações oficiais sobre a Lei Maria da Penha, como identificar a violência contra a mulher, a quais instâncias recorrer e onde procurar ajuda;

- Obter a geolocalização da usuária;

- Armazenar cinco contatos de emergência da usuária;

- Enviar uma mensagem de pedido de socorro com a geolocalização da usuária para os contatos de emergência.

Finalmente, os requisitos da Rede Neural Artificial seguem abaixo:

- Analisar os dados de quedas, batimentos cardíacos e geolocalização da usuária;

- Classificar as situações como perigosa para a usuária ou não;

### 4.1. Visão Geral do Sistema SALVE TODAS

Uma vez estabelecidos os requisitos do SALVE TODAS, segue abaixo, na Figura 1, um diagrama de blocos que mostra uma visão geral dos componentes

integrantes do sistema e como eles interagem entre si:

Figura 1. Diagrama de Blocos do Sistema SALVE TODAS

Como pode ser observado, o Sistema SALVE TODAS é composto por três partes: Rede Neural Artificial, Aplicativo e Dispositivo Eletrônico que se comunicam entre si. O Dispositivo Eletrônico apresenta Sensores de Quedas e de Batimentos Cardíacos, Módulo Bluetooth e o Botão de Socorro conectados ao Microcontrolador que, além de controlar os componentes citados, também se conecta à RNA e ao Aplicativo. E, uma vez que a RNA está em fase de modelagem e validação do modelo desenvolvido, a mesma ainda não foi implementada ao sistema, tendo o seu processamento realizado separadamente, o que é indicado no diagrama pelas setas hachuradas.

## 5. O Sistema SALVE TODAS

Esta seção visa apresentar os protótipos de hardware e software desenvolvidos para o Sistema SALVE TODAS, bem como os resultados obtidos a partir do modelo de Rede Neural Artificial construído. A seção é dividida em subseções que abordam individualmente cada um dos tópicos citados.

### 5.1. Protótipo do Hardware

Para a primeira versão do Sistema SALVE TODAS, foi desenvolvido um protótipo de mesa com sistemas embarcados e componentes eletrônicos de acordo com os requisitos citados na Seção 4. O formato de mesa foi escolhido para a primeira versão a fim de observar a funcionalidade dos sistemas e como eles interagem entre si.

No protótipo, mostrado na Figura 2, foram utilizados os seguintes dispositivos:

- Arduino NANO (2021);

- Chave Táctil;

- Módulo acelerômetro e giroscópio MPU6050 [InvenSense, 2012];

- Sensor de batimentos cardíacos PulseSensor 9 [Murphy & Gitman, 2018];

- Módulo bluetooth RS232 HC-05 [ITead Studio, 2010].

O Sistema é baseado no microcontrolador ATmega328 na plataforma de prototipação do Arduino NANO que possui um tamanho reduzido, baixo custo e baixo consumo de energia. O Arduino NANO controla os demais componentes do protótipo. A chave táctil é o botão responsável pelo pedido de socorro manual. Uma vez pressionada, é emitido um sinal para o aplicativo do SALVE TODAS que

imediatamente envia uma mensagem contendo a localização da usuária para uma lista com seus contatos de segurança cadastrados.

Figura 2. Hardware do Sistema SALVE TODAS

O módulo acelerômetro e giroscópio são responsáveis por detectar quedas e movimentos bruscos sofridos pela usuária a partir dos dados de aceleração e velocidade obtidos pelo sensor. Tais dados são empregados na detecção de situações de violência física sofrida pela mulher.

O sensor de batimentos cardíacos obtém a frequência cardíaca da usuária através de um sensor ótico. Este dado contribui para a identificação do perigo para a mulher, uma vez que o perigo se relaciona ao sentimento de medo que, por sua vez, desencadeia elevações na frequência cardíaca [Freitas-Magalhães; Reis et. al., 2013].

Finalmente, o módulo bluetooth é responsável pela comunicação sem fio entre o hardware e o aparelho de smartphone contendo o aplicativo.

### 5.2. Protótipo do Software

O protótipo do aplicativo SALVE TODAS também foi desenvolvido a partir dos requisitos listados na Seção 4. Para tanto foi utilizada a plataforma MIT App Inventor. O MIT App Inventor é um software web de código aberto que permite o desenvolvimento de aplicativos de software para o sistema operacional Android através de um navegador web e um smartphone ou emulador conectados [MIT, 2021].

O software foi desenvolvido a partir da ideia de diferentes telas, onde, de modo geral, cada uma delas focava em um dos requisitos do projeto. Assim que o aplicativo é inicializado, a usuária é encaminhada para a Tela de Login (Figura 3-a), que requer o nome de usuária e a senha para liberar o acesso ao aplicativo. Uma vez logada, a usuária é solicitada a conectar o bluetooth de comunicação com o hardware. Finalmente, a usuária é encaminhada para a Tela Inicial (Figura 3-b) que lhe dá as boasvindas e apresenta o aplicativo de modo sucinto. Essa tela tela também conta com um botão para o pedido de socorro manual, a redundância do botão no hardware e no software é melhor que a ausência de um dos mecanismos em um momento de perigo para a mulher.

O aplicativo também é capaz de captar a geolocalização da usuária. Para a modelagem da Rede Neural Artificial, foi adotado um ponto de referência arbitrário e um raio de cinco quilômetros deste ponto como a região de segurança. Coordenadas geográficas fora desta área eram interpretadas pelo modelo de RNA como regiões que poderiam representar perigo.

As demais telas do app podem ser acessadas através do menu e são as seguintes:

- Reconhecendo a Violência, que mostra como identificar o Ciclo da Violência;

- Tipos de Violência, que descreve os cinco tipos de acordo com a Lei Maria da Penha: física, moral, sexual, psicológica e patrimonial;

- Onde Procurar Ajuda, que lista os endereços e telefones dos principais órgãos e centros de apoio que uma mulher vítima de violência de gênero deve procurar; e

- • Cadastro de Contatos (Figura 3-c), onde a usuária pode cadastrar até cinco pessoas que serão contatadas em caso de disparo do pedido de socorro.

Figura 3. a) Tela de Login b) Tela Inicial c) Cadastro de Contatos

### 5.3. Modelo da Rede Neural Artificial

Para a construção de um modelo de Rede Neural Artificial para o Sistema SALVE TODAS foi desenvolvida uma base de dados artificiais. Uma vez que a Rede Neural está em fase de modelagem e seu processamento é feito separadamente, os dados foram gerados aleatoriamente, respeitando o formato dos dados fornecidos pelos sensores. Esta base foi utilizada no treinamento e testes do modelo de RNA que foi construído a partir do algoritmo MultiLayer Perceptron do software WEKA.

A base de dados desenvolvida conta com 5000 instâncias. Cada instância apresenta seis atributos a serem analisados: os dados do acelerômetro e giroscópio referentes ao eixo Z; os dados referentes ao eixo X; e os dados do eixo Y; a frequência cardíaca em batimentos por minuto; a latitude; e a longitude da geolocalização da usuária. Finalmente, o algoritmo retorna a classe, isto é, o resultado que indica se a usuária se encontra em uma situação de perigo ou não.

A base foi analisada através do método de validação cruzada utilizando 10 subgrupos. Nesta última avaliação, o modelo de RNA desenvolvido apresentou uma taxa de acertos de 90,68%. As taxas obtidas foram relativamente boas e promissoras para os primeiros testes do protótipo do Sistema. Além da taxa de acertos, é importante observar a presença de falsos-negativos. A Figura 4 abaixo mostra a matriz de confusão do teste. Nela, os falsos-negativos são representados pelas predições ‘0’ (situação rotineira), quando a saída deveria ter sido ‘1’ (situação de risco). Nota-se a ocorrência de 253 falsos-negativos, o que equivale a 5,06%, que, apesar de parecer um valor proporcionalmente baixo, dada a criticidade da problemática tratada neste projeto, ele deve ser investigado mais a fundo a fim de ser reduzido em trabalhos futuros.

Figura 4 – Matriz de Confusão.

## 6. Considerações Finais

O presente artigo descreveu o protótipo do SALVE TODAS, um sistema para a segurança de mulheres. O protótipo é composto por um hardware contendo um botão de socorro e sensores capazes de recolher dados de movimentação e sinais vitais da usuária; um modelo de Rede Neural Artificial, responsável pela análise desses dados e a identificação de possíveis situações de risco para a mulher; e, finalmente, um software capaz de disparar uma mensagem de pedido de socorro contendo a geolocalização da usuária em perigo para uma lista de contatos cadastrados e/ou a polícia.

O protótipo do Sistema SALVE TODAS se mostrou viável e capaz de cumprir com todos os requisitos funcionais exigidos do projeto. O hardware é capaz de coletar os dados dos sensores de forma a reconhecer o perigo de maneira fidedigna e o botão de socorro apresenta resposta instantânea. A comunicação sem fio com o software foi estabelecida de maneira eficiente via bluetooth. O software desenvolvido apresenta layout delicado e suas funcionalidades são disponibilizadas de maneira intuitiva e de fácil acesso para a usuária. Por fim, a investigação sobre a aplicação de uma Rede Neural Artificial na detecção de perigo foi capaz de gerar um modelo de aprendizado com uma taxa de acerto de 91,54% dos casos testados.

Quanto aos trabalhos futuros para o projeto, estão incluídos: um estudo mais aprofundado da técnica de Redes Neurais Artificiais; a melhoria do protótipo para uma versão de Produto Viável Mínimo (MVP, de Minimum Viable Product ); e novos contatos com a Secretaria Municipal de Políticas para Mulheres a fim de discutir a aplicabilidade do Sistema como política pública local.

Finalmente, cabe ressaltar a importância de projetos como o Sistema SALVE TODAS, não apenas nas atuais circunstâncias de aumento nos casos de feminicídio e de homicídios dolosos contra mulheres devido à pandemia do Covid-19 (FBSP, 2020), como também ao se considerar o alarmante histórico brasileiro de elevadas taxas de violência de gênero. Ademais, é válido destacar a necessidade de investimento em políticas públicas de conscientização e combate ao machismo, misoginia e violência contra a mulher conforme ressaltam diversos observatórios e órgãos especializados no enfrentamento à violência contra a mulher, como o Observatório da Mulher Contra a Violência do Senado Federal [Agência Senado, 2019] e a ONU Mulheres [ONU Mulheres Brasil, 2017]. Desta maneira, o Sistema SALVE TODAS se apresenta como uma ferramenta possível de identificação, denúncia e conscientização sobre a violência contra a mulher.
