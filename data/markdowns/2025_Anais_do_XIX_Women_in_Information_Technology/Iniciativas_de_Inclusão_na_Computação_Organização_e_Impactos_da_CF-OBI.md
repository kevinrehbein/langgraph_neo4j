# Iniciativas de Inclusão na Computação: Organização e Impactos da CF-OBI

Camila da Cruz Santos, Crishna Irion, Juliana Freitag Borin, Rafael Dias Araújo, João Henrique de Souza Pereira

1 Faculdade de Computação (FACOM) – Universidade Federal de Uberlândia(UFU) Uberlândia – MG – Brasil

2Instituto de Computação – Universidade Estadual de Campinas (Unicamp) Campinas – SP – Brasil

{ camilacruz, crishna, rafael.araujo, joaohs } @ufu.br, jufborin@unicamp.br

Abstract. The OBI Women’s Competition (CF-OBI) is an initiative aimed at promoting the inclusion of women in programming. The overall objective of this work is to evaluate the impact of CF-OBI on increasing female participation and developing technical skills. The methodology involved planning, creating challenges aligned with computational thinking, administering online tests through the CMS system, and performing statistical analysis of the results (Chi-Squared and Fisher’s Exact tests). The results demonstrated a significant increase in participation between 2023 and 2024, highlighting the effectiveness of CF-OBI as an inclusion strategy. In conclusion, CF-OBI is a promising initiative for reducing gender inequality in computing, and the continuation and improvement of the competition are crucial.

Resumo. A Competição Feminina da OBI (CF-OBI) e´ uma iniciativa que visa promover a inclusao˜ de mulheres na programação. O objetivo geral deste trabalho e´ avaliar o impacto da CF-OBI no aumento da participação feminina e no desenvolvimento de habilidades tecnicas.´ A metodologia envolveu o planejamento, a criação de desafios alinhados ao pensamento computacional, a aplicação de provas online por meio do sistema CMS e a analise estat´ ística dos resultados (testes Qui-Quadrado e Teste Exato de Fisher). Os resultados demonstraram um crescimento significativo na participação entre 2023 e 2024, evidenciando a efetividade da CF-OBI como uma estrategia de´ inclusao.˜ Conclui-se que a CF-OBI e uma iniciativa promissora para reduzir´ a desigualdade de generoˆ na computação, sendo crucial a continuidade e o aprimoramento da competição.

## 1. Introdução

A partir da aprovação da Resolução N° 1 de 2022, a Computação se torna um componente obrigatorio nas escolas do Brasil, visando´ a inclus` ao digital dos estudantes da Educa˜ ção Basica´ [Conselho Nacional de Educação 2022]. A implementação deve seguir a Base Nacional Comum Curricular (BNCC) e considerar a formação inicial e continuada de professores, conforme a Lei de Diretrizes e Bases da Educação Nacional (LDB).

As competições de programação temˆ emergido como um novo paradigma na educação computacional, com potencial para preencher lacunas na formação tradicional e desenvolver habilidades essenciais para o sucesso profissional. Estudos indicam que a participação em tais competições contribui significativamente para a melhoria da capacidade de resolução de problemas em estudantes de computação [Raman et al. 2018, Moura et al. 2019, e Silva Sousa et al. 2022].

Alem´ de aprimorar as habilidades tecnicas,´ as competições de programação tambem´ se configuram como um ambiente propício ao desenvolvimento de talentos, incentivando o desempenho academicoˆ e a busca por excelenciaˆ [Vitorino et al. 2018, Solórzano et al. 2019]. A natureza colaborativa e desafiadora dessas competições tambem´ promove o trabalho em equipe e a comunicação eficaz, preparando os alunos para a solução de problemas [Bloomfield and Sotomayor 2016, Theodoro et al. 2024].

A partir da analise´ historica´ dos participantes da Maratona Nacional de Programação, foi constatado que em 2024 houve um aumento substancial da participação feminina na Maratona, alcançando 15% na final, refletindo a importancia de iniciativas queˆ incentivam a diversidade de genero na tecnologia [ˆ Ramos et al. 2025]. Esse aumento foi possível graças a ações de incentivo e vagas afirmativas criadas para inclusao das meninas˜ [Irion et al. 2024].

A Competição Feminina da OBI (CF-OBI) e´ uma iniciativa para promover a participação de jovens mulheres na programação, sendo destinada a todas as competidoras que se identificam como do genero feminino ou nˆ ao-bin˜ ario.´ A competição oferece tresˆ níveis, com prova realizada on-line e apoio na premiação das melhores participantes. Certificados e medalhas sao concedidos, al˜ em da oportunidade de sele´ ção para eventos internacionais de informática [Olimpíada Brasileira de Informática 2024].

Este trabalho apresenta a metodologia utilizada na organização da Competição Feminina da OBI (CF-OBI) bem como os resultados obtidos nas duas edições do evento, realizadas em 2023 e 2024. Os resultados apresentados evidenciam o aumento na participação de competidoras na segunda edição do evento, alem´ de pontos que podem ser melhorados nas proximas´ edições. Por fim, espera-se que este trabalho inspire outras pessoas a se envolverem na organização da CF-OBI ou a promoverem iniciativas semelhantes para a promoção da redução da desigualdade de genero no campoˆ da tecnologia.

O trabalho contribui com evidencias do aumento da participaˆ ção feminina quando promovidos eventos proprios, acolhedores e inclusivos, como competi´ ções de programação para o desenvolvimento de talentos na area da computa´ ção, assim como a inspiração para novas iniciativas para a redução da desigualdade de gênero no campo da tecnologia.

O restante do artigo esta´ organizado da seguinte forma. A Seção 2 descreve a CF-OBI, seus objetivos e sua organização, detalhando como ela se diferencia de outras iniciativas. A Seção 3 detalha o processo de organização da CF-OBI, desde o planejamento ate a execu´ ção das provas. A Seção 4 apresenta e discute os resultados obtidos nas duas edições da CF-OBI. Por fim, a Seção 5 propoem a˜ ções para consolidar e ampliar o impacto da CF-OBI, e a Seção 6 resume as conclusoes obtidas e a relev˜ ancia da iniciativa paraˆ promover a inclusão feminina na área de computação.

## 2. Competição Feminina da OBI

A CF-OBI foi criada em 2023 como uma extensao da Olimp˜ íada Brasileira de Informatica´ (OBI), é uma competição de programação voltada para estudantes do ensino fundamental e medio que se identificam como femininas ou de outro g´ enero. A literatura tem demonstradoˆ que competições de programação podem ser ferramentas eficazes para atrair e reter mulheres na área de computação [Lima et al. 2021, Bastos et al. 2017, Pessoa et al. 2017].

A CF-OBI se diferencia de outras iniciativas por seu foco exclusivo em programação para estudantes do ensino fundamental e medio,´ e por sua abordagem inclusiva, que envolve participantes de diversas identidades de genero.ˆ A competição oferece tres nˆ íveis (Programação Junior, N´ ível 1 e Nível 2), permitindo a participação de estudantes com diferentes níveis de experiencia.ˆ Alem do reconhecimento por meio de´ certificados e medalhas, as melhores colocadas tem a oportunidade de participar da Semanaˆ Olímpica da OBI e concorrer a vagas em competições internacionais, o que aumenta o engajamento e a motivação das participantes [Olimpíada Brasileira de Informática 2024].

A competição se organiza com foco em:

- Enfase na Programa ção: dedicada exclusivamente a programa` ção, com tres nˆ íveis de competição (Programação Junior, N´ ível 1 e Nível 2), permitindo a participação de competidoras de diferentes idades e graus de experiência.

- Inclusão: a competição é inclusiva, garantindo um ambiente acolhedor.

- Reconhecimento e Oportunidades: as participantes recebem certificados e as melhores colocadas sao premiadas com medalhas.˜ As duas primeiras colocadas de cada nível sao convidadas para a Semana Ol˜ ímpica da OBI, possibilitando o acesso a cursos avançados de programação e podem concorrer a vagas na equipe brasileira em competições internacionais.

- Desenvolvimento de Habilidades: a CF-OBI busca fortalecer o aprendizado das participantes por meio de cursos e iniciativas que ampliam suas habilidades na área.

### 2.1. CF-OBI e Pensamento Computacional

Assim como a OBI, a CF-OBI utiliza desafios que envolvem a elaboração de algoritmos, logica, matem´ atica e estruturas de dados.´ Esses desafios estao diretamente relacionados ao˜ desenvolvimento do pensamento computacional [Santos et al. 2024], que é um conjunto de habilidades fundamentais para a resolução de problemas de forma sistematica e eficiente.´ O pensamento computacional e´ composto por quatro eixos principais: decomposição, reconhecimento de padrões, abstração e projeto de algoritmos [Wing 2006].

Os desafios da CF-OBI, assim como os da OBI, sao cuidadosamente elaborados˜ para estimular o desenvolvimento do pensamento computacional, um conjunto de habilidades essenciais para a resolução de problemas de forma sistematica´ e eficiente. Esses desafios exigem que as participantes apliquem os quatro eixos do pensamento computacional, conforme apresenta a Tabela 1:

## 3. Organização e Método

A organização da Competição Feminina da OBI (CF-OBI) seguiu uma metodologia estruturada, que começou com um cronograma elaborado para organizar as etapas do

Table 1. Correlaç ão com Pensamento Computacional

evento, desde a divulgação ate a aplica´ ção das provas e a divulgação dos resultados. A Figura 1 apresenta um resumo das etapas realizadas e as subseções a seguir detalham cada uma delas.

Figure 1. Fluxo de atividades realizadas para a competiç ão

### 3.1. Planejamento

O planejamento da competição incluiu a definição de objetivos, a elaboração de um cronograma e a seleção de uma equipe de apoio composta por mulheres da area´ de computação. As atividades de 2024 aconteceram entre os meses Abril e Setembro, onde foram realizadas reunioes quinzenais de 30 minutos para discutir estrat˜ egias de cria´ ção dos desafios, organização da prova e validação dos resultados.

A equipe organizadora, composta por 21 integrantes em 2024, foi formada majoritariamente por mulheres da área de computação, promovendo um ambiente inclusivo e representativo.

### 3.2. Inscrições

As inscrições na CF-OBI devem ser feitas por um(a) professor(a) ou funcionario(a) da´ escola, chamado(a) de Coordenador(a) Local da OBI na escola, atraves do site principal da´ OBI [Olimpíada Brasileira de Informática 2024]. A participação e gratuita para todos os´ participantes e as competidoras podem ser inscritas em qualquer nível do CF-OBI para o qual sejam elegíveis, independentemente dos níveis em que porventura tenham sido inscritas na OBI.

### 3.3. Criação do Ambiente de Competição

A competição e criada no´ Contest Management System (CMS), um sistema de avaliação de codigo´ aberto, gratuito e projetado para competições de programação no estilo da Olimpíada Internacional de Informatica´ (OII). O sistema prioriza a segurança e adaptabilidade, adotando uma arquitetura modular que permite a replicação de serviços para escalabilidade. A segurança e garantida atrav´ es de´ sandboxes que executam codigo´ nao˜ confiavel,´ prevenindo fraudes. O CMS utiliza um modelo de dados baseado em arquivos imutaveis e um banco de dados SQL (PostgreSQL), assegurando a integridade´ dos dados e a deduplicação [Maggiolo and Mascellani 2012]. A Figura 2 apresenta a arquitetura da ferramenta.

Figure 2. Arquitetura do Contest Management System (CMS). Fonte: [Maggiolo and Mascellani 2012].

Para a criação do ambiente da CF-OBI, o CMS foi utilizado como ferramenta de conteinerização e foram desenvolvidas as seguintes etapas neste processo:

- Preparação: Configuração da plataforma on-line para inscrição e aplicação das provas.

- Preparação dos Problemas: Adaptação dos desafios para o formato da plataforma.

- Testes: Verificação do funcionamento da plataforma e dos problemas.

### 3.4. Elaboração dos Desafios

O processo de criação das questoes˜ e bem minucioso, pois todas as quest´ oes s˜ ao pensadas˜ para que as meninas possam se sentir desafiadas durante a prova, mas que nao˜ sejam questoes˜ com resoluções extremamente difíceis. Toda a equipe organizadora participa desse processo, propondo temas e os algoritmos que serao˜ utilizados nos desafios da competição.

As ementas dos desafios estao organizadas por n˜ ível, apresentadas no site da OBI. Os grandes temas são:

1. Fundamentos de Matematica:´ Aritmetica´ e Geometria, Logica,´ Matematica´ Discreta e Grafos;

2. Fundamentos de Computação: Informatica´ Basica,´ Programação (sintaxe e semântica, variáveis, estruturas);

3. Algoritmos e Estruturas de Dados;

4. Analise de Algoritmos:´ Complexidade, Estrategias de Algoritmos, Estruturas de´ Dados, Algoritmos de Ordenação e Busca, Algoritmos de Matematica, Algoritmos´ em Grafos e em Arvores, Algoritmos de Geometria.

A equipe realiza reunioes para dimensionar a prova, buscando equilibrar os n˜ íveis de dificuldade de maneira abrangente e atender a todos os níveis de conhecimento dos participantes. As questoes s˜ ao estruturadas conforme os n˜ íveis (PJ, P1 e P2) e de acordo com as ementas apropriadas. Os desafios foram projetados para estimular o raciocínio logico e a criatividade, habilidades essenciais para o desenvolvimento de compet´ enciasˆ complexas. Alem disso, a realiza´ ção de testes em pares possibilitou uma revisao minuciosa,˜ garantindo a qualidade e a adequação das propostas. Em geral, as atividades desta etapa estão resumidas na Figura 3.

Figure 3. Desenvolvimento dos Desafios

### 3.5. Execução da Prova

As provas da edição de 2024 ocorreram no dia 13 de setembro, de forma presencial nas escolas-sedes. A prova pode ser aplicada de 08h as 18h, e ap` os o in´ ício, as competidoras tem um perˆ íodo de 3h para finalização. No dia da prova, elas devem dispor de computador e acesso a Internet para entrar no sistema.` As submissoes s˜ ao enviadas no site da OBI e˜ podem ser realizadas em C, C++, Python, Java e Javascript.

### 3.6. Validação das Submissões

As submissoes das participantes foram avaliadas automaticamente pelo CMS, com base em˜ criterios pr´ e-definidos, comparando as sa´ ídas esperadas com as geradas pelas soluções das competidoras. A fim de evitar plagios, ap´ os a aplica´ ção, as submissoes das participantes˜ sao analisadas e validadas pela equipe organizadora, que verifica a precis˜ ao das respostas e˜ aplica os critérios de correção previamente definidos.

### 3.7. Divulgação dos Resultados

Por fim, os resultados sao divulgados no site oficial da OBI, e as melhores participantes˜ recebem certificados e medalhas, alem´ de oportunidades de participar de eventos internacionais de informática.

A CF-OBI seleciona as quatro meninas mais bem colocadas em sua classificação para a Olimpíada Europeia de Meninas em Informatica´ (EGOI). A EGOI e´ uma competição internacional de informatica´ para concorrentes individuais da Europa e de países convidados, acompanhada de programas sociais e culturais. O Brasil tem tido resultados significativos em sua participação, com o total de 12 medalhas nos quatro anos de existência da Olimpíada.

A EGOI e´ a unica´ competição internacional de programação competitiva para jovens mulheres e tem como objetivos: fornecer uma plataforma para que jovens mulheres possam aproveitar e aprofundar seu interesse em Ciencia da Computaˆ ção; incentivar mais jovens mulheres a competir em nível internacional; descobrir e apoiar jovens talentosas e criar modelos femininos; promover o intercambio cultural europeu e fomentar relaˆ ções amigaveis entre diferentes pa´ íses, concorrentes, educadores de informatica e cientistas da´ computação [EGOI 2025].

## 4. Resultados e Discussão

A CF-OBI apresentou um crescimento significativo em termos de inscrições e participação efetiva entre os anos de 2023 e 2024, como ilustrado na Figura 4. Esse aumento reflete o impacto positivo das estrategias´ de divulgação e engajamento adotadas pela organização, bem como o interesse crescente das estudantes em participar de competições de programação. Em 2023, o numero de inscri´ ções foi de 672 no Nível 1 (P1), 694 no Nível Junior (PJ) e 1260 no N´ ível 2 (P2). Ja em 2024, esses n´ umeros aumentaram para´ 953, 925 e 1997, respectivamente. Esse crescimento representa um aumento de 58,4% no Nível 2, que e o mais avan´ çado da competição, e de 41,8% no Nível 1, evidenciando o sucesso das ações de engajamento.

Figure 4. Inscritas x Participantes

Alem do aumento nas inscri´ ções, a participação efetiva tambem apresentou uma´ evolução significativa. Em 2023, o numero de participantes que efetivamente realizaram´ as provas foi de 158 no Nível 1, 91 no Nível Junior e 162 no N´ ível 2. Em 2024, esses numeros subiram para 197, 102 e 333, respectivamente.´ O crescimento mais expressivo foi observado no Nível 2, com um aumento de 105,5% na participação efetiva, o que demonstra que as estrategias de reten´ ção e motivação das participantes foram bem-sucedidas. As Figuras 5 e 6 apresentam a distribuição das participantes por ano e categoria.

Figure 5. Participantes x Ano

Figure 6. Categoria x Ano

Para o aprofundamento na analise dos resultados da CF-OBI, foram aplicados dois´ testes estatísticos adequados para amostras pequenas no cenario de an´ alise dos dois anos´ do evento. O primeiro foi o teste Qui-Quadrado, que avalia se ha uma rela´ ção significativa entre os anos da competição (2023 e 2024) e a participação efetiva das estudantes.

O teste Exato de Fisher, por sua vez, foi empregado como complemento, dada sua robustez em tabelas de contingencia com frequˆ encias esperadas baixas, inferiores aˆ 5, conforme preconizado por Fisher [Abdulrazak et al. 2020, Leal et al. 2005]. Este teste avalia a associação entre duas variaveis categ´ oricas, neste caso, o ano da competi´ ção e a categoria de participação (Programação Júnior - PJ, Nível 1 - P1, e Nível 2 - P2).

O teste Qui-Quadrado, aplicado ao conjunto de dados das tresˆ categorias (PJ, P1 e P2), resultou em um valor de estatística de 17,9632 e um p-valor de 0,0001. Este p-valor, inferior ao nível de significanciaˆ adotado (alfa = 0,05), indica uma associação estatisticamente significativa entre o ano da competição e a participação. Consequentemente, os resultados sugerem que o aumento no numero´ absoluto de participantes nao˜ e atribu´ ível ao acaso, mas reflete um padrao consistente de crescimento.˜

O teste Exato de Fisher foi aplicado separadamente para cada categoria (PJ, P1 e P2). Os resultados revelaram p-valores extremamente baixos para todas as categorias: 0,0005 para P1, 0,0000 para PJ e 0,0000 para P2. Estes p-valores, significativamente inferiores a 0,05, indicam uma mudança substancial na participação em todas as categorias entre os anos de 2023 e 2024.

Todas as categorias (P1, PJ, P2) mostraram mudanças significativas na participação entre os anos 2023 e 2024. Como os p-valores estao todos muito abaixo de 0.05, podemos˜ rejeitar a hipotese nula (que seria a de que n´ ao houve diferen˜ ça entre os anos), sugerindo que as mudanças observadas nas proporções de participantes entre 2023 e 2024 sao˜ significativas do ponto de vista estatístico.

O crescimento no numero total de participantes pode ser relevante do ponto de´ vista organizacional. No entanto, o crescimento proporcional ainda nao˜ e significativo´ estatisticamente, sugerindo que o aumento pode ter ocorrido devido a um maior numero de´ inscrições, e nao por uma melhoria na taxa de convers˜ ao de inscritas para participantes,˜ um ponto a ser observado e estimulado nos próximos anos.

## 5. Estratégias Futuras

Para as proximas´ edições da Competição Feminina da OBI (CF-OBI), e´ essencial implementar ações que consolidem e ampliem o impacto da iniciativa. Uma das principais estrategias ser´ a a coleta sistem´ atica de´ feedback das participantes, professores e organizadores. Esse processo permitira identificar pontos de melhoria na organiza´ ção, nos desafios propostos e na experiencia geral da competiˆ ção. A analise desse retorno ser´ a´ fundamental para ajustar as etapas do evento e garantir que ele continue atendendo as` expectativas e necessidades das competidoras.

Alem´ disso, a documentação detalhada de todas as etapas da competição sera´ priorizada. A criação de um manual de execução, que inclua desde o planejamento inicial ate a divulga´ ção dos resultados, permitira que o processo organizacional seja mais eficiente´ e replicavel. Esse material tamb´ em servir´ a como refer´ encia para futuras ediˆ ções, facilitando a integração de novos membros a` equipe organizadora e garantindo a continuidade da qualidade do evento.

## 6. Conclusão

A CF-OBI esta em crescimento significativo e esse crescimento reflete o impacto positivo´ de estrategias de divulga´ ção e engajamento, impactando no interesse das estudantes em participar de competições de programação.

Sao necess˜ arias muitas a´ ções e trabalho para a promoção da equidade nos proximos´ anos, porem,´ o movimento ja´ foi iniciado e os resultados começam a aparecer. E´ necessaria a promo´ ção de projetos educacionais para a preparação teorica e tecnol´ ogica das´ estudantes, assim como desenvolver iniciativas socioemocionais. E fundamental entender as perspectivas das participantes e das nao participantes, assim como das que participaram˜ e depois desistiram.

A CF-OBI demonstra ser uma iniciativa eficaz para promover a inclusao feminina˜ na computação, com um crescimento significativo na participação e impacto positivo no desenvolvimento de habilidades tecnicas. Para consolidar e ampliar esse impacto, sugere-se´ a implementação de estrategias como parcerias com institui´ ções educacionais e a coleta sistemática de feedback das participantes.

A competição oferece um ambiente acolhedor e oportunidades de desenvolvimento para as participantes, contribuindo como um ponto de partida importante para a redução da desigualdade de genero no campo da tecnologia, pois a transformaˆ ção estrutural requer ações contínuas ao longo da trajetoria´ academicaˆ e profissional. A continuidade e o aprimoramento da CF-OBI sao essenciais para consolidar essa iniciativa e inspirar mais˜ mulheres a seguirem carreiras na área de computação.

## 7. Agradecimentos

Agradecemos ao PPGCO da UFU pelo incentivo, ao comiteˆ da CF-OBI e OBI pelo fornecimento dos dados das Olimpíadas de Programação, bem como ao apoio as a` ções afirmativas.
