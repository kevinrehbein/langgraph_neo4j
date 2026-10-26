# Avaliação Retrospectiva da Experiência de uma Coorte de Egressas de um Curso de Introdução à Programação para Alunas do Ensino Médio e Concluintes

Juliana Martins Leoncio Eusebio Maria da Graça Campos Pimentel

1Instituto de Ciências Matemática e de Computação – Universidade de São Paulo

julianaleoncio@usp.br, mgp@icmc.usp.br

Abstract. This study combines quantitative and qualitative methods to analyze responses from 133 former participants (33% high school students and 67% graduates) to a questionnaire about their participation in short, online, and synchronous Introduction to Computing with Python courses offered between 2021 and 2024 as part of the Meninas Programadoras project. It identifies participation patterns and examines how inclusive initiatives help reduce the gender gap in technology. Results indicate associations between participation, selfconfidence, and interest in tech careers, with correlations among belonging, motivation, and interest in Computing. The analysis of open-ended responses reinforces these findings and highlights the impact on participants’ experiences.

Resumo. Esta pesquisa combina métodos quantitativos e qualitativos para analisar respostas de 133 egressas (33% alunas do ensino médio e 67% concluintes) a um questionário sobre sua participação em cursos curtos, online e síncronos de Introdução à Computação com Python, oferecidos entre 2021 e 2024 pelo projeto Meninas Programadoras. O estudo identifica padrões de participação e examina como iniciativas inclusivas ajudam a reduzir a lacuna de gênero em tecnologia. Os resultados indicam associação entre participação, autoconfiança e interesse por carreiras tecnológicas, com correlações entre pertencimento, motivação e interesse em Computação. A análise de questões abertas reforça esses achados e evidencia impacto na experiência das alunas.

## 1. Introdução

A desigualdade de gênero nas áreas de Ciência, Tecnologia, Engenharia e Matemática (STEM) é um fenômeno amplamente documentado. Por exemplo, em um estudo que teve como foco principal os EUA, [Kahn and Ginther 2017] destacam que estereótipos de gênero, cultura, ausência de modelos, competição, aversão ao risco e diferenças de interesse contribuem para a lacuna de gênero em STEM. Esses fatores atuam desde a infância, se consolidam no ensino fundamental e impactam a trajetória educacional e profissional, especialmente em áreas mais intensivas em matemática, nas quais preferências e aspectos psicológicos ajudam a explicar a sub-representação feminina. Essa desigualdade reflete um desafio mais amplo relacionado à participação de mulheres na ciência: a

> 1Do inglês Science, Technology, Engineering and Mathematics.

própria Organização das Nações Unidas instituiu o dia 11 de fevereiro como o International Day of Women and Girls in Science, reforçando a importância de ações voltadas à inclusão e ao empoderamento feminino nas carreiras científicas e tecnológicas.

No Brasil, [Pessoa et al. 2021] apontam que meninas no ensino básico tendem a evitar carreiras STEM por conta de estereótipos e da baixa autoconfiança em disciplinas como Matemática. A associação dessas áreas a uma cultura majoritariamente masculina contribui para sua sub-representação. Trabalhos como os de [Menezes and Santos 2021] e [Santos et al. 2017] mostram que a percepção de inadequação afeta a autoimagem das alunas, orientando-as para áreas tradicionalmente vistas como femininas.

Embora a presença feminina no ensino superior tenha crescido, as mulheres seguem sub-representadas em cursos e profissões de Ciência da Computação e Engenharia, compondo cerca de 15% das matrículas no Brasil [IBGE 2022] e menos de 30% da força de trabalho em STEM globalmente [UNESCO 2020]. Essa disparidade não apenas compromete a equidade de oportunidades, mas também limita a diversidade de perspectivas necessária para a inovação tecnológica. Estudos mostram que equipes diversas têm maior capacidade de resolver problemas complexos, gerar lucro e promover soluções mais inclusivas [McKinsey & Company 2020, Harvard Business Review 2021]. No entanto, barreiras como estereótipos, ambientes pouco acolhedores e a ausência de modelos femininos dificultam a entrada e permanência de mulheres na tecnologia [Fórum Econômico Mundial 2021, Society of Women Engineers 2022].

Diversas iniciativas vêm sendo desenvolvidas para promover a equidade de gênero na tecnologia. Esforços como o Programa Meninas Digitais da Sociedade Brasileira de Computação, e o ACM-W, da Association for Computing Machinery, incentivam meninas do ensino médio a explorar a Computação como caminho acadêmico e profissional. No Instituto de Ciências Matemáticas e de Computação, da Universidade de São Paulo, iniciativas como o GRupo de Alunas de Ciências Exatas (GRACE) e o Women in Tech (WiT) também atuam na promoção da inclusão e do empoderamento feminino nas ciências exatas.

O projeto Meninas Programadoras, criado como atividade de extensão em 2021 no Instituto de Ciências Matemáticas e de Computação, da Universidade de São Paulo, tem como objetivo reduzir a lacuna de gênero na Computação por meio de cursos introdutórios à programação com Python os quais têm curta duração (um mês) e são totalmente gratuitos e online. Desde sua criação, o projeto já formou mais de 1.700 alunas. O curso combina aulas e monitorias síncronas e listas de exercícios obrigatórias corrigidas automaticamente. A linguagem Python foi escolhida por sua acessibilidade a iniciantes e ampla aplicabilidade em diversos contextos [Cutting and Stephen 2021, Castro et al. 2023, Dierbach 2014].

O curso é voltado a pessoas que se identificam como mulheres, e também acolhe pessoas não binárias interessadas em um ambiente inclusivo e de equidade de gênero. Em caso de excedente de inscrições, priorizam-se estudantes do ensino médio e de escolas públicas, sem exigência de conhecimentos prévios. Monitorias síncronas são oferecidas

> 2https://www.un.org/en/observances/women-and-girls-in-science-day

> 3https://meninas.sbc.org.br/

> 4https://women.acm.org/

em diferentes turnos, totalizando cerca de 40 horas semanais, para garantir flexibilidade e apoio contínuo. A maioria das pessoas monitoras são estudantes de graduação da área de Computação, servindo como modelos próximos às alunas, sendo que a maioria se identifica com o gênero feminino.

Além do conteúdo técnico, o projeto visa desenvolver competências interpessoais, como autoconfiança e criatividade, em um ambiente acolhedor que permita às participantes se sentirem seguras para explorar uma área predominantemente masculina. A cada edição, alunas de diferentes regiões do país participam de aulas síncronas, com atividades interativas e suporte contínuo de uma equipe de monitoria composta majoritariamente por mulheres da área de STEM.

As aulas acontecem em quatro tardes de sábado. O conteúdo inclui a estrutura básica de um computador, variáveis e estruturas condicionais, estruturas de repetição e listas. No quinto sábado, as alunas realizam uma prova final, com possibilidade de prova de recuperação. O desempenho é avaliado com base em atividades obrigatórias, sendo necessário alcançar nota mínima para receber o certificado de conclusão oficial da Universidade de São Paulo.

O presente estudo tem como objetivo analisar os impactos do projeto Meninas Programadoras com foco em uma coorte de egressas que responderam a um questionário retrospectivo. Busca-se identificar padrões de envolvimento e perfis de participantes que mais se beneficiaram do curso, bem como investigar como a experiência influenciou suas escolhas acadêmicas e profissionais.

A pesquisa adota uma abordagem quantitativa e qualitativa, com base em respostas voluntárias a um questionário online. A coleta e análise seguiram diretrizes éticas aprovadas por Comitê de Etica em Pesquisa, com anonimização e padronização dos dados. A análise quantitativa envolveu estatísticas descritivas e cálculo de correlações. A análise qualitativa seguiu categorização temática e foi complementada por técnicas de Processamento de Linguagem Natural (PLN), incluindo modelagem de tópicos com BERTopic, utilizando ferramentas como Python e bibliotecas de visualização de dados.

Os resultados apresentados nas próximas seções contribuem para a compreensão dos efeitos de iniciativas educacionais inclusivas na trajetória de alunas do ensino médio e concluintes que participaram do curso Meninas Programadoras, oferecendo subsídios para o aprimoramento contínuo do projeto e para a formulação de políticas e práticas voltadas à promoção da equidade de gênero na área de tecnologia.

No restante deste texto, a Seção 2 aponta para trabalhos relacionados, a Seção 3 sumariza a metodologia da pesquisa realizada, a Seção 4 apresenta resultados obtidos e Seção 5 sumariza as contribuições e limitações do estudo.

## 2. Trabalhos Relacionados

Vários estudos analisam a presença e os desafios enfrentados por mulheres na Computação. [Beaubouef and Zhang 2011] investigam motivações e obstáculos vivenciados por alunas de Ciência da Computação em duas universidades, buscando compreender os fatores que influenciam sua escolha e permanência na área. No contexto

brasileiro, [Oliveira et al. 2014] analisam o perfil de mais de 1.700 estudantes e profissionais de Computação e identificam a recorrência de preconceito de gênero, especialmente entre as profissionais. A percepção de que Computação é “coisa de homem” também aparece nos depoimentos de alunas do ensino médio analisados por [Aires et al. 2018], que propuseram ações práticas para combater essa visão. A revisão sistemática de [Menezes and Santos 2021] confirma que estereótipos de gênero ainda moldam negativamente a trajetória feminina na área, e [Figueiredo et al. 2016] descrevem ações de extensão regionais para estimular a entrada de meninas em Computação e Tecnologia.

Diversas iniciativas têm sido desenvolvidas com foco na promoção da igualdade de gênero em tecnologia. [Surmani et al. 2024], que atuam com meninas com idade entre 9 e 14 anos, combinam ensino técnico e questões socioemocionais e apontam bons resultados. [Zdawczyk and Varma 2023] observaram que linguagens baseadas em blocos, como Scratch, podem ser mais eficazes do que linguagens textuais na promoção de autoeficácia e interesse em Computação entre meninas do ensino fundamental e médio.

Focando em alunas de graduação dos anos iniciais de cursos de graduação em áreas técnicas, [Rodriguez et al. 2024] oferecem um programa de capacitação em desenvolvimento de software que tem sido bem sucedido. [Heinzmann et al. 2016] apresentam um projeto voltado para alunas do ensino médio que inclui a criação, pelas próprias alunas, de objetos de aprendizagem. Estratégias similares são exploradas por [Mattos et al. 2018], com oficinas de programação, e por [Oliveira et al. 2018], com oferecem um curso curto remoto de Python para um público que inclui jovens mulheres, mães, mulheres casadas e estudantes (meninas e meninos).

Iniciativas internacionais, como os esforços de [Ç akir et al. 2017] que utilizam oficinas de design de jogos para fortalecer o interesse e a confiança de meninas em Computação, e o de [Wang et al. 2020], que oferecem cursos de Python para alunas do ensino médio, reforçam a importância de ambientes interativos para o ensino de programação a meninas.

## 3. Metodologia

A coleta de dados foi realizada por meio de um questionário aplicado às alunas aprovadas no curso Meninas Programadoras, contendo perguntas de múltipla escolha, escala Likert e questões abertas. O questionário foi estruturado para investigar a experiência das participantes, seu desempenho e o impacto do curso em suas trajetórias. A pesquisa foi aprovada por Comitê de Etica em Pesquisa (CAAE: 85326324.2.0000.5390), e empregou formulários online para a obtenção dos Termos de Consentimento/Assentimento Livre e Esclarecido (TCLE/TALE) e para o questionário de pesquisa.

Os dados coletados passaram por um processo de tratamento e padronização. Respostas de campo aberto, como nomes de cidades e estados, foram revisadas e normalizadas para garantir consistência. Informações pessoais que poderiam identificar diretamente as participantes foram removidas, assegurando a privacidade das respondentes. Esse cuidado foi essencial para garantir uma análise ética e confiável.

Para compreender a percepção das alunas em relação ao curso, a análise quantitativa baseou-se em estatísticas descritivas das respostas numéricas obtidas por meio da escala Likert (de 1-Discordo Totalmente a 5-Concordo Totalmente ), além de dados sobre idade, região de residência e tipo de escola das participantes. Análises estatísticas e

correlações investigaram a percepção das alunas sobre o curso, incluindo sentimentos de pertencimento e autoconfiança no aprendizado de programação. Esses dados permitiram delinear o perfil das participantes e avaliar os impactos do curso em diferentes dimensões.

A escala Likert permitiu captar o grau de concordância ou satisfação das participantes sobre diferentes aspectos do programa, como qualidade do conteúdo, didática da equipe e impacto do curso na aprendizagem. As questões de escala Likert foram:

1. O curso me ajudou a superar inseguranças em relação à programação

2. Senti-me desafiada de forma positiva durante o curso

3. Sinto-me confiante para resolver problemas relacionados à programação após o curso

4. As atividades do curso aumentaram minha capacidade de resolver problemas de modo geral, inclusive fora da Computação

5. Durante o curso, senti-me parte de uma comunidade de apoio

6. A interação com colegas foi motivadora

7. A interação com monitores foi motivadora

8. A interação com a professora foi motivadora

9. O curso me influenciou a seguir na área de Computação

10. O curso me influenciou a seguir na área de Exatas

11. Recomendei os cursos Meninas Programadoras para outras meninas

A análise qualitativa foi conduzida a partir das respostas abertas do questionário, que foram agrupadas por meio de categorização temática. As respostas foram revisadas manualmente e organizadas em categorias como impacto na escolha profissional, apoio recebido, dificuldades enfrentadas e sugestões de melhoria. Essa abordagem permitiu explorar aspectos subjetivos da experiência das alunas e complementar os dados quantitativos com narrativas pessoais. Para a coleta, tratamento e análise dos dados, foram utilizadas ferramentas como Google Forms, Python, Pandas, Matplotlib e Seaborn no ambiente Google Colab.

Complementando a análise qualitativa, foi adotada uma abordagem híbrida com técnicas de Processamento de Linguagem Natural (PLN), incluindo a modelagem de tópicos com BERTopic [Grootendorst 2022]. Essa biblioteca aplica embeddings gerados pelo modelo Bidirectional Encoder Representations from Transformers (BERT), redução de dimensionalidade com Uniform Manifold Approximation and Projection (UMAP), agrupamento com Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN), e nomeação de tópicos com class-based Term Frequency–Inverse Document Frequency (c-TF-IDF). Para gerar os embeddings, foi utilizada a variante all-mpnet-base-v2, atualmente considerada uma das mais eficazes em tarefas semânticas, conforme documentado por [Reimers and Gurevych 2024]. O pré-processamento textual foi realizado com o suporte das bibliotecas Natural Language Toolkit (NLTK) [Bird et al. 2009] e SentenceTransformer. As etapas incluíram a remoção de stopwords, lematização e normalização de termos, com tratamento de plurais e sinônimos. Essas etapas garantiram que termos semanticamente equivalentes fossem agrupados de forma consistente, aprimorando a qualidade dos agrupamentos temáticos.

> 6Em BERTopic, o c-TF-IDF adapta o cálculo do TF-IDF tradicional para destacar termos relevantes em nível de tópico, e não apenas de documento.

> 7https://www.sbert.net/docs/sentence_transformer/pretrained_models.html

## 4. Resultados

Perfil das Alunas. O questionário foi enviado a todas as concluintes aprovadas (mais de 1.700 alunas) e foi respondido por 133 participantes até 22/02/2025. Do total de respondentes, 33% ainda estavam cursando o ensino médio no momento da participação no projeto, enquanto 67% já haviam concluído essa etapa. A maioria das respondentes tem entre 18 e 24 anos, é oriunda de escolas públicas (65%) e reside principalmente nos estados de São Paulo e Minas Gerais. A natureza online do curso permitiu ampla participação geográfica — sendo 10 estados de quatro regiões do Brasil representados — reforçando o potencial de alcance do programa para alunas de diferentes regiões do país.

Egressas em Cursos Superiores. Entre as participantes que informaram sua situação acadêmica no momento em que respondiam o questionário, 48,6% estavam cursando graduações na área de Exatas, sendo 42,1% especificamente em Computação. Embora os dados possam refletir um viés de resposta, já que é provável que tenham respondido as mais interessadas no tema, a proporção observada sugere que o programa tem alcançado seu objetivo de incentivar meninas a seguir trajetórias acadêmicas nessa área.

Tendências e Distribuição das Avaliações. A análise incluiu a distribuição das respostas para cada questão, permitindo identificar padrões e tendências nas avaliações. Essa abordagem permitiu identificar tendências nas avaliações, destacando os aspectos mais bem avaliados e aqueles que podem ser aprimorados. As respostas às perguntas de escala Likert, sintetizadas na Figura 1, mostraram alta satisfação com o curso: 83,1% recomendaram o programa, 82,3% sentiram-se positivamente desafiadas e mais de 70% destacaram a motivação advinda da interação com colegas, monitores e professora. O curso influenciou 55,4% das respondentes a seguirem na área de Computação e ampliou habilidades de resolução de problemas para 56,2% das alunas. Ainda assim, parte das alunas demonstrou necessidade de reforço na confiança para programar.

Figura 1. Distribuiç ão Percentual das Respostas nas Questões Likert

Análise por Faixa Etária. A análise por idade revelou diferenças sutis: alunas menores de 18 relataram maior sensação de desafio, enquanto as acima de 34 anos destacaram maior influência do curso na decisão profissional. A única diferença estatisticamente significativa ocorreu na questão “Senti-me desafiada de forma positiva durante o curso” ( χ = 19. 30, p = 0. 02). O teste post-hoc revelou que a principal diferença estava entre as participantes “Entre 18 e 24 anos” e “Acima de 34 anos” ( p corrigido = 0. 17), sugerindo que as mais jovens sentiram-se mais desafiadas em comparação às mais velhas.

Análise de Correlação. A análise da matriz de correlação revelou relações interessantes entre os aspectos do curso. Por exemplo, sentir-se desafiada positivamente correlacionouse fortemente com a motivação transmitida pela professora (r ≈ 0.64), e o sentimento de pertencimento com a interação entre colegas (r ≈ 0.64). A influência do curso nas áreas de Computação e Exatas apresentou correlação ainda mais forte (r ≈ 0.74), enquanto a relação entre autoconfiança e recomendação do curso foi mais fraca (r ≈ 0.24), sugerindo dimensões distintas de engajamento.

Figura 2. Matriz de Correlaç ão das Respostas de Questões com Escala Likert

Feedback Aberto das Participantes. Primeiramente, foi realizada uma leitura exploratória das respostas, seguida pela identificação de padrões e palavras mais recorrentes em cada categoria. Essa análise permitiu extrair os principais temas abordados pelas alunas, destacando as atividades mais e menos apreciadas, dificuldades encontradas, diferenciais do curso, impactos na formação acadêmica e profissional, além de sugestões de melhoria.

> 8Como em outras pesquisas em Educação e Interação Humano-Computador, a análise de dados de questionário reflete percepções subjetivas, sendo comum adotar critérios flexíveis para correlações: 0,10 (fraca), 0,30 (moderada) e 0,50 (forte), conforme [Ivie and MacKay 2024].

Em relação às atividades mais apreciadas, diversas participantes mencionaram exercícios que estimulavam o pensamento lógico e matemático. Eles foram particularmente valorizados, pois proporcionaram maior aprendizado e autonomia na resolução de problemas. Além disso, atividades práticas que exigiam a aplicação de conceitos aprendidos ao longo do curso foram mencionadas como essenciais para o desenvolvimento da confiança na programação. Uma aluna destacou essa experiência ao afirmar:

Apreciei muito a lógica de programação, porque foi dali que eu pude entender a parte de exatas e da tecnologia. E eu fui buscando mais conhecimento através dessas atividades!

Já quando questionadas sobre as atividades menos apreciadas, muitas participantes indicaram não haver atividades que considerassem negativas. No entanto, exercícios que envolviam manipulação de strings foram apontados como desafiadores, pois exigiam um nível de abstração maior. O formato das aulas também foi citado, como no exemplo:

Muitas horas seguidas de aulas, isso dificulta na absorção do conteúdo.

As dificuldades mais citadas ao longo do curso estavam relacionadas à compreensão da lógica de programação e ao uso de estruturas de repetição, como o laço for-in. Algumas alunas mencionaram que, no início, tiveram dificuldades para entender como estruturar soluções para problemas computacionais, mas destacaram que a prática constante ajudou a superar essas barreiras. A dedicação exigida também foi lembrada, e.g.:

Me disciplinar a estudar um pouco todos os dias.

Ao serem questionadas sobre o principal diferencial do curso, as respostas indicaram que a didática utilizada, o suporte oferecido pelas instrutoras e monitoras, e a sensação de fazer parte de um ambiente acolhedor foram aspectos fundamentais. Além disso, muitas participantes mencionaram que o curso proporcionou um espaço seguro para aprendizado, onde puderam experimentar e errar sem medo, o que contribuiu significativamente para seu desenvolvimento. O modelo acessível foi destacado, como em:

A acessibilidade.

No que se refere ao impacto acadêmico e profissional, várias alunas relataram que o curso influenciou diretamente suas escolhas acadêmicas e despertou um maior interesse pela área de tecnologia. Algumas participantes mencionaram que, após o curso, sentiramse mais confiantes para continuar estudando programação e considerar a Computação como uma possível carreira. Uma participante compartilhou:

Eu creio que me faltava a pergunta “Você já pensou em fazer um curso de exatas?” pra me fazer considerar a área, e esse curso fez isso pra mim, além de me mostrar todas as possibilidades da computação. Hoje estou fazendo graduação em Ciências da Computação [...]

Por fim, ao serem solicitadas a sugerir melhorias para o curso, as respostas indicaram que algumas alunas gostariam de ter mais desafios e exemplos práticos, além de explicações mais detalhadas para determinados conceitos. No geral, as sugestões apontam para um desejo de aprofundamento dos conteúdos abordados, evidenciando o impacto positivo que o curso teve na motivação das participantes. Algumas alunas solicitaram explicitamente mais material e orientações para continuidade, como no exemplo:

Mais material de apoio e indicações de como continuar estudando sozinha

Assim, a análise qualitativa revelou que os exercícios práticos, especialmente de lógica e resolução de problemas, foram os mais valorizados. As principais dificuldades estiveram relacionadas à lógica, repetição e tempo de estudo. O diferencial mais citado foi o ambiente acolhedor e a presença feminina na equipe. Várias alunas relataram que o curso influenciou diretamente suas escolhas acadêmicas. As sugestões de melhoria incluíram mais exemplos, apoio e continuidade. Essas respostas estão em consonância com as identificadas pela análise de tópicos com PLN, sumarizada a seguir.

Análise de Tópicos com PLN. A modelagem de tópicos por BERTopic complementou os achados manuais, identificando um total de 28 tópicos para as questões abertas. A Tabela 1 apresenta o tópico com maior número de ocorrências para cada questão identificando como temas principais: lógica e desafios como favoritos; dificuldades com abstração e tempo; valorização do ambiente seguro e feminino; e impacto na autoconfiança e interesse pela área. Os exemplos extraídos ilustram e reforçam os padrões previamente identificados na análise qualitativa.

Tabela 1. Primeira frase representativa no tópico com maior ocorrências em cada pergunta, do total de 28 tópicos. Q/T: quantidade de ocorrências no tópico.

|Pergunta|Q/T|Primeira frase representativa do tópico com Maior número de ocorrências|
|---|---|---|
|Quais atividades ou exercícios do curso você mais apreciou? Explique|23|Resolver os exercícios no Beecrowd. Foi muito instigante e divertido.|
|Quais atividades ou exercícios do curso você menos gostou? Porquê?|128|Não tive o problema de nao gostar de alguma atividade por algum motivo externo, apesar de ter algumas dificuldades na realizaç ão algumas vezes, nenhuma foi motivadapela estrutura oferecidapelo curso|
|Quais foram as principais dificul- dades que você encontrou no curso?|48|A quantidade de horas em um sábado eram um pouco puxadas, entretanto acredito ter sido o necessário para ter um aprendizado intensivo.|
|Para você, qual foi o prin- cipal diferencial do curso Meninas Programadoras?|76|Um ambiente completamente cheio de garotas buscando aprender, com orientadores mulheres e a professora. Sempre me senti solitária e tímida em curso de exata sendo uma das poucas meninas, não conseguia encontrar uma forma de me apoiar quando queria desistir. Ter monitorias também foi algo que fez uma grande diferença, afinal, mesmo que não conseguisse entender na aula de sábado,acabava tendo um apoio com os monitores.|
|Como o curso impactou sua formaç ão ou escolhas acadêmicas e profissionais? (relate brevemente)|26|Anterior ao curso, pensei seriamente em desistir da área, mesmo com pouca idade me sentia pouco evoluída quando me comparava com outras pessoas. Mas isso mudou depois do curso, finalmente encontrei uma linguagem na qual eu genuinamente gostava, e passei a não achar todas as outras tao complicadas. Comecei a estudar muito mais por conta própria e até me arriscar emprojetos solos. Decidique realmentequero essa area...|
|O que você sugere para melho- rar o Meninas Programadoras?|97|Gostaria que colocassem outros cursos como javascript, banco de dados, etc.|

## 5. Conclusão

Este estudo avaliou o impacto do curso Meninas Programadoras a partir de análises quantitativas e qualitativas com alunas egressas, revelando efeitos concretos e positivos na confiança e no interesse das participantes pela Computação. O curso tem se mostrado eficaz ao introduzir conteúdos técnicos de forma acessível e ao proporcionar experiências práticas que contribuem para o desenvolvimento da autonomia na resolução de problemas.

As interações com colegas, monitoras e instrutoras foram apontadas como um dos principais diferenciais da iniciativa. Esses vínculos formam uma rede de apoio que

fortalece o sentimento de pertencimento e engajamento, criando um ambiente acolhedor e motivador — especialmente importante para meninas em início de contato com a área de tecnologia. A formação dessa comunidade de incentivo é um dos pilares para promover a permanência feminina na Computação.

As atividades práticas foram amplamente valorizadas, em especial aquelas focadas em lógica e resolução de problemas. Entretanto, o curso ainda apresenta desafios relacionados ao ensino de conceitos mais abstratos, como estruturas de repetição e manipulação de strings. Tais dificuldades indicam oportunidades de aprimoramento metodológico, por meio de recursos didáticos complementares e estratégias de reforço que ajudem a consolidar a aprendizagem desses tópicos.

O impacto do curso nas escolhas acadêmicas e profissionais também se destacou nos relatos das participantes. Muitas respondentes mencionaram que passaram a considerar, ou reforçaram sua decisão de seguir, uma trajetória na área de Computação. Esses resultados evidenciam o potencial transformador da iniciativa na vida das participantes, reforçando a importância de políticas e programas que promovam a equidade de gênero em áreas historicamente masculinas.

Com base nesses achados, recomenda-se a ampliação do suporte oferecido pelas monitoras, bem como a criação de conexões com projetos mais avançados, para oferecer novos desafios a alunas com conhecimento prévio em programação. Essa continuidade pode contribuir para manter o engajamento e aprofundar a trajetória formativa dessas jovens.

Trabalhos futuros podem explorar análises mais refinadas, segmentando as alunas por escolaridade, experiência anterior com programação e áreas de interesse acadêmico. Além disso, comparações longitudinais entre turmas de diferentes anos poderão oferecer subsídios para avaliar a evolução do curso e guiar melhorias contínuas.

Embora os resultados sejam promissores, é importante reconhecer algumas limitações. A amostra analisada teve predominância de alunas de turmas recentes, o que restringe a compreensão dos efeitos de longo prazo do curso. Além disso, é possível que o questionário tenha sido respondido principalmente por alunas mais engajadas ou positivamente impactadas, gerando um viés de autoseleção nos dados analisados. O processo de submissão ao Comitê de Etica, apesar de essencial para garantir os princípios éticos e a privacidade das participantes, também impôs ajustes e atrasos na coleta.

Por fim, os dados indicam que o curso está alinhado aos seus objetivos. Entre as alunas que responderam sobre sua situação acadêmica, 48,6% estão matriculadas em graduações da área de Exatas, sendo 42,1% especificamente em cursos de Computação. Ainda que esse resultado esteja sujeito a viés de resposta, ele reforça a conclusão de que o Meninas Programadoras tem sido efetivo em ampliar o interesse e a presença de meninas na tecnologia.

Em síntese, o Meninas Programadoras tem desempenhado um papel fundamental não apenas na formação técnica de suas participantes, mas também na construção de um ambiente de acolhimento e pertencimento. Essa combinação tem se mostrado essencial para fortalecer a presença dessas alunas na Computação e contribuir para uma tecnologia mais diversa e inclusiva.

## Agradecimentos

Agradecemos às alunas que participaram do projeto Meninas Programadoras desde 2021, em especial às que contribuíram diretamente com esta pesquisa ao responderem ao questionário e compartilharem suas experiências. Agradecemos também os monitores, bolsistas e voluntários, cuja parceria e dedicação foram essenciais para o desenvolvimento das atividades e para a realização deste estudo. Agradecemos ainda o programa PUB da Universidade de São Paulo.
