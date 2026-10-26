20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

# Avaliação inicial de um modelo interinstitucional de mentoria para permanência de mulheres na Computação

Liliane Fonseca,Andreza Leite, Leticia Leitão, Mariana Coelho, Maria Eduarda Nunes, Leticia Pedrosa, Tarsila Amado, Beatriz Bandeira,

Gabrielle Canalle,Sergio Soares, Carolyn Seaman

1Escola Politécnica de Pernambuco – Universidade de Pernambuco (UPE) Recife – PE – Brazil

2Escola de Tecnologia e Comunicação – Universidade Católica

de Pernambuco (UNICAP)

Recife – PE – Brasil

3Centro de Informática – Universidade Federal de Pernambuco (UFPE) Recife – PE – Brasil

4Departamento de Computação –

Universidade Federal Rural de Pernambuco (UFRPE)

Recife – PE – Brasil

5Faculdade Cesar School (Cesar School)

Recife – PE – Brasil

6Information Systems Department – Universidade de Maryland Baltimore County (UMBC)

Baltimore County– Maryland – Estados Unidos

{ liliane.ssilva, bmbms@poli.br } @upe.br { liliane.fonseca, tarsila.00000849038@unicap.br, } @unicap.br, { lasl, mgc3,lblp, mena, prga, scbs } @cin.ufpe.br, gkc@cesar.school, cseaman@umbc.edu

Abstract. This paper presents the design and preliminary evaluation of an Interinstitutional Mentoring Model aimed at strengthening retention, engagement, and professional development among women in Computer Science programs. The model was developed following a Design Science Research (DSR) approach and integrates five higher education institutions, students at different academic stages, and industry professionals within a multilevel ecosystem that combines peer mentoring, academic mentoring, and professional mentoring supported by continuous monitoring activities. A longitudinal study was conducted during one academic semester to perform an initial evaluation of the proposed ecosystem, focusing on participant uptake, dropout, and satisfaction indicators. A total of 172 students enrolled in the program, of which 131 remained active, resulting in an uptake rate of 76.2% and a dropout rate of 23.8%. The results indicate high levels of overall satisfaction (91.21%) and statistically significant institutional differences in uptake rates. The findings suggest that the proposed mentoring ecosystem is viable and demonstrates strong potential for participant mobilization and retention, while also highlighting the influence of contextual institutional factors on participant engagement.

Resumo. Este artigo apresenta o desenvolvimento e a avaliação preliminar de um Modelo Interinstitucional de Mentoria voltado ao fortalecimento da permanência, do engajamento e do desenvolvimento profissional de mulheres em cursos de da área de Computação. O modelo foi desenvolvido com base na abordagem de Design Science Research (DSR) e integra cinco instituições de ensino superior, estudantes em diferentes etapas da trajetória acadêmica e profissionais da indústria em um ecossistema multinível que combina mentoria entre pares, mentoria acadêmica e mentoria profissional, apoiadas por atividades contínuas de acompanhamento. Foi conduzido um estudo longitudinal ao longo de um semestre acadêmico para realizar uma avaliação inicial do ecossistema proposto, considerando indicadores de adesão, evasão e satisfação das participantes. Ao todo, 172 estudantes ingressaram no programa, das quais 131 permaneceram ativas, resultando em uma taxa de adesão de 76,2% e uma taxa de evasão de 23,8%. Os resultados indicam elevados níveis de satisfação geral (91,21%), além de diferenças estatisticamente significativas entre as instituições quanto às taxas de adesão. Os resultados sugerem que o ecossistema de mentoria proposto é viável e apresenta forte potencial para mobilização e retenção das participantes, ao mesmo tempo em que evidenciam a influência de fatores contextuais institucionais no engajamento das estudantes.

## 1. Introdução

A sub-representação feminina em cursos de Computação permanece como um desafio persistente, mesmo diante do crescimento global da demanda por profissionais da área. Estudos clássicos mostram que desigualdades de gênero em Computação não se explicam apenas pelo acesso inicial, mas pela combinação de fatores acadêmicos, culturais e simbólicos que afetam pertencimento, autoconfiança e permanência ao longo da trajetória universitária, incluindo ausência de modelos de identificação, isolamento acadêmico e percepção de ambientes predominantemente masculinos [Margolis and Fisher 2002].

Mesmo entre estudantes com bom desempenho acadêmico, a percepção de não pertencimento pode influenciar decisões de permanência e projeção profissional. Ambientes pouco acolhedores tendem a reforçar mecanismos sutis de exclusão, reduzindo participação em espaços de colaboração, liderança e visibilidade acadêmica [Dennehy and Dasgupta 2017]. Nesse contexto, estratégias institucionais de suporte relacional têm sido apontadas como fundamentais para ampliar retenção e persistência [Rheingans et al. 2018, Women in High Performance Computing 2023]. Entre essas estratégias, programas de mentoria têm ocupado papel central. Evidências mostram que a mentoria contribui para acolhimento, orientação acadêmica, fortalecimento de confiança e ampliação de perspectivas profissionais, especialmente quando estruturada em interações recorrentes e com modelos de referência próximos [Maciel and Bim 2017]. Modelos de near-peer mentoring têm recebido destaque por combinarem apoio acadêmico e identificação geracional, favorecendo simultaneamente mentoradas e mentoras em aspectos como liderança, identidade profissional e engajamento acadêmico [Rheingans et al. 2018]

Revisões recentes reforçam que intervenções sustentadas apresentam melhores resultados quando articulam pertencimento, apoio social recorrente, visibilidade de trajetórias possíveis e integração institucional [Perez-Felkner et al. 2025]. Isso sugere que

programas de mentoria tendem a ser mais efetivos quando concebidos como ecossistemas contínuos de suporte. No Brasil, a produção científica sobre gênero e Computação tem se expandido evidenciando avanços em ações de acolhimento, oficinas, redes de apoio e incentivo à permanência feminina [Maciel and Bim 2017, Salgado et al. 2025]. Apesar disso, ainda são relativamente escassas propostas que integrem, em uma mesma arquitetura, colaboração interinstitucional, mentoria multinível, participação da indústria e monitoramento sistemático de indicadores de engajamento e permanência.

Diante dessa lacuna, este artigo apresenta o desenvolvimento e a avaliação preliminar de um modelo interinstitucional de mentoria multinível, concebido colaborativamente entre cinco instituições de ensino superior de naturezas distintas. O modelo articula professoras anfitriãs, embaixadoras, mentoras acadêmicas, mentoras da indústria, estudantes em diferentes fases da graduação e ações voltadas à educação básica, combinando acolhimento acadêmico, integração universidade–indústria, monitoramento longitudinal e fortalecimento de trajetórias femininas em Computação. Fundamentado na abordagem de Design Science Research (DSR), o estudo descreve o ecossistema proposto e apresenta resultados iniciais de um ciclo semestral realizado em 2025.2, discutindo indicadores de adesão, evasão, satisfação global e desafios observados em sua implementação em contexto multi-institucional.

## 2. Trabalhos Relacionados

A literatura internacional evidencia que a permanência de mulheres em cursos de Computação está fortemente associada a fatores como pertencimento, autoeficácia, suporte social e acesso a modelos de referência [Cheryan et al. 2017, Bandura 1997, Whitcomb et al. 2020]. Nesse contexto, programas estruturados de mentoria têm sido amplamente investigados como estratégias eficazes para mitigar barreiras acadêmicas e sociais, promovendo acolhimento, orientação e desenvolvimento profissional [Dennehy and Dasgupta 2017]. Modelos institucionais consolidados, como o proposto por Rheingans et al. [Rheingans et al. 2018], demonstram que abordagens integradas combinando mentoria entre pares, apoio acadêmico, construção de comunidade e desenvolvimento de carreira podem gerar impactos positivos na retenção e no sucesso acadêmico de mulheres em Computação. Iniciativas de programas institucionais baseados em coortes reforçam a importância de estruturas contínuas de suporte, com interações recorrentes e integração com o setor profissional [Women in High Performance Computing 2023].

Revisões recentes da literatura reforçam que intervenções isoladas tendem a apresentar efeitos limitados, enquanto abordagens sistêmicas e sustentadas ao longo do tempo, que articulam pertencimento, apoio social contínuo e visibilidade de trajetórias, apresentam maior potencial de impacto na permanência de grupos sub-representados [Moreira et al. 2025, Perez-Felkner et al. 2025]. Além disso, estudos destacam o papel central das comunidades de prática e do suporte relacional contínuo na construção do senso de pertencimento em Computação [Swackhamer et al. 2022]. No contexto brasileiro, observa-se um crescimento consistente de iniciativas voltadas à promoção da participação feminina em Computação. [Maciel and Bim 2017]. Essas iniciativas incluem oficinas, ações de sensibilização, programas de mentoria e redes de apoio que contribuem para o fortalecimento do interesse e da permanência de mulheres na área [Barino et al. 2024, Santos and Marczak 2023, Ferreira et al. 2025]. Estudos recentes no

Brasil têm investigado fatores associados à atração, evasão e permanência feminina em cursos de Computação, destacando a importância do apoio institucional, do ambiente acadêmico e de redes de suporte [Santos and Marczak 2023, Santos et al. 2024, Silva et al. 2024]. Trabalhos também evidenciam a relevância de iniciativas de empoderamento, eventos e comunidades para fortalecer a identidade e a trajetória de mulheres na área [da Cunha and Tomaz 2025, Novaes et al. 2025, Farao and Bordin 2025]. Entretanto, essas iniciativas são, em sua maioria, desenvolvidas de forma localizada, com escopo restrito a instituições específicas ou ações pontuais.

Apesar dos avanços, ainda são relativamente escassas propostas que integrem, em uma mesma arquitetura, colaboração interinstitucional, mentoria multinível, participação da indústria e monitoramento sistemático de indicadores de engajamento e permanência. Essa lacuna evidencia a necessidade de modelos mais estruturados, escaláveis e orientados por dados, capazes de articular diferentes níveis de formação e promover suporte contínuo ao longo da trajetória acadêmica e profissional das estudantes. Nesse contexto, o presente trabalho contribui ao propor um modelo interinstitucional de mentoria multinível que integra diferentes atores, níveis de formação e mecanismos de monitoramento, buscando avançar em direção a uma abordagem sistêmica e sustentável para o fortalecimento da permanência feminina em Computação.

## 3. Modelo de Mentoria Interinstitucional em Rede Baseado em Evidências

O modelo proposto organiza-se como uma arquitetura multinível de formação e mentoria em rede, estruturada para promover suporte contínuo ao longo da trajetória acadêmica e profissional de mulheres em Computação. A proposta articula diferentes níveis de formação, múltiplos atores e mecanismos de integração institucional, configurando um ecossistema de desenvolvimento progressivo e retroalimentado. A arquitetura do modelo é apresentada na Figura 1.

Figura 1: Arquitetura de Mentoria Interinstitucional em Rede. Elaborado pelos autores com apoio de ferramenta de Inteligência Artificial Generativa (ChatGPT).

Na base do modelo situam-se estudantes da educação básica, especialmente aquelas envolvidas em ações de extensão e atividades inspiracionais voltadas à aproximação com tecnologia, criatividade computacional e resolução de problemas. Essas iniciativas funcionam como porta de entrada para o interesse em Computação e possibilitam que estudantes universitárias atuem como referências próximas, contribuindo para a construção de identidade e pertencimento desde etapas iniciais da formação. No nível seguinte encontram-se estudantes ingressantes na graduação, que assumem o papel de mentoradas. Nesse estágio, recebem apoio para adaptação à vida universitária, organização dos estudos, compreensão da dinâmica acadêmica e fortalecimento do senso de pertencimento. Paralelamente, participam de atividades extensionistas, passando a atuar de forma ativa no ecossistema ao apoiar ações com estudantes da educação básica. Em níveis mais avançados da graduação, estudantes assumem o papel de mentoras acadêmicas, oferecendo mentoria entre pares para alunas ingressantes. Essa atuação envolve acolhimento acadêmico, compartilhamento de experiências, apoio à adaptação ao curso e fortalecimento da autoconfiança das mentoradas. Esse arranjo favorece relações horizontais de confiança e identificação, ao mesmo tempo em que promove o desenvolvimento de competências de liderança, comunicação e responsabilidade entre as mentoras. Em uma camada superior, profissionais da indústria, pesquisadoras e empreendedoras atuam como mentoras profissionais, especialmente para estudantes em fases intermediárias da graduação. Essa dimensão amplia o alcance do modelo ao integrar o contexto acadêmico com o setor produtivo, oferecendo orientação sobre trajetórias profissionais, competências demandadas pelo mercado, planejamento de carreira e desafios enfrentados por mulheres em contextos tecnológicos.

A governança do modelo é sustentada por docentes responsáveis pela mediação local em cada instituição participante, atuando na articulação das atividades, acompanhamento das participantes e integração entre ensino, extensão e mentoria. O modelo conta ainda com parceria internacional do Center for Women in Technology (CWIT), da University of Maryland Baltimore County (UMBC), essa colaboração envolveu apoio metodológico na estruturação das atividades de mentoria, formação de mentoras e compartilhamento de experiências relacionadas a programas internacionais voltados à permanência feminina em Computação.

Adicionalmente, o modelo incorpora a atuação de embaixadoras institucionais, compostas principalmente por estudantes voluntárias responsáveis por apoiar ações locais de mobilização, comunicação institucional, integração entre participantes e suporte operacional às atividades do programa. Além de comunicação e apoio à governança interinstitucional, bem como a participação do setor produtivo, que contribui por meio de oficinas, palestras, encontros profissionais e atividades de aproximação com o mercado. Essas ações ampliam o repertório técnico e profissional das participantes, fortalecem a conexão universidade–indústria e tornam mais visíveis trajetórias possíveis na área.

A integração desses elementos permite caracterizar o modelo como um ecossistema de mentoria multinível em rede, no qual as participantes podem transitar ao longo do tempo por diferentes papéis, evoluindo de mentoradas para mentoras, embaixadoras ou futuras profissionais e pesquisadoras. A robustez da proposta reside na articulação entre mentoria multinível, colaboração interinstitucional, integração com o setor produtivo e mecanismos de acompanhamento contínuo, configurando uma estratégia escalável

e sustentável para o fortalecimento da permanência feminina em Computação.

O modelo apresentado nesta seção constitui o artefato central desenvolvido nesta pesquisa no contexto da abordagem de Design Science Research (DSR). A seção seguinte apresenta os procedimentos metodológicos utilizados para orientar sua concepção, implementação e avaliação preliminar em contexto real de aplicação.

## 4. Metodologia

Este estudo foi conduzido com base na abordagem de Design Science Research (DSR), utilizada como framework metodológico para orientar a concepção, implementação e avaliação preliminar do modelo de mentoria apresentado na Seção 3 [Hevner et al. 2004]. A escolha dessa abordagem justifica-se pelo caráter interventivo da proposta, centrada no desenvolvimento de um modelo estruturado de mentoria para apoiar a permanência feminina em cursos de Computação. No contexto desta pesquisa, o artefato corresponde ao modelo interinstitucional de mentoria multinível em rede descrito na Seção 3, concebido para promover pertencimento, engajamento e desenvolvimento acadêmico e profissional.

A construção do artefato foi fundamentada tanto em evidências teóricas da literatura quanto em demandas observadas em contextos educacionais reais. A condução da pesquisa seguiu as etapas propostas por [Peffers et al. 2007]: (i) identificação do problema e motivação, relacionada à sub-representação feminina e aos desafios de permanência; (ii) definição dos objetivos da solução, com foco na construção de um modelo escalável e sustentável de suporte acadêmico e profissional; (iii) estruturação e refinamento do artefato, envolvendo definição de papéis, fluxos de mentoria e instrumentos de monitoramento; (iv) demonstração em ambiente real, por meio da implementação de um ciclo semestral; e (v) avaliação inicial, baseada em fontes de evidência.

### 4.1. Contexto institucional e participantes

A implementação ocorreu em cinco instituições de ensino superior, localizadas na região metropolitana do Recife, abrangendo diferentes perfis institucionais: instituições públicas federais (incluindo contexto rural), instituição pública estadual, instituição comunitária e instituição privada especializada em tecnologia. Essa diversidade permitiu avaliar o artefato em ambiente heterogêneo, contribuindo para análise de robustez, adaptabilidade e potencial de escalabilidade [Hevner et al. 2004].

Participaram do estudo estudantes autodeclaradas mulheres regularmente matriculadas em cursos da área de Computação, selecionadas por meio de chamada institucional aberta. As participantes foram selecionadas mediante inscrição voluntária, amplamente divulgada pelas instituições participantes por meio de canais institucionais, redes sociais e ações locais de mobilização. As participantes foram organizadas em diferentes perfis funcionais (mentoradas, mentoras acadêmicas, mentoras profissionais e embaixadoras), conforme descrito na Seção 3.

### 4.2. Protocolo de implementação do artefato

A implementação do modelo ocorreu ao longo de um semestre letivo, estruturada em ciclos progressivos de interação. O protocolo contemplou, para todos os participantes, 1 evento de abertura ( kick off ), 1 evento de pareamento entre mentoras e mentoradas ( match

party ) e 1 evento de encerramento Closing Meeting, além de 1 capacitação para mentoras e 1 para embaixadoras. Ao longo do ciclo, foram realizados 8 eventos remotos de integração com o setor profissional ( Career Nights ), 6 encontros formativos envolvendo oficinas, palestras, visitas técnicas e ações extensionistas com estudantes da educação básica, bem como 8 sessões de mentoria individual (1:1) entre mentoras e mentoradas e 2 sessões de mentoria conduzidas por profissionais da indústria. Essa estrutura operacionalizou o modelo ao articular formação, acompanhamento contínuo, construção de comunidade e integração universidade–indústria.

O eixo de integração profissional foi implementado com o apoio de cinco empresas parceiras da área de tecnologia, envolvendo palestras, workshops, visitas técnicas e encontros profissionais, ampliando a conexão das participantes com trajetórias reais de atuação em computação. Sessões temáticas remotas ( Career Nights ) ampliaram a exposição das estudantes a diferentes áreas da Computação, incluindo ciência de dados, desenvolvimento de software, cibersegurança, qualidade de software, sistemas embarcados e gestão de produto. Estas sessões foram protagonizadas por egressas das próprias instituições participantes, favorecendo identificação e percepção de trajetórias profissionais alcançáveis. A participação de egressas não constituiu requisito formal do programa, mas foi priorizada neste ciclo devido ao potencial de fortalecimento da identificação e da percepção de trajetórias profissionais alcançáveis pelas participantes.

Embora o modelo contemple múltiplas camadas de atuação, incluindo integração com profissionais da indústria, as análises apresentadas neste artigo concentram-se principalmente nas participantes diretamente envolvidas nas atividades de mentoria da graduação durante o ciclo inicial de implementação.

### 4.3. Coleta e análise dos dados

A avaliação do artefato foi conduzida a partir de múltiplas fontes de evidência, conforme recomendado em estudos de DSR [Hevner et al. 2004]. Foram considerados: registros sistemáticos de presença, formulários periódicos de acompanhamento, questionários estruturados de satisfação, motivação, escalas de engajamento e pertencimento, estudos demográficos que incluiram questionários semi-estruturados. A análise de satisfação considerou indicadores de reação e percepção das participantes em relação às atividades do programa, alinhando-se a abordagens clássicas de avaliação de experiências formativas [Kirkpatrick and Kirkpatrick 2006].

A coleta de dados foi realizada por meio de questionário online semiestruturado, desenvolvido com base em estudos prévios sobre pertencimento, permanência, engajamento e equidade de gênero em Computação. O instrumento continha questões fechadas, abertas e escalas Likert de cinco pontos, permitindo avaliar múltiplas dimensões da experiência das participantes no programa. A avaliação de satisfação contemplou indicadores relacionados à motivação para continuidade no projeto, avaliação geral dos encontros, percepção de utilidade dos conteúdos, acolhimento, clareza dos materiais e adequação do formato e duração das atividades. Questões abertas também foram utilizadas para identificar aspectos positivos, dificuldades e sugestões de melhoria dos encontros. Os questionários foram respondidos individualmente, de forma anônima e remota, com tempo estimado de 15 a 20 minutos, sendo os dados utilizados exclusivamente para fins acadêmicos e institucionais.

As análises apresentadas neste artigo consideram indicadores agregados de satisfação geral em relação às atividades desenvolvidas ao longo do ciclo.

Os dados quantitativos foram analisados por meio de estatística descritiva, incluindo frequências, médias e proporções, permitindo caracterizar padrões de adesão, participação e satisfação.

As respostas qualitativas provenientes de formulários abertos e registros reflexivos das participantes foram analisadas por meio de codificação temática, buscando identificar padrões recorrentes relacionados a acolhimento, pertencimento, apoio acadêmico, identificação profissional e percepção das atividades do programa. A análise foi conduzida iterativamente, agrupando categorias emergentes associadas às experiências relatadas pelas participantes.

A análise concentrou-se na identificação de evidências de adesão, evasão e satisfação global das participantes no modelo, características típicas de ciclos iniciais de validação em Design Science Research.

## 5. Resultados e Discussões

### 5.1. Implementação do ciclo do artefato

A implementação do ciclo analisado ocorreu ao longo de um semestre letivo completo, entre junho e dezembro de 2025. De modo geral, a execução manteve aderência à arquitetura originalmente proposta do artefato, embora ajustes pontuais tenham sido necessários em função da heterogeneidade dos calendários acadêmicos entre as instituições participantes. As etapas iniciais, incluindo evento de abertura, formação de mentoras e pareamento estruturado entre participantes, foram realizadas inicialmente em quatro instituições, com posterior incorporação de uma quinta instituição, decorrente de especificidades de calendário acadêmico. Essa inclusão tardia não comprometeu os componentes centrais do modelo. Isto foi evidenciado baseado na manutenção dos principais componentes do protocolo de implementação, incluindo pareamento das emntoras e mentoradas, realização de treinamento das mentoras realização das mentorias, participação nos encontros coletivos e integração às atividades formativas e profissionais previstas para o ciclo. A quinta instituição não conseguiu participar apenas de 1 oficina, as medidas de participação não foram consideradas para esta instituição.Isto evidencia a flexibilidade e adaptabilidade do programa em contextos institucionais distintos. A estrutura das atividades e os materiais formativos foram desenvolvidos com apoio de colaboração internacional [OMITIDO], em conjunto com a equipe local, permitindo adaptação metodológica ao contexto de aplicação. Uma adaptação relevante ocorreu no eixo de integração profissional: limitações de agenda com organizações parceiras inviabilizaram parte das atividades presenciais inicialmente previstas. Como estratégia de mitigação, foram incorporadas sessões remotas semanais de desenvolvimento profissional, realizadas entre outubro e novembro, mantendo-se o alinhamento com os objetivos de integração entre universidade e setor produtivo.

Os resultados apresentados referem-se a um ciclo inicial de implementação e devem ser interpretados como evidências preliminares. Nesse sentido, os achados indicam o potencial do modelo em termos de adesão, evasão e satisfação global do programa ainda que limitados ao escopo e à duração do período analisado.

### 5.2. Adesão ao programa

A Tabela 1 apresenta os resultados de adesão ao programa nas diferentes instituições. No total, foram registradas 172 inscrições iniciais, das quais 131 participantes permaneceram ativas, resultando em uma taxa global de adesão de 76,2%. A distribuição interna evidencia 83 mentoradas e 48 mentoras ativas, essa distribuição corresponde aproximadamente a uma razão de 1 mentora para cada 1,7 mentoradas, permitindo acompanhamento relativamente próximo entre as participantes e aracterizando a estrutura multinível do modelo. Observou-se variação relevante nas taxas de adesão entre instituições, com valores que variaram de 63,3% (Instituição B) a 91,7% (Instituição C). Para avaliar se essas diferenças são estatisticamente significativas, foi aplicado um teste de comparação de proporções (teste qui-quadrado de independência), que indicou diferença estatisticamente significativa entre as instituições ( χ, p < 0, 05), sugerindo influência do contexto institucional na conversão de inscrições em participação ativa.

Tabela 1: Adesão ao programa por instituiç ão

|Instituição|Inscrições|Ativas|Adesão(%)|
|---|---|---|---|
|Instituição A|72|54|75,0|
|Instituição B|30|19|63,3|
|Instituição C|24|22|91,7|
|Instituição D|14|11|78,6|
|Instituição E|32|25|78,1|
|Total|172|131|76,2|

### 5.3. Evasão ao longo do ciclo

A Tabela 2 apresenta os dados de evasão ao longo do ciclo. No total, foram registradas 41 desistências, correspondendo a uma taxa global de evasão de 23,8%. Observou-se variação entre instituições, com taxas que variaram de 8,3% (Instituição C) a 36,7% (Instituição B), indicando comportamentos distintos de retenção. A maior concentração de desistências ocorreu nas fases iniciais do ciclo, seguida por estabilização da participação, padrão consistente com programas voluntários. A proporção entre mentoradas e mentoras manteve-se relativamente equilibrada entre as instituições, indicando consistência na operacionalização da mentoria multinível. Esse equilíbrio constitui um elemento relevante para a sustentabilidade do modelo, uma vez que garante níveis adequados de suporte às participantes ingressantes. De forma geral, os resultados indicam que, embora o modelo seja viável em diferentes contextos institucionais, a evasão é influenciada por fatores locais, reforçando a necessidade de estratégias adaptativas para maximizar a retenção.

### 5.4. Satisfação global com os eventos

A Tabela 3 apresenta as estatísticas descritivas da satisfação dos eventos por instituição. De forma geral, os níveis de satisfação foram elevados ao longo de todo o ciclo, com média global de µ = 91, 2% ( σ ≈ 12, 6) e intervalo de confiança de 95% em [86,9%, 95,5%], indicando avaliação amplamente positiva das atividades. As Instituições D e B apresentaram os maiores níveis médios de satisfação ( µ = 97, 8% e µ = 96, 2%, respectivamente), com baixa variabilidade, evidenciando consistência na percepção positiva

Tabela 2: Evasão ao programa por instituiç ão

|Instituição|Inscrições|Desistências|Evasão(%)|
|---|---|---|---|
|Instituição A|72|18|25,0|
|Instituição B|30|11|36,7|
|Instituição C|24|2|8,3|
|Instituição D|14|3|21,4|
|Instituição E|32|7|21,9|
|Total|172|41|23,8|

dos eventos. A Instituição C também apresentou alta satisfação ( µ = 94, 5%), com leve variação ao longo do ciclo.

A Instituição E apresentou níveis elevados ( µ = 93, 6%), mesmo com entrada tardia, indicando rápida adaptação ao modelo. Ressalta-se que a Instituição E corresponde à instituição incorporada posteriormente ao ciclo inicial, o que torna particularmente relevante o elevado nível de satisfação observado mesmo diante de uma implementação parcialmente adaptada. Por outro lado, a Instituição A apresentou maior variabilidade ( σ ≈ 23, 4) e menor média ( µ = 76, 5%), com valores mais baixos nos eventos iniciais, seguidos por recuperação e estabilização nos encontros finais. Observa-se, de forma geral, uma tendência de aumento e estabilização da satisfação na segunda metade do ciclo, sugerindo amadurecimento do programa, maior alinhamento das atividades às expectativas das participantes e fortalecimento do senso de comunidade.

Tabela 3: Estatísticas descritivas da satisfaç ão dos eventos por instituiç ão

|Instituição|Média(%)|Desvio Padrão|Mín(%)|Máx(%)|IC 95%|
|---|---|---|---|---|---|
|A|76,5|23,4|35,0|100,0|[60,3; 92,7]|
|B|96,2|6,5|85,0|100,0|[91,7; 100,0]|
|C|94,5|8,7|80,0|100,0|[88,5; 100,0]|
|D|97,8|4,2|90,0|100,0|[94,9; 100,0]|
|E|93,6|9,8|70,0|100,0|[86,8;100,0]|
|Global|91,2|12,6|35,0|100,0|[86,9; 95,5]|

### 5.5. Desafios observados no ciclo

A implementação do modelo evidenciou um conjunto de desafios típicos de iniciativas interinstitucionais em fase inicial. Observou-se uma taxa de evasão de 23,8%, concentrada principalmente nas primeiras semanas do ciclo, indicando um período inicial de adaptação das participantes. Adicionalmente, foram identificadas variações significativas entre instituições nas taxas de adesão e satisfação, sugerindo influência de fatores contextuais, como características institucionais, apoio local e estratégias de mobilização. O engajamento ao longo do tempo apresentou padrão de oscilação, com redução após o início do ciclo e posterior estabilização, comportamento recorrente em programas voluntários e fatores como calendário acadêmico, incluindo períodos de recesso. Por fim, a coordenação interinstitucional exigiu adaptações locais para acomodar diferentes contextos organizacionais, evidenciando a necessidade de estratégias flexíveis. Ressalta-se ainda que os resultados referem-se a um ciclo inicial de implementação, o que limita análises de longo prazo.

### 5.6. Discussão

Os resultados obtidos neste estudo fornecem evidências iniciais sobre a viabilidade e o comportamento do modelo em contexto real de uso. A taxa de adesão global de 76,2% indica forte capacidade de mobilização, especialmente considerando o caráter voluntário, extracurricular e interinstitucional da iniciativa. Por outro lado, a taxa de evasão de 23,8%, concentrada nas fases iniciais, sugere a existência de um período de adaptação das participantes, padrão consistente com programas de mentoria e atividades voluntárias. A variação observada entre instituições nas taxas de adesão e evasão, estatisticamente significativa, reforça a influência de fatores contextuais no desempenho do programa. Entre os possíveis fatores contextuais, destacam-se diferenças relacionadas ao perfil institucional, disponibilidade de apoio local, características dos calendários acadêmicos e intensidade das estratégias de mobilização desenvolvidas em cada contexto. Embora este estudo não tenha como objetivo estabelecer comparações causais entre categorias institucionais, os resultados sugerem que tais elementos podem influenciar os níveis de adesão, participação e permanência observados.

Os elevados níveis de satisfação (91,21%) e motivação indicam que as atividades foram bem avaliadas pelas participantes, contribuindo para a sustentação do engajamento ao longo do programa. A tendência de estabilização desses indicadores na segunda metade do ciclo sugere um processo de amadurecimento do modelo, com maior alinhamento entre expectativas, formato das atividades e necessidades das participantes. A análise do engajamento evidencia um padrão de oscilação ao longo do tempo, com redução após o início do ciclo e posterior estabilização, comportamento recorrente em programas voluntários. Adicionalmente, atividades opcionais, como as Career Nights, apresentaram participação moderada, indicando a necessidade de ajustes no formato ou na integração com a rotina acadêmica das estudantes. De forma geral, os resultados indicam que o modelo apresenta consistência operacional e capacidade de adaptação a diferentes contextos institucionais, ainda que dependente de estratégias locais para maximizar adesão, engajamento e retenção.

## 6. Ameaças a Validade

Este estudo apresenta limitações relevantes para a interpretação dos resultados. Validade interna. A participação voluntária pode introduzir viés de auto-seleção, refletindo predisposição prévia a engajamento e motivação. Além disso, variações institucionais, como calendário acadêmico, disponibilidade local e intensidade de mediação, bem como fatores externos (carga acadêmica e demandas pessoais), podem ter influenciado os resultados. Validade de construção. A satisfação baseia-se em autorrelato, estando sujeita a vieses de percepção e desejabilidade social, podendo não capturar integralmente a experiência das participantes. Validade externa. A implementação ocorreu em cinco instituições de uma mesma região, o que, embora garanta diversidade contextual, limita a generalização para outros contextos. Ainda assim, o caráter interinstitucional fornece evidências iniciais de adaptabilidade. Validade longitudinal. A análise contempla apenas um semestre, não permitindo avaliar efeitos de longo prazo. Apesar dessas limitações, o estudo apresenta evidências iniciais da viabilidade e comportamento do modelo em contexto real. Ressalta-se que, embora outras métricas tenham sido coletadas, este artigo foca em adesão, evasão e satisfação, alinhado ao escopo deste ciclo inicial, sendo as demais exploradas em estudos futuros.

## 7. Conclusão

Este artigo apresentou um modelo interinstitucional de mentoria multinível voltado ao fortalecimento da permanência de mulheres em cursos de Computação. A proposta articula mentoria entre pares, mentoria acadêmica e profissional, integrando instituições de diferentes contextos em um ecossistema estruturado e orientado por dados. Os resultados preliminares indicam uma elevada taxa de adesão (76,2%), acompanhada de uma evasão de 23,8%, concentrada principalmente nas etapas iniciais do ciclo. Adicionalmente, foram observados altos níveis de satisfação global (91,21%), evidenciando avaliação positiva das atividades e contribuição para a sustentação do engajamento ao longo do programa. As análises também revelaram variações estatisticamente significativas entre instituições, sugerindo influência de fatores contextuais no desempenho do modelo. De forma geral, os achados indicam que o modelo é viável, apresenta consistência operacional e demonstra potencial para mobilização e retenção de participantes em contextos institucionais heterogêneos. Ao mesmo tempo, os resultados reforçam a importância de estratégias adaptativas para acomodar diferenças locais e maximizar os níveis de engajamento e permanência. Este estudo corresponde a um ciclo inicial de implementação e deve ser interpretado como evidência preliminar. Embora outras métricas tenham sido coletadas, este trabalho concentrou-se em adesão, evasão e satisfação, alinhado aos objetivos deste ciclo. Investigações futuras incluirão análises longitudinais, ampliação do conjunto de indicadores e aprofundamento das relações entre contexto institucional e desempenho do modelo.

## Aspectos Eticos

Este estudo foi submetido e aprovado pelo Comitê de Etica em Pesquisa (CEP) da Uni- versidade de Pernambuco (UPE), por meio da Plataforma Brasil, em conformidade com a Resolução nº 510/2016 do Conselho Nacional de Saúde (CNS). Todas as participantes foram previamente informadas sobre os objetivos da pesquisa, natureza dos dados coletados, garantia de confidencialidade, anonimização das informações e possibilidade de desistência a qualquer momento, sem qualquer prejuízo acadêmico ou institucional. A participação ocorreu de forma voluntária mediante aceite do Termo de Consentimento Livre e Esclarecido (TCLE), disponibilizado eletronicamente no momento da inscrição no programa. Os dados foram analisados de forma agregada e anonimizada, preservando a identidade das participantes e das instituições envolvidas.

## Declaração de Uso da IA

O ChatGPT foi utilizado para revisão textual, refinamento gramatical e geração de imagem. Todas as sugestões produzidas pela ferramenta foram analisadas de forma critica e revisada integralmente pelos autores, que assumem plena responsabilidade pelo conteúdo final apresentado.
