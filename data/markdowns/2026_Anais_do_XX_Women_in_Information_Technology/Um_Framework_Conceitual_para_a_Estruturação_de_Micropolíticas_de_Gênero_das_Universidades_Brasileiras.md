# Um Framework Conceitual para a Estruturação de Micropolíticas de Gênero das Universidades Brasileiras

Melissa Maria Souza de Carvalho, Gabriela Barbalho Batista, Karen da Silva Figueiredo Medeiros Ribeiro

1 Instituto de Computação – Universidade Federal de Mato Grosso (UFMT) Cuiabá – MT – Brasil

2 Faculdade de Engenharia – Universidade Federal de Mato Grosso (UFMT) Várzea Grande – MT – Brasil

`{melissa.carvalho, gabriela.batista}@sou.ufmt.br, karen@ic.ufmt.br`

Abstract. Women’s participation in Computing in Brazil still faces challenges related to access, retention, and leadership, highlighting gaps in institutional gender policies. This paper proposes a conceptual framework to structure gender micro-policies in Brazilian universities by articulating these dimensions with the institutional pillars of teaching, research, extension, and administration. The framework was developed through a theoretical and exploratory process and refined through a documentary case study at a public university. The results demonstrate the framework’s potential to support the organization, systematization, and analysis of institutional policies through information technology tools, contributing to evidence-based decision-making and to the advancement of gender equity in Computing and STEM fields.

Resumo. A presença feminina na Computação no Brasil ainda enfrenta desafios de acesso, permanência e liderança, evidenciando lacunas em políticas institucionais de gênero. Este artigo propõe um framework conceitual para estruturar micropolíticas em universidades brasileiras, articulando essas dimensões aos eixos de ensino, pesquisa, extensão e administração. A validação ocorre via estudo de caso em uma universidade pública, no qual foram identificadas quinze micropolíticas. Os resultados indicam o potencial do framework para apoiar a organização e análise de políticas por ferramentas de TI, contribuindo para decisões baseadas em evidências e para a equidade de gênero em Computação e STEM.

## 1. Introdução

A presença feminina nas áreas de Computação e STEM (do inglês: Ciência, Tecnologia, Engenharia e Matemática) no Brasil ainda é marcada por desafios estruturais relacionados ao acesso, à permanência e à ascensão a posições de liderança. Esses desafios refletem desigualdades historicamente construídas, que se manifestam tanto nos processos de formação quanto nas trajetórias acadêmicas e profissionais das mulheres [Rapkiewicz et al. 2025]. Estudos recentes na área da Computação evidenciam que essas desigualdades estão associadas a fatores sistêmicos, como vieses de gênero, cultura organizacional excludente e ausência de suporte institucional contínuo, os quais podem levar a altas taxas de evasão acadêmica [Oliveira et al. 2024,

Chang 2026, Silva et al. 2021].

Nos últimos anos, a comunidade de Computação tem avançado na investigação dessas questões, especialmente por meio de estudos empíricos sobre participação, evasão e experiências de mulheres em ambientes acadêmicos e profissionais. Esses estudos evidenciam que, além da sub-representação, persistem desafios relacionados ao senso de pertencimento, à progressão na carreira e ao reconhecimento profissional, que se iniciam na formação universitária e se estendem ao mercado de trabalho [Oliveira et al. 2024]. Nesse contexto, as universidades assumem papel estratégico na promoção da equidade de gênero em STEM, não apenas na formação e produção de conhecimento, mas também na formulação de políticas institucionais que se materializam em micropolíticas, i.e., instrumentos e práticas que operam no cotidiano universitário.

Apesar da relevância dessas iniciativas, revisões recentes indicam que muitas ainda carecem de fundamentação teórica consistente e de modelos que orientem sua concepção, implementação e avaliação, evidenciando lacunas em sua organização e sistematização [Cutrupi et al. 2026]. A ausência desses modelos conceituais limita tanto o avanço científico quanto o desenvolvimento de soluções computacionais baseadas em dados, capazes de apoiar a gestão e a tomada de decisão institucional. Estudos recentes reforçam que frameworks conceituais desempenham papel central na organização de domínios complexos [Perez-Felkner et al. 2025], ao explicitar relações entre elementos, apoiar a análise sistemática e viabilizar a construção de sistemas informacionais e ferramentas computacionais orientadas por dados.

Diante do cenário apresentado, este artigo propõe um framework conceitual para a estruturação de micropolíticas de gênero em universidades brasileiras, com o objetivo de organizar e sistematizar informações sobre políticas institucionais voltadas à equidade de gênero. O framework articula três dimensões centrais: acesso, permanência e liderança, junto aos eixos institucionais de ensino, pesquisa, extensão e administração, permitindo uma análise integrada dessas políticas. Para demonstrar sua aplicabilidade, foi conduzido um estudo de caso baseado na análise documental de uma universidade pública brasileira, no qual foram identificadas e categorizadas 15 micropolíticas de gênero. Os resultados evidenciam o potencial do framework para apoiar o mapeamento, a organização e a análise de políticas institucionais, contribuindo para a construção de bases de dados estruturadas e para o desenvolvimento de sistemas de apoio à decisão.

## 2. Referencial Teórico

### 2.1. Políticas de Gênero

Pesquisas recentes indicam que políticas de gênero constituem instrumentos institucionais estruturados voltados à redução de desigualdades e à promoção da equidade [Álvarez et al. 2025], atuando de forma transversal nas esferas social, econômica e política. De modo geral, essas políticas apresentam três características centrais: [Moreira et al. 2018, Nascimento 2016]: (i) incorporam a questão de gênero em seu design: quem beneficia, como e com qual propósito; (ii) podem ser dirigidas, especificamente, a mulheres ou a grupos historicamente discriminados (ex.: pessoas LGBTQIAPN+, pessoas com deficiência) ou incluir a categoria gênero como eixo em políticas gerais, como combate à pobreza; (iii) têm como finalidade melhorar as condições de vida, garantir os direitos humanos, combater a violência e promover

igualdade e autonomia. Alguns exemplos de políticas públicas de gênero do governo brasileiro são: o Pacto Nacional de Prevenção aos Feminicídios (Decreto nº 11.640/2023), a Lei da Igualdade Salarial (Lei nº 14.611/2023) e a internacionalmente reconhecida Lei Maria da Penha (Lei nº 11.340/2006).

Entre essas iniciativas, existem as políticas de gênero em STEM, tais como leis, normas institucionais e programas criados para reduzir as desigualdades de gênero nessas áreas, combatendo preconceitos, barreiras estruturais e desigualdades de oportunidades na educação e nas carreiras [Meyer e Du 2025]. No Brasil, alguns exemplos de políticas de gênero em STEM são a Lei nº 15.124/2025, que veda a adoção de critérios discriminatórios contra estudantes e pesquisadores em virtude de gestação, de parto, de nascimento ou de adoção, o Prêmio Mulheres e Ciência (Portaria CNPq nº 1.965/2024) e a Chamada Pública CNPq nº 31/2023 - Meninas Nas Ciências Exatas, Engenharias e Computação. No entanto, considerando que a educação em STEM é um dos elementos fundamentais para estas políticas, as universidades tornam-se instituições importantes na concepção e implementação de políticas de gênero em STEM que sejam viáveis e efetivas [Meyer e Du 2025].

### 2.2. Micropolíticas Universitárias

As micropolíticas universitárias referem-se às dinâmicas, fluxos de poder e práticas que ocorrem no cotidiano institucional, diferenciando-se das macropolíticas governamentais por sua natureza relacional e interpretativa. Segundo Pereira (2025), a micropolítica é o campo onde as normas são traduzidas em ações diretas pelos agentes acadêmicos, moldando a cultura organizacional. Nas Instituições de Ensino Superior (IES), essas políticas materializam-se em instrumentos formais, como resoluções, políticas institucionais, núcleos de gênero e outras práticas institucionais que influenciam as relações e experiências da comunidade acadêmica [Sobrosa e Freitas 2021].

Sob a perspectiva de gênero, a análise micropolítica revela que o ambiente universitário não é neutro, sendo estruturado por relações sociais que reproduzem desigualdades de gênero historicamente construídas [Louro 1997]. Essas desigualdades manifestam-se na divisão sexual do trabalho acadêmico, marcada por processos históricos de hierarquização das atividades desempenhadas por homens e mulheres [Hirata e Kergoat 2007]. Assim, as micropolíticas de gênero em instituições de ensino superior atuam como mecanismos de tensão e resistência, buscando corrigir assimetrias por meio de ações de acesso, permanência e valorização profissional.

### 2.3. Trabalhos Relacionados

A literatura recente, especialmente nos anais do Women in Information Technology (WIT), tem investigado de forma ampla a participação feminina na Computação, com ênfase em diagnósticos de acesso, permanência e liderança. Estudos como Magalhães et al. (2025) e Rocha et al. (2025) analisam representatividade e evasão em cursos de Engenharia e Ciência da Computação, evidenciando baixa participação feminina e maiores taxas de evasão. Na dimensão de liderança, Castilho e Gouveia (2025) apontam a sub-representação de mulheres na pós-graduação. Embora relevantes, esses trabalhos concentram-se predominantemente na caracterização do problema, bem como em análises contextuais específicas, sem propor modelos conceituais voltados à

### estruturação sistemática de micropolíticas institucionais.

Além disso, observa-se um avanço no uso de abordagens baseadas em dados e ferramentas computacionais, como em Silva et al. (2021) e Pimentel et al. (2025), que exploram problemas sociais relacionados ao gênero. Outras iniciativas, como o content hub de liderança feminina em TI [Gomes et al. 2024] e a plataforma ELLAS [Berardi et al. 2023], contribuem para a organização de dados e informações sobre gênero em STEM. No entanto, essas propostas focam majoritariamente em contextos externos ou em “macro” políticas, não contemplando as dinâmicas institucionais internas das universidades. Nesse contexto, identifica-se uma lacuna na literatura quanto à estruturação e análise sistemática de micropolíticas institucionais de gênero no contexto universitário. Este trabalho busca preencher essa lacuna ao propor um framework conceitual que organiza essas políticas, contribuindo para a sistematização do conhecimento e para o suporte à tomada de decisão baseada em evidências.

## 3. Metodologia

Um framework conceitual é uma estrutura teórica, visual ou narrativa que organiza ideias, crenças e teorias para fundamentar uma pesquisa ou projeto. Ele funciona como um mapa para definir relações entre variáveis, facilitando a compreensão de temas complexos e direcionando a tomada de decisão [Kulesa et al. 2024]. Na área de sistemas computacionais e integração tecnológica, frameworks conceituais desempenham papel fundamental ao estruturar problemas complexos, integrar conceitos teóricos e orientar o desenvolvimento de soluções [Patrício et al. 2025]. Estudos recentes indicam que esses frameworks permitem organizar e sintetizar conhecimento disperso, explicitar relações entre variáveis e apoiar a formulação e validação de contribuições científicas [Kulesa et al. 2024, Sale e Carlin 2025]. Dessa forma, optou-se pelo desenvolvimento de um framework conceitual para organizar o conhecimento acerca das micropolíticas de gênero das universidades brasileiras, visando que este possa subsidiar pesquisas e sistemas futuros relacionados ao tema. O processo de criação do framework proposto ocorreu de acordo com as etapas apresentadas na Figura 1.

#### Figura 1. Processo de criação do framework proposto.

O processo de criação do framework teve início com o estudo do referencial teórico, que, combinado ao conhecimento empírico das autoras da pesquisa, permitiu a estruturação preliminar dos conceitos-chave e variáveis do framework (passo 1), relacionados às questões de acesso, permanência e liderança, bem como ao contexto universitário. Em seguida, foi realizada uma sessão de brainstorming exploratório voltado à elicitação de possíveis políticas institucionais universitárias relacionadas a cada um dos conceitos da etapa anterior (passo 2), com o objetivo de mapear tipos de políticas que poderiam contribuir para o acesso, a permanência e a liderança de mulheres nas universidades. A partir dessa etapa, foram levantadas diferentes

possibilidades de políticas, como programas de incentivo à participação feminina, ações de permanência acadêmica e iniciativas voltadas ao fortalecimento da presença de mulheres em espaços de decisão, incentivando a liderança feminina.

Na etapa seguinte, foi realizada uma busca na web a fim de identificar micropolíticas universitárias reais que instanciassem as políticas elicidadas no brainstorm e, posteriormente, as micropolíticas identificadas foram analisadas segundo os conceitos e variáveis predefinidos (passo 3). Ao todo, 15 micropolíticas provenientes de 10 IES distintas foram analisadas no passo 3. Estes três passos serviram como base para a criação da versão inicial do framework (passo 4). A Tabela 1 ilustra o processo dos passos 1 a 3 para uma micropolítica universitária de gênero.

Tabela 1. Exemplo ilustrativo do processo: passos 1 a 3.

|Passo 1: Identificação de conceitos-chave e variáveis|Passo 2: Polí elicitada|tica|Passo analisad|3: Micropolítica a|real|
|---|---|---|---|---|---|
|Problema:Permanência|Política:Com|bate|RESOL|UÇÃO Nº 41/2022 -|CD:|
|Eixo:Administração|ao assédio|e|Aprova|a política de preven|ção e|
|Agentes beneficiadas: Todas as mulheres que integram a comunidade acadêmica e administrativa da|discriminação mulheres universidade|de na|enfrenta as mulh Univers|mento das violências c eres no âmbito da Fun idade do Estado do|ontra dação Rio|
|universidade|Instrumento:||Grande|do Norte - Fuern|e da|
|Influências contextuais proximais:|Política|de|Univers|idade do Estado do|Rio|
|Violências de gênero|prevenção||Grande|do Norte - UERN||

Com a primeira versão do framework criada, decidiu-se por realizar um estudo de caso na Universidade Federal de Mato Grosso (UFMT), a fim de realizar o mapeamento documental das micropolíticas de gênero desta instituição (passo 5). Os documentos selecionados passaram então a compor o conjunto de micropolíticas analisadas no estudo de caso apresentado na Seção 4 deste trabalho. Uma vez mapeadas, foi possível inferir novas variáveis e relações para atualizar a versão inicial do framework proposto (passo 6), cuja versão final é apresentada na Seção 5 deste artigo. Por fim, uma validação preliminar do framework foi realizada a partir da estruturação das 15 micropolíticas universitárias de gênero da UFMT (passo 7).

## 4. Estudo de Caso: Micropolíticas Universitárias da UFMT

Com o intuito de subsidiar as pesquisas para o desenvolvimento do framework, realizou-se um estudo de caso documental a fim de mapear todas as micropolíticas de gênero de uma IES, para isso, foi selecionada a UFMT, à qual as autoras desta pesquisa estão vinculadas.

O estudo de caso foi iniciado a partir da extração de micropolíticas institucionais previamente catalogadas em um estudo acadêmico relacionado à temática de políticas universitárias de gênero e de liderança [Pereira 2025]. Cada uma das 17 micropolíticas identificadas neste trabalho foi analisada individualmente com o objetivo de verificar sua relação com políticas voltadas às mulheres e às dimensões analíticas do framework. Durante esse processo, observou-se que muitas resoluções tratavam de temas institucionais mais amplos, como aspectos administrativos ou normativos da universidade, não estando diretamente relacionadas à criação de políticas específicas de

gênero. Dessa forma, foi necessário realizar um processo de filtragem das resoluções, mantendo apenas aquelas que apresentavam relação direta com a temática de gênero e/ou que estabeleciam ações voltadas às mulheres, totalizando 8 micropolíticas de gênero selecionadas para o estudo de caso.

Para completar os dados do estudo de caso, foram realizadas novas pesquisas no sistema público de resoluções da UFMT, a fim de complementar e atualizar os dados identificados na revisão da literatura. Para essas buscas foram utilizadas as strings: “ diversidade ”, “ gênero ”, “ ações afirmativas ”, “ cota ”, “ igualdade ” e “ inclusão ”, bem como filtros disponíveis no sistema, por meio da busca livre e da seleção da opção “todas as resoluções”, contemplando os órgãos Conselho Diretor, CONSEPE e CONSUNI, sem restrições por número ou ano. Estas buscas resultaram em um total de 13 micropolíticas de gênero, das quais, excluindo-se as duplicatas em relação às provenientes de [Pereira 2025], 4 foram selecionadas para o estudo. Também foram testadas outras strings de cunho social que não retornaram resultados, a saber: “ maternidade”, “ lactante ”, “ licença maternidade”, “ equidade ”, “ violência ”, “ auxílio creche ”, “ filhos”, “ puerpério ”, “ amamentação ”, “ gestante”, “gravidez ”, “ assédio ”, “ importunação ”, “ segurança ”, “ universidade ”, “ pesquisadora ”, “ bolsista ”, “ docente ”, “ liderança ” e “ representatividade ”. Adicionalmente, foram identificadas mais 3 micropolíticas por meio de mecanismos de busca, permitindo recuperar documentos institucionais não indexados no sistema público de resoluções, evidenciando limitações no processo de recuperação automática de documentos.

No total, 15 documentos entre resoluções, editais e portarias compuseram o conjunto de micropolíticas de gênero analisadas neste estudo. Para organizar as informações obtidas durante o processo de mapeamento, foi elaborada uma planilha analítica das micropolíticas de acordo com os conceitos e categorias do framework, permitindo sistematizar e comparar as características das políticas identificadas. A Tabela 2 lista as micropolíticas do estudo de caso com os seus respectivos instrumentos institucionais utilizados para implementação da política, as dimensões de impacto de gênero e as pessoas agentes beneficiadas pelas micropolíticas.

Tabela 2. Micropolíticas de gênero mapeadas na UFMT.

|Micropolítica de Gênero|Instrumento|Impacto de Gênero|Agentes Beneficiadas|
|---|---|---|---|
|Resolução CONSEPE nº 20/1995|Curso de especialização|Acesso|Mulheres estudantes de pós-graduação, Mulheres da comunidade externa|
|Resolução CONSUNI nº 04/2006|Criação de núcleo de pesquisa|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas,Mulheres da comunidade externa|
|Resolução CONSUNI nº 01/2011|Garantia de inclusão e uso de nome social|Acesso Permanência|Mulheres trans estudantes de graduação e depós-graduação|
|Resolução CONSEPE nº 96/2013|Curso de especialização|Acesso Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas, Mulheres da comunidade externa|
|Resolução CONSUNI nº 19/2016|Política institucional de prevenção à violência|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas,Mulheres da comunidade externa|

|Micropolítica de Gênero|Instrumento|Impacto de Gênero|Agentes Beneficiadas|
|---|---|---|---|
|Resolução Conselho Diretor nº 02/2018|Articulação institucional para liderança feminina|Liderança|Servidoras docentes e técnicas em cargos de gestão|
|Resolução CONSUNI-UFMT nº 42/2021|Regulamentação institucional de núcleo depesquisa|Acesso Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas,Mulheres da comunidade externa|
|Resolução CONSEPE-UFMT nº 197/2021|Reserva de vagas (Ação Afirmativa)|Acesso Permanência|Mulheres estudantes de pós-graduação pertencentes a grupos historicamente excluídos, Mulheres da comunidade externa pertencentes a grupos historicamente excluídos|
|Regimento do Núcleo de Estudo sobre a Mulher e as Relações de Gênero (NUEPOM)|Regulamentação institucional de núcleo de pesquisa|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas, Mulheres da comunidade externa|
|Resolução CONSUNI-UFMT nº 99/2022|Regulamentação institucional de núcleo depesquisa|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas|
|Edital de Seleção de Aluno Regular 2026/1 do Programa de Pós-Graduação em Computação Aplicada (PPGCOMP)| Reserva de vagas (Cotas)|Acesso|Mulheres estudantes de pós-graduação, Mulheres da comunidade externa|
|Resolução CONSUNI-UFMT nº 280/2025|Protocolo, Comissões e Monitoramento|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas, Mulheres da comunidade externa|
|PROPESQ nº 01-N/2025|Regulamentação institucional de grupos de trabalho|Acesso Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas|
|PROPESQ nº 04-N/2025|Reserva de vagas|Acesso Permanência|Mulheres estudantes de graduação e de pós-graduação pretas, com deficiência, indígenas, quilombolas e trans Servidoras docentes e técnicas pretas, com deficiência, indígenas, quilombolas e trans|
|Ofício Circular nº 08/2025-CONSUNI|Serviço institucional de acolhimento|Permanência|Mulheres estudantes de graduação e de pós-graduação, Servidoras docentes e técnicas,Mulheres da comunidade externa|

## 5. Framework para Micropolíticas Universitárias

O framework apresentado na Figura 2 foi desenvolvido a partir do processo metodológico descrito na Seção 3 e refinado com base nos achados do estudo de caso (Seção 4). Seu objetivo é estruturar, de forma sistemática, micropolíticas de gênero no contexto das universidades brasileiras, apoiando sua identificação, organização e análise. A versão atual do framework incorpora elementos empíricos observados durante a análise documental, incluindo: (i) o contexto institucional universitário de

publicação, (ii) a micropolítica documentada, (iii) suas dimensões de impacto de gênero e (iv) as agentes beneficiadas. Ressalta-se que o modelo apresentado não tem como intuito estabelecer todas as relações possíveis entre os elementos do modelo, mas sim representar quais elementos estão envolvidos na relação de causa e efeito investigada.

Figura 2. Framework conceitual de micropolíticas universitárias de gênero.

1. Contexto universitário: Refere-se ao ambiente organizacional no qual a micropolítica é concebida, publicada e aplicada. Cada IES possui cultura organizacional, estrutura administrativa própria, nível de institucionalização das políticas, disponibilidade de recursos e apoio da gestão. Esse contexto pode potencializar ou limitar os efeitos das micropolíticas de gênero.

2. Instituição de Ensino Superior (IES): Corresponde à instituição responsável pela formulação, regulamentação e implementação da micropolítica de gênero. Esse componente permite identificar a origem institucional da política, sua estrutura de governança e o contexto organizacional no qual está inserida.

3. Micropolítica de gênero: Variável independente. Representa o principal fenômeno institucional analisado no modelo, correspondendo às ações, normas, programas, serviços ou práticas institucionais voltadas à promoção da equidade de gênero no contexto universitário. As micropolíticas materializam-se por meio de instrumentos institucionais formais que atuam sobre desigualdades relacionadas ao acesso, à permanência e à liderança de mulheres na universidade.

4. Instrumento: Variável mediadora. Refere-se ao mecanismo institucional utilizado para operacionalizar a micropolítica de gênero (ex.: cotas, bolsas, programas). Os instrumentos representam a forma concreta pela qual a política é institucionalizada,

regulamentada ou executada na universidade. Esse elemento medeia a relação entre a micropolítica e seus impactos institucionais, uma vez que diferentes instrumentos podem influenciar o alcance, a formalização e a efetividade das ações implementadas.

5. Dimensões de impacto de gênero: Variável dependente. Corresponde à dimensão da desigualdade de gênero que a micropolítica busca enfrentar ou mitigar. O framework organiza essas dimensões em três categorias analíticas centrais:

- Acesso: relacionado ao ingresso e à ampliação da participação de mulheres na universidade;

- Permanência: relacionado às condições institucionais, sociais e acadêmicas necessárias para continuidade e conclusão da trajetória universitária de mulheres na universidade;

- Liderança: relacionado à ascensão, representação e ocupação de espaços de decisão, gestão e reconhecimento acadêmico-profissional por mulheres.

6. Agentes beneficiadas: Representam os grupos sociais diretamente contemplados pelas micropolíticas de gênero. Esse elemento permite identificar quais segmentos da comunidade acadêmica são priorizados ou impactados pelas ações institucionais, tais como estudantes de graduação, estudantes de pós-graduação, servidoras docentes e técnicas, e mulheres da comunidade externa.

7. Eixo: Variável moderadora. Indica o eixo universitário (ensino, pesquisa, extensão e administração) no qual a micropolítica é aplicada, ainda que, indiretamente, os eixos atuem de forma indissociada.

8. Interseccionalidades: Variável moderadora. Refere-se aos diferentes marcadores sociais que atravessam as experiências das mulheres e influenciam os efeitos das micropolíticas. A perspectiva interseccional reconhece que desigualdades de gênero não ocorrem de forma isolada, mas articuladas a fatores como raça, etnia, classe social, deficiência, identidade de gênero, territorialidade e pertencimento a grupos historicamente marginalizados. Assim, diferentes grupos de mulheres podem experienciar de maneira distinta os impactos de uma mesma micropolítica.

9. Influências contextuais proximais: Variável moderadora. Refere-se aos fatores socioculturais e institucionais mais imediatos que afetam diretamente as experiências das agentes beneficiadas e influenciam os resultados das micropolíticas de gênero. Essas influências podem atuar como barreiras ou facilitadores no processo de acesso, permanência e liderança das mulheres no ambiente universitário. Alguns exemplos são a violência de gênero, discriminação, ausência de suporte institucional, cultura organizacional excludente e redes de apoio e pertencimento.

O modelo proposto retrata como as micropolíticas universitárias de gênero, implementadas pelas IES e operacionalizadas por diferentes instrumentos institucionais, atuam sobre as dimensões de acesso, permanência e liderança de mulheres nas universidades. Essa relação é mediada pelos instrumentos de implementação das políticas, os quais influenciam sua formalização, alcance e efetividade institucional. Além disso, os efeitos das micropolíticas são moderados pelo eixo universitário de aplicação, pelas influências contextuais proximais e pelas condições interseccionais das agentes beneficiadas, evidenciando que os impactos das políticas variam conforme o contexto institucional e os diferentes marcadores sociais envolvidos.

Para operacionalizar o framework, foi desenvolvido um template estruturado em planilha, acompanhado de um dicionário de dados que orienta a extração e o registro padronizado das informações dos documentos de micropolíticas para análise conforme a estrutura dos elementos e relações do modelo, bem como algumas das suas principais propriedades. Todos os artefatos produzidos, incluindo: o modelo do framework conceitual, a planilha template, o dicionário de dados, o conjunto de dados abertos das 15 micropolíticas da UFMT e o conjunto de dados abertos das 15 micropolíticas do brainstorm, foram disponibilizados na plataforma de ciência aberta Open Science Framework (OSF) no endereço https://osf.io/xsu37.

## 6. Considerações finais

Este trabalho apresentou um framework conceitual para a estruturação de micropolíticas de gênero em universidades brasileiras, articulando as dimensões de acesso, permanência e liderança aos eixos institucionais de ensino, pesquisa, extensão e administração. Como principal contribuição científica, o framework sistematiza um domínio ainda pouco explorado na literatura, organizando conceitos, variáveis e relações que apoiam a análise comparativa, a organização do conhecimento e o desenvolvimento de pesquisas e sistemas voltados à gestão de dados de políticas institucionais de gênero, como ontologias, plataformas de dados, sistemas de recuperação da informação, mecanismos de mineração documental e ferramentas de apoio à tomada de decisão. Nesse sentido, a proposta dialoga diretamente com os interesses da comunidade do WIT, ao oferecer uma contribuição estruturante para pesquisas interdisciplinares em Computação, STEM, gênero e políticas institucionais.

Do ponto de vista prático, o framework demonstrou aplicabilidade ao estruturar as 15 micropolíticas identificadas no estudo de caso da UFMT, ainda que esse processo não tenha sido detalhado passo a passo neste artigo devido à limitação de espaço. Essa validação preliminar evidencia o potencial do modelo para apoiar pesquisadores da Computação na coleta, categorização, modelagem e análise de dados institucionais relacionados à equidade de gênero. Além disso, a integração do framework com um dicionário de dados e uma planilha estruturada contribui para reduzir limitações associadas à recuperação não padronizada de documentos institucionais, promovendo maior transparência, acessibilidade e interoperabilidade dos dados. O modelo também pode subsidiar aplicações práticas em áreas como Ciência de Dados, Inteligência Artificial, Governo Eletrônico, Sistemas de Informação e Web Semântica, permitindo desde a construção de bases de conhecimento até o treinamento de modelos computacionais para identificação automática de micropolíticas em documentos institucionais.

Como trabalhos futuros, pretende-se realizar uma avaliação sistemática do framework com especialistas das áreas de políticas públicas universitárias e estudos de gênero, analisando sua clareza, completude e aplicabilidade. Além disso, almeja-se ampliar a coleta e estruturação de micropolíticas em diferentes IES brasileiras, bem como desenvolver uma plataforma baseada no framework proposto, incorporando mecanismos de pesquisa estruturada, transparência de dados e participação colaborativa da comunidade universitária, alinhados aos princípios de governo eletrônico, ciência aberta e governança de dados.

## Uso de Inteligência Artificial

De acordo com a Portaria CNPq nº 2.664, de 6 de março de 2026, esta pesquisa usou tecnologias de inteligência artificial generativa nos seguintes contextos: (i) a ferramenta Consensus foi utilizada como suporte à identificação e organização parcial do referencial teórico; (ii) a ferramenta Gemini foi usada para análise preliminar de documentos institucionais e para a identificação de termos-chave na busca de resoluções relacionadas às políticas de gênero; (iii) a ferramenta ChatGPT (GPT 5.5) foi utilizada como apoio à revisão gramatical, organização estrutural e adequação da redação acadêmica do texto. As autoras permaneceram totalmente responsáveis pelo conteúdo científico, pela interpretação dos dados e pela revisão final do manuscrito.
