# Fortalecendo a confiança das mulheres para atuar na área de computação

Ana Lúcia de Moura, Jessica Ribas, Maria Julia de Lima, Noemi Rodriguez

1Instituto Tecgraf, PUC-Rio

Rio de Janeiro – RJ – Brasil

2Departamento Informática, PUC-Rio Rio de Janeiro – RJ – Brasil

noemi@inf.puc-rio.br, mjulia@tecgraf.puc-rio.br

analuciadm@tecgraf.puc-rio.br, jessicabarbarasr@tecgraf.puc-rio.br

Abstract. In this paper, we report our experience with teaching soft skills in the context of TWIST, a training program that prepares university students, both technically and emotionally, for a confident and comfortable entry in the software development market. We discuss how we approached the development of teamwork skills and how we mapped several other fundamental socioemotional skils to group dynamics and interactive presentations led by experts from diverse areas of knowledge.

Resumo. Nesse artigo, relatamos nossas experiências e aprendizado com o ensino de soft skills no TWIST, um programa para estudantes universitárias que tem o objetivo de capacitá-las tecnica e emocionalmente para um ingresso confiante e confortável no mercado de desenvolvimento de software. Discutimos como abordamos o aprendizado do trabalho em equipe e como trabalhamos várias questões socioemocionais que identificamos como importantes para a formação das participantes em dinâmicas e rodas de conversa envolvendo convidadas e colaboradoras de áreas de atuação diversas.

## 1. Introdução

Com a proposta de atrair e dar suporte à permanência de mais mulheres na área de computação, lançamos em 2023 um programa de capacitação para desenvolvedoras de software, o TWIST. Em um mercado onde a presença feminina ainda é reduzida, especialmente na área de desenvolvimento, o objetivo do programa é funcionar como uma cápsula de fortalecimento para as participantes, fornecendo recursos e competências necessários para que se sintam seguras e preparadas para enfrentar os desafios do ambiente de trabalho. Além de oferecer uma formação técnica básica para que se familiarizem com atividades de desenvolvimento de software, o TWIST também enfatiza, especialmente, o ensino de soft skills, buscando equipar as participantes com conhecimento sobre atitudes e comportamentos comuns na área, assim como sobre boas práticas para enfrentar algumas situações adversas. O programa também pretende que as participantes criem uma primeira rede de apoio, estabelecendo contatos das novas desenvolvedoras com mulheres em diferentes pontos de suas carreiras, que podem contribuir não apenas durante o programa mas também ao longo das trajetórias futuras das participantes.

O TWIST é uma iniciativa do Instituto Tecgraf da PUC-Rio. O Tecgraf desenvolve software científico para problemas desafiadores da indústria, integrando conhecimentos e pesquisas realizadas na universidade. Além de profissionais do próprio instituto, o TWIST também conta com a colaboração de professores e pesquisadores de diferentes áreas de conhecimento da universidade. Desde seu início, o programa está inscrito como projeto parceiro do Programa Meninas Digitais da Sociedade Brasileira de Computação.

Ao planejar o programa, até por nossa experiência como professoras, achamos relativamente fácil desenhar a parte técnica de nossa capacitação, baseada no desenvolvimento de uma sequência de projetos com nível crescente de complexidade. O que acabou demandando bastante discussão e reflexão foi a forma como introduziríamos o ensino de soft skills, permitindo o desenvolvimento de competências socioemocionais necessárias para garantir que as participantes egressas do programa se sintam confortáveis e seguras em seus futuros ambientes de trabalho.

Podemos dividir nosso apoio ao desenvolvimento de soft skills em duas grandes frentes. Na primeira está o desenvolvimento de competências para trabalho em equipe, fundamentais para o desenvolvimento de software. A segunda frente trata de tornar as participantes mais confiantes em sua escolha de profissão e de fornecer a elas recursos para uma interação mais segura e confortável com os ambientes profissionais que encontrarão.

Em artigo anterior[Rodriguez et al. 2024] descrevemos a estrutura do TWIST e relatamos observações iniciais sobre seu funcionamento. Neste trabalho relatamos nossa experiência de dois anos com o programa, com atenção especial ao fortalecimento da confiança das participantes para atuar na área de computação, através do desenvolvimento de soft skills. Na Seção 2 fazemos uma apresentação sucinta do programa. Em seguida, na Seção 3, apresentamos nossa abordagem para a prática de trabalho em equipe. Na Seção 4 discutimos as dinâmicas que organizamos com objetivo de fornecer às participantes outros recursos relacionados ao desenvolvimento de competências socioemocionais. Finalmente, encerramos o artigo com algumas conclusões na Seção 5.

## 2. O Programa

As turmas do TWIST são compostas por alunas dos períodos iniciais dos cursos do centro técnico que já tenham cursado ao menos uma disciplina de programação, mas que, preferencialmente, ainda não tenham tido uma experiência de estágio ou trabalho na área. Realizamos a seleção de participantes no primeiro semestre do ano, entre maio e junho, sempre buscando formar grupos com algum grau de diversidade, como por exemplo, a situação socio-economica familiar. Para essa seleção, pedimos que as candidatas enviem pequenos vídeos respondendo algumas perguntas e realizamos também entrevistas. As atividades do programa propriamente ditas ocorrem no segundo semestre do ano, entre julho e dezembro.

Em 2023 tivemos 14 participantes e em 2024, 11. A maioria das alunas selecionadas cursam Ciência da Computação ou Engenharia de Computação. Selecionamos também algumas alunas de outros cursos (como Engenharia de Produção e Engenharia de Controle e Automação), que durante a entrevista demonstraram interesse em atuar de alguma forma na área de computação.

A tabela 1 contém um resumo de nosso cronograma de funcionamento. O programa conta com uma equipe dedicada composta da seguinte forma: três coordenadoras,

|período|atividade|equipe envolvida|
|---|---|---|
|janeiro a abril|planejamento de atividades epreparação do material didático|equipe dedicada|
|maio ajunho|inscrições e seleção|equipe dedicada|
|julho|curso HTML, CSS e Javascript dinâmicas iniciais workshopSCRUM|equipe dedicada e estendida|
|agosto a dezembro|desenvolvimento de projetos workshops e palestras dinâmicas e rodas de conversa|equipe dedicada e estendida|

Tabela 1. TWIST: Cronograma anual e equipe envolvida.

da área de computação, a quem cabem as decisões estratégicas e estruturação das atividades; duas tutoras, estudantes de graduação ou pós-graduação que acompanham as atividades do dia-a-dia das participantes e desenvolvem materiais de apoio, e uma designer, responsável pela programação visual, divulgação nas redes sociais e mentoria na definição das interfaces das aplicações a serem desenvolvidas nos projetos. Como equipe estendida, contamos com o apoio voluntário de mentores, membros das equipes de desenvolvimento de software no Instituto Tecgraf, que acompanham e orientam o trabalho das participantes em reuniões semanais; e convidados externos, profissionais do mercado e da academia, de diferentes áreas, que colaboram com atividades de desenvolvimento técnico e de soft skills previamente planejadas

As atividades do programa propriamente dito têm início nas férias acadêmicas, em julho, quando utilizamos um horário mais intenso durante três semanas para apresentar as tecnologias básicas empregadas nos projetos a serem desenvolvidos posteriormente – HTML, CSS, Javascript e GitHub – e realizar algumas primeiras dinâmicas. Optamos, nas duas edições, pelo trabalho com desenvolvimento front-end por permitir que as participantes visualizem, rapidamente, o resultado de seus esforços de codificação.

A partir de agosto, passamos a trabalhar com aprendizado baseado em projetos [Khabbali et al. 2023], com carga horária de 15 horas semanais. Em 2023 deixamos 6 dessas horas em formato remoto, mas em 2024 passamos ao formato de 3 horas presenciais diárias, de 15 às 18h, sempre buscando interferir o mínimo possível no horário de disciplinas das participantes.

Além do desenvolvimento de projetos em equipes, a capacitação técnica das participantes contempla também diversas apresentações técnicas e workshops, que introduzem conceitos de diferentes áreas, como interação humano-computador (IHC), segurança da informação, inteligência artificial, acessibilidade em interfaces web, entre outras.

As sextas-feiras do programa são normalmente dedicadas a dinâmicas – rodas de conversa, apresentações e interações guiadas – que, juntamente com a prática do trabalho em equipe, têm como objetivo complementar a capacitação técnica das participantes com o desenvolvimento de soft skills.

As estudantes participantes recebem, de julho a dezembro, um valor compatível com o de uma bolsa de iniciação científica. Ao final do programa, recebem um certificado que muitas delas utilizam para solicitar horas em atividades complementares.

## 3. Trabalho em equipe

O desenvolvimento de software é uma atividade essencialmente colaborativa, exigindo que profissionais trabalhem em equipe para entregar soluções eficazes. No entanto, trabalhar bem em equipe exige um conjunto de soft skills fundamentais, como comunicação, resolução de problemas e liderança. O relatório da National Association of Colleges and Employers [NACE 2024] destaca que a capacidade de trabalhar em equipe está entre as habilidades mais valorizadas pelos empregadores, reforçando a necessidade de que programas educacionais priorizem experiências colaborativas.

Ainda que muitos trabalhos acadêmicos em cursos de graduação em computação sejam realizados em grupo, ainda é pouco comum que se reflita sobre como os estudantes podem organizar esse trabalho de forma eficaz e aprender a lidar com as dificuldades que surgem, incluindo os conflitos naturais do trabalho colaborativo. Pesquisas indicam que apesar do aumento da demanda por habilidades técnicas avançadas, habilidades interpessoais como comunicação e trabalho em equipe ainda são sub-representadas nos currículos acadêmicos, criando uma lacuna entre a formação e as exigências do mercado [Börner et al. 2018, Mohammed and Ozdamli 2024, Seagull and Souza 2023].

Para enfrentar esse desafio, em nosso programa adotamos a Aprendizagem Baseada em Projetos (PBL) integrada a métodos ágeis, que incentivam a interação contínua, a adaptação a mudanças e a tomada de decisões coletivas. O objetivo é criar um ambiente estruturado que permita às participantes desenvolverem tanto habilidades técnicas quanto interpessoais, preparando-as para os desafios reais do ambiente profissional. Nesta seção, apresentamos como essas duas abordagens estão sendo aplicadas no TWIST.

### Aprendizagem Baseada em Projetos

A Aprendizagem Baseada em Projetos (PBL) é uma abordagem conhecida por proporcionar aos alunos uma experiência mais imersiva e prática, aproximando-os do que vivenciam num ambiente de trabalho real. Um dos principais benefícios da PBL é a oportunidade de aplicar, na prática, os conceitos ensinados, permitindo que os alunos percebam a relevância do que estão aprendendo. Além de ajudar na assimilação dos conhecimentos técnicos, o PBL favorece o desenvolvimento de habilidades como autonomia, pensamento crítico e comunicação – competências essenciais para o trabalho colaborativo na indústria de software [Cintra and Bittencourt 2023, Garcés and Oliveira 2024].

No TWIST, usamos o PBL durante todo o programa, organizando os projetos em níveis crescentes de dificuldade conforme novos conteúdos são apresentados. Reforçamos assim a importância da aprendizagem contínua, com novos desafios em cada projeto.

O projeto final é o momento de consolidação das habilidades adquiridas e, portanto, em ambas as edições do TWIST, um tempo maior é dedicado a ele. Em 2023, por ter sido a primeira edição do programa, optamos por um tema já previamente definido pela coordenação. Essa opção nos permitiu ter mais controle sobre o tempo e o esforço no desenvolvimento do projeto e o conteúdo necessário a ser ensinado. O tema escolhido foi baseado em livro que traz relatos de experiências de lideranças femininas. A proposta do projeto final foi transformar o livro em uma aplicação Web, possibilitando tanto a aplicação das técnicas de desenvolvimento ensinadas como também uma reflexão necessária sobre o protagonismo de mulheres em diferentes condições sociais.

1Referência omitida para anonimato.

Já em 2024, foi dada a cada equipe a liberdade na escolha do seu próprio tema para o projeto final, um modelo que aumentou o engajamento e favoreceu o desenvolvimento de autonomia entre as participantes. Para facilitar esse processo, realizamos dinâmicas de ideação conduzidas por profissionais de Design, destacando a importância da interdisciplinaridade e da co-criação no desenvolvimento de software.

Tanto nos projetos finais de 2023 como em 2024, contamos com a colaboração de uma professora e pesquisadora da área de Serviço Social, que trouxe temas e reflexões sobre o papel das mulheres na sociedade. Com essa troca de experiências, as alunas ampliaram sua visão sobre o papel da tecnologia como ferramenta de transformação social.

### Adoção de Métodos Ágeis

No TWIST, optamos por incorporar o ensinamento dos princípios ágeis na condução dos projetos desenvolvidos pelas alunas. Essa abordagem não é uma novidade, mas aqui queremos explorar a contribuição dos princípios ágeis no desenvolvimento de soft skills para trabalho em equipe, como nos trabalhos de Fioravanti[Fioravanti et al. 2023] e de Chassidim[Chassidim et al. 2018]. Princípios [Beck et al. 2001] como “indivíduos e interações mais do que processos e ferramentas"e “responder a mudanças mais do que seguir um plano"são apresentados como forma de orientar o trabalho colaborativo dentro das equipes. Outro princípio das metodologias ágeis que incorporamos no programa é a auto-organização das equipes. Em vez de uma estrutura rígida e hierárquica, incentivamos as participantes a tomarem decisões coletivas sobre suas tarefas, permitindo que cada participante desenvolva habilidades de liderança, colaboração e resolução de problemas.

Já no início da etapa de desenvolvimento de projetos em grupo, organizamos desde a primeira edição um workshop sobre SCRUM [Khabbali et al. 2023]. No entanto, percebemos que apenas essa introdução não era suficiente para o nível de experiência das participantes. Em 2024, acrescentamos novas atividades. Depois da conclusão do primeiro sprint, realizamos um workshop para revisitar a metodologia, rediscutindo os papéis dos membros da equipe. Também fizemos uma atividade dirigida para dar suporte à primeira retrospectiva das equipes. Além disso, ao longo do semestre, contamos com o apoio de uma profissional com grande experiência como scrum master para mediar algumas retrospectivas com equipes nas quais observamos dificuldades. Em 2025, planejamos introduzir uma mentoria específica para apoiar o uso de SCRUM, novamente contando com profissionais com experiência no tema.

Outra mudança introduzida em 2024 foi adotarmos a estratégia de manter as mesmas equipes ao longo de todos os projetos do programa. Essa decisão teve um impacto grande no desenvolvimento das participantes, pois permitiu uma evolução na dinâmica de colaboração. Com o tempo, as equipes passaram a se conhecer melhor, aprimorando a comunicação, o alinhamento de expectativas e a distribuição de tarefas. A manutenção da equipe ao longo dos projetos também reforçou a ideia de melhoria contínua, um dos princípios fundamentais das metodologias ágeis, incentivando as participantes a refletirem sobre os desafios enfrentados e ajustarem suas práticas de trabalho a cada nova entrega.

Uma premissa importante para o programa é que as participantes se sintam confortáveis e seguras no ambiente em que estão. Por outro lado, queremos preparar as participantes para o que encontrarão no dia a dia de seus trabalhos, que tipicamente não comporta escolher colegas de equipe ou retirar-se de equipes onde não estejam se sentindo

bem. A formação das equipes de participantes foi sempre decidida pela coordenação do programa, e procuramos investir ao máximo no apoio a resolução de conflitos pelos próprios grupos. Utilizamos os próprios mecanismos da metodologia, em particular as dailies e reviews, para acompanhar e apoiar, quando necessário, o funcionamento das equipes de participantes. De fato ocorreram algumas situações de conflito e esses mecanismos se mostraram apropriados para abordar, coletivamente, formas de resolvê-los.

Além disso, enfatizamos que a responsabilidade pelas entregas dos trabalhos nos projetos é do grupo como um todo, e não apenas de indivíduos isolados. Esse princípio está alinhado com a ideia ágil de que a equipe inteira é responsável pelo sucesso do projeto. Para reforçar essa mentalidade, trabalhamos a importância da comunicação, do alinhamento de expectativas e da cooperação entre as participantes, evitando que o trabalho fique sobrecarregado em algumas e garantindo que todas contribuam para o resultado final. Nos dois anos do programa, todas as equipes chegaram ao final com bom nível de integração e bons resultados em seus projetos.

Na edição de 2024 introduzimos também uma conversa de feedback com cada participante no meio do semestre. Naturalmente, tivemos várias outras interações mais informais, individuais ou em grupos, mas as próprias participantes expressaram o desejo de receberem um feedback individual, pois sabiam que eram periodicamente avaliadas em formulários preenchidos por tutoras e mentores. Essas conversas acabaram provendo um ótimo canal para discussão de algumas posturas que geravam conflitos dentro das equipes. Muitas vezes as próprias participantes envolvidas no conflito estavam conscientes de suas posturas e motivadas para refletir sobre possíveis soluções das questões.

No encontro de fechamento da edição de 2024, onde as participantes puderam externar suas reflexões e avaliações sobre o programa, o trabalho em equipe foi o assunto que mais as entusiasmou. Além da satisfação de todas com a experiência, algumas colocaram sugestões muito interessantes que pretendemos explorar em 2025, em especial para maior interação entre as participantes das diferentes equipes.

## 4. Dinâmicas: rodas de conversa e outras interações

Nesta seção descrevemos o conjunto de dinâmicas que criamos para o desenvolvimento de soft skills que apoiem uma participação segura e confortável no mercado de trabalho, nosso maior foco de interesse. Com rodas de conversa, apresentações e interações guiadas, buscamos promover o sentimento de pertencimento e também reflexões sobre representatividade e estratégias para lidar com desafios acadêmicos e profissionais.

Permeando todas as nossas atividades, trabalhamos um dos objetivos principais de nosso programa, que é o da criação de uma primeira rede de apoio para as participantes: Queremos que elas terminem o programa fazendo parte de um grupo ao qual podem recorrer para apoio pessoal ou profissional.

### Organização das rodas de conversa e apresentações

Em quase todos os eventos com convidadas, definimos uma pessoa da coordenação do programa como mediadora: essa pessoa propõe às convidadas alguns temas, e em seguida passa a palavra ao grupo de estudantes para que coloquem suas perguntas ou comentários.

Na primeira edição do TWIST, observamos pouca interação das participantes com

as convidadas nas primeiras conversas. Passamos então a promover uma atividade que chamamos de “esquenta” das conversas e apresentações: Pedimos às participantes que previamente assistissem a um vídeo ou lessem um texto relacionado ao contexto das convidadas e que elaborassem duas ou três perguntas para a roda de conversa. Como resultado, a discussão passou a fluir mais livremente.

Ao final de cada evento, procuramos criar um espaço para uma interação informal das participantes do TWIST com as convidadas. Sempre tiramos algumas fotos de convidadas com participantes, criando uma primeira aproximação física, e em seguida permanecemos por algum tempo conversando no próprio espaço do auditório ou na sua antessala. Esses artifícios bem simples acabam se mostrando bastante eficazes para a aproximação entre participantes e convidadas.

### Quebrando o gelo

Na primeira semana do programa, conduzimos uma dinâmica mediada por duas profissionais da universidade com experiência no acolhimento a estudantes. As mediadoras começam a atividade com uma motivação, falando um pouco sobre a falta de representatividade feminina nos ambientes de estudo e trabalho em computação, e em seguida propõem um exercício, onde cada grupo escolhe algumas imagens entre um conjunto disponível (fixadas nas paredes) e cria uma pequena narrativa sobre elas. Depois de um intervalo de tempo dedicado a isso, cada grupo relata para todas o que criou com as imagens escolhidas. Em seguida, fazemos uma roda para falar um pouco de experiências e percepções relacionadas à falta de mulheres na área de computação que já tenham vivenciado.

Essa atividade, que chamamos de “dinâmica de integração”, cumpre diversos papéis. Logo no início, pedimos que cada participante se apresente e fale um pouco de si e de seus hobbies, facilitando a interação e socialização das participantes, e o início da formação da rede de apoio entre elas. Ao guiar a discussão abrindo espaço até para experiências desagradáveis, as mediadoras criam para as participantes uma primeira experiência com o espaço seguro que o programa proporciona: algumas relatam acontecimentos ou conversas nas quais se sentiram agredidas e é palpável como o ambiente vai se tornando mais solto ao longo desses relatos. A atividade cumpre também o papel de um primeiro exercício de empatia, sensibilizando algumas participantes com menos visão sobre possíveis desconfortos sofridos por mulheres em ambientes predominantemente masculinos.

Fundamental para o sucesso dessa atividade é a experiência das mediadoras, uma delas psicóloga atuante no serviço de atendimentos a estudantes e a outra uma profissional de serviço social que estuda especificamente a questão de gênero.

### Gestão de Tempo

Desde o início do programa, em 2023, tivemos uma preocupação com a organização acadêmica de nossas participantes, que tipicamente são alunas dos primeiros períodos de seus cursos. Esses semestres são muito exigentes e é importante que, apesar da carga horária demandada pelo programa, as participantes consigam priorizar sua formação acadêmica.

Na segunda edição do programa, com nossa aproximação com a equipe de psicopedagogia da universidade, organizamos, logo na primeira semana, um encontro para

falar de organização de tempo. Nesse encontro, as psicopedagogas discutem algumas dificuldades comuns entre estudantes e falam de alguns expedientes que podem ajudá-las. O encontro é bastante interativo e inclui um exercício onde cada participante descreve sua organização diária e percebe alguns delizes de planejamento.

Ao final da dinâmica, a equipe de psicopedagogas faz um convite para que as participantes agendem orientação para a matrícula no semestre acadêmico a ser iniciado (como o programa começa em julho, é possível ainda fazer essa atividade antes do período de matrícula). A atividade foi muito bem recebida pelas participantes e todas compareceram ao atendimento para ajuda na composição de suas grades para 24.2.

Ao longo do semestre, a organização do trabalho em sprints e as reuniões de planejamento e de retrospectiva também constituem um exercício de gestão de tempo. Observamos o amadurecimento das participantes em relação ao que se propõem fazer no tempo de cada sprint, levando também em consideração as demandas acadêmicas que teriam naquele mesmo período.

Ao final das duas edições do TWIST, alguns depoimentos de participantes, incluindo os de alunas ainda terminando o segundo semestre na universidade, apontaram para o ganho que haviam tido em organização de tempo.

### Desconstruindo estereótipos

A falta de exemplos e modelos de mulheres atuantes na área é muito gritante. Várias participantes falam disso já nas entrevistas de seleção. Essa falta de modelos contribui para os estereótipos do profissional de computação, e para o consequente desânimo em permanecer na área[Schuster and Martiny 2017, Cheryan et al. 2013].

Para abrir novas perspectivas em relação a profissionais da área, buscamos convidar para rodas de conversa mulheres atuantes tanto no mundo corporativo como na academia, para mostrar diferentes caminhos de carreira possíveis. Convidamos desde estagiárias até pessoas em cargos executivos em grandes empresas. Essa foi uma preocupação que surgiu a partir de nossas observações na primeira edição do programa, em que convidamos mulheres mais senior e observamos que seus depoimentos eram por vezes distantes da realidade atual das participantes do TWIST. Achamos adequado então trazer mulheres em diferentes momentos de suas carreiras. Também com o objetivo de aumentar o horizonte de possibilidades, convidamos mulheres com diferentes perfis de atuação. Algumas convidadas trabalham em grandes empresas, algumas em startups, outras em institutos de pesquisa e desenvolvimento e ainda outras são empreendedoras.

Buscamos também trazer mulheres com vidas pessoais diversas (mulheres solteiras, mulheres com filhos, etc) para mostrar que essas escolhas são compatíveis com a atuação na área (ainda que seja importante reconhecer as dificuldades encontradas).

Sempre que possível, pedimos que as convidadas falem de maneira introdutória sobre suas áreas de atuação específicas, algumas tradicionalmente não associadas à presença feminina (por exemplo, computação em nuvem ou computação gráfica).

Observamos que esse conjunto de rodas de conversa é muito bem recebido pelas participantes. Tanto nas avaliações como em seus depoimentos ao final do programa, várias estudantes comentam como foi impactante interagir com tantas mulheres bemsucedidas (em alguns dos depoimentos chamadas de “mulheres incríveis”). Acreditamos

que esse contato com um grande número de mulheres trabalhando na área e mostrando suas experiências positivas, ainda que com uma visão crítica das questões a serem enfrentadas, contribui para a autoeficácia das participantes, levando a uma maior tranquilidade em relação a suas escolhas de profissão[Schuster and Martiny 2017, Marra et al. 2009].

Essa também é uma oportunidade para a expansão da rede de apoio das participantes. Ao final dos eventos, tipicamente as convidadas se despedem pedindo que as estudantes entrem em contato caso queiram mais informações sobre o que foi discutido e permanecem algum tempo em rodas informais de conversa que permitem alguma proximidade inicial entre estudantes e convidadas.

### Comunicação Eficaz e Técnicas de Apresentação

Ao longo do programa, várias atividades trabalham habilidades de comunicação, em especial comunicação oral.

As dinâmicas da metodologia Scrum, mediadas por profissionais com experiência, trabalham a comunicação das participantes com seus grupos quase diariamente. Muitas vezes exploramos também técnicas de programação em pares, exercitando a comunicação em diferentes duplas.

Relativamente cedo em nosso cronograma, organizamos um workshop sobre apresentações conduzido por uma designer. Depois de abordar tanto cuidados mais visuais, como fontes, cores e legibilidade, como preocupações com narrativas e organização de conteúdo, com muitos exemplos, essa mediadora pede que as participantes preparem uma pequena apresentação, que em seguida mostram ao grupo, recebendo feedbacks da mediadora e do próprio grupo.

Ao longo do semestre, percebemos que o aprendizado resultante dessa atividade é incorporado às apresentações dos projetos desenvolvidos, e observamos que essas apresentações têm uma qualidade não comum em estudantes com esse nível de maturidade.

### Autoapresentação

Um recurso importante para quem vai ingressar no mercado de trabalho é se apresentar com confiança a potenciais empregadores ou colaboradores. Convidamos uma profissional de recrutamento para discutir diferentes pontos dessa autoapresentação. De maneira bastante interativa, ela discute com o grupo preocupações e questões na elaboração de currículos e no comportamento em entrevistas. A discussão é bastante rica, com provocações para uma reflexão sobre que informações e impressões devem resultar da leitura de um currículo ou de respostas numa entrevista. O que se deseja comunicar num currículo? E por outro lado, o que recrutadores desejam saber de fato quando fazem determinada pergunta? As participantes se mostram bastante motivadas e animadas nessa discussão.

Como no momento atual boa parte do recrutamento se dá através do Linkedin, as próprias participantes pediram, na segunda edição do programa, uma apresentação com recomendações e cuidados para a manutenção de perfis nessa plataforma. Convidamos para isso uma profissional de desenvolvimento de software com interesse no assunto.

### Conscientização sobre direitos

Uma questão que vem se tornando bastante presente em ambientes de trabalho

onde há grupos subrepresentados é a de importunação e assédio, tanto moral como sexual. Para orientar as participantes sobre o assunto, uma convidada do departamento jurídico da universidade faz uma apresentação explicando o que caracteriza importunação e assédio e que providências podem ser tomadas caso ocorra uma dessas situações.

A própria convidada salienta a importância de redes de apoio para lidar com episódios de importunação, levando o grupo a refletir sobre como essas redes nos permitem ter pessoas de confiança com quem conversar sobre qualquer situação desconfortável e sobre a necessidade de observar ao nosso redor se alguma outra pessoa está sofrendo algum tipo de constrangimento (empatia).

### Consciência Social

Para contextualizar o nosso programa num cenário mais amplo de projetos de inclusão feminina no mercado de trabalho, promovemos conversas sobre iniciativas junto ao ensino médio e dentro de empresas. Para discutir iniciativas no ensino médio, organizamos rodas de conversa com programas parceiros do Meninas Digitais e com projetos em outras áreas técnico-científicas. Convidamos também profissionais envolvidos em programas de diversidade e inclusão em algumas empresas que relatam suas experiências, com casos de sucesso e dificuldades enfrentadas. Achamos importante motivar as participantes para um horizonte mais amplo de diversidade e inclusão, refletindo também sobre outros grupos subrepresentados além das mulheres.

## 5. Observações Finais

O desenvolvimento de soft skills é visto hoje como um componente fundamental da formação de um profissional. Diante dos desafios pela baixa representatividade ainda enfrentados pelas mulheres na computação, no contexto do TWIST estamos especialmente interessadas em competências que dêem suporte a uma participação confortável e segura dessas mulheres na comunidade de desenvolvimento de software.

Para desenhar a forma de desenvolver essas competências, usamos uma abordagem inicialmente intuitiva, aproveitando como ponto de partida nossa própria experiência e a de muitas outras mulheres desenvolvedoras de software. Pensando em algumas habilidades importantes para enfrentar os desafios presentes em ambientes profissionais onde mulheres são subrepresentadas, procuramos pessoas de várias áreas da universidade que nos ajudaram a planejar e conduzir muitas das dinâmicas relatadas. Consideramos que esse apoio interdisciplinar é essencial para um trabalho consistente de desenvolvimento de habilidades socioemocionais.

Várias outras iniciativas para promoção da participação feminina na área de Computação trabalham com o desenvolvimento de soft skills [Desidério et al. 2023]. Um diferencial do nosso trabalho é o ambiente em que ele ocorre. Procuramos emular um ambiente profissional, com prazos para desenvolvimento e entregas. Isso permite que o desenvolvimento de habilidades como as de trabalho em equipe seja tratado de forma muito realista. Por outro lado, por se tratar de um ambiente onde só há mulheres, as participantes se sentem naturalmente seguras para externar e trabalhar suas dúvidas e dificuldades. Em edições futuras do TWIST planejamos explorar em maior profundidade os impactos de iniciativas como essa, avaliando, por exemplo, sua influência na permanência e progressão das participantes em carreiras na área de computação.

## 6. Agradecimentos

Gostaríamos de agradecer imensamente aos mentores e a todos que colaboraram com o TWIST. Vocês foram essenciais para o sucesso de nosso programa.
