# Meninas, Computação e Música

Thayna Gimenez, Caroline R. Barroso, Jéssika M. Pereira, André L. Przybysz, Adriano Rivolli, Carlos N. Silla Jr.

1Laboratório de Computação e Tecnologia Musical Universidade Tecnológica Federal do Paraná (UTFPR) Cornélio Procópio – PR – Brasil

{ gimenezthayna, carol.rezendebarroso, jessikamachado17 } @gmail.com

{ andrelp, rivolli, carlosjunior } @utfpr.edu.br

Abstract. This work presents an overview of the project Girls, Music and Computer Science. The goal of this project is to promote Computer Science-related courses to pre-university female students. The project is aimed at public school girls and teaches them Java programming along music theory and practice.

Resumo. Este trabalho descreve o projeto Meninas, Computação e Música, que busca incentivar meninas para ingressarem em cursos da área de Computação. O projeto propõe o ensino de programação em linguagem Java aliado ao ensino de teoria e práticas musicais para meninas do ensino médio da escola pública.

## 1. Introdução

O famoso ENIAC, primeiro computador do mundo, foi programado por seis jovens mulheres, em 1946. A história ao decorrer dos anos fez questão de ocultar esse fato de tamanha importância para as mulheres e que mostrava seu posicionamento no âmbito computacional [Schwartz et al. 2006]. Hoje, porém; é comum observar que os homens são a grande maioria nas áreas referentes à computação. A mitologia grega diz que Prometeu foi o grande responsável pelo nascimento da tecnologia, mas e se este fato histórico tivesse sido marcado por uma mulher, uma deusa grega? A presença feminina e o olhar para as mulheres da área de computação seriam diferentes? A grande maioria de indivíduos na área de computação ainda seria masculina? [Cabral and Bazzo 2005]

O astrofísico americano Neil DeGrasse Tyson, homem negro que enfrentou preconceitos raciais, disse em uma discussão que antes mesmo de debatermos nossas diferenças genéticas, devemos nos tratar igualmente, gerando oportunidades iguais a todos e somente a partir disso poderemos discutir sobre nossas genéticas [Lima 2014]. Assim como o preconceito racial vivido por Tyson, o mesmo depoimento é válido em relação ao preconceito que as mulheres sofrem na área de computação, por se tratarem da minoria.

Essa presença masculina em massa pode se tornar um problema às mulheres. Os casos de preconceito relatados por mulheres da área de exatas constatam que são obrigadas a conviver com a impressão de que a mulher não é capaz de exercer um cargo como programadora ou coisa do tipo. A sociedade traçou um estereótipo de que mulheres se enquadram melhor nos cursos de humanas, tais como enfermagem ou pedagogia e que cursos de computação são bastante complexos para o entendimento das mulheres; assim, as jovens que estão finalizando o ensino médio já se imaginam em cursos relacionados a

área de humanas e não a área de exatas [Cabral and Bazzo 2005]. Não há um incentivo que mostra a estas jovens que elas são capazes e que também podem ingressar nessa área.

Com o intuito de dar este incentivo, o projeto Meninas, Computação e Música, mostra a alunas do ensino médio, ensinando conceitos de programação aliados ao ensino de música, que elas também são capazes de entrar em cursos relacionados a computação e que esse não é um privilégio único e exclusivo do público masculino.

## 2. Meninas, Computação e Música

Visando diminuir os problemas de preconceitos relatados por mulheres e derrubar o paradigma de que cursos de exatas são restritos ao público masculino, o projeto Meninas, Computação e Música busca trazer meninas/mulheres para os cursos de Computação da universidade. Para isso, foram selecionadas quatro meninas do ensino público, com idade entre 16 e 17 anos.

As alunas aprenderam programação em Java aliado ao aprendizado de música, o que tornava o processo mais lúdico e um problema visível do mundo real para ser tratado por elas. O laboratório recebia as meninas duas vezes por semana, sendo quatro horas diárias. Nesses dias, professores das áreas de música e computação, ensinavam conceitos de cada área. No primeiro dia da semana, as meninas tinham aulas sobre música, onde aprendiam o modo de manuseio de cada instrumento, como tocar notas básicas e notas mais complexas, como acordes. No segundo dia, recebiam aulas relacionadas a programação Java, onde aprendiam conceitos que envolviam declaração e tipos de variáveis, estruturas de repetição, estruturas condicionais, como capturar os sons provenientes dos instrumentos e também como trabalhar com o ambiente de desenvolvimento dos jogos, o Greenfoot [Kolling 2009].

Ao decorrer do projeto, também foram ministradas aulas relacionadas a edição de imagens, para que as meninas pudessem criar suas próprias telas para os jogos. As meninas também contavam com o apoio de alunas dos cursos de Análise e Desenvolvimento de Sistemas e Engenharia de Computação para o desenvolvimento dos jogos e também para que as mesmas tivessem um contato mais próximo com alunas da área.

## 3. Materiais e Métodos

O projeto foi desenvolvido utilizando quatro instrumentos musicais reais, sendo eles: bateria, contrabaixo, guitarra e teclado. Todos os instrumentos possuem entradas para conexão MIDI.

O cabo conector MIDI é responsável por realizar a comunicação entre computador e instrumento musical. Ele transforma o som do instrumento em linguagem de máquina, para que o computador seja capaz de interpretar esta linguagem. Assim, é possível manipular os sons recebidos e os que serão transferidos ao instrumento [Guerin 2005].

Para manipulação dos dados recebidos através do cabo conector MIDI, foi utilizada a biblioteca open source JFugue. A biblioteca recebe através do cabo uma sequência de instruções e os manipula gerando eventos musicais [Koelle 2008]. A partir das sequências recebidas do instrumento, é possível comparar com as instruções exigidas no jogo e conferir o desempenho do usuário [Koelle 2008].

Os jogos foram desenvolvidos na plataforma interativa Greenfoot. Os efeitos de mudanças realizadas no código podem ser observados em tempo real no projeto; aumentando a compreensão do usuário no desenvolvimento [Kolling 2009].

## 4. Resultados

Com as aulas dadas pelos professores e com a orientação das graduandas, cada aluna desenvolveu um jogo para um determinado instrumento musical.

### 4.1. Jogo para a Bateria

Neste jogo, o participante deve tocar na bateria real o som que a bateria virtual emitir. Em caso de acerto, ganhará pontos ao término do jogo. O mesmo trabalha a audição do jogador e sua capacidade de saber diferenciar qual parte da bateria está sendo tocada.

### 4.2. Jogo para o Contrabaixo

Este jogo é voltado para iniciantes que já possuem um conhecimento básico a respeito de música e do instrumento contrabaixo. O usuário deve tocar as mesmas notas que estão dispostas na tela e em seguida são exibidas, dizendo se estão corretas ou incorretas.

### 4.3. Jogo para a Guitarra

A ideia deste jogo é ter uma aplicação em que o usuário possa aprender novas escalas e assim ficar mais hábil no uso do instrumento. O jogo possui diferentes níveis e ao final é mostrada a porcentagem de erros e acertos do usuário.

### 4.4. Jogo para o Teclado

O jogo baseia-se em tocar as notas que aparecem dispostas na partitura. E composto por notas simples e por tríades (acordes), com o objetivo de ensinar partituras e acordes no teclado. O jogo também é voltado para treinamento.

## 5. Feedback das Alunas

As meninas que participaram do projeto se sentiram muito interessadas e motivadas em participar após descobrirem que seria desenvolvido jogos relacionados a determinados instrumentos musicais e que elas mesmas iriam desenvolver estes jogos, aprendendo sobre programação e música.

Foram realizados questionários com as alunas no início e fim do projeto. Para elas, os cursos relacionados a Computação eram vistos como cursos complexos por envolver programação. Ao término do projeto, elas puderam notar que programar não era tão difícil e que bastava dedicação para aprender os conceitos que foram passados. Como as alunas desenvolveram todo o jogo, desde as telas, botões, a programação, a lógica e os conceitos musicais utilizados, as mesmas ficaram muito surpresas com o resultado final do projeto e acharam interessante conseguir interagir com um objeto do mundo real (instrumento) através do programa desenvolvido.

O projeto também auxiliou na escolha do curso para o vestibular, onde algumas alunas consideraram a possibilidade de cursar algo relacionado a Computação.

De forma espontânea, o projeto foi divulgado pelas meninas nas escolas para seus amigos e colegas e acabou despertando interesse em diversos outros alunos, meninas e meninos; surgindo possíveis novas alunas para uma próxima turma e gerando reclamação por parte dos meninos que também gostariam de participar do projeto.

## 6. Considerações finais

Com o projeto Meninas, Computação e Música, foi possível incentivar as alunas e mostrar que mulheres podem e tem direito igual em ingressar nos cursos de exatas, principalmente na área de computação e que não podem ser motivos de preconceitos.

Além do mais, foi possível mostrar as alunas que o estereótipo gerado pela sociedade em relação às mulheres na área de computação pode ser desmistificado, mostrando que com esforço e empenho, qualquer pessoa é capaz de ingressar e permanecer nesta área, independente de sexo. O ensino da música paralelo ao ensino de programação foi essencial para que as alunas pudessem notar essa quebra de paradigma; pois além de ser uma prática lúdica, também representava um problema do mundo real e que elas são capazes de transformar este problema em linhas de códigos.

O projeto auxiliou as alunas na tomada de decisão em relação ao vestibular, onde cogitaram a possibilidade de ingressar em cursos de computação por terem uma mínima noção sobre programação; uma vez que antes do projeto esta possibilidade não tinha sido considerada.

## Agradecimentos

Agradecemos o apoio financeiro recebido do Ministério da Ciência, Tecnologia e Inovação (MCTI), do Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq), da Secretaria de Políticas para as Mulheres da Presidência da República (SPMPR), da Petrobras, da Fundação Araucária e da Universidade Tecnológica Federal do Paraná (UTFPR).
