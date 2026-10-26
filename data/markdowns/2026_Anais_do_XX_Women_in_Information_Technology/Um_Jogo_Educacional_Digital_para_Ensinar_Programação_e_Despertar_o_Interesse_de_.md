# Um Jogo Educacional Digital para Ensinar Programação e Despertar o Interesse de Meninas do Ensino Médio pela Computação

Ana Clara Laredo, Pedro Henrique Dias Valle, Alessandreia Marta de Oliveira

1 Universidade Federal de Juiz de Fora – DCC/UFJF – Juiz de Fora, MG, Brasil

2Universidade de São Paulo – IME/USP – São Paulo, SP, Brasil

pedrohenriquevalle@usp.br, alessandreia.oliveira@ufjf.br

Abstract. The inclusion of girls and women in programming and Computer Science remains a significant obstacle. In this context, Digital Educational Games (DEGs) can encourage female participation and support the teaching of problem-solving and programming. This work presents PrograDuck, a DEG created to teach programming logic concepts to high school students, with a focus on engaging girls. The game uses a drag-and-drop mechanic to organize command blocks (such as variables, conditionals, loops, and functions) without requiring text-based coding. A heuristic evaluation demonstrated the potential of the DEG to support programming instruction and identified areas for improvement.

Resumo. A participação de meninas e mulheres na programação e nas áreas de Computação ainda enfrenta obstáculos significativos. Nesse contexto, Jogos Educacionais Digitais (JED) podem contribuir para despertar o interesse de meninas pela Computação, enquanto apoiam o ensino de resolução de problemas e programação. Este trabalho apresenta um JED desenvolvido para ensinar lógica de programação no Ensino Médio, com foco em despertar o interesse de meninas pela Computação. O jogo utiliza a mecânica drag-and-drop, permitindo organizar blocos de comandos (variáveis, condicionais, loops e funções) sem escrever código textual. Uma avaliação heurística indicou o potencial do JED para apoiar o ensino de programação e direções para seu aprimoramento.

## 1. Introdução

Nas últimas décadas, os Jogos Educacionais Digitais (JEDs) têm se consolidado como ferramentas com potencial para apoiar processos de ensino-aprendizagem. De acordo com Furtado e Sotil (2024), seu uso tem se mostrado uma estratégia promissora para engajar estudantes e promover uma aprendizagem mais significativa. Contudo, essa consolidação deve ser analisada de forma crítica, pois a transição do potencial teórico para a aplicação eficaz ainda enfrenta barreiras substanciais. Os mesmos estudos que apontam vantagens, como maior interatividade e engajamento, também destacam desafios persistentes, como a capacitação docente e o acesso limitado a hardware de qualidade. Assim, para viabilizar seu uso em diferentes contextos, é essencial que essas ferramentas sejam intuitivas para professores e operem adequadamente em infraestruturas tecnológicas limitadas.

Paralelamente, a inserção de meninas e mulheres na programação e nas áreas de tecnologia ainda enfrenta obstáculos significativos. No Brasil, elas representam cerca de

20% das ingressantes em cursos da área de Computação [Lopes et al. 2023], evidenciando uma sub-representação persistente. A desigualdade também se manifesta em contextos competitivos. Irion et al. (2023) analisaram a participação feminina em maratonas de programação e demonstraram que a baixa representação não decorre de limitações técnicas, mas de fatores socioculturais, como a pouca identificação com a área, a ausência de modelos femininos, ambientes pouco acolhedores e estigmas de gênero que reforçam a sensação de não pertencimento. Esses achados reforçam a necessidade de iniciativas que tornem o contato com a programação mais acessível, seguro e motivador para meninas desde o ensino básico, uma abordagem defendida e já implementada em faculdades federais, por meio de ações como hackathons afirmativos para mulheres [Oran et al. 2025].

Nesse contexto, este trabalho tem como objetivo apresentar o JED denominado PrograDuck, uma ferramenta educacional digital desenvolvida para apoiar o ensino introdutório de lógica de programação a estudantes do Ensino Médio, com foco no engajamento de meninas. A ferramenta foi concebida para integrar conceitos de programação, como variáveis, condicionais e loops, a uma experiência interativa baseada na organização de blocos de comandos, favorecendo a aprendizagem por experimentação. Sua concepção foi orientada por dados coletados junto ao público-alvo, no âmbito de um projeto de extensão vinculado à Universidade [Omitido para revisão], visando desenvolver uma solução acessível e alinhada às preferências e necessidades desse público.

A escolha de um personagem central, um pato, tem função de facilitar a compreensão de conceitos abstratos. Isso permite que conceitos como variáveis, condicionais e loops sejam apresentados de forma mais concreta e contextualizada. A proposta foi orientada por uma investigação com estudantes do Ensino Médio, que indicou interesse por experiências interativas e preferência por estéticas amigáveis, orientando decisões de design voltadas ao engajamento do público-alvo. Uma avaliação heurística foi conduzida para identificar melhorias na ferramenta e avaliar sua adequação ao uso educacional.

Além disso, a proposta apresentada está alinhada aos Objetivos de Desenvolvimento Sustentável (ODS) da Organização das Nações Unidas, em especial ao ODS 4 (Educação de Qualidade) e ao ODS 5 (Igualdade de Gênero), ao buscar promover o acesso equitativo a experiências educacionais de qualidade em Computação e incentivar a participação feminina em áreas historicamente sub-representadas [United Nations 2015].

Este trabalho está organizado da seguinte forma: a Seção 2 apresenta a fundamentação teórica relacionada ao ensino de Computação e ao uso de JEDs. A Seção 3 discute os trabalhos relacionados à proposta do JED. A Seção 4 descreve a metodologia e a estratégia adotadas para o desenvolvimento do JED. A Seção 5 descreve o desenvolvimento do JED e a Seção 6, o planejamento, a execução e os resultados da avaliação. Por fim, a Seção 7 apresenta considerações finais e perspectivas para trabalhos futuros.

## 2. Fundamentação Teórica

O uso de JEDs tem sido amplamente investigado nas últimas décadas, por seu potencial de promover engajamento e aprendizagem ativa [Li et al. 2024]. Esses jogos oferecem ambientes ricos em exploração, tentativa e erro e feedback imediato, características que favorecem a construção de conhecimento e a compreensão progressiva dos conteúdos [Gee 2003, Papert 1980]. A abordagem game-based learning usa elementos de jogos para engajar estudantes em tarefas cognitivas, favorecendo a experimentação e a resolução de

problemas em contextos simulados [Prensky 2001]. Nesse contexto, JEDs podem estimular a motivação intrínseca ao oferecer desafios adequados, autonomia e feedback imediato.

Resultados empíricos recentes corroboram essa perspectiva. Junior et al. (2024) analisaram o engajamento de estudantes do Ensino Médio durante a interação com JEDs e observaram um alto nível de envolvimento ao longo das atividades. Os resultados indicam que emoções positivas, como diversão e ausência de tédio, contribuem para a experiência, reforçando o potencial dos JEDs para aumentar a persistência e o envolvimento em tarefas de raciocínio lógico e de resolução de problemas.

No contexto do ensino de programação, plataformas visuais baseadas em blocos, como o Scratch, tornam conceitos abstratos mais concretos, permitindo que estudantes construam e testem sequências de instruções sem a barreira da sintaxe textual [Resnick et al. 2009]. Essa abordagem é relevante para introduzir conceitos como variáveis, condicionais e loops, ao combinar a manipulação direta e a visualização do comportamento do agente [Tsai et al. 2025].

Além dos aspectos cognitivos, fatores socioculturais influenciam o acesso e a participação em Computação. Estudos indicam que a representatividade, os estereótipos de gênero e o contexto institucional impactam a identificação de meninas com a área e seu engajamento [Holanda and Araujo 2024]. Escolhas de design relacionadas à estética e à narrativa podem reduzir barreiras e tornar a experiência mais acolhedora e acessível [Carrion and Classe 2024]. Em suma, a literatura evidencia o potencial dos JEDs no engajamento e apoio ao ensino, bem como a eficácia de abordagens baseadas em blocos para iniciantes. Nesse contexto, o PrograDuck incorpora essas diretrizes ao tornar visíveis estruturas lógicas e adotar uma estética alinhada às preferências do público-alvo.

## 3. Trabalhos Relacionados

A integração entre educação e JEDs tem sido investigada por uma literatura crescente, com estudos empíricos e revisões sobre seu uso. Como exemplo, [Genesio et al. 2024] discute sua aplicação no ensino de estruturas de dados. Esta seção analisa ferramentas no formato de jogo com objetivos semelhantes, buscando posicionar o PrograDuck e fundamentar suas escolhas de design.

No contexto do ensino superior, Yamashita et al. (2024) propuseram o ProgramADAs, uma ferramenta no formato de jogo voltada ao ensino de algoritmos para mulheres, com foco na permanência na área. A proposta destaca o papel da representatividade e do design inclusivo no engajamento feminino.

Entre as iniciativas para o Ensino Médio, destaca-se o Mapa do Tesouro [Marques et al. 2021], uma ferramenta no formato de jogo voltada ao ensino de paralelismo e PC concorrente por meio de desafios progressivos. A proposta evidencia o uso de mecânicas lúdicas para tornar conteúdos complexos mais acessíveis, sendo aplicada em oficinas com avaliação simplificada. Os resultados indicaram engajamento dos participantes, mesmo diante da alta exigência de raciocínio.

Outra iniciativa é o Lightbot [Souza et al. 2018], que utiliza puzzles baseados em

> 1https://scratch.mit.edu/

> 2https://docs.google.com/spreadsheets/d/1TPUO3nXOVScRTXhP3FoXf_ UkTEbmNU6Q/edit?gid=1779625258#gid=1779625258

comandos para introduzir lógica, modularização e loops. Assim como o PrograDuck, incentiva tentativa e erro e a visualização da execução dos comandos, porém sem foco específico em público ou engajamento feminino.

Codebricks [Shahin et al. 2025] é uma ferramenta em RPG 2D que usa blocos visuais inspirados no Scratch para a construção de algoritmos. A proposta combina gamificação e Pensamento Computacional (PC), com foco em acessibilidade e dispositivos móveis. Embora apresente mecânicas semelhantes ao PrograDuck, difere por não incorporar, de forma explícita, estratégias voltadas ao engajamento de meninas, enquanto PrograDuck prioriza uma experiência narrativa acolhedora com esse foco.

Para facilitar a comparação entre as iniciativas, a Tabela 1 sintetiza suas principais características, considerando aspectos como público-alvo, mecânicas, plataforma e conteúdos abordados. A organização desses elementos permite evidenciar diferenças relevantes entre as ferramentas, especialmente quanto ao foco de uso, às estratégias de interação e à consideração (ou ausência) de recortes específicos de público.

Tabela 1. Comparaç ão entre as iniciativas existentes

|Jogo|Gênero|Mecânica|Público-|alvo|Plataforma|Conteúdo|
|---|---|---|---|---|---|---|
|ProgramADA|RPG|Mecânicas tradicionais de RPG|Mulhere graduaçã|s da o|Computador (PC)|Variáveis, sequenciamento, condicionais, loops e funções|
|Mapa do Tesouro|Estratégia/ Lógica|Drag and drop de blocos|Crianças a 10 ano|de 5 s|Computador (PC)|Sequenciamento, estado, condicionais, loops e funções|
|Lightbot|Estratégia/ Lógica|Programação em blocos (sequência de comandos)|Alunos ensino f mental|do unda-|PC e dispositivos móveis|Sequenciamento, estado, condicionais, loops e funções|
|CodeBricks|Estratégia/ Lógica|Programação em blocos (semelhante ao Lightbot)|Alunos ensino damenta médio|do funl e|Dispositivos móveis|Sequenciamento, estado, condicionais e loops|

A análise evidencia que, embora existam ferramentas no formato de jogo voltadas ao ensino de lógica de programação, poucas consideram explicitamente o público feminino do Ensino Médio. Em geral, priorizam mecânicas e conteúdos, com menor atenção a aspectos como estética, narrativa e identificação com o público. Nesse contexto, o PrograDuck diferencia-se ao integrar esses elementos desde sua concepção, com base em dados do público-alvo, posicionando-se como uma ferramenta educacional digital voltada à introdução à programação e ao engajamento de meninas na Computação.

## 4. Metodologia e Estratégias de Ação

Este trabalho tem caráter qualitativo e descritivo, com o objetivo de compreender percepções e preferências de estudantes do Ensino Médio quanto ao uso de JEDs no ensino de lógica de programação. A investigação foi conduzida por meio de uma pesquisa

> 3 https://drive.google.com/drive/folders/19WVi6k4sfvrJ0BPH9qPToo6yenKSumEZ

com turmas do Ensino Médio. O instrumento de coleta foi elaborado para captar aspectos técnicos e preferências estéticas e emocionais relacionadas ao engajamento com jogos.

A primeira etapa consistiu na identificação do perfil dos participantes. A coleta foi realizada por meio de um formulário aplicado a duas turmas de uma escola pública, totalizando 64 participantes. O instrumento incluiu questões fechadas e abertas sobre hábitos de jogo, familiaridade com programação e preferências de gênero e aprendizagem com JEDs. As respostas foram analisadas de forma qualitativa e quantitativa, permitindo identificar padrões entre as estudantes. Esses dados subsidiaram a compreensão do público-alvo e orientaram decisões de design do JED.

Além disso, os procedimentos observaram princípios éticos aplicáveis à pesquisa com seres humanos. Por envolver estudantes do Ensino Médio, menores de idade, a participação foi voluntária, com autorização dos responsáveis e concordância dos participantes. As respostas foram coletadas de forma anônima, garantindo a privacidade dos dados, e as participantes puderam interromper sua participação a qualquer momento. O instrumento não envolveu avaliação de desempenho, evitando classificações individuais.

Os resultados indicaram alta receptividade ao uso de jogos como recurso educativo. A maioria relatou jogar com frequência em dispositivos móveis, evidenciando afinidade com experiências interativas. Entre os gêneros mais citados, destacaram-se jogos de raciocínio lógico, simulação e aventura, reforçando a adequação desta proposta. Outro ponto relevante foi o engajamento emocional e estético. A pesquisa indicou que personagens simpáticos e ambientes visuais leves, associados ao estilo cozy, aumentam o interesse e reduzem a percepção de dificuldade. Esse padrão foi especialmente observado entre as alunas, evidenciando o potencial de um design mais inclusivo.

A segunda etapa correspondeu ao planejamento do JED, incluindo a seleção da engine, a definição da narrativa e o esboço da jogabilidade. A narrativa foi estruturada em torno de um pato em um ambiente acolhedor, no qual o jogador organiza blocos de comando para realizar tarefas. A jogabilidade foi planejada para promover aprendizagem por tentativa e erro, com feedbacks imediatos e progressão gradual.

Na terceira etapa, o desenvolvimento do PrograDuck foi realizado com base nos dados coletados. O foco é integrar conceitos de lógica de programação, como sequências, condicionais e repetições, de forma contextualizada às ações do personagem.

A quarta etapa correspondeu à avaliação do PrograDuck, por meio de uma AH para identificar problemas de usabilidade, jogabilidade e recursos multimídia. Os resultados estão sendo utilizados para o refinamento do jogo. Em suma, o processo de desenvolvimento do PrograDuck é caracterizado por um ciclo contínuo de avaliação e refinamento, representado na Figura 1.

## 5. Ferramenta PrograDuck

A ferramenta PrograDuck é um JED desenvolvido para introduzir, de forma lúdica e acessível, conceitos fundamentais de lógica de programação a estudantes do Ensino Médio, com foco especial em meninas. A proposta é oferecer uma experiência interativa em que a estudante aprenda por meio da experimentação e da resolução de desafios, sem o uso direto de códigos textuais. O JED foi concebido para ser utilizado tanto em contextos formais de ensino, como aulas regulares de Computação ou oficinas pedagógicas, quanto

20º Women In Information Technology (WIT 2026): Ferramentas

Figura 1. Etapas metodológicas do projeto

em atividades extracurriculares. Sua estrutura modular permite que os educadores adotem o jogo gradualmente, de acordo com os conteúdos abordados em sala de aula.

O JED apresenta a história de um pequeno pato que vive em um ambiente tranquilo e realiza tarefas cotidianas, como alimentar-se, locomover-se e descansar. Para executar essas ações, o jogador deve organizar blocos de comandos que representam conceitos de programação, como variáveis, condicionais, loops e funções. As mecânicas básicas de funcionamento de cada fase estão representadas na Figura 2. A cada fase, a jogadora é desafiada a compreender uma nova estrutura lógica e aplicá-la no contexto narrativo, de modo que o aprendizado ocorra de forma natural e contextualizada. O erro é tratado como parte do processo: se as instruções forem mal organizadas, o pato tentará executar as ações incorretamente, o que ajuda a estudante a entender o porquê do erro e a importância da lógica sequencial.

### 5.1. Aspectos técnicos

O desenvolvimento do PrograDuck está sendo realizado na plataforma GameMaker Studio, utilizada para a criação de jogos 2D que combina recursos de programação visual ( drag and drop ) e de programação textual. A escolha dessa engine foi devida à sua acessibilidade, versatilidade e baixo custo de implementação, fatores essenciais em um projeto de extensão voltado à produção colaborativa e educativa.

O design adotado, pixel art, foi escolhido por suas características estéticas e técnicas. Além de remeter à nostalgia dos jogos clássicos, apresenta baixo custo computacional, garantindo leveza e compatibilidade com equipamentos escolares de desempenho limitado [Telocken et al. 2016]. Essa escolha também favorece a coerência visual do projeto, reforçando a simplicidade e o caráter acolhedor da proposta educacional. Vale mencionar que a ferramenta, em fase de refinamentos, está publicamente disponível para

> 4https://gamemaker.io/pt-BR

(a) Fase 0 – Variáveis

(b) Fase 1 – Condicionais

(c) Fase 2 – Loops

(d) Fase 3 – Funç ões

Figura 2. Mecânicas de jogo do PrograDuck.

fins de pesquisa e educacionais. As informações sobre a licença estão disponíveis nos metadados do repositório.

### 5.2. Aspectos Artísticos

Do ponto de vista artístico, a escolha de um pato como protagonista decorreu da intenção de criar um personagem simples e empático. O pato é um animal associado à leveza e ao humor, transmitindo a ideia de inocência e curiosidade, características que se alinham à proposta educativa do JED. O estilo cozy, com uma paleta de cores suave e elementos visuais confortáveis, foi definido com base nos resultados da pesquisa supracitada. As respostas mostraram forte identificação com estilos visuais “fofinhos” e amigáveis, o que indicou que esse tipo de estética poderia favorecer o engajamento e reduzir a resistência inicial ao conteúdo técnico. Assim, o visual do PrograDuck atua como parte do próprio processo de ensino, tornando a experiência divertida, segura e significativa.

### 5.3. Arquitetura da ferramenta

A arquitetura do PrograDuck (Figura 3) é organizada de forma modular, integrando componentes responsáveis pela interface, lógica de jogo e interação do usuário. A interface gráfica concentra os elementos visuais e os blocos de comandos manipulados pela jogadora, permitindo a construção das soluções por meio de interação direta.

O núcleo do sistema é responsável pela execução das ações definidas nos blocos, interpretando a sequência de comandos e controlando o comportamento do personagem no ambiente do jogo. Esse componente também gerencia a progressão entre as fases e as regras associadas a cada desafio. Além disso, o sistema incorpora um módulo de feedback, que fornece respostas imediatas às ações da jogadora, tanto em nível visual

quanto em nível textual, auxiliando na compreensão dos resultados e na correção de erros. Componentes adicionais incluem o gerenciamento de estados do jogo e o controle de eventos, garantindo a consistência da experiência ao longo da execução.

Essa organização modular favorece a manutenção, a evolução da ferramenta e a inclusão de funcionalidades, como mecanismos de adaptação ao desempenho e recursos de acompanhamento do progresso.

Figura 3. Arquitetura Proposta.

### 5.4. Cenário de uso

Considerando seu uso como ferramenta educacional digital, o PrograDuck pode ser aplicado em um cenário típico em que a jogadora inicia a exploração do ambiente narrativo e progride por fases de complexidade crescente, interagindo com desafios baseados na organização de blocos de comandos. A interação ocorre por meio de mouse e teclado, permitindo manipular elementos visuais e testar soluções de forma iterativa. O sistema fornece feedback imediato, tanto visual quanto textual, auxiliando na compreensão dos resultados das ações e no avanço entre as fases. Recursos adicionais, como dicas integradas à interface, contribuem para a compreensão das instruções e dos elementos do jogo.

## 6. Avaliação do Jogo

Esta seção apresenta o planejamento, a execução e os resultados da avaliação realizada para verificar a efetividade do PrograDuck. A Figura 4 sintetiza as principais etapas do processo avaliativo, incluindo a caracterização dos participantes.

### 6.1. Planejamento da Avaliação

Para verificar a coerência, a clareza e a viabilidade das ideias propostas no PrograDuck, realizou-se uma AH da concepção preliminar do jogo. Esse método permite identificar problemas de usabilidade ainda nas fases iniciais do desenvolvimento, o que contribui para ajustes antes da implementação completa. De acordo com Nielsen [1995], a AH deve envolver entre três e cinco avaliadores, que classificam os problemas observados em quatro níveis de severidade: estético, baixa prioridade, alta prioridade e catastrófico.

A avaliação foi realizada por meio de um formulário estruturado, que contém todas as heurísticas do conjunto AHJED [Silva 2019], amplamente utilizado na avaliação

> 5https://forms.gle/whe4uqku8twMWY5c8

Figura 4. Visão geral do processo de avaliaç ão do PrograDuck.

de jogos educacionais. O formulário contemplava as seguintes dimensões: interface (IN), jogabilidade (JG), multimídia (MM), história do jogo (HJ), elementos educacionais (ED), conteúdo (CN) e agente educacional (AE).

### 6.2. Execução da Avaliação

Participaram da avaliação três professores da área de Computação, com experiência no ensino de programação. As sessões ocorreram presencialmente e individualmente, garantindo autonomia na inspeção do jogo, sem interferência dos demais. Como o jogo ainda se encontra em desenvolvimento, foi apresentada aos avaliadores a concepção inicial do jogo correspondente a cada fase, permitindo a análise da proposta geral de interação planejada, a partir de um protótipo funcional.

Antes da avaliação, os participantes seguiram dois procedimentos preliminares: (i) assinaram o Termo de Consentimento Livre e Esclarecido (TCLE) e preencheram o formulário de caracterização do perfil, usado para mapear sua experiência prévia com JEDs e ensino de programação; (b) participaram de um treinamento introdutório, no qual foram apresentados os conceitos fundamentais do JED e os princípios da AH.

Durante a execução, os avaliadores registraram problemas em cada heurística, classificando-os conforme os níveis de severidade recomendados por Nielsen (1995). Isso permite mapear tanto problemas leves (como inconsistências estéticas) quanto graves e catastróficos que impactam diretamente a usabilidade e a experiência do jogador.

### 6.3. Resultados da Avaliação

A Tabela 2 apresenta os problemas identificados na AH do PrograDuck classificados com severidade 3. A primeira coluna apresenta os IDs das heurísticas AHJED utilizadas para identificar os problemas, a segunda coluna (S) registra os graus de severidade, a terceira coluna descreve o problema encontrado, a quarta coluna propõe soluções potenciais, e a quinta coluna indica a porcentagem de avaliadores que relataram cada ocorrência.

Os resultados evidenciam limitações na experiência do usuário, especialmente relacionadas à autonomia do jogador, à adaptação ao desempenho e ao acompanhamento do

progresso. Esses aspectos indicam oportunidades de aprimoramento no uso do JED como ferramenta educacional, particularmente no que se refere à personalização da aprendizagem e ao apoio ao processo de ensino. Nesse sentido, destacam-se como prioritárias intervenções como a inclusão de níveis de dificuldade, a adaptação ao desempenho do jogador e a geração de relatórios de progresso, que ampliam o suporte ao professor e o uso do jogo em contextos educacionais. Dessa forma, os resultados fornecem subsídios concretos para o refinamento do PrograDuck, orientando sua evolução e aplicação futura.

Tabela 2. Resultado da Avaliaç ão Heurística do PrograDuck

|ID|S|Descrição do Problema|Possível Solução|%|
|---|---|---|---|---|
|IN-9|3|O jogo não oferece informações de ajuda ou documentação acessíveis ao usuário.|Adicionar um menu de ajuda com tutoriais ou dicas contextuais.|33,33|
|ED-2|3|O jogo não permite que o usuário exerça autonomia sobre seu processo de aprendizagem.|Adicionar opções de escolha de conteúdo ou da ordem de aprendizagem.|33,33|
|ED-3|3|O jogo apresenta apenas um nível de aprendizagem fixo.|Implementar múltiplos níveis de dificuldade ou modos de jogo diferenciados.|66,66|
|ED-5|3|O jogador não pode escolher o nível de dificuldade.|Adicionar seleção de dificuldade no menu inicial.|66,66|
|ED-6|3|O jogo não se adapta ao desempenho do jogador.|Implementar dificuldade dinâmica ou mecanismos de aprendizagem adaptativa.|66,66|
|ED-7|3|O instrutor não pode personalizar as atividades ou os desafios.|Criar um painel para instrutores com ferramentas de personalização.|33,33|
|ED-8|3|O jogo não apresenta relatórios ou históricos de desempenho.|Gerar relatórios detalhados e histórico das atividades realizadas.|66,66|

## 7. Considerações Finais e Trabalhos Futuros

Como contribuição, este artigo apresenta: (i) o desenvolvimento de uma ferramenta educacional digital, no formato de JED, voltada ao ensino introdutório de lógica de programação, com foco no engajamento e no despertar do interesse de meninas do Ensino Médio pela Computação; (ii) um processo de concepção orientado por dados do públicoalvo; e (iii) uma AH que identifica limitações e orienta a evolução da ferramenta.

O PrograDuck apresenta potencial como ferramenta educacional digital ao apoiar a aprendizagem por experimentação, integrando narrativa, desafios progressivos e uma estética acolhedora, concebida para reduzir barreiras de entrada e favorecer a identificação de meninas com a área de Computação. Atualmente, a ferramenta encontra-se com sua estrutura principal consolidada, incluindo narrativa, sistema de blocos e mecanismos de feedback, estando em andamento o refinamento de funcionalidades relacionadas à progressão, suporte ao jogador e testes de usabilidade.

Como continuidade, o trabalho encontra-se em fase de aplicação em contextos educacionais reais, para avaliar seu impacto na aprendizagem de programação, bem como no interesse, engajamento e percepção de pertencimento das estudantes em relação à Computação. Assim, PrograDuck se posiciona como uma ferramenta educacional digital no formato de jogo, voltada à introdução à programação e à ampliação da participação feminina na área, contribuindo para práticas mais inclusivas na Educação em Computação.

## Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial foram utilizadas exclusivamente para apoio editorial. O ChatGPT auxiliou na revisão linguística do texto, o Grammarly em ajustes pontuais de gramática e estilo, e o Gemini no apoio à elaboração de figuras. Todas as decisões de pesquisa, métodos, análises e interpretações foram realizadas integralmente pelos autores, sem influência dessas ferramentas no conteúdo científico ou nas conclusões do trabalho.
