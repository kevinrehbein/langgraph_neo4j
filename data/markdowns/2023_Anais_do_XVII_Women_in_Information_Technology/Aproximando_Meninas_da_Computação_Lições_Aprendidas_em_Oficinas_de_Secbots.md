# Aproximando Meninas da Computação: Lições Aprendidas em Oficinas de Secbots

Luciana Salgado, Meirylene Avelino, Iris Herdy, Amara Santoyani, Mateus Monteiro

1Instituto de Computação – Universidade Federal Fluminense (UFF) 24.210-310, Niterói - RJ, Brasil

{ lucianasalgado, amarasantoyani, mateusmonteiro } @id.uff.br

{ meiryleneavelino, irishmpeixoto } @gmail.com

Abstract. This article reports lessons learned from Workshops offered by the Include Meninas UFF Project. These activities were focused on bringing practical knowledge about Information Security and Chatbot Design to the participants so that they associate the daily use of technologies, necessary and related knowledge to produce them, and assigned professions.

Resumo. Este artigo relata as lições aprendidas em oficinas sobre Conceitos da Computação oferecidas pelo Projeto Include Meninas UFF. O foco destas oficinas é levar conhecimento prático às participantes sobre segurança da informação e projeto de chatbots, de forma que associem o uso cotidiano de tecnologias, conhecimentos necessários e relacionados para produzi-las e profissões associadas.

## 1. Introdução

Dados recentes divulgados pela Associação das Empresas de TIC e de Tecnologias Digitais (Brasscom), indicam que ainda estamos longe da equidade de gênero no setor [Brasscom dade]. Embora as mulheres sejam 51% da população, elas ocupam 44% dos empregos formais e 39% dos cargos do Setor de TIC. Um olhar mais atento observando a distribuição dos cerca de 1,1 milhões de cargos no setor de TI, revelam que as mulheres são maioria em funções administrativas e minoria em funções de Pesquisa e Desenvolvimento (P&D), TIC e Engenharia, onde as mulheres ocupam apenas 20% destes postos.

Nessas condições, o estímulo desde a Educação Básica pode dar a meninas e mulheres oportunidades profissionais no futuro e de melhorar as condições de vida das suas famílias. O projeto Include Meninas UFF objetiva aproximar as alunas da Educação Básica da Computação e despertar o interesse e conhecimento das subáreas e possíveis profissões. De forma mais específica, o projeto atua de forma culturalmente informada [Salgado et al. 2023], dado que as realidades sócio-culturais das nossas crianças difere em cada região do Brasil. Alguns dos problemas regionais enfrentados pelo projeto, por exemplo, neste último ano, foi o de lidar com o desconhecimento e desinteresse quase total pela área da Computação que identificamos com as estudantes das Escolas Parceiras. Além disso, as escolas não possuem laboratórios de Informática ativos e nem oferecem disciplinas ou qualquer atividade de introdução ao tema.

Várias iniciativas têm como objetivo ensinar conceitos da área de tecnologia para a Educação Básica. Alguns trabalhos reportam iniciativas com foco nas pessoas docentes

[Hoger et al. 2022] e confirmam as vantagens da construção de oficinas com personagens que desconstruam estereótipos [Salgado et al. 2022]. O artigo [Moura et al. 2018], por exemplo, relata como as meninas sentiram mais vontade de aprender ao verem que existem figuras femininas importantes da área. Outros trabalhos buscam despertar interesse das meninas com letramento em programação [Bim et al. 2019] [Salinas 2021].

Este artigo relata as lições aprendidas e os impactos percebidos durante a aplicação de oficinas em escolas parceiras do projeto em 2022 sobre Conceitos da Computação relacionados à segurança da informação e o projeto de chatbots. O trabalho está organizado da seguinte forma: a próxima seção descreve os procedimentos da Oficina Secbots; a seção 4 relata detalhes da aplicação da oficina nas escolas parcerias. Finalmente, a seção final compartilha as lições aprendidas e perspectivas de trabalhos futuros.

Figura 1. Etapas da Oficina de SecBots

## 2. A Oficina Desplugada de SecBots

O objetivo da oficina (Figura 1) é o projeto da conversação humano-chatbot, em um contexto onde seja importante zelar pela segurança das informações compartilhadas, o qual nomeamos nesta trabalho de secbot. A oficina foi idealizada levando-se em consideração que as participantes são estudantes da Educação Básica sem experiência no projeto de tecnologias e que todas as etapas serão feitas de forma desplugada.

A preparação da oficina requer a adaptação da aula para o contexto das participantes e atualização dos exemplos para serem mais próximos da realidade das estudantes. Os seguintes materiais são necessários: cartolinas, papel adesivo, lápis, canetas coloridas e, um projetor para exibição do conteúdo didático. O local recomendado para aplicação da oficina é um espaço com mesas para trabalhos em grupos, mas pode ser aplicada em uma sala de aula tradicional. Todas as etapas devem ser guiadas e acompanhadas por uma ou duas pessoas facilitadoras com formação em Computação e conhecimentos teóricos de chatbot e segurança da informação.

A oficina começa (Etapa 1) com uma introdução ao tema, os objetivos do workshop e os conceitos fundamentais sobre chatbots e segurança da informação. Nesta etapa é dada a definição básica de um chatbot, a exemplificação da tecnologia com chatbots comumente conhecidos, como a Lu, da Magazine Luiza e explicações sobre como

> 1material de apoio: https://github.com/Include-Meninas-UFF/Oficina-de-SecBots

funciona um chatbot. A etapa também explica o que são dados e informações, motivos para se investir em segurança cibernética e abordou os pilares da segurança da informação: disponibilidade, integridade e confidencialidade. Finalmente essa etapa apresenta exemplos de rupturas da disponibilidade, integridade e confidencialidade.

A etapa (2) explica como esses conceitos se encaixam e como eles se relacionam com a atividade prática. A facilitadora explica que, que além de informativo, chatbots (assim como toda tecnologia) pode tomar medidas proativas para proteger as informações pessoais e financeiras das pessoas usuárias. O conceito sobre a importância de se pensar em segurança desde o início do projeto é compartilhado. Temas sobre engenharia de software, security by design e ciclo de desenvolvimento seguro são abordados de tal forma que as participantes tenham essa sensibilidade no processo de desenvolvimento de qualquer software, não somente de chatbots.

Após a introdução dos conceitos básicos, chegamos à etapa (3) ”mão na massa”. As participantes realizam uma atividade prática que lhes permitirá aplicar os conceitos aprendidos na segunda etapa. A facilitadora fornece instruções e orientações conforme necessário. Com processo similar ao visto em [Monteiro et al. 2020], neste momento da oficina as participantes são convidadas a formar grupos. O tamanho do grupo depende do número total de participantes e também do contexto do grupo, por exemplo, a faixa etária e se as pessoas estudam na mesma turma e/ou escola. No caso da oficina que realizamos os grupos tiveram em média 3 (três) pessoas. A etapa envolve as seguintes atividades: (a) definir o perfil da persona; (b) definir uma necessidade da persona; (c) usar os papéis adesivos para escrever as falas do diálogo entre o secbot e a pessoa usuária; e, (d) fazer as conexões entre as falas. A atividade (a) de definição da persona solicita que os grupos idealizem uma pequena história que relate o uso do secbot indicando as seguintes características: nome da pessoa usuária, idade, família, grau de instrução e conhecimento tecnológico da persona. A atividade (b) exige que a participante proponha uma situação de uso do secbot, apresentando o problema que a persona quer resolver e envolver alguma situação de fragilidade com dados pessoais. Com isso em mãos, as participantes constroem os diálogos do secbot nas atividades (c) e (d).

Na etapa (4), após a conclusão da atividade prática, as participantes apresentam o seu trabalho ao resto do grupo. Elas explicam o processo que seguiram, os desafios que enfrentaram e os resultados que alcançaram. Finalmente, na etapa (5) a oficina é concluída. A facilitadora convida as participantes a fazerem perguntas e compartilharem suas dúvidas e percepções. Adicionalmente, a facilitadora faz um resumo e responde a quaisquer perguntas que as participantes possam ter.

## 3. Aplicação da Oficina de SecBots nas Escolas Públicas

Foram realizadas 3 (três) oficinas, uma em cada escola parceira do projeto: Escola 1 (E1), Escola 2 (E2) e Escola 3 (E3), conforme Tabela 1. Todas as escolas são públicas, sendo E1 e E2 municipais e E3 estadual. Tais escolas se tornaram parceiras do projeto (anonimizado) em 2022. Todas as ações realizadas em 2022 foram programadas para serem frequentadas prioritariamente por meninas. O número de vagas para as atividades foram definidas pela professora parceira do projeto da escola, em função do tamanho do espaço e da proposta de atividade. Caso o número de alunas interessadas fosse menor que o número de vagas, os alunos interessados também poderiam preencher as vagas.

|id|Tipo|Faixa Etária|Alunas|Alunos|Total de Estudantes|Num SecBots|
|---|---|---|---|---|---|---|
|E1|Municipal|11-13|4|0|4|1|
|E2|Municipal|13-15|23|5|28|6|
|E3|Estadual|15-18|24|0|24|6|

Tabela 1 - Participantes

Figura 2. Exemplo de Secbots - imagem original e transcriç ão do diálogo

Ao todo participaram da oficina 56 (cinquenta e seis) pessoas, sendo 51 meninas e 5 meninos. 57,14% estudantes do Ensino Fundamental II e 42,86% estudantes do Ensino Médio. Conforme pode ser observado na Tabela 1, E1 teve apenas 4 estudantes. Isso se deve ao fato da escola ter passado por problemas locais (falta de merenda escolar), que ocasionaram baixa frequência na escola. Destas pessoas participantes, 50% nunca tinha participado ainda de uma oficina do nosso projeto, 18,8% participou de todas 5 ações (palestras ou oficinas) do projeto até a data desta oficina (setembro de 2022). E 31,2% já tinha participado de pelo menos 1 ação do projeto em 2022. Com relação à temática tratada na oficina de Secbots, 41,7% das pessoas participantes nunca tinha ouvido falar em chatbots; 35,4% já tinham ouvido falar, mas não sabiam do que se tratava; e, 22,9% já sabiam exatamente o que são chatbots.

A dinâmica da oficina seguiu conforme descrito na seção 3, portanto, os Secbots foram desenvolvidos em grupos. Entretanto, em função do espaço oferecido pela escola, do número de pessoas e grau de proximidade, a quantidade de pessoas por grupo foi variado. E1 teve apenas um grupo com as 4 alunas participantes. Os grupos formados na E2 e E3 tiveram entre 3 a 4 participantes. Os principais dados empíricos coletados nas oficinas foram os projetos desenvolvidos pelas pessoas participantes e as anotações realizadas pelas pesquisadoras durante as oficinas. Quanto aos projetos, ao todo foram gerados 13 (treze) secbots sobre temas completamente diferentes tais como: internet banking, aluguel de livros, agenda para consulta médica, e-commerce, assistente de compras, etc. As imagens de todos os projetos foram catalogadas e transcritas. A figura 2, por exemplo,

mostra o secbot desenvolvido na E1. O tema foi a tentativa de recuperação de senha e acesso a uma conta bancária.

A avaliação foi realizada por meio de um questionário de avaliação distribuído para todas as pessoas participantes das oficinas. Das 56 estudantes participantes, 48 responderam o questionário. O questionário possui 2 perguntas sobre o entendimento do conceitos de chatbots e 4 questões construídas a partir da escala Likert com uma afirmação auto descritiva. Os seguintes itens foram investigados: nível de dificuldade do conteúdo; interesse por continuar o desenvolvimento do secbot; nível de motivação durante a oficina; e, grau de satisfação geral.

Sobre o grau de facilidade ou dificuldade na criação dos chabots, 58,3% das pessoas participantes consideraram fácil ou muito fácil. Entretanto, um número expressivo de estudantes considerou a atividade com nível mediano de dificuldade e 4,2% considerou difícil. Esse fato indica a necessidade de termos monitores acompanhando a aplicação da oficina. Quanto ao interesse por continuar o desenvolvimento do sectbot iniciado na oficina, 87,5% estudantes gostariam muito de continuar o projeto. Já o nível de motivação das participantes durante a oficina também foi expressivo: 75% das participantes sentiram-se motivadas durante a oficina. O nível geral de satisfação das alunas também foi bem alto com 81,3% das participantes indicando que gostaram muito da oficina e 18,8% informando que gostaram.

## 4. Conclusões

A análise dos dados empíricos coletados e da avaliação realizada com as participantes indicam as seguintes lições aprendidas. Primeiro, assim como em trabalhos relacionados [Angeli et al. 2020], a importância da representatividade feminina ao levarmos conteúdos da Computação para as escolas. Todas as pesquisadoras e facilitadoras que atuaram nas oficinas são mulheres. Um ponto que nos chamou atenção foi interesse pela profissão e atuação do mercado das voluntárias do projeto que atuaram como facilitadoras. Elas trabalham no mercado de TIC em empresas popularmente conhecidas e isso despertou a atenção e admiração das estudantes ao longo das oficinas.

A segunda lição aprendida é que apesar de algumas pessoas participantes terem considerado a tarefa difícil, as pesquisadoras observaram nos material coletado que houve aprendizado de Fundamentos da Computação, pois os conceitos foram facilmente aplicados pelas participantes; as participantes rapidamente pensaram em um cenário de problema e o relacionaram a segurança da informação. Outra evidência do aprendizado satisfatório do conteúdo foi possível com a análise dos secbots desenvolvidos. Os projetos indicam que as troca de turnos nos diálogos foram corretamente definidos. Em nossa interpretação esse resultado tem como impacto o textitdespertar feminino sobre como a Computação pode ajudar a sociedade.

Em trabalhos futuros, pretendemos fazer uma pesquisa ao longo de um ano para avaliar se os impactos percebidos nas participantes se refletem nas motivações e interesses das participantes na escolha das carreiras, na motivação por conteúdos das áreas tecnológicas e na desconstrução de estereótipos de gênero.

## Agradecimentos

O presente trabalho foi realizado com apoio da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES) - Código de Financiamento 001 e da Fundação de Apoio à Pesquisa no Estado do Rio de Janeiro Projeto: E26-210838 /2021. As pessoas autoras também agradecem ao Programa Meninas Digitais da SBC pelo apoio e a todas as pessoas que voluntariamente contribuíram com essa pesquisa.
