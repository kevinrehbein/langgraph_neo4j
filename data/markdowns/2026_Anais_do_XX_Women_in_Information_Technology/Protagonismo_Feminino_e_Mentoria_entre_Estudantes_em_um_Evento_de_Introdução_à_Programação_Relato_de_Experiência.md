# Protagonismo Feminino e Mentoria entre Estudantes em um Evento de Introdução à Programação: Relato de Experiência

Barbara Quintela, Lara Esteves, Eduarda Miguel, Mell Feital, Lorenza Moreno, Luciana Brugiolo, Alessandreia Oliveira

1 Departamento de Ciência da Computação (DCC/UFJF)

2Programa de Pós-graduação em Modelagem Computacional (PPGMC/UFJF)

3Mestrado Profissional em Ensino de Computação (PROFCOMP) Universidade Federal de Juiz de Fora – Juiz de Fora, MG, Brasil

barbara.quintela@ufjf.br,lara.esteves@estudante.ufjf.br,

{ eduardamartins.miguel,mell.feital } @estudante.ufjf.br,

{ lorenza.moreno,lbrugiolo,alessandreia.oliveira } @ufjf.br

Abstract. This article presents an experience report on the First Meeting of the Project “Meninas no Mundo Digital”, an initiative aimed at encouraging girls’ participation in computing-related activities. The event included an introductory programming course using Scratch, taught by Junior Scientific Initiation scholarship students to new participants, promoting peer mentoring among students. The program also included participation in a university program showcase and educational activities addressing adolescent health and gender-based violence. At the end of the event, an evaluation questionnaire was applied. The results indicate that the initiative contributed to stimulating interest in programming and in the university environment.

Resumo. Este artigo apresenta um relato de experiência sobre a realização do I Encontro do Projeto “Meninas no Mundo Digital”, iniciativa voltada ao incentivo da participação de meninas em atividades de Computação. O evento incluiu um curso introdutório de programação com Scratch ministrado por bolsistas de Iniciação Científica Júnior para novas participantes, promovendo mentoria entre estudantes. A programação também contou com participação em uma mostra de cursos da universidade e atividades formativas sobre saúde na adolescência e violência de gênero. Ao final, foi aplicado um questionário de avaliação. Os resultados indicam que a iniciativa contribuiu para estimular o interesse pela programação e pelo ambiente universitário.

## 1. Introdução

Nas últimas décadas, as áreas de Ciência, Tecnologia, Engenharia e Matemática (STEM) têm desempenhado papel fundamental no desenvolvimento científico, econômico e social das sociedades contemporâneas. A crescente digitalização de processos produtivos e educacionais tem ampliado a demanda por profissionais qualificados nessas áreas, especialmente em campos relacionados à Computação e às tecnologias digitais. No entanto, apesar desse cenário de expansão, observa-se uma persistente desigualdade de gênero na participação feminina em STEM. Dados globais indicam que as mulheres representam cerca de 35% dos graduados em áreas STEM, percentual que permanece relativamente

estável nas últimas décadas e evidencia desafios estruturais para a promoção da equidade de gênero na ciência e tecnologia [Bello et al. 2021].

No contexto brasileiro, essa disparidade também se manifesta de forma significativa, especialmente nas áreas de Computação e tecnologia da informação. Estudos apontam que a participação feminina em cursos de graduação em Computação permanece significativamente inferior à masculina, refletindo um fenômeno complexo influenciado por fatores socioculturais, estereótipos de gênero, falta de representatividade feminina e oportunidades limitadas de contato com a área durante a Educação Básica. A literatura destaca que essas desigualdades não estão associadas a diferenças de capacidade cognitiva entre homens e mulheres, mas sim a barreiras sociais e culturais que afetam o interesse, a autoconfiança e o sentimento de pertencimento das meninas em relação às áreas tecnológicas [Lopes, R. et al. 2023].

Diante desse cenário, diversas iniciativas têm sido propostas para estimular o interesse de meninas pela Computação desde os níveis iniciais da formação escolar. Programas educacionais que combinam atividades de ensino de programação, experiências de aprendizagem colaborativa e contato com modelos de referência femininos têm demonstrado potencial para aumentar o engajamento e a permanência de meninas em áreas STEM [Quintela, B. et al. 2024]. Nesse contexto, projetos de extensão universitária e programas de Iniciação Científica Júnior desempenham papel estratégico ao aproximar estudantes da Educação Básica do ambiente científico, promovendo experiências formativas que contribuem para o desenvolvimento do Pensamento Computacional (PC), da autonomia intelectual e do interesse por carreiras científicas [Maciel et al. 2021].

Outro aspecto relevante destacado pela literatura refere-se ao papel da mentoria e do protagonismo feminino em ambientes educacionais. A criação de espaços de troca de experiências entre estudantes, pesquisadoras e profissionais da área pode contribuir para o fortalecimento da identidade acadêmica das meninas e para a construção de redes de apoio que favorecem sua permanência em trajetórias científicas e tecnológicas [Denner et al. 2012]. Essas práticas são particularmente importantes em áreas historicamente masculinas, como a Computação, nas quais a ausência de modelos femininos pode reforçar percepções de não pertencimento.

Nesse contexto, foi desenvolvido o projeto “Meninas no Mundo Digital”, que tem como objetivo incentivar a participação de estudantes da Educação Básica em atividades relacionadas ao Pensamento Computacional. O projeto, que atende meninas do 8 ano do Ensino Fundamental ao 3 ano do Ensino Médio, busca promover ambientes de aprendizagem colaborativos e inclusivos que valorizem o protagonismo feminino e estimulem o interesse de meninas pela Computação por meio de ações formativas, atividades práticas e espaços de diálogo sobre trajetórias acadêmicas na área. Desde sua concepção, o projeto, cuja duração é de 3 anos, tem o objetivo de estimular o protagonismo das estudantes, com foco na formação de alunas para atuarem como monitoras e tutoras em diferentes contextos educativos, dentro e fora de suas escolas. Entre as ações realizadas no âmbito do projeto, destaca-se a realização do I Encontro do Projeto Meninas no Mundo Digital, evento que reuniu estudantes participantes, mentoras e integrantes da equipe do projeto em um espaço de interação, formação e compartilhamento de experiências. O encontro foi estruturado com atividades voltadas ao fortalecimento da mentoria entre estudantes e ao incentivo à participação das alunas em atividades de introdução à programação e

iniciação científica além de rodas de conversa sobre saúde e violência de gênero.

O presente artigo tem como objetivo relatar as ações desenvolvidas durante o I Encontro do Projeto Meninas no Mundo Digital, com foco nas estratégias adotadas para promover o protagonismo feminino e a mentoria entre estudantes no processo de introdução à programação no contexto da Iniciação Científica Júnior. Como contribuição, o trabalho evidencia o potencial do evento enquanto espaço formativo que articula ensino de programação, mentoria entre pares e aproximação com o ambiente universitário, destacando o papel de estudantes da Educação Básica não apenas como participantes, mas também como mediadoras do processo de aprendizagem. Ao apresentar essa experiência, busca-se contribuir para a disseminação de práticas educacionais inclusivas em Computação e para o fortalecimento de iniciativas voltadas à ampliação da participação feminina nas áreas de ciência e tecnologia.

Por fim, este artigo está organizado da seguinte forma. A Seção 2 apresenta a fundamentação teórica que sustenta o trabalho, abordando conceitos relacionados ao Pensamento Computacional, ao ensino de programação na Educação Básica e às iniciativas voltadas à inclusão de meninas na Computação. A Seção 3 descreve o desenho do estudo, a caracterização do evento e os procedimentos adotados para coleta e análise dos dados. Em seguida, a Seção 5 apresenta os resultados obtidos a partir da análise das atividades realizadas e das percepções das participantes. Por fim, a Seção 6 apresenta as considerações finais do estudo, destacando as principais contribuições da experiência relatada e possíveis direções para trabalhos futuros.

## 2. Fundamentação Teórica e Trabalhos Relacionados

O PC tem sido reconhecido como uma habilidade fundamental para a formação de estudantes no século XXI, envolvendo processos como decomposição, reconhecimento de padrões, abstração e construção de algoritmos [Wing 2006]. No contexto educacional, atividades de programação têm sido utilizadas como estratégia para desenvolver essas habilidades desde os níveis iniciais da formação escolar. Ambientes de programação visual, como o Scratch, têm se destacado nesse cenário por possibilitar a introdução de conceitos computacionais de forma interativa e acessível, favorecendo a compreensão de estruturas fundamentais da programação e estimulando o raciocínio lógico e a resolução de problemas. No Brasil, a relevância da Computação na Educação Básica foi reforçada com a homologação do Complemento da Computação à Base Nacional Comum Curricular (BNCC), que estabelece diretrizes para o ensino de Computação estruturadas nos eixos de PC, Mundo Digital e Cultura Digital [MEC 2022].

Apesar da crescente demanda por profissionais na área de tecnologia, a participação feminina em cursos e carreiras relacionadas à Computação permanece significativamente inferior à masculina. Estudos indicam que essa desigualdade está associada a fatores socioculturais, como estereótipos de gênero, ausência de modelos de referência e menor exposição de meninas a experiências relacionadas à tecnologia durante a Educação Básica [Cheryan et al. 2017]. Nesse contexto, iniciativas educacionais voltadas ao incentivo da participação de meninas em atividades de Computação têm sido desenvolvidas em diferentes países. Programas que combinam ensino de programação, experiências

colaborativas e estratégias de mentoria têm demonstrado potencial para ampliar o interesse das estudantes pela área e fortalecer seu sentimento de pertencimento em ambientes tecnológicos [Denner et al. 2012].

No Brasil, um dos principais espaços de discussão sobre a participação de mulheres na Computação é o Women in Information Technology (WIT), evento realizado no âmbito do Congresso da Sociedade Brasileira de Computação. O evento reúne pesquisas e relatos de experiência voltados à promoção da equidade de gênero na área de tecnologia. Nos últimos anos, diversos trabalhos apresentados no WIT têm descrito iniciativas educacionais voltadas ao incentivo da participação de meninas na Computação, incluindo oficinas de programação, projetos de extensão universitária, atividades de mentoria e participação em competições de programação [Maciel et al. 2021, Holanda, M. et al. 2025, Quintela, B. et al. 2024]. Esses relatos indicam que atividades práticas de introdução à programação, aliadas a ambientes colaborativos de aprendizagem e presença de modelos de referência femininos, podem contribuir para ampliar o interesse de estudantes pela área. Nesse contexto, o presente trabalho dialoga com essas iniciativas ao relatar a realização de um evento voltado à introdução à programação e ao fortalecimento do protagonismo feminino entre estudantes da Educação Básica. A experiência descrita diferencia-se por articular, em uma mesma ação formativa, atividades de ensino de programação, mentoria entre estudantes e aproximação com o ambiente universitário, com destaque para a atuação de estudantes da própria Educação Básica como ministrantes da oficina, assumindo papel ativo na mediação da aprendizagem.

## 3. Métodos

### 3.1. Desenho do estudo e caracterização do evento

Este trabalho caracteriza-se como um relato de experiência de natureza qualitativa, cujo objetivo é descrever e analisar as atividades realizadas durante o I Encontro do Projeto Meninas no Mundo Digital. Relatos de experiência constituem uma estratégia para documentar e compartilhar práticas educacionais, permitindo a disseminação de iniciativas voltadas à inclusão e ao ensino de Computação, especialmente no contexto de projetos de extensão. O evento, realizado nas dependências da Universidade Federal de Juiz de Fora (UFJF) foi organizado no âmbito do projeto Meninas no Mundo Digital e teve como objetivo promover um espaço de integração entre as estudantes participantes do projeto, estimular o protagonismo feminino e fortalecer o interesse pela Computação e pela iniciação científica. A programação foi estruturada em atividades formativas e de integração realizadas ao longo de um dia, contemplando momentos de aprendizagem em programação, participação em atividades acadêmicas da universidade e oficinas voltadas ao desenvolvimento pessoal e social das participantes. A escolha da data do evento foi planejada para coincidir com a realização de uma mostra de cursos da área de exatas da Universidade, permitindo que as estudantes da Educação Básica participantes do projeto também pudessem conhecer diferentes cursos de graduação e vivenciar o ambiente universitário.

### 3.2. Participantes

Participaram do evento estudantes da Educação Básica de três escolas distintas, todas bolsistas de Iniciação Científica Júnior vinculadas ao projeto, além de integrantes da equipe (docentes e estudantes de graduação). Todas as alunas já haviam tido contato com Pensamento Computacional, por meio de atividades de lógica. Em uma das escolas, cujo tempo

de atividade do projeto era superior às demais, as estudantes já estavam tendo contato com programação em blocos utilizando Blockly e algumas alunas tinham participado de uma oficina de Scratch (que não foi exclusiva para participantes do projeto). Entre as alunas que mais se destacaram, três foram convidadas a ministrar uma oficina de programação durante o evento, atuando como mentoras em um primeiro momento, mas fazendo parte do público alvo no restante das atividades.

### 3.3. Curso de Introdução à Programação com Scratch

O evento teve início com um curso introdutório de programação utilizando a plataforma Scratch, conduzido por bolsistas de Iniciação Científica Júnior do próprio projeto. A atividade foi planejada e ministrada pelas estudantes que já participavam das atividades do projeto, promovendo um ambiente de aprendizagem baseado no protagonismo estudantil e na mentoria entre pares. As bolsistas responsáveis pelo curso escolheram como temática da atividade o universo da Barbie, utilizando personagens e elementos narrativos associados ao tema como forma de tornar a atividade mais próxima do universo das participantes. A proposta consistiu na construção de um jogo interativo no Scratch, nos quais foram explorados conceitos fundamentais de programação, como sequência de comandos, eventos, estruturas de repetição e interação entre objetos. A utilização do Scratch permitiu introduzir conceitos de programação de forma visual e interativa, favorecendo a compreensão dos conceitos básicos de Pensamento Computacional por parte das estudantes que estavam tendo o primeiro contato com programação.

### 3.4. Participação na Mostra de Cursos de Exatas

Ao final do curso de programação, as participantes foram convidadas a visitar a mostra de cursos da área de exatas da Universidade Federal de Juiz de Fora (UFJF), que ocorreu na mesma data do evento. A atividade teve como objetivo proporcionar às estudantes da Educação Básica a oportunidade de conhecer diferentes áreas de formação acadêmica, interagir com estudantes universitários e obter informações sobre cursos de graduação oferecidos pela instituição. A participação nessa atividade buscou ampliar o contato das estudantes com o ambiente universitário, contribuindo para a construção de perspectivas futuras relacionadas à continuidade dos estudos no ensino superior.

### 3.5. Atividades formativas

No período da tarde, foram realizadas duas atividades voltadas ao desenvolvimento pessoal e à discussão de temas relevantes para a formação das participantes. A primeira atividade consistiu na oficina “Saúde na adolescência: conhecer para prevenir”oferecida por uma equipe de enfermagem parceira do projeto. A oficina teve caráter informativo e educativo, proporcionando um espaço de diálogo sobre cuidados com a saúde e prevenção. Em seguida, foi realizada uma roda de conversa utilizando o jogo “Memórias Transversais”, que buscou promover reflexões e discussões sobre temas relacionados à violência de gênero. O jogo da memória foi desenvolvido por duas especialistas em políticas e gênero e a oficina foi mediada por elas. O jogo foi utilizado como ferramenta mediadora para estimular o diálogo entre as participantes, permitindo a troca de experiências e a reflexão coletiva sobre situações de violência de gênero e estratégias de enfrentamento.

> 2https://www.transversais.com.br/cartas

### 3.6. Momentos de convivência e integração

Além das atividades formativas, o evento também incluiu momentos destinados à convivência e integração entre as participantes. Durante o evento, as estudantes almoçaram no Restaurante Universitário da UFJF, proporcionando uma experiência de vivência no cotidiano universitário. No período da tarde, também foi oferecido um lanche às participantes, contribuindo para a manutenção de um ambiente acolhedor e de interação entre as estudantes. Esses momentos de convivência foram considerados importantes para fortalecer os vínculos entre as participantes do projeto e promover um ambiente de troca de experiências e construção coletiva de conhecimentos.

## 4. Coleta de dados e avaliação do evento

Com o objetivo de obter percepções das participantes sobre as atividades realizadas e identificar possíveis contribuições do evento para o interesse das estudantes pela Computação e pelas atividades do projeto, foi aplicado um questionário de avaliação ao final do evento. O instrumento foi respondido voluntariamente pelas participantes e teve caráter exploratório, sendo utilizado como estratégia para coletar feedback sobre a experiência vivenciada. O questionário foi estruturado com questões fechadas e abertas. A questão fechada buscou avaliar a atividade de maior interesse entre as participantes. Já as questões abertas permitiram que as estudantes expressassem suas opiniões sobre a organização do evento, satisfação em relação às diferentes atividades realizadas ao longo do dia e indicassem os momentos que consideraram mais relevantes, bem como sugestões para futuras edições do encontro. Entre os aspectos investigados no questionário estavam: (i) a atividade de maior interesse, (ii) a experiência na universidade em geral, (iii) o que sentiram falta no evento (iv) o que poderia ter sido melhor.

As respostas obtidas foram analisadas de forma descritiva e qualitativa, considerando tanto a frequência das respostas nas questões objetivas quanto os comentários registrados nas questões abertas. Essa análise permitiu identificar percepções das participantes sobre os aspectos mais positivos do evento, bem como elementos que podem orientar o planejamento de futuras ações do projeto. A utilização do questionário como instrumento de avaliação buscou, portanto, fornecer subsídios para compreender a experiência das estudantes durante o encontro e contribuir para o aprimoramento das estratégias adotadas pelo projeto no incentivo à participação de meninas em atividades relacionadas à Computação e à iniciação científica.

## 5. Resultados

### 5.1. Público participante

O evento contou com a participação de 46 pessoas credenciadas sendo: 8 professoras da equipe (5 da universidade e 3 de escolas parceiras), 2 especialistas em estudos de gênero vinculadas ao projeto, 4 bolsistas de graduação, 9 bolsistas que iniciaram no projeto em abril/2025 e 11 bolsistas que iniciaram em setembro/2025. Os demais participantes foram estudantes de uma das escolas parceiras que não são bolsistas do projeto.

### 5.2. Protagonismo e superação das alunas que ministraram a oficina

As três alunas do Ensino Médio, participantes do projeto, convidadas para ministrar a oficina tiveram acesso ao material de uma oficina semelhante da qual já haviam participado.

Ao invés de somente reutilizar este material que está disponível no site do projeto, as alunas surpreenderam toda equipe ao desenvolverem, de forma cuidadosa, novo material ( slides, jogo e projeto), incluindo uma identidade visual combinando o universo feminino e diferentes profissões da área de Exatas. O treinamento das mentoras foi realizado através de encontros com a professora de apoio na própria escola, e uma prévia antes do evento na universidade em que apresentaram para a equipe do projeto e receberam comentários de pequenos ajustes sobre dimensionamento de tempo e ordem de apresentação do conteúdo.

Sua atuação superou as expectativas da equipe e passou muita segurança às participantes do curso, que puderam perceber, de forma concreta, (1) que meninas podem efetivamente ocupar posições de destaque na área de Exatas, e (2) que o projeto abre a possibilidade para que cada uma delas também trilhe esse caminho. A presença das mentoras, ainda estudantes do Ensino Médio, aproximou o conteúdo da realidade das participantes e fortaleceu a identificação entre elas.

Para as três mentoras, essa experiência representou uma oportunidade de desenvolver habilidades pouco exploradas no ambiente escolar, como liderança, comunicação, trabalho em equipe, cuidado e criatividade na elaboração de materiais didáticos e senso de responsabilidade no planejamento e na condução de atividades educativas.

### 5.3. Engajamento das alunas na oficina de programação com Scratch

As estudantes que foram introduzidas à programação com o Scratch participaram ativamente da oficina. De forma geral, os relatos recebidos demonstraram que elas não apenas aprenderam, mas também se divertiram neste processo, com algumas alunas manifestando espontaneamente o interesse em aprender mais sobre o assunto. Todas as participantes conseguiram executar o projeto proposto e realizar pequenas modificações na lógica do jogo, demonstrando compreensão dos conceitos apresentados (Figuras 1b-1d).

(a) (b) (c)

(d)

Figura 1. Oficina de Introduç ão a Programaç ão com Scratch apresentada por bolsistas de Iniciaç ão Científica Junior para demais bolsistas.

### 5.4. Aproximação das estudantes com o ambiente universitário

Após um breve intervalo, as bolsistas foram conduzidas para a mostra de cursos de Exatas que estava acontecendo no mesmo prédio do laboratório utilizado no evento. As bolsistas puderam conhecer um pouco mais sobre os cursos e o ambiente universitário (Figura 2).

> 3https://www2.ufjf.br/meninasnomundodigital/material

> 4https://bit.ly/4tuuvie

Figura 2. Participantes do evento visitando a mostra de cursos da área de Exatas.

### 5.5. Percepções das participantes sobre o evento

Ao final do evento foi passado um questionário para coleta de impressões das participantes bolsistas de iniciação científica júnior. O questionário não solicitou dados que permitissem identificação e sua resposta não era obrigatória. Sendo assim, foram coletadas 18 respostas no total. Para identificar a atividade preferida das participantes foi apresentada uma questão fechada com as 4 atividades principais oferecidas (Figura 3a). Metade das participantes identificaram a atividade de programação com Scratch, 22% a roda de Conversa, 17% a mostra de Cursos e por fim a 11% palestra sobre saúde na adolescência. Considerando que parte das bolsistas já conhecia o Scratch é compreensível que tenham indicado preferência por atividades diferentes.

A equipe buscou identificar o nível de interesse em Computação com base nas respostas. Foi proposto o seguinte critério para quantificação: baixo (0-1) não escolheu o curso de programação como atividade preferida e não mencionou nada sobre; médio (2-3) - mencionou ter gostado do curso mas não escolheu como atividade preferida; alto (4-5) escolheu o curso como atividade preferida e indicou que gostaria de ter mais tempo nesta atividade. Observou-se que a maioria das participantes demonstra interesse pela área, o que pode estar relacionado ao fato de terem ingressado no projeto já motivadas por uma curiosidade prévia sobre o tema. (Figura 3b).

Figura 3. Interesse das participantes nas atividades.

Considerando as respostas abertas, foi gerada uma nuvem de palavras para visualização dos termos mais utilizados (Figura 4). Além disso, um script em Python foi utilizado para identificar os termos mais frequentes após exclusão de palavras de parada ( stopwords ). As 10 palavras mais frequentes são apresentadas na Tabela 1. Ficou

clara, pelas respostas, a impressão positiva que o evento causou, sendo que a maioria indicou ter gostado das atividades propostas e de ter conhecido a universidade, demonstrando gratidão pela oportunidade. Vale ressaltar que, nos campos abertos para indicar o que faltou e o que poderia ter sido oferecido, 7 respondentes indicaram que não faltou nada. Entre as sugestões, as participantes indicaram que gostariam de ter tido mais tempo para conhecer a universidade e a mostra de cursos, da qual realmente tiveram que sair cedo para almoçar no restaurante universitário. Outra resposta que chamou a atenção sugeria mais tempo na atividade de programação, para que criassem um jogo em grupo.

Figura 4. Nuvem de palavras a partir das respostas do questionário.

|Palavra|Frequência|Palavra|Frequência|
|---|---|---|---|
|gostei|19|nada|9|
|tudo|16|tempo|9|
|ter|10|experiência|7|
|conhecer|10|Scratch|7|
|legal|9|oportunidade|6|

Tabela 1. Dez palavras mais frequentes nas respostas abertas.

### 5.6. Contribuições do evento para inclusão de meninas na Computação

As atividades realizadas durante o I Encontro do Projeto Meninas no Mundo Digital evidenciam o potencial de iniciativas educacionais e de extensão para promover o interesse de meninas pela Computação. A iniciativa traz a representatividade por meio da equipe do projeto majoritariamente feminina e incentivo ao protagonismo das estudantes em consonância com outros trabalhos relatados no WIT [Santos et al. 2023, Castro, B. et al. 2024]. A realização do curso de introdução à programação com Scratch ministrado por bolsistas de Iniciação Científica Júnior destacou-se como uma estratégia de mentoria entre pares, na qual estudantes com maior experiência no projeto atuaram como facilitadoras do processo de aprendizagem. Esse tipo de abordagem tem sido apontado na literatura como um elemento importante para ampliar o engajamento de meninas em atividades de Computação, uma vez que a presença de modelos de referência e a construção de redes de apoio contribuem para fortalecer o sentimento de pertencimento em áreas tradicionalmente masculinas [Cheryan et al. 2017].

Outro aspecto relevante refere-se à aproximação das estudantes com o ambiente universitário, proporcionada pela participação na mostra de cursos da área de exatas da

universidade durante o evento. Experiências que promovem o contato direto com o contexto acadêmico podem contribuir para ampliar as perspectivas educacionais de estudantes da Educação Básica, especialmente no que se refere à possibilidade de continuidade dos estudos em áreas científicas e tecnológicas. Além disso, o evento incorporou atividades formativas voltadas à discussão de temas relevantes para a realidade das participantes, como saúde na adolescência e violência de gênero. A inclusão dessas atividades reforça a importância de abordagens educacionais que considerem aspectos sociais e culturais que influenciam a participação de meninas em áreas STEM. Nesse sentido, iniciativas que promovem espaços seguros de diálogo e reflexão podem contribuir para fortalecer a autonomia e o protagonismo das estudantes.

Por fim, os resultados observados neste relato dialogam com experiências descritas na literatura nacional sobre iniciativas voltadas à inclusão de meninas na Computação, especialmente aquelas apresentadas no âmbito do WIT [Maciel et al. 2021, Holanda, M. et al. 2025]. Esses trabalhos destacam que projetos de extensão, oficinas de programação e eventos formativos têm papel relevante no incentivo à participação feminina na área, contribuindo para ampliar o interesse de estudantes pela Computação e promover ambientes educacionais mais inclusivos.

## 6. Considerações Finais

Este trabalho apresentou um relato de experiência sobre a realização do I Encontro do Projeto Meninas no Mundo Digital, iniciativa voltada ao incentivo da participação de meninas em atividades relacionadas à Computação e ao desenvolvimento do PC. O evento foi estruturado como um espaço de integração entre participantes do projeto, combinando atividades de introdução à programação, experiências de aproximação com o ambiente universitário e ações formativas voltadas ao fortalecimento do protagonismo feminino.

As percepções coletadas por meio do questionário de avaliação indicam que as atividades desenvolvidas foram bem recebidas pelas participantes e podem ter contribuído para o interesse pela programação e pelas atividades do projeto. Além disso, os resultados sugerem que a criação de ambientes de aprendizagem colaborativos, nos quais estudantes assumem papéis ativos no processo de ensino e aprendizagem, pode fortalecer o engajamento de meninas em atividades relacionadas à Computação. Do ponto de vista educacional, a experiência relatada evidencia o potencial de iniciativas de extensão universitária e programas de Iniciação Científica Júnior como estratégias para aproximar estudantes da Educação Básica da Computação. A combinação de ensino de programação, mentoria entre estudantes e experiências de vivência no ambiente universitário mostrou-se uma abordagem promissora para estimular o interesse de meninas por áreas STEM e fortalecer sua participação em atividades científicas e tecnológicas.

Como limitações deste estudo, destaca-se o caráter exploratório da avaliação realizada, baseada principalmente nas percepções das participantes e no contexto específico de um único evento. Investigações futuras podem ampliar essa análise, incorporando instrumentos de avaliação mais estruturados e acompanhando ao longo do tempo o impacto dessas atividades na trajetória educacional das estudantes. Por fim, espera-se que este relato possa contribuir para a disseminação de práticas educacionais voltadas à inclusão de meninas na Computação, oferecendo subsídios para a organização de eventos e iniciativas semelhantes em projetos de ensino, extensão e divulgação científica.

- 20º Women In Information Technology (WIT 2026): Relatos de Experiência

## Uso de Inteligência Artificial

Os autores declaram que foi utilizado o Grammarly para revisão gramatical.
