# A primeira Maratona Feminina de Programação do Brasil: motivações para o desenvolvimento do projeto e relatos da primeira edição do evento

Jasmine B. Nunes, Larissa G. de S. Escaliante, Letícia L. M. da Silva, Luísa de Melo B. Penze

1Instituto de Computação – Universidade Estadual de Campinas (UNICAMP) Campinas – SP – Brasil

`{j247181,l219788,l184423,l238001}dac.unicamp.br`

Abstract. Studies on the participation of women in the Brazilian Programming Marathon point to the scarce representation of the female public in the competition. This article discusses the importance of creating projects that encourage women’s engagement in competitive programming activities, and presents the development of the Women's Programming Marathon project, created by a group of students from Unicamp.

Resumo. Estudos sobre a participação do público feminino na Maratona de Programação brasileira apontam para a escassa representatividade de mulheres na competição em questão. Este artigo discute a importância da criação de projetos que visem ao incentivo do engajamento feminino nas atividades de programação competitiva, além de apresentar o desenvolvimento do projeto da Maratona Feminina de Programação, voltado para a promoção de tal incentivo, criado por um grupo de alunas da Unicamp.

## 1. Introdução

Programação Competitiva é um esporte cerebral que envolve a resolução de problemas lógicos e matemáticos por meio de códigos computacionais durante um limite de tempo. A prática constante de tal atividade estimula o desenvolvimento de habilidades pessoais importantes como: raciocínio lógico, organização de ideias, rapidez em enxergar possíveis soluções para problemas do cotidiano, dentre outros. Além disso, atualmente, renomadas empresas de tecnologia compõem suas entrevistas de emprego com questões muito semelhantes àquelas praticadas por programadores competitivos. Assim, esse esporte pode, também, ajudar o competidor a se destacar durante o processo seletivo de grandes empresas tecnológicas. A competição de programação mais antiga é a ICPC, International Collegiate Programming Contest, criada na década de 1970 e que, atualmente, conta com aplicação em 88 países.

No Brasil, atualmente, as competições de programação mais conhecidas são a OBI (Olimpíada Brasileira de Informática) e a Maratona de Programação, realizada pela Sociedade Brasileira da Computação. A organização da Olimpíada Brasileira de Informática está a cargo do Instituto de Computação da Universidade Estadual de Campinas. Podem participar desta competição estudantes do Ensino Fundamental, do Ensino Médio e do primeiro ano de Graduação. A Maratona SBC de Programação existe desde 1996 e teve sua origem pautada nas competições regionais classificatórias para a participação de estudantes nas finais mundiais do concurso ICPC.

A Maratona SBC é destinada a estudantes que cursam graduação ou início de pós-graduação na área de Computação (ou em áreas de estudo semelhantes) e é organizada em três fases: sub-regional, nacional e mundial. Tal competição apresenta como principais objetivos o desenvolvimento da criatividade dos estudantes, a melhoria na capacidade de trabalhar em equipe, a promoção da busca por novas soluções de software e o fortalecimento da habilidade de resolver problemas sob pressão. Na competição, os estudantes devem se organizar em times de três participantes para resolver 10 (ou mais) problemas, em um limite de tempo de 5 horas, utilizando apenas um computador. Dessa forma, exige-se organização por parte do grupo em relação à distribuição de tarefas e ao revezamento na utilização do dispositivo. O time recebe um balão para cada questão resolvida durante o tempo de prova, como forma de incentivo e de estímulo à competição.

Dados das últimas edições da Maratona de programação da SBC (Figura 1) apontam para uma escassa representatividade feminina em tal atividade. Nota-se que [IRION, 2023], desde 2011 até 2022, o índice de mulheres que participaram da fase sub-regional da Maratona oscilou entre 8,42% e 15,20%, apenas.

Figura 1. Desigualdade de gênero na participação da fase sub-regional da Maratona SBC de Programação.

Uma variedade de estudos a respeito da baixa representatividade feminina em atividades de programação já foram publicados e discutidos. Dentre as causas mais discutidas para tal fenômeno, está o estereótipo social. Em [SILVEIRA, 2023], discute-se que o afastamento das mulheres de cursos e de atividades de programação deve-se principalmente aos estereótipos adotados pela sociedade de que mulheres não devem se interessar por computadores. Além disso, como apresentado no artigo mencionado, desde o período escolar, as mulheres são pouco estimuladas a desenvolverem interesse pela área de exatas como um todo.

Diante de tal cenário de escassa participação feminina nas competições de programação, a organização da Maratona de Programação tomou algumas medidas para incentivar mulheres a desenvolverem interesse por essa atividade.

Uma dessas medidas é a Escola de Verão, um treinamento, de duas semanas de duração, destinado a competidores da Maratona SBC de Programação. É realizada pela SBC e organizada pelo Instituto de Computação da UNICAMP. Na edição de 2020 da Escola de Verão, algumas participantes mulheres receberam auxílio para transporte e suporte financeiro para estadia durante o período do evento. Além disso, todas foram isentas da taxa de inscrição do evento,

Ainda, o Comitê Diretor da Maratona de Programação aprovou, dentre outras, a seguinte mudança nas regras do evento a partir de 2023: vagas extras para os melhores times femininos na final brasileira. Consta do edital do evento [SBC, 2022] a seguinte nova regra: “6 vagas para equipes com participação feminina: 3 vagas para os times com 3 mulheres melhor colocados; 2 vagas para os times mais bem colocados com pelo menos 2 mulheres; 1 vaga para o time melhor colocado com participação feminina.”

Notando a urgência de desenvolver projetos para incentivar o engajamento feminino na programação competitiva, com inspiração nas medidas tomadas pela SBC neste sentido, um grupo de alunas da Unicamp fundou a primeira Maratona Feminina de Programação brasileira em 2023. A MFP surgiu como uma iniciativa para ampliar a participação de mulheres e pessoas não-binárias na área da computação, especialmente no ensino superior. Assim, com o apoio da Unicamp, do Instituto de Computação e de empresas patrocinadoras, o evento foi realizado no dia 24 de junho de 2023.

## 2. Metodologia

A Maratona Feminina de Programação surgiu com o objetivo principal de fazer com que o cenário competitivo brasileiro tivesse uma participação maior do público feminino e não-binário. Dessa forma, o evento teve como base algumas metas principais:

a) estimular a participação feminina e não-binária na programação competitiva;

b) incentivar o interesse pela computação entre o público feminino e não-binário;

c) ampliar a participação feminina e não-binária na Maratona SBC de Programação;

d) proporcionar um ambiente mais inclusivo e diverso na área das ciências exatas, em geral;

e) estimular o raciocínio lógico a partir de desafios computacionais;

f) expandir a prática da programação competitiva pelo país.

### 2.1. Divulgação e Redes Sociais

A principal forma de divulgação utilizada pelo evento foi a rede social Instagram, por ser acessível e largamente utilizada. Nela, foram publicados diversos conteúdos, como: explicação sobre a maratona de programação, guias de estudo, apresentação da equipe de organização, entre outras informações. Além disso, o Instagram constituiu o meio mais comum de contato por parte das participantes, sendo um portal para tirar dúvidas do evento. Outras formas de divulgação utilizadas ocorreram presencialmente — por meio de iniciativas realizadas em algumas universidades —, pelo e-mail do evento — para comunicados importantes às pessoas inscritas — e pelo Whatsapp — através do

1 O grupo de alunas corresponde às autoras do presente artigo.

envio de mensagens em grupos de diferentes universidades do país. Por fim, o evento também contou com o apoio de influenciadores digitais da área da computação, de comunidades femininas de programação e da Maratona SBC de Programação, que divulgaram o evento em suas redes sociais. Todas essas iniciativas garantiram que o evento chegasse ao conhecimento de pessoas de todo o país.

### 2.2. Guias e Treinamentos

Com o objetivo de estimular, de maneira acessível, o aprendizado na área de programação competitiva e, dessa forma, incentivar resultados melhores nas competições, a Maratona Feminina de Programação criou guias de estudo contendo materiais, fontes de exercícios práticos, principais tópicos cobrados nas provas e linguagens de programação comumente utilizadas. A ideia do guia foi democratizar o acesso à informação e oferecer direcionamentos a quem estivesse estudando de forma autônoma para a prova.

Paralelamente, foram convidadas duas mulheres brasileiras que obtiveram destaque na programação competitiva para ministrarem aulas preparatórias para a prova. As aulas foram oferecidas no formato online, na plataforma Google Meet, em 20 de maio de 2023. Para compreender a demanda do público em relação ao nível de dificuldade do conteúdo das aulas, disponibilizou-se um formulário de inscrição avaliando o nível de experiência em programação de cada participante, entre as categorias iniciante, intermediária e avançada. Por meio de análise das respostas obtidas, concluiu-se que o mais adequado seria a oferta de duas modalidades de aula: uma de nível iniciante e outra de nível intermediário; dada a baixa demanda por uma turma de nível avançado. A convidada que ministrou a aula da turma iniciante foi Estela Batista, enquanto a aula da turma intermediária foi ministrada pela convidada Giovanna Kobus.

### 2.3. Organização financeira

Para a organização das finanças da MFP, foi criado um setor de coordenação financeira para lidar com as pendências dos gastos relacionados ao evento. Dentre as tarefas estabelecidas para o funcionamento deste setor, são as principais:

a) planejamento de orçamento, incluindo gastos essenciais para o evento acontecer;

b) elaboração de uma carta-patrocínio, contendo todas as informações interessantes para as empresas, os valores e os benefícios de patrocinar o evento;

c) criação de uma planilha de controle de gastos, com a receita total e o valor ainda disponível para utilização no evento.

Os recursos captados foram provenientes dos patrocínios contratados, além do saldo disponível na conta da Fundação de Desenvolvimento da Unicamp destinado aos gastos com eventos de uma entidade estudantil do Instituto de Computação, responsável pelos estudos em programação competitiva. Em 2023, contou-se com 6 empresas

> 2 Aluna de mestrado na Universidade Federal de Viçosa. Foi maratonista e coach de maratonas de programação.

> 3 Primeiro lugar da maratona da América Latina em 2019.

patrocinadoras, sendo quatro na categoria Bronze, uma na Prata e uma na Ouro. Com isso, foi possível arcar com os principais gastos previstos.

Figura 2. Divisão de gastos da receita captada a partir dos patrocínios.

Além disso, a Comissão de Extensão do Instituto de Computação da Unicamp aprovou o custeio, por parte do instituto, da contratação do coffee break pela manhã e do rodízio de pizza à noite. Esse apoio institucional foi imprescindível para garantir às participantes e aos membros da organização uma alimentação gratuita e de qualidade durante todas as etapas do evento.

### 2.4. Auxílios

Um dos objetivos da Maratona Feminina de Programação é ser inclusiva para mulheres e pessoas não-binárias, independente da classe social, localização, instituição de ensino ou qualquer fator discriminatório. Na modalidade presencial da competição, existiu um obstáculo financeiro relacionado à necessidade de arcar com custos de locomoção, hospedagem e alimentação, impactando principalmente pessoas residentes de locais distantes de Campinas. Dessa forma, a Maratona Feminina teve como uma de suas metas prover auxílio financeiro para algumas participantes. No formulário de inscrição, foi adicionado um campo onde as inscritas indicaram se precisariam de auxílio para participar do evento. Devido à alta demanda, a organização do evento precisou elencar alguns critérios para selecionar as pessoas beneficiárias:

a) foram selecionadas as 5 instituições de ensino com mais inscritas na categoria "preciso de auxílio financeiro";

b) de cada uma dessas instituições, foi selecionada uma estudante com base na experiência prévia com programação competitiva (indicada no formulário de inscrição) e no período atual da graduação (estudantes mais próximas de se formar tiveram prioridade);

O auxílio cobriu despesas com transporte e acomodações, limitando-se a mil reais por participante. Além disso, algumas competidoras receberam auxílio das próprias universidades para comparecerem ao evento, iniciativa que demonstra compromisso dessas instituições com as ideologias de incentivo à participação feminina do evento [MORESCO, 2023]

### 2.5. Abertura, Palestras e Cerimônia de premiação

> 4 As categorias de patrocínio da edição de 2023 do evento foram determinadas pelo valor de patrocínio (em reais) e pelos benefícios cedidos à empresa patrocinadora.

Além da prova, o evento contou com uma programação pautada em oferecer inspiração, networking e oportunidades profissionais às participantes (Figura 3). O evento começou com uma cerimônia de abertura, seguida por uma palestra que abordou desafios no mercado de trabalho para mulheres, realizada por uma das empresas patrocinadoras. O evento também contou com uma palestra de Letícia Freire, finalista mundial da ICPC, que apresentou dicas de como se preparar para competições de programação. Após a aplicação da prova, o evento foi finalizado com uma cerimônia de premiação, acompanhada de um rodízio de pizza com a proposta de ser um momento de descontração e de conexão entre participantes de diferentes localidades.

Figura 3. Fotos registradas no dia do evento, incluindo a palestra do patrocinador ouro, a aplicação da prova, as organizadoras e todos os participantes do evento no seu encerramento.

### 2.6. Prova e Mirror Contest

A prova da MFP consistiu em uma lista de 10 problemas de programação, com duração total de 4 horas. Observou-se a necessidade de considerar a falta de experiência com programação competitiva indicada pelas participantes no formulário de inscrição (Figura 4) para a elaboração da prova.

Figura 4. Gráfico que relaciona as inscrições para o evento com o grau de familiaridade das inscritas com programação competitiva.

Uma das principais estratégias para tal demanda consistiu em determinar a estrutura da prova com base no nível de dificuldade dos problemas. Visando garantir

que a maior parte das participantes acertassem ao menos uma questão - de modo que finalizassem a prova motivadas e satisfeitas -, foi determinada uma estrutura de 5 questões fáceis, 3 médias e 2 difíceis.

Outra medida tomada durante a preparação do evento, visando à proposta de um ambiente acolhedor - principalmente a participantes com pouco contato com programação -, foi a adoção de instruções comentadas por monitores minutos antes do início da prova. Dentre as instruções dadas, estão inclusas: tutorial sobre como submeter as soluções das questões na plataforma utilizada ( Codeforces ) e sugestões de e tutoriais para aplicativos de desenvolvimento de software, nos quais as participantes poderiam escrever e testar seus códigos. Simultaneamente ao evento presencial, houve uma competição-espelho ( Mirror Contest ) da MFP, destinada exclusivamente ao público que não esteve presencialmente na competição. A competição-espelho foi independente do evento presencial, tendo premiações distintas para os primeiros lugares. A premiação do evento presencial foi dividida em duas categorias diferentes: iniciante e geral, sendo premiadas 18 participantes no total (9 medalhas para cada categoria). Com tal medida, buscou-se incentivar competidoras que tinham pouca ou nenhuma familiaridade com competições de programação e que obtiveram um desempenho expressivo na prova.

## 3. Resultados e Discussões

### 3.1. Inscrições e processo de seleção

Em 2023, a MFP contou com cerca de 280 inscrições, um número expressivo para a 1ª edição do evento. Com isso, uma vez que não seria possível a alocação de todas as inscritas no Instituto de Computação da Unicamp, foi feita uma seleção das pessoas que participariam do evento presencialmente. Aqui, destaca-se a importância do Mirror Contest supracitado como uma alternativa para participantes não-selecionadas realizarem a prova de forma remota.

No que tange ao processo seletivo, os principais aspectos levados em questão, em ordem decrescente de prioridade, foram os seguintes: organização interna da universidade, experiência com programação competitiva, maior período de graduação e ordem de inscrição para o evento. Em relação à organização interna da universidade, o processo consistiu em uma seleção interna para vagas com ou sem auxílio. Caso a universidade desejasse realizar tal seleção interna para o limite de vagas oferecido, esta deveria entrar em contato com a organização do evento para alinhar as questões de auxílio. Caso contrário, o processo seletivo seguiria os demais critérios mencionados acima. O edital de seleção, o qual explicava detalhadamente os critérios seletivos e os prazos estabelecidos, foi divulgado nas redes sociais oficiais do evento. Com isso, a Maratona Feminina de Programação contou com três chamadas, sendo realizadas até que o número limite de participantes previsto fosse atingido.

> 5 As qualificações “fácil”, “médio” e “difícil” foram determinadas de acordo com o grau de complexidade dos algoritmos envolvidos na resolução dos problemas, bem como com a experiência necessária para sua implementação.

> 6 Codeforces é uma plataforma online que oferece competições de programação, treinamento e prática de algoritmos e estruturas de dados, sendo popular entre programadores competitivos.

### 3.2. Regiões de abrangência

Dentre as maratonistas, foi evidente o predomínio de estudantes da região sudeste, especialmente do estado de São Paulo, o que corresponde a 68,1% do público da competição (Figura 5). Esses dados evidenciam uma grande disparidade em relação à abrangência da MFP, visto que um só estado compôs a maior parte do gráfico de maratonistas. Apesar dos esforços para fornecer auxílio às participantes que residiam em cidades distantes do polo de aplicação da competição, os valores destinados à ajuda de custo foram suficientes apenas para 5 participantes selecionadas, fato que se tornou um obstáculo para o objetivo de expandir a programação competitiva para o público feminino a nível nacional. Foi possível constatar, através do formulário de inscrição, que grande parte das candidatas não podia arcar com os custos de transporte e estadia que seriam necessários para comparecer ao evento.

a) b)

#### Figura 5. a) Gráfico que relaciona o número de participantes por universidade brasileira. b) Gráfico que relaciona a porcentagem de participantes por unidade federativa brasileira.

Apesar disso, com 113 participantes no total, a MFP abrangeu 8 estados brasileiros, com participantes de 16 universidades. Das 9 medalhistas do ranking geral, 5 residiam fora do estado de São Paulo, com representantes da região Norte, Sul e Centro-Oeste. Isto demonstra a importância de continuar desenvolvendo projetos que garantam oportunidades e incentivos a estudantes de programação por todo o país, de modo a dar espaços a novas maratonistas, incentivar o estudo de computação entre o público feminino a nível nacional e tornar este universo mais democrático.

### 3.3. Nível de dificuldade da competição

Uma análise do ranking geral da competição revela que cerca de 84% das competidoras resolveram pelo menos um problema (Figura 6). Este percentual demonstra uma das conquistas do evento, tendo em vista o objetivo de que a maioria das participantes finalizasse a prova com ao menos um balão. Além disso, considerando que a maioria das competidoras não tinha experiência com competições de programação, a prova se demonstrou como um desafio possível até mesmo para o público iniciante.

Figura 6. Relação entre o número de questões resolvidas e participantes.

Com base na análise do gráfico da Figura 6, estabeleceu-se para as próximas edições do evento uma melhor estruturação de dificuldade das questões da prova, pautada na adoção de uma progressão mais gradual entre as exigências dos desafios. Tal medida busca cumprir o objetivo da MFP de encorajar as participantes a continuarem com os estudos de programação, independentemente do nível.

### 3.4. Depoimentos positivos

Muitas participantes dependeram de auxílio financeiro para atender ao evento e demonstraram agradecimento pela oportunidade: “Quando recebi a bolsa para participar presencialmente foi uma alegria enorme. O evento foi um desafio, já que foi a primeira vez que participei individualmente. Os problemas envolviam lógica de programação e conhecimentos sobre algoritmos e estrutura de dados. Mas, foi muito divertido, fiquei muito contente com meu resultado.” - depoimento de graduanda em Engenharia de Computação. Seguindo a dinâmica proposta pela Maratona SBC de Programação, a MFP contou com a atribuição de balões que representavam as questões resolvidas por cada participante. Tal ação motivou as competidoras e resultou em retornos positivos: “Gostei bastante de ser chamada para participar, nunca tinha participado realmente de uma maratona competitiva de programação! Foi incrível e era emocionante receber balões:) Mandaram muito bem!! Obrigada.” - depoimento anônimo. Uma das metas propostas pelo evento foi a maior interação entre mulheres e pessoas não-binárias que se interessam pela área de computação, principalmente no que tange à programação competitiva. O atingimento deste objetivo foi extremamente gratificante para a organização da MFP e pode ser ilustrado pelo depoimento anônimo: “Muito obrigada por fazerem este momento acontecer! Foi incrível encontrar mais mulheres nas maratonas de programação!”.

### 3.5. Aumento do número de mulheres na Maratona SBC de Programação

Em setembro de 2023, a SBC publicou em seu site oficial uma notícia com a seguinte chamada: “Com mais participação feminina, Maratona SBC de Programação realiza final nacional em outubro, na cidade de Chapecó (SC)” [OLIVEIRA, 2018]. No conteúdo da notícia, consta que, na edição do evento de 2023, a Maratona SBC de Programação atingiu a inscrição recorde de 48 equipes compostas totalmente por meninas, 46 equipes com duas meninas e 129 equipes com uma menina. Tal notícia é

extremamente relevante dentro do cenário de precária participação feminina nas competições de programação e pode ser um reflexo do incentivo ao estudo de programação entre o público feminino, proporcionado tanto por eventos como a Maratona Feminina, quanto por iniciativas tomadas pela SBC em relação à introdução das vagas femininas na fase nacional da Maratona SBC de Programação.

### 3.6. Integração com a SBC

As ideologias em comum entre a Sociedade Brasileira de Computação e a Maratona Feminina de Programação, em conjunto com os resultados alcançados a partir da primeira edição do evento feminino, acarretaram a integração da MFP com a SBC. Tal parceria confere maior dimensão e credibilidade ao evento, bem como garante uma estrutura de apoio mais fortificada. A partir de 2024, a Maratona Feminina de Programação é um evento realizado pela SBC.

### 3.7. Projetos inspirados pela Maratona Feminina de Programação

Com a popularidade crescente da Maratona Feminina de Programação e de seus ideais, algumas universidades se demonstraram sensibilizadas com a iniciativa e se engajaram no desenvolvimento de projetos que incentivassem a participação feminina nas competições de programação. Neste sentido, pode-se destacar a Competição feminina de programação liderada por alunas do ensino superior em Brasília e o evento “ Monkeys Contest - Girls Edition ” realizado em Goiás. Ambas as competições foram abertas para alunas de todas as universidades brasileiras. É importante ressaltar, em relação à competição em Goiás, que sua realização se deu anteriormente à primeira edição da MFP e contou com a seguinte regra em seu regulamento: “As 3 melhores colocadas da universidade terão a viagem custeada para representar nossa instituição em Campinas - SP no dia 24/06” [UFG, 2023]; o que indica que a MFP contribuiu diretamente para o surgimento de uma nova equipe para a Maratona SBC de Programação.

### 3.8. Influência da MFP na formação de novas equipes femininas

A premiação da categoria iniciante da MFP contou com isenção de taxa de inscrição de uma equipe, por premiada, para a Maratona SBC de Programação, contribuindo diretamente para a formação de equipes inéditas femininas - uma vez que contaram com participantes iniciantes (i.e., que nunca participaram de competições de programação).

## 4. Conclusão

Infelizmente, a participação das mulheres e pessoas não-binárias em competições de programação permanece baixa, o que significa que ainda se deve investir em projetos - já existentes ou em ascensão - que visem à mudança deste cenário. Por outro lado, diante da alta demanda de inscrições para a Maratona Feminina de Programação, dos retornos positivos de participantes e dos resultados conquistados com a primeira edição do evento, pode-se concluir que o projeto foi muito bem-sucedido e que tende a alcançar cada vez mais suas metas. Por fim, ressalta-se que este projeto é uma das várias iniciativas existentes e necessárias para que o público feminino ocupe cada vez mais a área de computação e para desconstruir os estereótipos sociais fortificados no país que causam a escassez de mulheres na tecnologia.

## Agradecimentos

Agradecemos ao Instituto de Computação pelo apoio dado à realização do evento. Em destaque, gostaríamos de agradecer aos seguintes professores do Instituto de Computação: Fábio Usberti, Rafael Schouery, Flávia Luciane Consoni. Além disso, demonstramos agradecimento pelos alunos da Unicamp, membros da entidade de programação competitiva MaratonIC, e pelos voluntários, membros da equipe de organização do evento. Em especial agradecemos ao graduando em Engenharia da Computação na Unicamp, Raphael Kitahara, pela elaboração da identidade visual do evento. Por fim, agradecemos ao Carlos Eduardo Ferreira, diretor de competições científicas da Sociedade Brasileira de Computação, pelo apoio e pela disposição em relação à Maratona Feminina.
