# O Moodle de Lovelace e a Interpretação Surda no Ensino e na Aprendizagem do Pensamento Computacional

Márcia Gonçalves de Oliveira, Soraya Roberta dos Santos Medeiros, Ana Carla Kruger Leite, Clara Marques Bodart, Cibelle Amorim Martins

- 1 Centro de Referência em Formação e Educação a Distância (Cefor) Instituto Federal do Espírito Santo (Ifes) - Vitória - ES

2Universidade Federal do Rio Grande do Norte (UFRN) - Natal - RN

marcia.oliveira@ifes.edu.br, soraya.roberta.js@gmail.com

Abstract. Lovelace’s Moodle is a set of hybrid courses in Computational Thinking, Programming and Robotics that aims to provide initial training as a girls call for computing careers. As this call extends to deaf girls, we developed the Computational Thinking course of Lovelace’s Moodle in Libras with video lessons interpreted by a deaf teacher and with Vlibras tool. Through this proposal of hybrid teaching with the inclusion of deaf people, we report the experience of teaching Computational Thinking of a deaf interpreter and a learning experience of a deaf student who, in Libras, creatively expresses her computational thinking in solving a problem. These experiences show how deaf people can become interested in computing if they are initiated in Computational Thinking and encouraged to develop it freely and creatively.

Resumo. O Moodle de Lovelace é um conjunto de cursos híbridos de Pensamento Computacional, Programação e Robótica que tem como objetivo dar uma formação inicial como chamada de meninas para as carreiras de computação. Como essa chamada se estende às meninas surdas, desenvolvemos o curso de Pensamento Computacional do Moodle de Lovelace com videoaulas interpretadas por uma professora surda e com conteúdos traduzidos para Libras através da ferramenta Vlibras. Com essa proposta de ensino híbrido com a inclusão de surdas, relatamos a experiência de ensino de Pensamento Computacional de uma intérprete surda e uma experiência de aprendizagem de uma estudante surda que, em Libras, expressa de forma criativa o seu pensamento computacional na resolução de um problema. Essas experiências mostram como os surdos podem se interessar pela computação se forem iniciados no Pensamento Computacional e incentivados a desenvolvê-lo de forma livre e criativa.

## 1. Introdução

O Pensamento Computacional (PC) é um conceito iniciado por Seymour Papert na década de 80 em seu livro Mindstorms [Seymour 1980]. À época, o autor enfatizava a criação do Construcionismo, corrente teórica baseada no Construtivismo e no Sociointeracionismo, propondo o aluno como centro do processo de aprendizagem, com o pensamento crítico e com total domínio sobre a elaboração de ações em ambientes como os de programação.

Em 2006, Jeannet Wing traz às discussões científicas essa conceituação de Papert descrevendo o PC como uma habilidade para resolver problemas que deve ser ensinada

às crianças ainda na Educação Básica, visto que é tão importante quanto aprender conceitos aritméticos, de escrita e leitura de textos, pois o ser humano irá utilizá-la ao longo de sua vida [Wing 2006]. Além disso, aborda que o PC compartilha características do pensamento matemático, do pensamento científico e da engenharia [Wing 2008].

Complementando Papert e Wing, o trabalho de [Csizmadia et al. 2015] destaca a apresentação de tópicos como Pensamento Algoritmico, Abstração, Decomposição, Reconhecimento de Padrões e Evolução presentes no PC, que, junto com outros estudos, são sintetizados e descritos em [Brackmann 2017] como os quatro pilares do Pensamento Computacional: Abstração, Decomposição, Reconhecimento de Padrões e Algoritmos.

Nesse contexto, segundo o trabalho de revisão de [Bordini et al. 2016], observa-se que, no Brasil, a aplicação do PC em atividades de sala de aula começou a ser discutida a partir de 2010. Assim, ao longo desses dez anos, houve uma ampliação dessas discussões em eventos de Educação na Computação, tal como o Workshop de Ensino em Pensamento Computacional, Algoritmos e Programação (WAlgProg), a menção do PC na nova Base Nacional Comum Curricular(BNNC) e a elaboração de documentos pela Sociedade Brasileira de Computação (SBC) para a inclusão da Computação na Educação Básica, o que demonstra a relevância desse conhecimento para a ciência e para a sociedade.

Considerando tal relevância, este trabalho chama a atenção para a necessidade de se ensinar o PC não apenas de forma aplicada e integrada a conteúdos do currículo da Educação Básica, mas também na perspectiva de popularizar o ensino do PC tornando-o acessível a diferentes grupos sociais.

Com essa perspectiva, desenvolvemos o curso híbrido Moodle de Lovelace do Pensamento computacional que consiste em um curso a distância com momentos presenciais e que possui uma abordagem introdutória à Ciência da Computação destinada às mulheres das perifierias capixabas e acessível a pessoas surdas.

O Moodle de Lovelace do Pensamento Computacional tem como objetivo ensinar conceitos, técnicas e práticas de resolução de problemas do PC que podem ser aplicadas em outras áreas do conhecimento abrangendo públicos além da Educação Básica e considerando especificidades de gênero e de acessibilidade. Além disso, esse curso dá um passo à frente ao incluir mulheres surdas no ensino de PC.

## 2. Revisão de Literatura

Ao analisar os trabalhos publicados nos eventos de computação nos últimos anos, observa-se o surgimento de discussões sobre a inclusão de surdos na área de computação [Boscarioli et al. 2015, Oliveira et al. 2018a]. Como exemplo mais recente, tem-se o estudo de [Oliveira et al. 2019], em que se criou um espaço online através do Moodle de Lovelace [Oliveira et al. 2018b] com momentos presenciais para ensinar uma estudante surda a programar em Linguagem Python.

Nesse estudo, relatou-se a experiência dessa estudante surda nas oficinas presenciais antes e durante a execução de uma nova turma do curso online Moodle de Lovelace de Programação [Oliveira et al. 2019]. Como resultados, observou-se um progresso nessa inserção, mas também a necessidade de alguém para guiar a estudante surda na compreensão da programação, uma vez que a língua portuguesa ainda é uma dificuldade para

> 1WalgProg: http://walgprog.gp.utfpr.edu.br/

surdos e os intérpretes são necessários. Além disso, existem especificidades que a EaD ainda não proporciona e que representam um desafio para a inclusão de surdos.

Em outros eventos como o Congresso Brasileiro de Informática na Educação (CBIE), em 2019, percebeu-se uma discussão sobre a criação de ferramentas para se trabalhar com computação em sala de aula acessível para surdos. Como exemplo, tem-se o trabalho de [Teran et al. 2019], que relata o desenvolvimento de uma ferramenta para auxiliar alunos surdos da Educação Básica no ensino de lógica. Como resultados, além da ferramenta desenvolvida, [Teran et al. 2019] mostram que os surdos conseguiram aprender novas palavras e os ouvintes aprenderam sinais em LIBRAS.

Na base do Institute of Electrical and Electronic Engineers (IEEE), destaca-se o estudo de [Nascimento et al. 2017], que apresenta a JAD() como uma ferramenta para depuração de códigos. Nesse estudo, os autores fazem uma comparação entre alunos surdos e ouvintes. Para tanto, adotam métricas que apontam como resultados a inexistência de diferenças significativas nas tarefas realizadas por essas duas classes de alunos indicando progressos dos alunos surdos e a construção de valores inclusivos dos ouvintes.

Em relação ao ensino de computação para surdos e à produção de materiais para esse público com finalidade de formação profissional, destacamos o trabalho de [Gonçalves et al. 2015]. Esse estudo apresentou os resultados obtidos no Projeto de Capacitação Profissional e teve como ênfase a produção de videoaulas com estruturação e produção de conteúdos sistematizadas e acessíveis para surdos [Gonçalves et al. 2015].

Este trabalho se aproxima de [Gonçalves et al. 2015] por desenvolver videoaulas acessíveis e por apresentar soluções que favoreçam a formação profissional de surdos que, neste trabalho, se destina a uma formação inicial em ensino. Também se aproxima de [Oliveira et al. 2019] por propor o ensino híbrido para formação de estudantes surdas. Por outro lado, diferencia-se de [Teran et al. 2019] e de [Nascimento et al. 2017] porque faz uso de ferramentas já desenvolvidas como o Moodle e o Vlibras.

Concluindo, embora a inclusão de mulheres em TI com deficiência auditiva venha sendo destaque em eventos de computação, as pesquisas ainda são restritas a poucos projetos, o que evidencia a necessidade de se pensar e divulgar mais tais práticas.

## 3. O Moodle de Lovelace do Pensamento Computacional

O Moodle de Lovelace do Pensamento Computacional é um curso híbrido e acessível de introdução à computação que tem como objetivo ensinar conceitos, técnicas e práticas de resolução de problemas do PC que podem ser aplicadas para solucionar problemas do mundo real.

O curso foi executado em cinco escolas de periferias do estado do Espírito Santo com carga horária de 20 horas, sendo que seis horas foram utilizadas para aulas presenciais (três horas em cada semana e em cada escola) para atendimento às alunas e discussão das atividades da semana. As outras 14 horas foram desenvolvidas no ambiente virtual de aprendizagem Moodle através do estudo e discussão dos conteúdos e da prática de resolução de desafios aplicando técnicas do PC.

Para alcançar o objetivo de introduzir o PC em uma chamada de mulheres das periferias, incluindo mulheres surdas, para as carreiras de computação, o Moodle de Lovelace do Pensamento Computacional reúne os seguintes objetivos específicos:

- Organizar os conteúdos e atividades a partir das habilidades do Pensamento Computacional: decomposição, abstração, reconhecimento de padrões e algoritmo.

- Desenvolver videoaulas acessíveis a surdos

- Promover a discussão dos conteúdos com exemplos e atividades simples.

- Propor atividades criativas para desenvolvimento das habilidades do PC.

- Desenvolver as habilidades de compreensão, análise e construção de algoritmos contextualizados a problemas do mundo real.

- Promover o trabalho colaborativo dos alunos para construção de novos conhecimentos para as novas turmas do curso.

Visando alcançar esses objetivos, o Moodle de Lovelace do Pensamento Computacional é organizado a partir de uma metodologia meta-ativa de aprendizagem em que os conteúdos são apresentados e as atividades são propostas a partir dos próprios conceitos-chave do curso mapeados nas habilidades do PC [Brackmann 2017]: Decomposição, Abstração, Reconhecimento de Padrões e o Algoritmo.

Dessa forma, em uma estratégia simples e inclusiva de formação de mulheres para a computação, o projeto do curso Moodle de Lovelace do Pensamento Computacional se organiza em quatro blocos: Introdução, Espaço Interativo, Aulas-Fóruns de Pensamento Computacional e Desafios do Pensamento Computacional.

A parte de Introdução apresenta os conceitos do PC, os professores, os informes do curso em fórum atualizado pelo professor ao longo do curso e o material da aula inaugural, que é presencial. Além da aula inaugural, em cada semana, há uma aula presencial dos tutores para esclarecimento de dúvidas, discussão de conteúdos e prática do PC.

No Espaço Interativo, os alunos têm a oportunidade de se apresentarem de forma a se conhecerem melhor para compartilharem ideias e experiências.

As Aulas-Fóruns são estruturas que apresentam conteúdos e ampliam o conhecimento sobre um assunto através de discussões e reflexões. Cada aula-fórum contém uma videoaula de apresentação interpretada em Libras, um exemplo de problema do mundo real e um exercício contextualizado resolvido. A Figura 1 apresenta essa organização das Aulas-fóruns do curso a partir das habilidades do PC.

As videoaulas têm curta duração e são interpretadas por uma professora surda, que já foi aluna do Moodle de Lovelace. A ideia de chamar uma pessoa surda para interpretar as aulas do PC se justifica em favorecer uma melhor comunicação dos conteúdos de surdo para surdo. Este curso é relevante também por criar oportunidades de formação de surdos para o Ensino de Computação, começando pelo PC.

Os conteúdos das Aulas-fóruns também são muito curtos e possuem ilustrações que favorecem o entendimento dos conceitos do PC. A Figura 2, por exemplo, ilustra o conceito de Decomposição fazendo a decomposição do problema de fazer um café em Entrada, Processamento e Saída.

Após a apresentação de uma videoaula com interpretação surda e do resumo do conceito e sua aplicação, os alunos foram convidados a discutirem e a refletirem sobre a aplicação dos conceitos do PC contextualizados, por exemplo, ao funcionamento de um caixa de supermercados e da urna eleitoral eletrônica, Já os Desafios reúnem atividades para criar sequências lógicas, reconhecer padrões de soluções, interpretar enunciados de problemas como também para analisar e criar algoritmos para resolução de problemas

Figura 1. Aulas-fóruns do Moodle de Lovelace do Pensamento Computacional

Figura 2. Decomposição do Problema de Fazer um Café

do mundo real. A proposta de aplicar esses tipos de atividades é desenvolver as habilidades de compreensão, de sequenciação, de reflexão e de construção de algoritmos para que alunos, antes de iniciarem as etapas de programação, aprendam a compreender com clareza o problema, a pensar como as soluções automatizadas funcionam e a representar essas soluções em instruções de algoritmos.

Além das videoaulas interpretadas em Libras, utilizamos o recurso VLibras, que já é incluído na plataforma de cursos abertos do Centro de Referência em Formação e Educação a Distância (Cefor) do Instituto Federal do Espírito Santo. No entanto, é importante

destacar que, segundo opiniões de pessoas surdas da instituição que oferta o Moodle de Lovelace, elas preferem a comunicação via intérprete a aplicativos de tradução automática para Libras. Isso porque esse aplicativo não possui um glossário amplo, o que o faz produzir uma tradução pelo alfabeto datilológico. Dessa forma, o recurso de tradução automática para Libras é utilizado apenas como um auxílio para traduzir os conteúdos não interpretados. Valorizamos, portanto, a comunicação de surdo para surdo para melhor ambientação de surdos ao curso.

Na próxima seção, relatamos a experiência da professora surda em participar na interpretação em Libras das videoaulas das Aulas-fóruns do curso de PC e a experiência de uma estudante surda que acompanhou e participou dessas aulas interpretadas pela professora surda.

## 4. A Expressão do Pensamento Computacional na Interpretação Surda

O relato de experiência a ser apresentado é uma resposta às dificuldades dos surdos em aprender programação ao lidarem com três linguagens (Língua Portuguesa, linguagem de programação e LIBRAS) [Oliveira et al. 2019] e representa um apelo para que mais ações de inclusão de surdos na computação sejam desenvolvidas.

Considerando essas dificuldades dos surdos, este trabalho destaca como podemos ajudá-los em sua aprendizagem a partir do desenvolvimento das habilidades do Pensamento Computacional e incentivando-os a expressarem livremente como entendem a aplicação dos conceitos de computação.

Para isso, entendendo que se aprende melhor ensinando, convidamos uma estudante surda do curso de programação Python do Moodle de Lovelace para atuar como professora e intérprete de Libras das videoaulas de PC do Moodle de Lovelace de Pensamento Computacional.

O que mais chamou a atenção da professora coordenadora do curso foi o interesse, a dedicação e o encantamento com os quais a professora surda estudou os textos dos scripts das videoaulas. Para ela, não era só um trabalho de tradução do que já estava escrito, mas sim um trabalho de estudo aprofundado da terminologia para ajudar os surdos a entenderem o PC. O resultado desse esforço aparece na expressividade e entusiasmo da professora surda em comunicar o PC para a comunidade surda, conforme exemplo da videoaula de Algoritmo da Figura 3, em que aparecem, respectivamente, a professora coordenadora do curso e a professora surda interpretando a aula em Libras.

Durante o período em que a professora surda se preparava para interpretar as videoaulas do PC, comemorava-se o Ada Lovelace’s day e, por iniciativa própria, a professora surda criou o sinal em Libras para representar Ada Lovelace e o explicou em uma videoaula associando-o à organização dos cabelos de Ada Lovelace e a uma coroa caracterizando a sua nobreza e o projeto Corte de Lovelace.

Nas palavras da professora surda, a interpretação dos scripts das videoaulas, envolveu um trabalho de estudo, análise e reflexão da terminologia. Segundo ela, a contextualização de todas as terminologias de cada sinal em Libras para o curso que antes ela

> 2Youtube:https://bit.ly/2Vx2Xvz

> 3Sinal em Libras da Ada Lovelace: https://bit.ly/2NF5SOt

> 4Projeto Corte de Lovelace; http://meninas.sbc.org.br/portfolio/corte-de-lovelace/

Figura 3. Videoaula de Algoritmo

não achava e nem entendia, tornou-se possível por meio de pesquisas e detalhes, de modo a contextualizar a interpretação dela para surdos e ouvintes do curso entenderem.

Considerando esse relato, analisamos como foi a participação de uma estudante surda em duas Aulas-fóruns em que havia videoaulas interpretadas pela professora surda.

Na Aula-fórum 1, referente ao conceito Decomposição do PC, após a explicação dos conceitos de Entrada, Processamento e Saída na videoaula, aplicaram-se três perguntas: a) O que a máquina precisa receber para fazer a receita, isto é, o que você precisa fornecer para ela?; b) o que será feito automaticamente pela máquina (ações)? e c) o que a máquina deverá entregar pronto? Prontamente a estudante respondeu, respectivamente: a) colocar água e pó na máquina; b) A máquina ferve água, e depois passa o café: esse processo é automático da máquina e c) Entrega à pessoa o café pronto.

Em seguida, foram realizadas as seguintes perguntas: Qual o problema que dá quando você inverte a ordem das instruções ao explicar uma receita para uma pessoa ou para uma máquina? O resultado será o mesmo? Por quê? Ela respondeu: Dessa forma não funciona, porque bagunça os procedimentos e o café fica grosso e ruim. Precisa organizar primeiro a entrada para colocar água e café. No processamento, deixa a máquina misturando os elementos até ferver. E para finalizar, se entrega o café pronto à pessoa, e assim fica mais gostoso.

Observamos que nessa atividade, em que é mais simples, a resposta da estudante surda mostra que ela compreendeu corretamente os conceitos de entrada, processamento e saída e os contextualizou bem nos procedimentos de preparo de um café.

Na Aula-fórum 2, após a apresentação das videoaulas associadas aos conceitos de Abstração e Reconhecimento de Padrões do PC, foram levantadas as seguintes questões para discussão: Em um jogo de computador, como você se movimenta por um cenário? O que você acha que tem a ver com Abstração? ii) Um padrão em muitos jogos de tabuleiro é o arrastar-e-soltar uma peça. Mas você já reparou que muitas regras de jogos têm condições desse jeito: Se (condição) faça isso, senão, faça outra coisa. Dê um exemplo de regra de qualquer jogo que siga esse padrão.

Em resposta a essas atividades, a estudante surda produziu dois videos bem criativos para explicar os conceitos Abstração e Reconhecimento de Padrões do PC através dos jogos (que também possuem a versão digital) UNO e Damas, respectivamente.

No video disponível do Youtube, em que a estudante surda explica em Libras as regras do jogo do UNO, em resposta à pergunta da atividade i, ela associa as possibilidades de jogo de uma pessoa ao conceito de Abstração do PC. No entendimento dela, ter a mesma cor, o mesmo número da carta ou uma carta coringa (quando não se tem uma carta de mesma cor ou mesmo número para jogar), representam uma jogada possível para não perder. Nesse caso, ela abstrai em uma expressão lógica ligada com operadores lógicos OU, que é verdadeira quando uma dessas sentenças é verdadeira.

Na videoaula da Figura 4, a estudante surda, em resposta à pergunta da atividade ii tenta associar os conceitos Reconhecimento de Padrões e os padrões se...senão aos movimentos das peças no Jogo de Damas. Segundo ela, há um trabalho de análise nas jogadas que tem a ver com a lógica, uma vez que o jogador precisar avaliar possibilidades de jogo para avançar ou não uma peça para uma posição do tabuleiro.

Nessa análise de possibilidades, ela envolve condicionais e tomadas de decisões sem fazer menção diretamente à estrutura condicional se...senão. Nesse ponto, partindo de como ela expressou seu entendimento, o professor poderia levá-la a construir sequências lógicas e estruturas se...entao para as jogadas e condicionais do jogo por ela apresentadas. Dessa forma, se conduziria naturalmente o processo de aprendizagem dela para iniciação ao desenvolvimento de algoritmos.

A professora surda, ao ver a estudante surda demonstrando a percepção dela ilustrando o PC com um jogo de tabuleiro, conclui que isso é resultado de todo o apoio do trabalho de interpretação e da equipe do curso que apóia com didática os surdos para que isso abra a mente do surdo. Para ela, só esse esforço já é uma defesa para o ensino do PC.

Observamos que tanto a professora surda quanto a estudante surda têm uma certa preocupação e um notável entusiasmo de compreenderem bem e de explicarem bem os conteúdos. Por isso, destacamos a importância de se ter uma atenção especial na preparação de materiais e atividades para a aprendizagem de surdos.

Recomendamos, dessa forma, que os materiais de ensino de computação para surdos tenham muita clareza, simplicidade, boa comunicação visual, excelência na interpretação em LIBRAS, contextualização com o mundo real e atividades que favoreçam a livre expressão dos surdos para que estes melhor compreendam seus caminhos de aprendizagem e avancem em seus conhecimentos de computação.

Concluimos, portanto, que podemos favorecer o desenvolvimento dos surdos nos processos de ensino e de aprendizagem de computação dando-lhes a oportunidade de expressarem livremente como eles compreendem as informações que recebem e, a partir daí, iniciar um processo de intervenção e regulação no caminho de aprendizagem deles.

> 5Youtube: https://bit.ly/3dLOiD8; Áudio de tradução: https://bit.ly/2NJPWdC

> 6Como jogar UNO: https://www.jogos360.com.br/como_jogar_uno

> 7Youtube: https://bit.ly/31t7nqZ; Áudio de Tradução: https://bit.ly/31sTB7Z

Figura 4. Análise do PC no Jogo de Damas

## 5. Considerações finais

Este trabalho apresentou uma pesquisa que vem sendo desenvolvida no ensino de PC com a inclusão de meninas surdas. Mostramos nessa pesquisa a experiência da atuação de uma professora surda na interpretação de Libras nas videoaulas de PC do Moodle de Lovelace do Pensamento Computacional e a experiência de uma estudante surda na compreensão e na aplicação dos conceitos do PC ensinados nessas videoaulas.

Embora as meninas surdas ainda apresentem muitas dificuldades na programação, essas experiências esclarecem-nos como o ensino de PC pode contribuir para introduzir pessoas surdas na programação e como, possibilitando-lhes a livre expressão de como compreendem e aplicam os conceitos do PC, podemos promover mais avanços delas na aprendizagem de computação.

Como trabalhos futuros a partir deste apontamos o desenvolvimento de mais estudos sobre o trabalho de interpretação em Libras e sobre estratégias que facilitam a compreensão dos surdos com o objetivo de reproduzir esses conhecimentos em tradutores automáticos de Libras de forma que ofereçam maior qualidade de tradução e tenham maior aceitação na comunidade surda.

Concluimos, portanto, que podemos favorecer o desenvolvimento dos surdos nos processos de ensino e aprendizagem de computação dando-lhes a oportunidade de expressarem livremente como eles compreendem as informações que recebem e, a partir daí, iniciar um processo de intervenção e regulação no caminho de aprendizagem deles. Com isso, contribuimos para abrir mais possibilidades de inclusão de surdos na computação e na Educação em Computação.

## 6. Agradecimentos

Agradecemos à Fundação de Amparo à Pesquisa e Inovação do Espírito Santo (FAPES) e ao Programa Agenda Mulher da Vice-governadoria do Estado do Espírito Santo, apoiadores do Projeto CORTE DE LOVELACE - RESOLUÇÃO N 244/2019, através do qual foi desenvolvida a pesquisa deste trabalho.
