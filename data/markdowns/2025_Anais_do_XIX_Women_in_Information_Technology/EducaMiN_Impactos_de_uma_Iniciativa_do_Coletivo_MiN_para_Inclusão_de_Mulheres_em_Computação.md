# EducaMiN@: Impactos de uma Iniciativa do Coletivo MiN@ para Inclusão de Mulheres em Computação

Júlia Oliveira Pessoa¹, Giovanna Fincatti Dos Santos¹, Maria Eduarda Brandão¹, Carla Rodriguez², Juliana M. Berbert²

¹ Universidade Federal do ABC (UFABC)

² Centro de Matemática, Computação e Cognição (CMCC/UFABC) Campus Santo André - Avenida dos Estados, 5001 - Bairro Santa Terezinha Santo André - SP - Brasil - CEP: 09210-580

`{julia.pessoa,g.fincatti,maria.brandao}@aluno.ufabc.edu.br,{c.rodrigue z,juliana.berbert}@ufabc.edu.br`

## Abstract.

The low participation of women in STEM (Science, Technology, Engineering, and Mathematics) fields is still a challenge in Brazil, especially in courses such as Computer Science and Engineering. This work presents the initiatives of Project EducaMiN@, linked to Collective MiN@, which seeks to encourage the entry and retention of women in these areas through introductory programming and database courses. In 2024, three courses were offered, reaching 311 participants, of which 220 obtained certification. The evaluation of the courses indicated a positive impact on the students' confidence and interest in the area, highlighting the importance of continuous initiatives to increase diversity in STEM.

## Resumo.

A baixa participação feminina nas áreas de STEM (Ciências, Tecnologia, Engenharia e Matemática) ainda é um desafio no Brasil, especialmente em cursos como Ciência da Computação e Engenharia. Este trabalho apresenta as iniciativas do Projeto EducaMiN@, vinculado ao Coletivo MiN@, que busca incentivar o ingresso e a permanência de mulheres nessas áreas por meio de cursos introdutórios de programação e banco de dados. Em 2024, foram oferecidos três cursos, atingindo 311 participantes, das quais 220 obtiveram certificação. A avaliação dos cursos indicou um impacto positivo na confiança e no interesse das alunas pela área, evidenciando a importância de iniciativas contínuas para aumentar a diversidade em STEM.

## 1. Introdução

Apesar de representarem a maioria da população brasileira, as mulheres ainda são minoria nas áreas de Ciências Físicas, Engenharias, Tecnologias da Informação e Comunicação (TICs) e Matemática [BRASIL, 2024]. Dados recentes apontam que, em 2022, apenas 22% das mulheres matriculadas no ensino superior escolheram essas áreas, com uma participação ainda menor em cursos como Computação (15%) e Engenharias (22,7%). Essa desigualdade não é exclusiva do Brasil: globalmente, apenas 28% das pesquisadoras em STEM são mulheres [UNESCO, 2018], e a participação

feminina em carreiras tecnológicas nos Estados Unidos gira em torno de 26% [NSF, 2023]. Essa sub-representação impacta diretamente a inovação e o mercado de trabalho, limitando a diversidade de perspectivas e a criação de soluções mais inclusivas. Estudos indicam que equipes diversas geram produtos mais eficientes e acessíveis [PAGE, 2007], tornando essencial a ampliação da presença feminina nessas áreas.

No contexto da graduação em Ciência da Computação, verifica-se um estado crítico. As mulheres enfrentam um índice significativo de reprovação em disciplinas de programação. Isso é frequentemente atribuído à falta de experiência prévia com computação e ao ambiente em sala de aula, muitas vezes, caracterizado por uma predominância masculina [RIBEIRO, 2019]. Além disso, estudos indicam que, em eventos da área, a participação feminina tende a se concentrar em áreas com um viés interdisciplinar, como Informática na Educação, enquanto há uma menor presença em eventos que abordam temas considerados mais técnicos, e predominantemente ocupados por homens, como Segurança da Informação, Sistemas Computacionais de Alto Desempenho e Métodos Formais [DUARTE; MOURA; MORO, 2019]. Esses padrões refletem não apenas a influência de fatores sociais e culturais na formação acadêmica e profissional das mulheres em STEM, mas também destacam a necessidade emergente de criar ambientes mais inclusivos e acessíveis para todas as pessoas interessadas em seguir carreiras em Ciência da Computação e áreas afins.

Nesse sentido, a UNESCO (2018) conduziu uma análise abrangente sobre os diversos fatores que influenciam a participação, progressão e desempenho de meninas e mulheres em STEM. O estudo examinou aspectos individuais, familiares, escolares e sociais que moldam o envolvimento feminino nessas áreas, destacando a importância crucial na motivação e trajetória das alunas. Entre as estratégias que demonstraram eficiência no estímulo do interesse pelas áreas de STEM, destacam-se programas de incentivo, formação de professores e parcerias institucionais, que ajudam a fortalecer a autoconfiança e a identidade STEM das estudantes. Experiências internacionais demonstram que iniciativas voltadas ao ensino inclusivo de computação geram impactos positivos. Nos Estados Unidos, o programa Girls Who Code aumentou significativamente o interesse de alunas do ensino médio por carreiras tecnológicas, reduzindo a diferença de gênero na computação. No Reino Unido, a reformulação do currículo nacional em 2014 incluiu a obrigatoriedade do ensino de computação desde o ensino fundamental, garantindo que meninas tenham acesso a essas habilidades desde cedo e promovendo maior equidade de gênero na área [THE ROYAL SOCIETY, 2017]. Além disso, diversas parcerias entre instituições acadêmicas e o setor privado têm sido implementadas para promover a participação feminina em áreas STEM, reforçando a necessidade de ações contínuas e diversificadas para enfrentar as barreiras existentes.

Dado este cenário, se faz imperativa a adoção de medidas que sejam inclusivas e que obtenham resultados capazes de corroborar com a redução da disparidade de gêneros, promovendo a participação equitativa das mulheres em áreas de STEM. No Brasil, diversas instituições públicas e privadas estão empenhadas em promover

esforços para incentivar e fomentar a participação feminina em eventos e seminários dedicados às mulheres. O Programa Mulher Sistema Confea/Crea-Mútua exemplifica esse compromisso ao citar a organização de eventos, seminários e palestras como parte de suas ações destinadas a “estimular a participação protagonista das mulheres [...], visando maior inserção da mulher em cargos de liderança e alta gestão nas diversas esferas do Sistema” [CONFEA, 2021, p. 23]. Essas iniciativas são fundamentais para avançar em direção ao alcance do Objetivo de Desenvolvimento Sustentável (ODS) número 5, que trata da Igualdade de Gênero e Empoderamento de Mulheres. Observa-se, portanto, a importância crucial de implementar ações destinadas a motivar e encorajar meninas e mulheres a seguirem carreiras em STEM desde os estágios iniciais da educação escolar até a formação profissional. Isso valida a necessidade premente de iniciativas que estabeleçam conexões entre as áreas de tecnologia e os interesses das estudantes de maneira lúdica e acessível, ao mesmo tempo em que promovem sua autoestima, especialmente em relação ao ambiente acadêmico. Embora exista um grande potencial entre as mulheres nessa área, ainda há muitas inseguranças a serem superadas, como destacado por Medeiros et al. (2022).

Uma vez que temos esse cenário crítico, por meio deste trabalho apresenta-se o Projeto EducaMiN@, parte do Coletivo MiN@, vinculado à Universidade Federal do ABC, que tem como objetivo fomentar a inclusão e permanência de mulheres em STEM por meio do desenvolvimento do pensamento computacional e do ensino de programação. Criado em 2018, o projeto já impactou centenas de alunas, promovendo cursos de introdução à programação e banco de dados voltados tanto para estudantes universitárias quanto para mulheres da comunidade externa [SASS et al., 2018; 2021; 2023]. Ao longo dos anos, o projeto evoluiu, ampliando seu escopo e metodologia para melhor atender às necessidades das participantes. Focamos neste artigo nas ações realizadas em 2024, quando foram oferecidos três cursos, totalizando 10 turmas e atendendo 311 participantes, das quais 220 concluíram a formação e obtiveram certificação. Os resultados evidenciam um impacto positivo no aumento da confiança e do interesse das alunas pela área, reforçando a importância de ações contínuas para ampliar a participação feminina em áreas STEM e a permanência delas na universidade.

O restante do artigo é organizado da seguinte forma. A seção 2 apresenta as características e os objetivos do Coletivo, enquanto a seção 3 descreve a metodologia adotada e as ações em curso. Na seção 4, traz os resultados obtidos, seguidos pelas conclusões e perspectivas futuras do projeto, na seção 5.

## 2. O Coletivo

O Coletivo, vinculado à Universidade Federal do ABC, atua através de atividades extensionistas e de melhoria do ensino para apresentar e desmistificar as áreas STEM para mulheres. Seu principal objetivo é reduzir as desigualdades de gênero, capacitando mulheres para ocuparem papéis de destaque na academia e no mercado de trabalho,

tornando-as agentes ativas na produção de conhecimento e tecnologia [SASS et al., 2018; 2021; 2023]. Desde sua criação, o Coletivo já impactou centenas de alunas, contribuindo para a ampliação da confiança em programação e o aumento da taxa de aprovação em disciplinas introdutórias de computação. Depoimentos de participantes indicam que a abordagem inclusiva e colaborativa do projeto tem sido fundamental para sua permanência na área.

Para atingir seus objetivos, atualmente, o Coletivo se organiza em quatro projetos de extensão universitária: EducaMiN@, Mirtic@, UFABC para MiN@s e o podcast Assunto de Menina, cada um voltado para um público específico e utilizando estratégias complementares para estimular o interesse e a formação de meninas e mulheres em STEM. Cada projeto possui autonomia para realizar suas ações, seguindo os objetivos macro do Coletivo. A organização é feita de forma a alcançar meninas e mulheres em diferentes fases de suas vidas, aplicando diversas estratégias para aproximação de cada público às áreas STEM, mantendo as ações e oficinas de maneira lúdica, objetiva e interdisciplinar.

Durante o ano de 2024 a equipe do Coletivo foi composta por duas coordenadoras, egressas do Bacharelado em Ciência da Computação (BCC), 5 coordenadoras docentes (de diferentes áreas de conhecimento), 10 colaboradoras(es) docentes, 11 estudantes bolsistas e 16 voluntárias, totalizando 42 colaboradoras(es) que atuam diretamente nos projetos. Destas, as duas coordenadoras egressas do BCC, 1 coordenadora e 1 colaboradora docente, 4 estudantes bolsistas e 13 voluntárias compõem a equipe do Projeto relatado neste artigo. Essa equipe multidisciplinar desempenha um papel essencial na implementação e expansão das iniciativas do Coletivo, garantindo a continuidade e evolução das atividades ao longo dos anos.

## 3. Metodologia e Ações em Andamento

O Projeto EducaMiN@ é uma iniciativa de extensão e de melhoria do ensino que busca dar continuidade e ampliar a metodologia proposta inicialmente pelo Coletivo e busca desenvolver iniciativas e estratégias pedagógicas para motivar o aumento do número de meninas ingressantes e concluintes nos cursos de STEM, focando no desenvolvimento do pensamento computacional (SASS et al., 2018; 2019; 2021). Inicialmente, o projeto buscava complementar o ensino de lógica de programação das disciplinas introdutórias dos cursos de bacharelados da Universidade. O público-alvo eram alunas com pouco ou nenhum contato prévio com programação, visando reduzir a reprovação e a evasão feminina nesses cursos. No entanto, logo nos primeiros anos, identificou-se a necessidade de expandir a atuação para além do ensino superior, levando conceitos de Ciência da Computação para alunas de escolas públicas da região. Muitas dessas estudantes não haviam tido qualquer exposição à área e sequer a consideravam como uma possibilidade de carreira [SASS et al., 2018].

## 3.1 Estrutura e Expansão do Projeto

Nos últimos anos, o projeto ganhou dois novos minicursos e seu público passou a abranger todas as mulheres da comunidade interna e externa. O repertório atual conta com os seguintes cursos, cujos nomes foram escolhidos para homenagear mulheres pioneiras na computação:

1. Ada Lovelace - Introdução à Lógica de Programação em Python

2. Barbara Liskov - Avançando nos Conceitos da Programação em Python

3. Grace Hopper - Banco de Dados com SQL

Os cursos foram organizados em um modelo presencial, com turmas distribuídas ao longo do ano. A tabela 1 ilustra a organização das ofertas em 2024.

Tabela 1 - Público-alvo e período de oferta dos cursos ao longo do ano

|Curso|Período|Formato|Carga horária|Público-alvo|
|---|---|---|---|---|
|Ada Lovelace – Introdução|Junho e|Presencial|15h (3 sábados)|Iniciantes em programação|
|à Lógica de Programação|Agosto||||
|Barbara Liskov –|Junho e|Presencial|15h (3 sábados)|Quem já tem noções básicas de|
|Avançando nos Conceitos|Agosto|||programação|
|de Programação|||||
|Grace Hopper – Banco de Dados com SQL|Novembro|Presencial|10h (2 sábados)|Mulheres interessadas em SQL e bancos de dados|

## 3.2 Critérios de Seleção das Participantes

Para garantir que as alunas fossem alocadas nos cursos mais adequados ao seu nível de conhecimento, a inscrição foi realizada por meio do preenchimento de um formulário no qual as candidatas forneceram informações como: Nível de conhecimento prévio em lógica de programação e bancos de dados; Experiência anterior com linguagens de programação; Motivação para participar do curso; Disponibilidade para frequentar os encontros presenciais.

A seleção priorizou alunas com menor experiência na área e maior disponibilidade para comparecer às aulas, buscando democratizar o acesso ao ensino de computação. Nos cursos mais avançados, a seleção também levou em conta a conclusão de cursos anteriores oferecidos pelo projeto.

## 3.3 Avaliação de Impacto

Ao final de cada curso, as participantes responderam um formulário anônimo para avaliar diversos aspectos da experiência, incluindo: Qualidade do material didático e das

aulas; Clareza e acessibilidade do conteúdo; Organização e estrutura do curso; Percepção de aprendizado e nível de confiança após a conclusão; Comentários à equipe.

Os resultados dessas avaliações são fundamentais para aprimorar continuamente as metodologias adotadas e garantir que os cursos atendam às necessidades das alunas de forma eficaz.

## 4. Resultados

Desde 2018, o EducaMiN@ tem promovido ações para incentivar a participação feminina em áreas STEM. Estudos anteriores [SASS, 2023] relataram o andamento de três iniciativas antes e durante a pandemia da Covid-19, demonstrando a importância da continuidade do projeto. Ao todo, entre os anos de 2018 e 2023 foram ministradas 17 turmas, com capacidade para 30 alunas (com exceção das duas turmas da edição online, em 2021, que não possuíam limite) totalizando um público de 574 participantes, que representam cerca de 32,91% do total das 1744 inscrições recebidas para todas as edições dos cursos ofertados pelo projeto.

Nesta seção, são apresentadas as atividades desenvolvidas em 2024, destacando o alcance dos cursos oferecidos, os impactos gerados e a evolução do projeto ao longo dos anos.

## 4.1 Relato das ações de 2024.

## Cursos Ada Lovelace e Barbara Liskov

Durante o mês de junho houve a oferta presencial e simultânea dos cursos Ada Lovelace (três turmas) e Barbara Liskov (uma turma), para meninas e mulheres moradoras da região do ABC e para alunas da UFABC. Os cursos possuíam capacidade para atender 30 alunas por turma.

No mês de agosto foram ofertadas mais duas turmas de cada curso, no mesmo formato da oferta anterior. Estas edições contaram com uma carga horária de 15 horas, divididas entre 3 sábados consecutivos, das 9h às 16h, com dois intervalos de 15 min e uma pausa de 1h30 para o almoço (Tabela 1).

Para obter o certificado de conclusão dos cursos, as participantes deveriam comparecer a pelo menos cinco dos seis períodos programados. Cada dia de curso era dividido em dois turnos: manhã e tarde. A presença foi registrada por meio de assinatura em lista de chamada em cada período. Em casos de ausência justificada, era possível compensar uma falta mediante a realização de uma lista de exercícios, desde que a participante tivesse comparecido a, no mínimo, quatro períodos.

## Curso Grace Hopper:

Durante o mês de novembro, houve a primeira oferta do curso Grace Hopper, que contou com duas turmas com capacidade para 30 alunas cada. O curso Grace Hopper

seguiu o mesmo formato dos cursos Ada Lovelace e Barbara Liskov, com a exceção da duração, que foi de 2 sábados consecutivos, totalizando uma carga de 10 horas e tendo 3 períodos como presença mínima para a obtenção do certificado (Tabela 1).

Ao todo, durante o ano de 2024 foram ministradas 10 turmas, com capacidade para 30 alunas, totalizando um público de 311 participantes, que representam cerca de 59,6% do total das 522 inscrições recebidas para todas as edições dos três cursos. Dentre as participantes, 220 concluíram os cursos e obtiveram certificado (Tabela 2).

Tabela 2 - Distribuição das participantes por curso

||Curso A|da Lovelace -|Introdução à Lóg|ica de Programação||
|---|---|---|---|---|---|
||Turmas|Inscrições|Participantes|Participantes com certificado|Avaliações Respondidas|
|Junho|3|163|102|71|22|
|Agosto|2|103|56|47|16|

||Curso Bar|bara Liskov -|Avançando nos Co|nceitos de Programação||
|---|---|---|---|---|---|
||Turmas|Inscrições|Participantes|Participantes com certificado|Avaliações Respondidas|
|Junho|1|47|35|23|8|
|Agosto|2|72|54|37|3|

||Cur|so Grace Hop|per -Banco de Da|dos com SQL||
|---|---|---|---|---|---|
||Turmas|Inscrições|Participantes|Participantes com certificado|Avaliações Respondidas|
|Novembro|2|137|64|42|4|

## 4.2 Verificação de impacto dos cursos

De modo geral, considerando as ofertas dos 3 cursos durante o ano de 2024, 53 participantes preencheram os formulários de avaliação. Destas, após o curso, em relação à lógica de programação, 92,45% afirmaram saber o que é e como aplicá-la, 5,66% afirmaram saber o que é, mas não como aplicar e 1,89% disseram ainda ter dúvidas sobre o assunto. Sobre a área de programação 73,58% afirmaram se sentir confiantes e desejar aprender mais, enquanto 16,98% afirmaram não se sentir nada confiantes, mas gostariam de aprender mais, 5,66% estavam confiantes, mas não desejavam aprender

mais e 3,77% estavam neutras. Quanto ao fato do curso ser só para mulheres, 96,23% alegaram terem se sentido mais à vontade e 3,77% disse não sentir nenhuma diferença. Ao fim, 90,57% manifestaram interesse em participar do Coletivo. Dados individuais de cada curso são apresentados a seguir:

Curso Ada Lovelace - Introdução à Lógica de Programação

Considerando a média total das participantes das edições de junho e agosto, no formulário de inscrição: das 266 meninas inscritas, 36,09% afirmaram não conhecer nada sobre programação e lógica de programação, mas ter vontade de aprender, 59,77% afirmaram já ter tido contato com lógica de programação, mas ainda não conseguir aplicar e 4,14% afirmaram já conhecer a lógica de programação e saber programar e querer apenas aprender Python.

Após o curso, nos formulários de avaliação, foram obtidas ao todo 38 respostas, onde 34 (89,5%) das meninas afirmaram saber o que é lógica de programação e como aplicá-la (Figura 1B). Em relação à área de programação, 28 (73,7%) afirmaram se sentir confiantes e desejar aprender mais, 7 (73,7%) afirmaram não se sentir nada confiantes, mas gostariam de aprender mais, 2 (5,3%) disseram não perceber mudança e uma alegou estar confiante, mas não desejar aprender mais (Figura 1A). Sobre o curso ser só para mulheres, 37 (97,4%) alegaram terem se sentido mais à vontade e 1 afirmou não notar diferença. Nas avaliações, 37 (97,4%) manifestaram interesse em fazer parte da equipe do projeto (Figuras 2A e 2B).

Nas questões dissertativas, tivemos relatos de participantes que ao longo do curso se sentiram motivadas e acolhidas pela equipe e puderam dar seus primeiros passos no mundo da programação, ou recuperar o entusiasmo pela área, perdido após experiências muito negativas em outras disciplinas da Universidade.

Curso Barbara Liskov - Avançando nos Conceitos de Programação

Considerando a média total das participantes das edições de junho e agosto, no formulário de inscrição: das 119 meninas inscritas, 1,68% afirmaram não conhecer nada sobre programação e lógica de programação, mas ter vontade de aprender, 88,24% afirmaram conhecer o básico, mas ter vontade de dar os próximos passos no aprendizado de programação e 10,08% afirmaram já conhecer a lógica de programação e saber programar e querer apenas aprender Python.

Após o curso, nos formulários de avaliação, foram obtidas ao todo 11 respostas, onde todas afirmaram saber o que é lógica de programação e como aplicá-la (Figura 1B). Em relação à área de programação, 8 (72,7%) afirmaram se sentir confiantes e desejar aprender mais e as 3 restantes afirmaram, respectivamente, não se sentir nada confiante, mas gostaria de aprender mais, não perceber mudança e estar confiante, mas não desejar aprender mais (Figura 1A). 10 (90,9%) alegaram terem se sentido mais à vontade em um curso só para mulheres, 1 afirmou não notar diferença. Todas

manifestaram interesse em fazer parte da equipe do projeto (Figuras 2A e 2B). Nas questões dissertativas, também houveram muitos elogios ao curso e à equipe e algumas sugestões de melhorias para o material (que ainda está em desenvolvimento).

Curso Grace Hopper - Banco de Dados com SQL

No formulário de inscrição: das 136 meninas inscritas, 64% afirmaram não conhecer nada de banco de dados e SQL, mas ter vontade de aprender, 27,2% afirmaram já ter tido contato, mas ainda não conseguir aplicar e 8,8% afirmaram ter noções básicas de SQL e conseguir aplicar em projetos simples.

No formulário de avaliação do curso, foram obtidas 4 respostas, todas afirmaram saber o que é lógica de programação e como aplicá-la em sql (Figura 1B). Em relação à área de programação, 3 afirmaram se sentir confiantes e desejar aprender mais e 1 afirmou não se sentir nada confiante, mas gostaria de aprender mais (Figura 1A). Todas alegaram terem se sentido mais à vontade em um curso só para mulheres e ter interesse em fazer parte da equipe do projeto (Figuras 2A e 2B).

Nas questões dissertativas, houve um feedback bastante positivo em relação ao novo curso e à equipe. Algumas das meninas também relataram terem aplicado no trabalho os conhecimentos adquiridos.

Figura 1. (A) Confiança na área; (B) Compreensão da lógica de programação

Figura 2. (A) Interesse em participar do Coletivo; (B) Importância do ambiente exclusivo para mulheres

## 5. Conclusões e Trabalhos Futuros

Os resultados obtidos em 2024 demonstram o impacto positivo do EducaMiN@ na promoção da inclusão feminina em STEM. A expansão dos cursos e o aumento da participação de mulheres da comunidade externa evidenciam a relevância da iniciativa para democratizar o acesso ao ensino de computação. As avaliações indicaram que, além de aprimorar a compreensão das alunas sobre lógica de programação e banco de dados, os cursos contribuíram para o fortalecimento da confiança das participantes, incentivando sua continuidade nos estudos e maior envolvimento com o Coletivo.

Apesar dos avanços, o projeto ainda enfrenta desafios que precisam ser abordados nas próximas edições. Um dos principais obstáculos identificados em 2024 foi a taxa de evasão ao longo dos cursos, especialmente entre as alunas com pouca experiência prévia em computação. Para reduzir esse problema, futuras edições podem incluir monitoria pré-curso para nivelamento das participantes, proporcionando um primeiro contato com os conteúdos antes do início das aulas. Além disso, planeja-se o desenvolvimento de materiais complementares, como vídeos e exercícios interativos, que possibilitem maior autonomia no aprendizado.

Outro desafio refere-se à necessidade de ampliar o alcance do projeto para diferentes públicos e localidades. Para isso, a equipe pretende buscar novas parcerias com instituições de ensino, empresas e organizações do terceiro setor, visando oferecer mais edições presenciais e, eventualmente, expandir a iniciativa para um formato híbrido, permitindo a participação remota de mulheres que não residem na região atendida. Essa abordagem pode potencializar o impacto do projeto, alcançando um número ainda maior de beneficiadas.

Entre as perspectivas futuras, destaca-se a inclusão de novos cursos, abordando temas como desenvolvimento web, análise de dados, inteligência artificial, desenvolvimento de sistemas alinhados às demandas do mercado de tecnologia. Além disso, o projeto continuará a fortalecer ações de mentoria, promovendo o contato das alunas com profissionais da área para incentivar sua inserção no mercado de trabalho.

Dessa forma, o EducaMiN@ segue comprometido com a redução das barreiras que afastam mulheres da computação, promovendo um ambiente mais acessível, acolhedor e estimulante, para que possam explorar e desenvolver plenamente seu potencial na área de STEM.

## Agradecimentos

Agradecemos à Universidade Federal do ABC (UFABC) pelo apoio institucional e financeiro, viabilizado por meio das bolsas de extensão concedidas pela Pró-Reitoria de Extensão e Cultura (ProEC) e Pró-Reitoria de Graduação (ProGrad). Expressamos nossa gratidão ao projeto REBECA – CNPq (Processo nº 440425/2024-7) pelo suporte financeiro também através de bolsa de extensão. Reconhecemos e agradecemos a colaboração de Camila Sass e Lara Tenore, cuja liderança nas primeiras edições deste curso foi fundamental para a consolidação das ações do Coletivo Mirtha Lina (cMiN@). Estendemos nossos agradecimentos às professoras Denise Goia e Cristiane Sato pelo apoio contínuo e pelas contribuições valiosas ao longo do projeto, e às monitoras que nos ajudaram durante o curso. Agradecemos, ainda, aos(as) revisores(as) anônimos(as) pelas sugestões e comentários que enriqueceram e aprimoraram a qualidade deste manuscrito.
