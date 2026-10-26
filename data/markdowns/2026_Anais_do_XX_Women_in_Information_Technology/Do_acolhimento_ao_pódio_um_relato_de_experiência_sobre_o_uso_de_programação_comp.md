# Do acolhimento ao pódio: um relato de experiência sobre o uso de programação competitiva como estratégia para empoderar mulheres na área de computação

Letícia Cristina A. da Silva, Estela Miranda Batista, Thais Regina de M. B. Silva e Gláucia Braga e Silva

1Universidade Federal de Viçosa (UFV) Florestal – MG – Brasil

{ leticia.c.silva, estela.batista, thais.braga, glaucia } @ufv.br

Abstract. Recent studies demonstrate the existence of female underrepresentation in competitive programming competitions, a space traditionally associated with learning and empowerment for students in the field of Computer Science. In recent years, several initiatives have sought to develop mechanisms to mitigate this issue. This paper presents the trajectory, over a period of 10 years, of one such group, contributing with a critical analysis of its competitive and methodological evolution, as well as its role as a student support environment, also discussing the results achieved throughout its implementation.

Resumo. Pesquisas recentes comprovam a existência de uma subrepresentação feminina em competições de programação competitiva, um espaço tradicional de aprendizado e empoderamento para alunos da área de computação. Algumas iniciativas desenvolvidas nos últimos anos têm buscado mecanismos para mitigar esta questão. Este artigo apresenta a trajetória, ao longo de um período de 10 anos, de um grupo como este, trazendo como contribuição uma análise crítica de sua evolução competitiva, metodológica e como espaço de acolhimento estudantil, discutindo também os resultados alcançados ao longo de sua implementação.

## 1. Introdução

As maratonas de programação, historicamente se destacam como importantes ambientes de formação para estudantes de computação. Essas competições propõem que equipes resolvam problemas computacionais em um tempo limitado, estimulando habilidades como raciocínio lógico, criatividade, trabalho em equipe e tomada de decisão sob pressão [Lima et al. 2021]. Tais iniciativas são frequentemente utilizadas como forma de proporcionar aos estudantes oportunidades de desenvolvimento de competências técnicas e autoconfiança, permitindo que os mesmos vivenciem experiências colaborativas relevantes para sua formação acadêmica e inserção no mercado de trabalho.

No Brasil, destacam-se iniciativas como a Olimpíada Brasileira de Informática (OBI), a Maratona de Programação da Sociedade Brasileira de Computação (SBC) e maratonas estaduais. Nos últimos anos, surgiram também competições voltadas

> 1https://olimpiada.ic.unicamp.br/

> 2https://maratona.sbc.org.br/

à participação feminina, como a Maratona Feminina de Programação (MFP) e a Competição Feminina da OBI (CF-OBI), que buscam ampliar o engajamento de mulheres nesses ambientes.

Apesar do potencial formativo dessas competições, a participação feminina nas maratonas de programação ainda é significativamente inferior à masculina. Estudos indicam que, mesmo com avanços recentes, a presença de mulheres permanece baixa tanto nas competições do ensino superior quanto nas etapas anteriores da formação acadêmica [Irion et al. 2023, Silva et al. 2024]. Para além do baixo número de mulheres frequentando cursos da área de computação [Irion et al. 2024], outros fatores associados a esse cenário são a menor exposição prévia à programação, a presença de estereótipos relacionados às habilidades das mulheres na área de tecnologia e a falta de ambientes de treinamento que promovam acolhimento e incentivo à participação feminina [Irion et al. 2024]. Esse é um cenário que traz prejuízo para as estudantes, uma vez que elas acabam não utilizando as competições como espaço de engajamento e oportunidade para se fortalecerem tecnicamente. Além disso, cabe ressaltar que forma-se um ciclo vicioso, uma vez que a ausência de mulheres desestimula a adesão de outras.

Diante desse contexto, torna-se relevante o desenvolvimento de iniciativas que incentivam a participação feminina em maratonas de programação por meio de estratégias de formação técnica, apoio coletivo e construção de ambientes mais inclusivos. Nesse sentido, este trabalho apresenta a trajetória e as metodologias adotadas pelo BOTz, um grupo de estudos em programação competitiva vinculado ao programa de extensão universitária MinasCoders, voltado ao incentivo da participação feminina na área. O estudo configura-se como um relato de experiência sob uma perspectiva crítica, no qual são discutidos o histórico, as metodologias adotadas, os resultados obtidos e as lições aprendidas ao longo do processo. O trabalho contribui para a literatura ao apresentar reflexões sobre o caminho para a consolidação de um grupo voltado à programação competitiva feminina em um contexto ainda marcado por desafios relacionados à equidade de gênero.

O restante do texto está organizado da seguinte forma: a Seção 2 apresenta uma visão geral do estado da arte sobre o tema; a Seção 3 descreve a evolução do programa de extensão e do grupo de estudos; a Seção 4 discute os resultados alcançados, bem como as lições aprendidas ao longo da experiência; as considerações finais e perspectivas para trabalhos futuros são apresentadas na Seção 5.

## 2. Trabalhos Relacionados

Os autores em [Holanda et al. 2025] apresentam uma iniciativa da Universidade de Brasília (UnB) voltada à ampliação da participação feminina em competições de programação, por meio de treinamentos, formação de equipes e simulados. O estudo, de abordagem quantitativa e qualitativa, aponta que a iniciativa contribuiu para aumentar a motivação e o engajamento, evidenciando o potencial de grupos de estudo.

O estudo de [Hartmann et al. 2025] apresenta a iniciativa Turma Lovelace, da Universidade Federal da Fronteira Sul (UFFS), voltada ao ensino de programação competitiva para mulheres e pessoas não binárias. A metodologia inclui aulas teórico-práticas

> 3https://mfp.ic.unicamp.br/

> 4https://olimpiada.ic.unicamp.br/info/competicao ~~f~~ eminina/

> 5https://minascoders.caf.ufv.br/

semanais e ensino de C++. A avaliação qualitativa aponta impactos positivos no desenvolvimento de lógica, trabalho em equipe, além de maior motivação e autoconfiança.

No trabalho de [da Silva et al. 2025], descreve-se um estudo no Instituto Federal do Amazonas (IFAM) voltado à criação de espaços de formação e apoio que buscam não apenas desenvolver habilidades técnicas, mas também fortalecer o pertencimento. O projeto teve duração de quatro meses, com atividades de treinamento, incentivo à participação em competições e momentos de interação. O estudo, de abordagem qualitativa, indica que ações que combinam capacitação técnica com estratégias de construção de comunidade podem ampliar o engajamento de mulheres em competições.

Os pesquisadores [Souza et al. 2025] apresentam uma proposta voltada à utilização da programação competitiva como ferramenta de aprendizagem e engajamento, sem trabalhar um recorte de gênero. A iniciativa incentiva estudantes não apenas a resolver problemas algorítmicos, mas também a produzir materiais educacionais relacionados às soluções, como explicações e conteúdos de apoio. Essa estratégia busca fortalecer o aprendizado ativo e colaborativo, ao mesmo tempo em que amplia o repertório disponível.

Nesse contexto, o presente trabalho dialoga com outras iniciativas de incentivo à participação feminina em maratonas de programação, mas apresenta diferenças importantes. O grupo adota uma abordagem inclusiva, envolvendo também estudantes homens, e prioriza o desenvolvimento da lógica e da resolução de problemas, em vez do ensino de linguagens específicas. Além disso, diferencia-se por incorporar uma avaliação quantitativa, em contraste com abordagens exclusivamente qualitativas presentes na literatura.

## 3. BOTz: uma história

O programa de extensão universitária MinasCoders, vinculado à UFV - campus Florestal, foi fundado em 2017 com o objetivo de incentivar o ingresso e a permanência de mulheres e pessoas não-binárias na área da Computação. Para isso, o programa atualmente desenvolve ações voltadas a participantes de diferentes idades e níveis de ensino, incluindo ensino fundamental, médio, técnico e graduação. O MinasCoders atua em diferentes frentes, sendo subdividido em quatro grupos principais:

- HighSchoolMinas: voltado à participação em competições de empreendedorismo e inovação com alunas da educação básica;

- Codeloures: destinado ao acolhimento das novas alunas da graduação, oferecendo apoio nos primeiros passos na universidade e na disciplina de programação;

- FullStackMinas: direcionado ao aprendizado de tecnologias utilizadas no mercado e à participação em competições de inovação, com o objetivo de ampliar o pensamento crítico e técnico;

- BOTz: foco principal do presente trabalho, é o grupo mais antigo do programa, voltado ao estudo e à prática de programação competitiva, buscando fortalecer a aprendizagem sobre algoritmos.

Embora voltado ao acolhimento feminino, desde o seu início o MinasCoders também absorveu estudantes do sexo masculino, buscando torná-los parte do processo de conscientização. No entanto, como forma de manter o ambiente do grupo o mais seguro possível para mulheres, algumas regras foram seguidas ao longo do tempo, dentre elas a manutenção do número de mulheres sempre igual ou superior ao dos homens e a priorização de meninas para a participação em maratonas e competições.

É importante destacar que o MinasCoders iniciou suas atividades por meio do BOTz, fazendo deste o único grupo de atuação contínua ao longo de um período de 10 anos. Neste intervalo, muitas situações foram vivenciadas e estratégias testadas tanto com o objetivo de melhorar a efetividade do grupo na atração, fixação, motivação e ascensão de meninas na área de computação, como também para alavancar a participação e os resultados, principalmente femininos, em competições de programação. Neste trabalho, buscamos compartilhar este relato de experiência sobre a história e o funcionamento do BOTz, apresentando resultados quantitativos e lições aprendidas, de maneira a inspirar e colaborar com outros grupos que desejam seguir pelo mesmo caminho.

Com o objetivo de melhor apresentar a trajetória do BOTz, foi realizada uma segmentação histórica de sua existência, organizada em fases evolutivas, apresentadas na Figura 1. Cada fase busca evidenciar mudanças estruturais, metodológicas e estratégicas ao longo do tempo.

Figura 1. Evoluç ão e organizaç ão temporal do subgrupo

### 3.1. Fase 1: implantação e mobilização

Na Fase 1, o MinasCoders funcionava exclusivamente por meio do BOTz, com foco em fomentar a participação de meninas na programação competitiva e apoiá-las no desenvolvimento acadêmico. A divulgação e captação de participantes eram prioridades, resultando na participação de 10 pessoas, sendo 40% mulheres, no primeiro ano. Nessa etapa, contemplava estudantes do ensino superior em Ciência da Computação e do ensino médio técnico em Informática.

Os encontros eram estruturados predominantemente no formato de oficinas, nas quais eram abordados diferentes conteúdos conforme as demandas dos estudantes, como programação em blocos e uso do GitHub. Destaca-se que, desde o início, o grupo contou com a atuação de lideranças femininas na condução das atividades, de forma intencional, buscando promover representatividade e oferecer referências próximas às participantes. Com coordenação de professores e execução por alunas selecionadas, essa dinâmica incentivava a participação ativa e contribuía para a construção de um ambiente mais acolhedor e representativo. Além disso, favoreceu não apenas a formação acadêmica e técnica, mas também o fortalecimento da confiança das participantes.

Ainda nessa fase, em 2018, o grupo iniciou sua participação em competições de programação, sendo responsável por levar a primeira equipe totalmente feminina para a Maratona de Programação do Estado Minas Gerais (Figura 2(a)). Esse acontecimento representou um marco não apenas para o grupo, mas também para a própria competição,

evidenciando o impacto de iniciativas voltadas à ampliação da participação feminina em ambientes tradicionalmente masculinizados. A partir dessas experiências, o grupo passou a direcionar maior atenção à programação competitiva como ferramenta de aprendizado e incentivo à permanência das meninas na área, consolidando um modelo inicial de treinamento baseado na combinação entre discussões teóricas e atividades práticas individuais.

(a) 1ª equipe feminina na maratona esta(b) 1ª edição da maratona feminina estadual dual

Figura 2. Marcos na trajetória do grupo

Posteriormente, como parte do processo de amadurecimento, foi criada em 2019 a maratona interna do grupo, com o objetivo simular os ambientes de maratonas por meio de uma competição realizada na plataforma Beecrowd. Utilizando exercícios antigos das competições oficiais, o grupo passou a se organizar em trios e a ter um tempo determinado para resolver os desafios propostos. Vale ressaltar que esse modelo de competição ainda é utilizado, contando com mais de 180 questões aplicadas até 2025.

### 3.2. Fase 2: consolidação e expansão

Já na segunda fase, o MinasCoders apresentou uma participação mais ativa dos estudantes, alcançando cerca de 30 integrantes, sendo 12 meninas, o que evidenciou tanto o crescimento do grupo quanto o desafio de ampliar a participação feminina.

Esse período também foi marcado por um evento de grande impacto social: a pandemia do coronavírus, que afetou significativamente as dinâmicas educacionais no país [Santos et al. 2021]. Diante desse cenário, o grupo precisou adaptar suas estratégias para manter a continuidade das atividades e o engajamento de seus participantes. As reuniões passaram a ocorrer integralmente em formato remoto, sendo realizadas tanto de maneira síncrona quanto assíncrona. Durante esse período, o grupo promoveu treinamentos voltados à programação competitiva e ao apoio às disciplinas do curso, abordando conteúdos como grafos, programação dinâmica e matemática. Além disso, foram realizados encontros de integração, com jogos e sessões de filmes em ambiente virtual, com o objetivo de preservar o vínculo entre os estudantes e contribuir para o bem-estar coletivo.

Posteriormente, com a retomada das atividades presenciais, iniciou-se um processo de reestruturação interna do grupo. Nesse momento, tornou-se necessário revisar as estratégias de captação implementadas nos anos iniciais, bem como desenvolver novas ações voltadas à permanência e ao engajamento. Como parte desse processo, consolidouse um novo formato de encontros semanais, com duração de duas horas, organizados

> 6https://judge.beecrowd.com/pt

em diferentes momentos de aprendizagem. As atividades passaram a alternar entre estudos teóricos, apresentação de minicursos ministrados por estudantes mais experientes e realização de maratonas internas de programação, buscando fortalecer o aprendizado e a participação ativa dos integrantes.

Além disso, para preservar o objetivo central do grupo, definiu-se que a quantidade de homens não deveria ultrapassar a de meninas e pessoas não binárias, garantindo um ambiente mais acolhedor. Ainda assim, houve dificuldades na atração e permanência das participantes, possivelmente relacionadas à insegurança frente às competições e à baixa representatividade no curso. Diante disso, intensificaram-se ações de acompanhamento, com maior atuação de professoras e alunas experientes, além de momentos de integração, com os demais grupos do projeto, para fortalecer o engajamento.

### 3.3. Fase 3: maturidade estratégica

Por fim, observa-se uma terceira fase marcada pela consolidação das atividades voltadas à atração e permanência de participantes alinhados ao objetivo do grupo. O inicio desse período, contou com 25 integrantes, dos quais 17 eram mulheres, evidenciando o fortalecimento das estratégias de participação feminina e maior estabilidade organizacional. Como evolução, estabeleceu-se que todas as equipes em competições deveriam contar com pelo menos uma menina, visando garantir protagonismo e incentivar sua permanência.

Em contraste com os primeiros anos, observa-se uma participação feminina mais expressiva, evidenciada, por exemplo, na primeira edição da maratona feminina estadual (Figura 2(b)), na qual a UFV foi a instituição com maior número de participantes, totalizando 22 não-homens (categoria que inclui mulheres cis, mulheres trans e pessoas nãobinárias), incluindo duas equipes medalhistas. O surgimento dessas competições contribuiu para o aumento do engajamento, ao oferecer um ambiente mais acolhedor, fortalecer a autoconfiança e incentivar a participação em outras competições, além de promover a troca de experiências entre meninas da área.

No momento atual, o grupo passa a direcionar esforços para a análise sistemática de seus próprios dados históricos, buscando compreender padrões de participação, engajamento e desempenho em competições. Esse movimento tem como objetivo orientar melhorias no processo de ensino e aprendizagem em programação competitiva, bem como fortalecer estratégias voltadas à atração, permanência e desenvolvimento de meninas, visando não apenas sua participação, mas também seu destaque em competições.

## 4. Resultados - Acolhendo meninas e subindo ao pódio!

### 4.1. Conjunto de Dados

Para subsidiar a análise histórica do grupo, foram utilizados dados obtidos por meio de entrevistas com antigas lideranças e da consulta a materiais institucionais, como registros de chamadas, listas de participantes e cronogramas. Vale salientar que todos os participantes são maiores de idade, e ao entrarem no programa consentem com o uso de imagem para materiais de divulgação do programa. A partir dessas informações, foi realizado um processo de organização e sistematização dos registros, resultando na construção de quatro conjuntos de dados.

Dois conjuntos de dados se referem às pessoas e a organização do grupo. O primeiro reúne informações sobre os participantes do grupo ao longo do tempo, permitindo identificar períodos de participação e características gerais dos integrantes. O segundo corresponde aos cronogramas dos encontros, contendo registros dos temas e conteúdos abordados nas atividades realizadas pelo grupo ao longo dos anos.

Além disso, foram organizados dois conjuntos de dados relacionados às competições de programação. O primeiro reúne informações sobre a participação do grupo em maratonas externas, incluindo dados sobre número de participantes e eventuais premiações obtidas. O segundo registra as maratonas internas realizadas no grupo, contendo informações sobre os problemas utilizados, seus temas e níveis de dificuldade.

A organização desses dados constitui um resultado relevante deste trabalho, uma vez que permitiu consolidar informações históricas que anteriormente se encontravam dispersas, viabilizando análises temporais. Por conseguinte, esse material foi utilizado como pilar para a construção das discussões apresentadas nas próximas subseções.

### 4.2. Atração e Fixação

Nesta seção serão apresentados resultados sobre o processo de atração e maturação do grupo. Para as análises foi utilizado o conjunto de dados sobre os participantes. Com isso, busca-se verificar se a iniciativa tem conseguido sustentar o vínculo para além da adesão inicial.

Com relação à evolução histórica da quantidade de participantes e do engajamento do BOTz, a Figura 3 apresenta o total de pessoas do grupo e de participantes não-homens. Observa-se que, durante o período pandêmico, houve redução na participação total, bem como na participação de não-homens. Contudo, no período pós-pandêmico, verificase crescimento contínuo da participação, indicando possível efetividade das políticas de reestruturação implementadas.

Figura 3. Evoluç ão do tamanho do grupo ao longo dos anos.

Vale ressaltar que os gráficos analisados a seguir foram construídos por meio de um ajuste de granularidade temporal, uma vez que, entre 2018 e 2019, os registros eram anuais, e desde de 2020, passaram a ser semestrais. Para garantir comparabilidade, todos os dados foram convertidos para anos, considerando-se a quantidade de participantes únicos na união dos semestres, quando aplicável.

20º Women In Information Technology (WIT 2026): Relatos de Experiência

Para analisar o padrão de permanência no grupo, foi construído um boxplot (Figura 4), que revela um padrão inicial semelhante entre homens e não-homens. A mediana para ambos os grupos situa-se próxima a um ano, com intervalo interquartil entre um e dois anos. Isso sugere que o grupo também funciona como um espaço de experimentação em maratonas de programação, ainda pouco exploradas na formação tradicional.

Ainda que os homens apresentem maior número de valores extremos, sugerindo um pequeno conjunto de casos com permanência significativamente prolongada, o padrão central da distribuição não aponta desvantagem estrutural de permanência para mulheres. Assim, observa-se que, no contexto atual do grupo, a retenção inicial e intermediária ocorre de forma relativamente equilibrada entre os gêneros, não indicando barreiras imediatas de entrada ou permanência nos primeiros anos.

Figura 4. Distribuiç ão da permanência por grupo de gênero no grupo.

Complementarmente, foi elaborado o gráfico apresentado na Figura 5(a), que evidencia a distribuição da quantidade de períodos de permanência por gênero. Observase concentração expressiva de participantes femininas e não binárias nas faixas de permanência entre um e três anos, indicando envolvimento que ultrapassa a adesão inicial. Esse achado é particularmente relevante em um campo historicamente marcado por baixa participação feminina, como é o caso das maratonas, sugerindo que o grupo de estudo tem conseguido sustentar não apenas a atração, mas também a retenção ao longo do tempo.

(a) Número de participantes por tempo de permanência e grupo de gênero.

(b) Anos de participação nas maratonas.

#### Figura 5. Indicadores de participaç ão do grupo.

Nesse sentido, a presença consistente dessas participantes em faixas intermediárias de permanência aponta para um ambiente de acolhimento e engajamento progressivamente mais estruturado. Esses resultados podem indicar que o grupo encontrou

um formato de funcionamento no qual as estratégias de retenção começam a produzir efeitos observáveis. Entretanto, é importante destacar a limitação referente ao período temporal ainda em curso, especialmente para os anos mais recentes, o que pode minimizar a permanência final nas faixas superiores.

### 4.3. Motivação e Ascensão

Uma vez evidenciado que o grupo vem atingindo seu objetivo de atrair e engajar meninas, esta seção tem como propósito analisar os resultados sob a perspectiva competitiva. Para além do número absoluto de premiações obtidas, busca-se compreender a evolução da participação nas maratonas e, especialmente, o comportamento da participação feminina ao longo dos anos, uma vez que, conforme discutido na literatura, o aumento da presença de mulheres em ambientes competitivos de programação representa, por si só, um avanço significativo para a área de computação.

A Figura 5(b) apresenta uma linha do tempo das competições das quais o grupo participou ao longo de sua trajetória. Observa-se participação recorrente em maratonas tradicionais, como as organizadas pela SBC e a maratona estadual, com presença constante nos últimos anos. Além disso, há participações pontuais em outras competições, importantes para a adaptação a diferentes ambientes, bem como adesão às iniciativas recentes voltadas exclusivamente para mulheres, evidenciando alinhamento com ações de incentivo à diversidade na área.

A Tabela 1 consolida, por ano, o total de participantes, o número de não-homens e a quantidade de premiações obtidas. A análise desses dados permite identificar três movimentos principais. Inicialmente, os primeiros anos são marcados por baixa incidência de premiações, característica esperada em fase de criação. Em seguida, depois de 2021, observa-se crescimento gradual no número de resultados positivos, com destaque para os anos mais recentes, nos quais há manutenção ou ampliação do número de premiações.

Tabela 1. Evoluç ão anual da participaç ão e premiaç ões do grupo

|Ano|Marat|ona Mineira SBC||Flisol||Maral|ol|Nacion|al|MFP||Minas|de Minas|Premiacões|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||Total|Não-Homens Total|Não-Homens|Total|Não-Homens|Total|Não-Homens|Total|Não-Homens|Total|Não-Homens|Total|Não-Homens|¸|
|2018|3|3 9|5|||||||||||0|
|2019||12|5|12|5|||||||||0|
|2020||30|14|||||3|0|||||1|
|2021||9|3|||6|3|3|0|||||3|
|2022|3|3 12|7|||||3|0|||||1|
|2023|9|5 15|9|||||||7|7|||4|
|2024|12|9 9|5|||||||5|5|||2|
|2025|9|4 12|7|||||||1|1|22|22|4|

No que se refere ao engajamento feminino, observa-se aumento consistente na proporção de não-homens nas equipes ao longo do tempo. Por fim, destaca-se que iniciativas externas, como a criação de maratonas exclusivamente femininas, parecem ter contribuído para fortalecer o engajamento e ampliar oportunidades. Os resultados indicam que tais iniciativas, combinadas com estratégias internas de formação e acompanhamento, potencializam não apenas a permanência, mas também o desenvolvimento técnico.

### 4.4. Discussão dos Resultados

A análise conjunta das subseções anteriores indica que o programa apresenta resultados consistentes tanto no eixo de atração e permanência, quanto no eixo competitivo, evidenciando um processo de amadurecimento estrutural do grupo. A partir dessa análise, destacam-se as seguintes observações:

- Ao longo da experiência do grupo, observou-se que o aumento do número de atividades nem sempre resulta em maior aprendizagem. Mais do que a quantidade, a escolha de atividades que estimulem diferentes aspectos do raciocínio lógico e da resolução de problemas mostrou-se fundamental, tornando importante manter o equilíbrio entre volume de prática e qualidade pedagógica das atividades.

- Embora a ampliação do número de participantes seja positiva, é importante equilibrar quantidade e qualidade, buscando atender estudantes com maior interesse na área, sem deixar de oferecer apoio àqueles que apresentam menor engajamento. Para tanto, a preparação da equipe organizadora é fundamental.

- O grupo de estudos atua como complemento às disciplinas do curso, ao possibilitar a aplicação prática de conteúdos abordados em aula. Logo, montar um cronograma que acompanhe os alunos no curso é uma estratégia interessante.

- A participação de estudantes do gênero masculino contribui para o fortalecimento do ambiente colaborativo e para a dinâmica do grupo, além de auxiliar na conscientização destes em relação ao desequilíbrio de gênero e desafios enfrentados por mulheres e minorias dentro da área de computação.

- A promoção de um ambiente em que os próprios alunos compartilham conhecimentos e auxiliam colegas mostra-se uma estratégia promissora para ampliar o engajamento do grupo. No BOTz, parte das atividades já é conduzida por estudantes mais experientes, favorecendo a troca entre pares. Ampliar essas oportunidades, incentivando mais participantes a explicar soluções e discutir estratégias, pode potencializar o aprendizado, uma vez que o ato de ensinar reforça a compreensão dos conteúdos.

- As competições funcionam como fator importante de motivação, mas também podem gerar frustração ou insegurança, o que demanda atenção pedagógica.

- As maratonas de programação simulam dinâmicas presentes no mercado de trabalho, como atuação sob pressão e trabalho em equipe [Ramos et al. 2025]. Assim, estratégias voltadas ao desenvolvimento da autoconfiança competitiva precisam estar mais presentes na formação dos estudantes.

## 5. Conclusões e Trabalhos Futuros

Este trabalho teve como objetivo apresentar e analisar a trajetória do grupo BOTz como iniciativa voltada à formação em programação competitiva, com foco na promoção da participação feminina. A análise histórica das atividades desenvolvidas, permitiu observar resultados relevantes tanto no eixo de atração quanto de permanência de alunos, além da consolidação gradual da participação em competições. Esses resultados evidenciam que a criação de um ambiente acolhedor, aliado à prática constante, contribui não apenas para o desenvolvimento técnico dos estudantes, mas também para o fortalecimento do sentimento de pertencimento e autoconfiança.

Nos próximos anos, pretende-se aprimorar a condução do BOTz por meio da incorporação das lições aprendidas ao longo de sua trajetória, bem como da exploração de novas abordagens metodológicas que fortaleçam o processo de ensino e aprendizagem em programação competitiva. Como trabalhos futuros deste relato de experiência, propõe-se ampliar a coleta e análise de dados sobre a participação e evolução dos estudantes ao longo do tempo, além de realizar uma análise qualitativa do grupo, com base em relatos e avaliações dos participantes, buscando compreender de forma mais aprofundada os impactos técnicos, motivacionais e competitivos das metodologias adotadas.

- 46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

 - 20º Women In Information Technology (WIT 2026): Relatos de Experiência

## Agradecimentos

Agradecimentos ao Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) - Brasil (Processo nº 440447/2024-0) pelo apoio e concessão de bolsas, e ao programa MinasCoders, pelo fomento a pesquisas sobre temáticas de gênero em Computação.

## Uso de Inteligência Artificial

Esse trabalho contou com o uso de Inteligência Artificial (IA) Generativa ChatGPT, para o auxílio da correção ortográfica e gramatical. O artigo foi elaborado e revisado integralmente pelas pessoas autoras, que assumem total responsabilidade pelo seu conteúdo.
