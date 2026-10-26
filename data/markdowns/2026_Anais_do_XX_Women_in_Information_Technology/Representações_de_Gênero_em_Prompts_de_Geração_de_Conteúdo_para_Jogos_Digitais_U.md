# Representações de Gênero em Prompts de Geração de Conteúdo para Jogos Digitais: Uma Análise Preliminar Envolvendo Profissionais da Indústria

Emily Lopes Almeida, Gláucia Braga e Silva, Thais Regina de M. B. Silva

1Instituto de Ciencias Exatas e Tecnológicas – Universidade Federal de Viçosa (UFV) 35.690-000 – Florestal – MG – Brazil

{ emily.almeida,glaucia,thais.braga } @ufv.br

Resumo. O avanço da IA generativa tem ampliado o uso de prompts para geração de conteúdo em diferentes áreas, incluindo o desenvolvimento de jogos digitais. Este trabalho apresenta uma análise exploratória preliminar de prompts elaborados por profissionais da indústria de jogos para criação de personagens, narrativas e elementos sonoros. Os dados foram coletados por meio de um formulário online no qual os participantes criaram prompts para um jogo hipotético. A análise preliminar dos textos dos prompts indicou diferenças na forma como características e ações são atribuídos a personagens de diferentes gêneros, sugerindo a presença de padrões narrativos e possíveis vieses de representação.

Palavras-chave: viés de gênero, IA generativa, desenvolvimento de jogos digitais.

## 1. Introdução

O uso de inteligência artificial (IA) em jogos digitais tem se expandido significativamente nos últimos anos, oferecendo novas possibilidades para o design e a experiência do usuário. O trabalho de [Yang et al. 2025] destaca que a IA tem sido aplicada em cinco principais etapas nesse contexto: geração procedural de conteúdo, design de jogos com iniciativa mista, jogabilidade com iniciativa mista, jogar de forma autônoma e pesquisa com usuários. Essas aplicações evidenciam o potencial das IAs generativas não apenas para automatizar processos criativos, mas também para ampliar a interatividade e a personalização na experiência do jogador.

Evidenciando o risco de reprodução de vieses presentes nos dados de treinamento, observa-se que, embora essa tecnologia traga benefícios ao desenvolvimento de jogos, há preocupação de que IAs generativas reforcem desigualdades, especialmente na representação de gênero [Batista et al. 2025]. Nesse contexto, mesmo diante de uma proporção semelhante entre os gêneros dos jogadores, personagens femininas permanecem sub-representadas e frequentemente retratadas de forma estereotipada e sexualizada [Viana et al. 2025].

Diante desse cenário, torna-se fundamental compreender não apenas como as IAs generativas são aplicadas no desenvolvimento de jogos, mas também como as instruções fornecidas aos modelos são formuladas. O prompt, enquanto interface entre humano e IA, influencia diretamente no conteúdo gerado. No entanto, a maior parte das pesquisas sobre prompt engineering e vieses em modelos de linguagem concentra-se na língua inglesa,

havendo poucos estudos dedicados a análise da formulação de prompts em língua portuguesa [Assi and Caseli 2024, Candido et al. 2025]. Essa lacuna torna-se especialmente relevante, já que o português apresenta marcação de gênero em substantivos e adjetivos, o que pode influenciar a forma como conteúdos são gerados por IA, uma vez que elementos da própria língua podem já trazer consigo vieses implícitos.

Analisar como profissionais da área de jogos digitais formulam prompts é fundamental, uma vez que eles ocupam posições estratégicas no processo criativo. Designers, roteiristas, desenvolvedores e produtores traduzem conceitos estéticos e narrativos em instruções para as IAs generativas, influenciando diretamente a construção de personagens, ambientações e sons. Nesse sentido, a análise desses prompts possibilita observar se padrões já consolidados na indústria, como determinados enquadramentos de personagens ou associações recorrentes de atributos, também se manifestam na etapa de instrução, antes mesmo da geração automatizada do conteúdo. Essas análises estão alinhadas ao uso responsável de IA no contexto do desenvolvimento de jogos digitais, conforme previsto nas diretrizes da Ethical Games Initiative e também vai ao encontro, no contexto brasileiro, às exigências do recém-aprovado estatuto ECA Digital (Lei 15.211/2025).

Por esses motivos, este estudo objetiva investigar a presença e a distribuição de termos gênero-dependentes em prompts utilizados para geração de conteúdo em jogos digitais, analisando diferenças entre as dimensões de personagens, narrativa e sons. Para fins desta pesquisa, consideram-se termos gênero-dependentes aqueles que apresentam marcação morfológica explícita de gênero gramatical ou que semanticamente indiquem referência à identidade de gênero. Em línguas como o português, essa distinção pode ser compreendida a partir da diferença entre gênero gramatical e gênero semântico, conforme discutido por [Muñoz-García et al. 2025]. No primeiro caso, o gênero é marcado morfologicamente na própria estrutura da palavra, geralmente por meio de sufixos, como em guerreiro/guerreira ou aventureiro/aventureira. Já no segundo caso, o gênero é indicado pelo significado da palavra, como em termos que fazem referência direta a identidades de gênero, por exemplo homem, mulher, menino ou menina.

- Para guiar o trabalho e atingir o objetivo proposto, as seguintes questões de pes-

- quisa foram delimitadas: • QP1: Como termos gênero-dependentes são utilizados na descrição de personagens e seus atributos em prompts para jogos digitais?

 - QP2: De que forma termos gênero-dependentes se manifestam na construção narrativa dos prompts, considerando a definição de protagonistas, papéis e ações?

 - QP3: Como termos gênero-dependentes são utilizados na descrição de elementos sonoros, como voz e música?

O restante do artigo está organizado da seguinte forma: a Seção 2, apresenta os trabalhos relacionados; a Seção 3 descreve os materiais e métodos adotados na pesquisa; a Seção 4 discute os resultados obtidos a partir das três questões de pesquisa; e, por fim, a Seção 5 apresenta as conclusões do estudo.

## 2. Trabalhos Relacionados

Diversos estudos utilizam os prompts como variável para investigar a emergência de vieses em modelos generativos. Nesse contexto, a seleção dos trabalhos relacionados apre-

> 1https://ethicalgames.org/

sentados nesta seção foi conduzida a partir de uma busca exploratória em bases de dados acadêmicas amplamente utilizadas na área de Computação, incluindo o Google Scholar, IEEE Xplore e ACM Digital Library. O processo de pesquisa empregou combinações de termos relacionados ao tema investigado, tais como ”prompts”, ”games”, ”artificial intelligence”, ”generative AI”e ”bias”. Como critérios de seleção, foram priorizados estudos publicados nos últimos anos, revisados por pares e diretamente relacionados à análise de vieses, representação de personagens ou influência de prompts em sistemas generativos aplicados a jogos digitais.

Nessa linha, o trabalho de [Muñoz-García et al. 2025] propõe uma metodologia para quantificar o viés de gênero em LLMs, como GPT-4, Llama 3 e Gemini, especificamente para a língua espanhola, que possui gênero gramatical marcado. Os autores demonstram que a forma como o prompt é estruturado altera significativamente a resposta, os prompts não indutores (neutros) tendem a gerar conteúdos com viés masculino, enquanto prompts indutores (que sugerem um tópico de gênero) podem levar modelos a produzirem saídas com viés feminino. O estudo utiliza análises de coocorrência e polaridade para evidenciar que os modelos ainda recorrem para estereótipos de gênero na produção textual automatizada.

De forma semelhante, a pesquisa de [Wu et al. 2024] aprofunda a análise ao investigar como o viés de gênero se propaga por todas as etapas da geração de imagens no Stable Diffusion, desde o espaço do prompt até o processamento interno do modelo. Utilizando ” prompts em trio”(neutro, feminino e masculino), os pesquisadores confirmam a tendência quantitativa de que ”pessoa = homem”, uma vez que prompts neutros geram imagens e representações internas muito mais próximas das masculinas. Além da representação humana, o estudo revela que objetos não especificados (como cenários e vestimentas) variam drasticamente conforme o gênero indicado: homens são associados a esportes e ferramentas, enquanto mulheres aparecem ligadas a contextos de cuidado e alimentação.

Outra vertente investiga a engenharia de prompts como mecanismo de mitigação de vieses, no estudo de [Sant et al. 2024] exploraram o viés de gênero na tradução automática do inglês para o catalão e espanhol, observando que os LLMs base tendem a apresentar níveis de viés mais elevados do que os modelos tradicionais de Tradução Automática Neural (NMT). Para enfrentar esse problema, os autores testaram diversas técnicas de prompt, como few-shot, fornecimento de contexto e Chain-of-Thought (CoT). Os resultados demonstraram que uma abordagem de CoT curta e simplificada, combinada com cinco exemplos contendo conteúdo antiestereotípico e maior representação feminina, foi a mais eficaz, reduzindo o viés em até 12,4% no conjunto de dados WinoMT. O estudo concluiu que descrever o problema do viés ou usar instruções detalhadas não era tão eficiente quanto o uso de esquemas de raciocínio simplificados que guiam o modelo passo a passo.

No trabalho de [Valov 2025], é proposta uma abordagem que relaciona o design de prompts com conceitos da teoria da informação e da teoria dos jogos. O autor define o prompt não apenas como uma instrução ou pergunta, mas como um operador simbólico fundamental que inicializa uma ”curvatura”de pensamento, definindo o que é assumido, enfatizado ou omitido na interação entre usuário e IA. Essa perspectiva é relevante para estudos sobre vieses, pois sugere que a forma como um prompt é formulado pode direcionar o modelo a reproduzir determinados padrões ou interpretações. Assim, vieses podem surgir quando certos contextos ou pressupostos presentes no prompt favorecem interpretações estereotipadas. Nesse sentido, o design de prompts pode ser visto também como uma prática ética, na medida em que escolhas linguísticas mais cuidadosas podem contribuir para reduzir distorções e evitar o reforço de estereótipos na geração de conteúdo por sistemas de IA.

No contexto específico de vieses de gênero em jogos digitais, [Viana et al. 2025] realizaram um estudo comparativo entre o DALL-E 3 e o Llama 3, analisando tanto o viés de representação (quantidade) quanto o de apresentação (estereótipos). Os resultados indicam uma grave sub-representação feminina: quando solicitadas a gerar ”protagonistas”de forma neutra, a ferramenta DALL-E 3 apresenta 0% de mulheres. Ademais, o trabalho destaca um alto índice de sexualização e objetificação das personagens femininas geradas, reforçando padrões prejudiciais da indústria de jogos e evidenciando a incapacidade das IAs atuais de oferecer representações diversas e éticas sem intervenções diretas nos comandos.

Em conjunto, os trabalhos revisados reforçam que o prompt não é apenas mecanismo de entrada textual, mas desempenha um papel central na manifestação, propagação e mitigação de vieses em sistemas generativos, influenciando diretamente tanto o conteúdo quanto a forma que as respostas são produzidas. Assim como observado nesses estudos, este trabalho também identifica que mudanças na formulação dos prompts podem impactar a representação de gênero. No entanto, enquanto pesquisas como as de [Muñoz-García et al. 2025] e [Wu et al. 2024] utilizam métodos mais quantitativos, este estudo adota uma abordagem exploratória qualitativa baseada em prompts criados por profissionais da indústria de jogos, buscando refletir situações mais próximas do uso real. Diferentemente de trabalhos focados na mitigação de vieses por meio de técnicas de prompt, como em [Sant et al. 2024] e [Valov 2025], o foco deste trabalho está em observar como esses vieses aparecem de forma espontânea e explícita na construção dos prompts. Além disso, embora [Viana et al. 2025] investiguem vieses em jogos digitais por meio da geração de imagens, este trabalho amplia essa análise ao considerar também aspectos textuais e narrativos, com foco na língua portuguesa. Dessa forma, este estudo contribui ao ampliar e estender a literatura, no que diz respeito à análise de viés de gênero em prompts para geração conteúdo em jogos digitais.

## 3. Materiais e Métodos

Este estudo caracteriza-se como uma pesquisa exploratória, de abordagem qualitativa. A investigação concentra-se na análise textual de prompts formulados por profissionais da indústria de jogos digitais, para geração de conteúdo de personagens, narrativa e sons, com foco na ocorrência de termos gênero-dependentes.

A pesquisa abrangeu três etapas: planejamento; coleta de dados; e análise dos resultados.

Na etapa de planejamento, o público-alvo foi mapeado, o instrumento de coleta de dados foi elaborado e foram definidas as formas de divulgação do mesmo. O públicoalvo abrange profissionais que atuam na indústria de jogos digitais, incluindo designers, roteiristas, desenvolvedores e produtores. Para coleta dos dados, foi elaborado um formulário online, usando o GoogleForms, estruturado para possibilitar a investigação das

três questões de pesquisa definidas neste estudo. O formulário solicitava aos participantes a elaboração de prompts para um jogo hipotético, contemplando cinco tipos de conteúdos: Personagens, Atributos, Narrativa, Música e Voz. Para facilitar a avaliação, esses conteúdos foram agrupados em três dimensões: Personagens e Atributos; Narrativa; e Sons.

Durante a etapa de coleta de dados, o formulário foi divulgado em diferentes canais, incluindo comunidades online voltadas para desenvolvimento de jogos digitais, redes sociais e envio de e-mails para empresas e estúdios do setor, permanecendo ativo por aproximadamente dois meses. Apesar da ampla divulgação e do tempo em que o formulário permaneceu aberto, apenas 7 respostas foram obtidas.

Por fim, na etapa de análise dos resultados, foi utilizada a técnica de Part-ofSpeech Tagging (POS Tagging), para apoiar a identificação das classes gramaticais presentes nos prompts elaborados pelos participantes. Essa técnica consiste na rotulação automática de palavras de acordo com suas funções gramaticais, como verbos, substantivos e adjetivos, permitindo analisar padrões linguísticos nos textos. Para sua aplicação, foi utilizada a biblioteca Natural Language Toolkit (NLTK) no ambiente Google Colab, por meio de scripts desenvolvidos especificamente para este estudo, possibilitando a extração e organização dos termos relevantes. Uma abordagem semelhante foi utilizada por [Muñoz-García et al. 2025] para investigar vieses em conteúdos gerados por modelos de linguagem. No presente estudo, o uso do POS Tagging foi complementado por uma análise manual detalhada, na qual cada prompt foi lido individualmente. Além disso, foram observados aspectos como a distribuição de personagens por gênero e o nível de especificidade dos prompts, considerando o grau de detalhamento na descrição de atributos, ações e contextos.

## 4. Discussão e Resultados

Esta seção apresenta os resultados da análise dos termos gênero-dependentes identificados nos prompts, organizados conforme as três dimensões investigadas: Personagens e Atributos, Narrativa e Sons. Inicialmente são apresentados dados de distribuição e nível de especifidade dos prompts, seguidos de análise qualitativa dos padrões observados.

Embora a amostra seja reduzida, esse fator possibilitou uma análise mais aprofundada, qualitativa e manual, permitindo identificar nuances que poderiam passar despercebidas em análises automatizadas em larga escala. A menor taxa de participação pode estar associada a diferentes fatores, como o uso de IA generativa ainda ser um tema relativamente novo no contexto do desenvolvimento de jogos. Além disso, a utilização de IA na produção de arte, narrativa e outros conteúdos criativos tem sido motivo de debates na indústria de jogos e em comunidades artísticas, especialmente no que se refere a questões éticas, de autoria e impacto no trabalho de profissionais criativos [Khatiwada et al. 2025]. Isso pode ter influenciado a disposição de alguns profissionais em participar da pesquisa. Também é possível que questões de tempo ou a necessidade de respostas mais elaboradas no formulário tenham contribuído para a menor taxa de retorno. Ainda assim, as respostas obtidas fornecem um conjunto de dados qualitativos relevantes para a investigação proposta neste trabalho.

> 2https://doi.org/10.5281/zenodo.18991324

> 3https://doi.org/10.5281/zenodo.18991324

### 4.1. Distribuição de personagens por gênero

A Tabela 1 apresenta a distribuição de personagens por gênero nos prompts analisados.

Tabela 1. Presença de personagens por gênero nos prompts

|Respostas|Protagonista F|Protagonista M|Coadjuvante F|Coadjuvante M|
|---|---|---|---|---|
|R1|1|-|-|2|
|R2|-|1|-|-|
|R3|1|1|-|-|
|R4|-|1|-|-|
|R5|1|-|-|-|
|R6|-|1|-|-|
|R7|1|-|-|1|

É possível observar uma divisão relativamente equilibrada entre protagonistas femininos e masculinos. Três respostas apresentam protagonistas femininas (R1, R5 e R7), três apresentam protagonistas masculinos (R2, R4 e R6) e uma resposta inclui protagonistas de ambos os gêneros (R3). Sobre os personagens coadjuvantes são apresentados dois personagens masculinos (R1 e R7), enquanto nenhum participante descreveu coadjuvantes femininas. Outro aspecto relevante é que todos os participantes explicitaram o gênero dos personagens em seus prompts, mesmo quando essa informação não era estritamente necessária para a descrição do jogo.

### 4.2. Nível de especificidade dos prompts

O nível de detalhamento dos prompts produzidos pelos participantes variou entre descrições mais elaboradas e prompts mais simples. O primeiro grupo incluiu elementos como personalidade dos personagens, aparência física, referências culturais, estilo artístico para as imagens, ambientação sonora, cenários e definição de persona para a IA (R1, R3, R5 e R7). Em contraste, as outras respostas (R2, R4 e R6) apresentam descrições básicas do personagem e solicitam sugestões adicionais à IA.

Além disso, cinco participantes (R1, R2, R3, R6 e R7) fizeram referência explícita a imagem do primeiro prompt ou contextos previamente fornecidos no formulário. Essa referência foi incentivada pelas instruções do próprio formulário, que orientavam os participantes a considerar os conteúdos apresentados anteriormente na elaboração dos prompts.

### 4.3. QP1: Como termos gênero-dependentes são utilizados na descrição de personagens e seus atributos em prompts para jogos digitais?

Na análise da QP1, foram considerados principalmente substantivos e adjetivos diretamente associados aos personagens, por representarem características e atributos descritivos. Esses elementos foram identificados com o apoio da técnica de POS Tagging, que possibilitou a extração das classes gramaticais relevantes nos prompts. Para responder à QP1, os textos dos prompts foram analisados com o intuito de identificar e categorizar os atributos atribuídos aos personagens e suas relações com o gênero. A Tabela 2 apresenta os atributos mapeados para cada personagem especificado e suas relações de gênero.

Tabela 2. Características associadas a cada gênero

|Conteúdo|Feminino||Masculino|Ambo |s |
|---|---|---|---|---|---|
|Personagem|idosa, i de andar sábia, viajante galáxias, nerável, cautelosa, empática, mentora,c|dificuldade e enxergar, atiradora, entre invulcolérica, corajosa, sensível, harmosa|viajante no tempo, forte, forasteiro, super héroi, simples, delicado, programador, universitário, estudioso, ferreiro, hiperfocado|robôs carism guros, fofos,|, inteligentes, áticos, insesonhadores, jovens, capaz|

1Personagem não humano de gênero feminino. 2Personagem não humano de gênero masculino.

Os resultados revelam diferentes padrões de representação de gênero. Além de personagens femininas serem descritas como cautelosas, corajosas e empáticas, ocorre também a presença de características menos comuns, como uma protagonista idosa com dificuldades físicas (R1). Em contraste, alguns personagens masculinos são descritos seguindo alguns arquétipos tradicionais frequentemente presentes em jogos digitais, como super-heróis, ferreiros ou viajantes do tempo. Também aparece representação associada ao contexto tecnológico, como o personagem programador universitário.

Um ponto interessante é que as representações que rompem de alguma forma com estereótipos tradicionais ocorrem principalmente em personagens não humanos. Como apresentado na Tabela 2, o personagem masculino descrito como ”fofo”e ”delicado”corresponde a um coelho, enquanto a personagem feminina associada a atributos como ”atiradora”e ”viajante entre galáxias”corresponde a uma nave robótica.

### 4.4. QP2: De que forma termos gênero-dependentes se manifestam na construção narrativa dos prompts, considerando a definição de protagonistas, papéis e ações?

Para responder à QP2, a análise apoiada pela técnica POS Tagging focou nos verbos relacionados às ações desempenhadas pelos personagens nas narrativas propostas. A Tabela 3 apresenta os verbos identificados nos prompts associados aos personagens de cada gênero.

Tabela 3. Verbos associados a cada gênero nos prompts

|Personagem feminino|Personagem masculino|Ambos|
|---|---|---|
|precisar, encontrar, pedir, esquecer, tossir, engasgar, destruir, entregar, explorar, reunir, restaurar,|parecer, ajudar, flutuar, planar, locomover, inspirar, errar, aprender, coletar, buscar, voltar,|enfrentar, seguir, superar, decidir, conquistar, sonhar, perder, viajar|
|enfrentar, desvendar, mentorar, concentrar, planejar, pensar,irritar|programar, resolver, ganhar, evoluir||

1Personagem não humano de gênero feminino. 2Personagem não humano de gênero masculino.

De modo geral, tanto personagens femininos quanto masculinos são descritos por

meio de verbos relacionados à ação, progressão e resolução de desafios. Isso indica que os participantes tendem a estruturar narrativas baseadas em objetivos e desenvolvimento do personagem.

Entre os verbos associados aos protagonistas femininos, observam-se algumas ações como ”precisar”, ”pedir”, ”esquecer”, ”tossir”e ”engasgar”, que podem sugerir momentos de fragilidade, vulnerabilidade ou dependência dentro da narrativa. No entanto, também aparecem verbos como ”reunir”, ”planejar”, ”mentorar”, ”desvendar”e ”pensar”, que apontam para papéis ativos e estratégicos, associados à organização, liderança e resolução de problemas. Essa combinação sugere uma representação mais complexa da personagem feminina, que alterna entre momentos de vulnerabilidade e de protagonismo intelectual ou estratégico. O verbo ”irritar”também merece destaque, sendo complementar ao atributo ”colérica”apresentado na 2, que sugerem uma dimensão de descontrole emocional nas ações da personagem.

Por outro lado, os verbos associados aos protagonistas masculinos incluem ações como ”ajudar”, ”inspirar”, ”resolver”, ”evoluir”e ”programar”. Esses termos tendem a enfatizar atividades relacionadas à resolução de problemas, desenvolvimento de habilidades e competências técnicas. Em comparação com as personagens femininas, os verbos masculinos parecem focar mais em ações de progresso e desempenho, enquanto os femininos apresentam uma maior diversidade entre aspectos emocionais, vulnerabilidades e capacidades estratégicas.

### 4.5. QP3: Como termos gênero-dependentes são utilizados na descrição de elementos sonoros, como voz e música?

Por fim, para a QP3, os resultados foram analisados com o objetivo de identificar as características sonoras associadas aos personagens e suas possíveis relações com o gênero. A partir da aplicação da técnica de POS Tagging, foram extraídos termos relevantes presentes nos prompts, conforme ilustra a Tabela 4. Nessa etapa, o POS Tagging foi utilizado como apoio, com uma análise mais cuidadosa, uma vez que as descrições se concentravam em características funcionais.

Tabela 4. Características associadas a cada gênero nos prompts de Voz e Música

|Conteúdo|Feminino|Masculino|Ambos|
|---|---|---|---|
|Voz|doce, lenta, aguda|- |robóticas, animadas, melodiosas|
|Música|calma, natureza, tranquilidade, paz, exploração, eletrônica, instrumentos musicais, coral etéreo, piano suave, percussão marcante, atmosfera mágica,emocional|ambiência fofa|aventura, culturais|

1Personagem não humano de gênero feminino. 2Personagem não humano de gênero masculino.

O conteúdo sonoro apresenta menor incidência de termos gênero-dependentes em

comparação com a descrição de personagens. Porém, algumas diferenças podem ser observadas principalmente na forma como as vozes e trilhas sonoras são descritas. As descrições de vozes associadas a personagens femininas incluem atributos como ”doce”, ”lenta”e ”aguda”. Já para os personagens masculinos, não foram identificadas descrições explícitas de características vocais além daquelas que foram utilizadas para ambos os gêneros ”robóticas”, ”animadas”e ”melodiosas”.

Já em relação à trilha sonora, os prompts com protagonistas femininas apresentam descrições mais detalhadas e frequentemente associadas a atmosferas emocionais ou ambientais, como tranquilidade, natureza, exploração ou magia. Uma exceção ocorre na resposta R5, na qual a protagonista feminina é descrita como uma nave robótica atiradora e a trilha sonora é caracterizada por elementos eletrônicos e tecnológicos, indicando que atributos narrativos ou de gênero do jogo também influenciam a definição dos elementos sonoros. Nos prompts com protagonistas masculinos, por sua vez, as descrições musicais tendem a ser mais simples ou funcionais, sendo em alguns casos inexistentes. Um dos poucos exemplos mais específicos aparece apenas como a indicação de ”ambiência fofa”, associada a um personagem coelho, o mesmo caso discutido anteriormente, reforçando que essas representações ocorrem principalmente em personagens não humanos.

## 5. Considerações Finais

Este trabalho apresentou uma análise exploratória de prompts elaborados por profissionais da indústria de jogos digitais, com o objetivo de investigar como termos gênerodependentes se manifestam na construção de personagens, atributos, narrativas e elementos sonoros. Os resultados indicam que embora personagens de diferentes gêneros compartilhem diversos atributos e elementos narrativos, algumas distinções podem ser observadas nas ações e características atribuídas a cada um. Enquanto alguns verbos associados às personagens femininas sugerem momentos de vulnerabilidade ou fragilidade, outros indicam papéis estratégicos e de liderança, como planejamento, mentoria e investigação. Já os protagonistas masculinos tendem a ser associados a ações relacionadas à resolução de problemas, progresso e conquista de objetivos dentro da narrativa.

A análise dos atributos associados aos personagens também revelou diferentes padrões de representação de gênero. As personagens femininas foram descritas por meio de características como cautelosas, corajosas e empáticas, além da presença de representações menos comuns, como uma protagonista idosa com dificuldades físicas. Em contraste, alguns personagens masculinos foram descritos a partir de arquétipos frequentemente presentes em jogos digitais, como super-heróis, ferreiros ou viajantes do tempo, além de representações relacionadas a contextos tecnológicos, como um programador universitário. Um aspecto interessante é que representações que rompem com estereótipos tradicionais aparecem principalmente em personagens não humanos. Por exemplo, um personagem masculino descrito como ”fofo”e ”delicado”corresponde a um coelho, enquanto uma personagem feminina associada a atributos como ”atiradora”e ”viajante entre galáxias”corresponde a uma nave robótica.

Embora o estudo possua caráter exploratório e amostra reduzida, os resultados contribuem para ampliar a discussão sobre o uso de IA generativa no processo de criação de conteúdo para jogos digitais e sobre como representações de gênero podem surgir já na etapa de elaboração de prompts. Como trabalhos futuros, pretende-se ampliar o conjunto

de participantes e aprofundar a análise, submetendo os prompts fornecidos em diferentes tipos de sistemas generativos para fins de comparação entre os achados nos prompts e os respectivos conteúdos gerados.

### Uso de Inteligência Artificial

Neste trabalho, ferramentas de IA generativa foram utilizadas como apoio em atividades específicas relacionadas à revisão textual e organização da pesquisa. O modelo ChatGPT foi empregado para auxiliar na revisão de trechos do texto, na sugestão de sinônimos, melhorias de clareza na redação e organização preliminar de ideias. Além disso, a ferramenta NotebookLM foi utilizada como suporte para a leitura e síntese de artigos científicos. Essas ferramentas foram utilizadas apenas como suporte ao processo de escrita e análise. O artigo foi elaborado e revisado integralmente pelas pessoas autoras, que assumem total responsabilidade pelo seu conteúdo.

### Agradecimentos

As autoras agradecem ao CNPq [Processo número 440447-2024-0] pelo apoio concedido e ao Programa de Pós-Graduação da Universidade Federal de Viçosa - Campus Florestal (UFVCAF), pelo suporte acadêmico e institucional no desenvolvimento deste trabalho.
