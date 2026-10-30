# HerCode: Uma Ferramenta Gamificada para Meninas Descobrirem a Programação com Representatividade Feminina

Wanuelle Rodrigues Gonçalves, Amanda Vasconcelos Sales, David Washington Freitas Lima, Fabiann Matthaus Dantas

1Instituto Federal de Educação, Ciência e Tecnologia do Amazonas (IFAM) Campus Manaus Zona Leste – Manaus – AM – Brazil

{ 2025000461, 2025000185, david.lima, fabiann.dantas } @ifam.edu.br

Abstract. This paper presents HerCode, a gamified mobile application designed to introduce programming logic to girls in lower secondary education, integrating technical instruction with the recognition of pioneering women in Computing. The proposal is grounded in scaffolding, meaningful learning, microlearning, and gamification, organizing content into progressive modules supported by an achievement system. The development process included a literature review, interviews with education specialists, requirements definition, prototyping, and implementation using Flutter. As a contribution, HerCode combines introductory programming learning with the promotion of female representation in Computing.

Resumo. O presente trabalho apresenta o HerCode, um aplicativo móvel gamificado voltado à introdução de lógica de programação para meninas do Ensino Fundamental II, integrando ensino técnico e valorização de mulheres pioneiras na Computação. A proposta fundamenta-se em scaffolding, aprendizagem significativa, microlearning e gamificação, organizando o conteúdo em módulos progressivos com sistema de conquistas. O desenvolvimento incluiu revisão teórica, entrevistas com especialistas da educação, definição de requisitos, prototipação e implementação em Flutter. Como contribuição, o HerCode articula aprendizagem inicial em programação e representatividade feminina.

## 1. Introdução

A desigualdade de gênero na área da Computação e das Tecnologias da Informação (TIC) é amplamente evidenciada. Dados do IBGE [2024] indicam que as mulheres representam apenas 15% dos estudantes matriculados em cursos de graduação nesse campo [Nizer, 2024]. Esse cenário reflete tanto a baixa procura por cursos da área quanto os elevados índices de evasão feminina, associados a fatores culturais, históricos, sociais e psicológicos [Morais and Morais 2020].

No âmbito sociocultural, as desigualdades de gênero impactam significativamente as dificuldades enfrentadas pelas mulheres [Aguiar et al. 2024]. Preconceito, sexismo, misoginia, segregação feminina e tratamento desigual em relação aos homens configuram problemas persistentes que contribuem para a evasão e o desinteresse nas áreas da Computação [dos Santos and Marczak 2023].

Além disso, a ausência de destaque às contribuições femininas na história da ciência e da computação fortalece estereótipos de gênero [Oreskes 1996]. A reduzida visibilidade de modelos femininos no setor dificulta a identificação e o sentimento de pertencimento de meninas em carreiras STEM (Ciência, Tecnologia, Engenharia e Matemática) [Morais and Morais 2020], reforçando a percepção de que a Computação é uma área predominantemente masculina [Santos 2018].

A combinação entre estereótipos de gênero, ausência de representatividade feminina e fatores socioculturais contribui para o afastamento de meninas da área da Computação desde as fases iniciais de formação. A falta de conhecimento sobre a área, somada à influência desses estereótipos, reduz o interesse e compromete a construção de uma percepção positiva sobre carreiras em STEM [de Galés Silva et al. 2023].

Evidências apontam que o incentivo precoce é fundamental para ampliar a participação feminina na Computação. Iniciativas voltadas ao ensino fundamental tendem a ser mais eficazes do que aquelas realizadas no ensino médio, fase em que muitas jovens já definiram suas escolhas profissionais [de Holanda et al. 2017, Fiori et al. 2020]. Estudos indicam que, entre os onze e treze anos, estudantes passam a identificar áreas com as quais possuem maior afinidade e desempenho [Denner 2011]. Nesse período, a percepção que as meninas constroem sobre si mesmas influencia diretamente suas escolhas futuras [de Galés Silva et al. 2023]. Assim, o contato precoce com a ciência e a computação torna-se relevante para a formação de percepções e compreensões sobre o mundo [Lucena et al. 2025].

Apesar da relevância do incentivo precoce, ainda há necessidade de ferramentas educacionais que integrem aprendizagem de conceitos computacionais com estratégias de representatividade feminina, especialmente voltadas ao público adolescente. A criação de recursos que promovam identificação, pertencimento e interesse desde cedo mostra-se essencial para ampliar a participação feminina na área.

Diante desse contexto, este trabalho apresenta o HerCode, um aplicativo móvel gamificado voltado para meninas adolescentes, com o objetivo de ensinar conceitos introdutórios de lógica de programação guiado por pioneiras da computação. A abordagem pedagógica articula o scaffolding de Vygotsky [Nordlof 2014], com suporte gradual à aprendizagem, e a Aprendizagem Significativa de Ausubel, conectando conceitos abstratos à realidade das meninas.

A principal contribuição desse trabalho consiste na proposição de uma ferramenta educacional que utiliza gamificação e representatividade feminina para promover um aprendizado de computação mais acessível e inclusivo, incentivando o interesse e o sentimento de pertencimento de meninas na área da Computação.

## 2. Trabalhos Relacionados

Diversas iniciativas têm sido desenvolvidas com o objetivo de motivar e ensinar meninas sobre a área da Computação. Essas propostas adotam diferentes abordagens pedagógicas e tecnológicas, buscando criar ambientes mais inclusivos para o público feminino em distintas faixas etárias, além de ampliar a visibilidade de mulheres que contribuíram significativamente para o desenvolvimento científico e tecnológico. A partir de uma análise de soluções alinhadas aos objetivos deste trabalho, foram identificadas quatro ferramentas, descritas a seguir.

O estudo de [Lucena et al. 2025] apresenta o desenvolvimento do jogo digital Garotas Espertas – O Jogo, concebido para divulgar a trajetória de mulheres cientistas cujas contribuições impactaram a Computação. A proposta caracteriza-se como uma ferramenta lúdica voltada ao público infantil, com o intuito de promover a construção de conhecimento científico dissociado de estereótipos de gênero. O jogo aborda a carreira e as realizações de quatro figuras históricas relevantes para a tecnologia e a Ciência da Computação: Hipátia, Ada Lovelace, Hedy Lamarr e Joan Clarke.

De forma semelhante, [Nizer et al. 2024b] descreve o desenvolvimento do jogo OurPlace: Amazing Grace, com foco na motivação de meninas para áreas STEM, nas quais a participação feminina ainda é inferior à masculina. Trata-se de um jogo digital 2D do tipo Point and Click Adventure, centrado em diálogos e resolução de desafios. A narrativa explora eventos da vida de Grace Hopper, destacando sua contribuição para a criação do primeiro compilador e a popularização do termo “bug”, com o objetivo de evidenciar a relevância feminina na área e estimular o interesse por carreiras tecnológicas.

Adicionalmente, [Nizer et al. 2024a] apresenta o jogo OurPlace: Hedy Lamarr, também no formato 2D Point and Click Adventure, desenvolvido para dispositivos móveis Android. A proposta busca inspirar jovens mulheres a considerarem carreiras em STEM, por meio da contextualização da vida e das realizações de Hedy Lamarr, ressaltando seu papel como pioneira na história da computação e sua contribuição para tecnologias que fundamentaram o Wi-Fi.

Complementarmente, [Briceno et al. 2021] propõem o Mundo Bit Byte, um jogo digital de plataforma para dispositivos móveis Android que utiliza uma narrativa de ficção científica para apresentar personalidades femininas históricas da computação com o objetivo central de incentivar jovens mulheres a considerarem carreiras em TI por meio da representatividade. No enredo, um grupo de garotas viaja no tempo para recuperar pilares do conhecimento roubados por alienígenas, passando por cinco fases que homenageiam figuras como Ada Lovelace e Grace Hopper.

Embora compartilhem o objetivo de promover representatividade feminina e incentivar o interesse pela Computação, as iniciativas descritas concentram-se principalmente na divulgação histórica e na inspiração por meio de narrativas biográficas. O HerCode diferencia-se por propor um aplicativo educacional gamificado com foco explícito no ensino de conceitos técnicos introdutórios de lógica de programação, articulando representatividade feminina e fundamentação pedagógica. Assim, além de promover identificação e pertencimento, a ferramenta busca desenvolver competências iniciais na área. A Tabela 1 apresenta uma síntese comparativa das principais características dos trabalhos analisados.

|Ferramenta|Plataforma|Tipo|Estratégia Educacional|
|---|---|---|---|
|OurPlace: Hedy Lamarr [Nizer et al. 2024a]|Mobile|Jogo 2D Point and Click|Narrativa histórica com resolução de quebra-cabeças baseada na trajetória de Hedy Lamarr.|
|Garotas Espertas – O Jogo [Lucena et al. 2025]|Web|Jogo digital|Minigames educativos para apresentar pioneiras da ciência e tecnologia.|
|OurPlace: Amazing Grace [Nizer et al. 2024b]|Mobile/Desktop|Jogo narrativo 2D|Narrativa interativa baseada na vida de Grace Hopper com desafios e diálogos.|
|Mundo Bit Byte [Briceno et al. 2021]|Mobile|Jogo digital plataforma|Narrativa de ficção científica com quebra-cabeças baseados nas trajetórias de cinco pioneiras da computação.|
|HerCode (Proposta)|Mobile|Aplicativo educacional gamificado|Lições curtas com mentorias de pioneiras, atividades práticas de lógica e sistema de conquistasparaprogressão.|

Tabela 1. Comparaç ão entre ferramentas relacionadas e a proposta HerCode.

## 3. Metodologia

Esta pesquisa caracteriza-se como aplicada, de natureza qualitativa, com objetivos exploratórios. Do ponto de vista dos procedimentos técnicos, configura-se como uma pesquisa de desenvolvimento, envolvendo a concepção, prototipação e implementação de um artefato educacional digital, apoiada por revisão bibliográfica e pesquisa de campo por meio de entrevistas semiestruturadas.

O desenvolvimento do HerCode seguiu uma abordagem metodológica estruturada em etapas sequenciais, conforme ilustrado na Figura 1, com o objetivo de garantir que a ferramenta fosse fundamentada tanto em evidências empíricas quanto em abordagens pedagógicas adequadas ao público-alvo.

O processo compreendeu: (i) identificação da problemática, (ii) levantamento teórico e definição das abordagens pedagógicas, (iii) coleta de dados qualitativos com especialistas da área da educação, (iv) levantamento de requisitos, (v) prototipação e (vi) implementação da solução, buscando assegurar fundamentação científica consistente, validação pedagógica por profissionais da área e alinhamento da proposta às necessidades do público-alvo.

A etapa inicial consistiu na identificação da problemática por meio de revisão bibliográfica. A análise de estudos sobre a participação feminina na Computação e nas Tecnologias da Informação evidenciou fatores associados ao desinteresse e à evasão, como a ausência de estímulo precoce, a limitada representatividade feminina e a percepção da área como predominantemente masculina [Morais and Morais 2020, dos Santos and Marczak 2023].

Também foram analisadas iniciativas educacionais e ferramentas digitais voltadas à introdução da lógica de programação e do pensamento computacional. Esse levanta-

Figura 1. Etapas Metodológicas

mento subsidiou a definição do público-alvo, meninas entre 11 e 13 anos, matriculadas no Ensino Fundamental II, fase considerada estratégica para intervenções voltadas ao incentivo em STEM [Fiori et al. 2020, Denner 2011].

Com base nesse levantamento, foram selecionadas as abordagens pedagógicas que fundamentaram a proposta, incluindo: (i) scaffolding, com oferta de suporte progressivo até a autonomia da usuária; (ii) aprendizagem significativa, promovendo a conexão entre novos conteúdos e conhecimentos prévios; (iii) microlearning, com organização do conteúdo em unidades curtas; e (iv) gamificação, utilizada como estratégia de engajamento baseada em conquistas e progressão estruturada.

Após o levantamento teórico e a definição preliminar da proposta pedagógica, realizou-se uma etapa complementar de coleta de dados qualitativos por meio de entrevistas semiestruturadas com 10 profissionais da área da educação, incluindo professoras, pedagogas e coordenadoras escolares. Nessa etapa, além de compreender percepções sobre o ensino de lógica de programação para meninas e identificar desafios pedagógicos, foi apresentada a proposta do aplicativo e seu alinhamento pedagógico às especialistas, com o objetivo de obter considerações, sugestões de aprimoramento e validação quanto à adequação da abordagem didática e da faixa etária definida.

A etapa de levantamento de requisitos definiu as funcionalidades essenciais do aplicativo, considerando os objetivos pedagógicos e a experiência da usuária. Foram estabelecidos requisitos funcionais, como sistema de módulos, desafios interativos, progressão por níveis e desbloqueio de conteúdo, e não funcionais, como usabilidade, acessibilidade e desempenho, que orientaram o desenvolvimento da solução.

Posteriormente, foi realizada a prototipação de alta fidelidade da interface utilizando a ferramenta Figma, permitindo a definição do fluxo de navegação, organização dos módulos e elementos visuais de gamificação.

Por fim, a implementação do aplicativo foi conduzida utilizando a linguagem Dart e o framework Flutter, escolhidos por sua capacidade de desenvolvimento multiplataforma e desempenho em aplicações móveis. Foram empregadas bibliotecas para gerenciamento de estado, navegação entre telas e persistência local de dados, possibilitando a estruturação modular do conteúdo e o controle da progressão da usuária. A arquitetura adotada buscou garantir escalabilidade e organização do código, facilitando futuras expansões da ferramenta.

## 4. HerCode

O HerCode é um aplicativo móvel gamificado voltado ao ensino introdutório de lógica de programação para meninas, estruturado com foco na progressão sequencial, aprendizagem gradual e promoção da representatividade feminina na Computação. A aplicação organiza o conteúdo em módulos de complexidade crescente, integrando ensino técnico, prática interativa e mecanismos de motivação baseados em conquistas.

A arquitetura pedagógica da ferramenta fundamenta-se em cinco eixos principais: (i) gamificação, por meio de desbloqueio progressivo de módulos e recompensas; (ii) scaffolding, com suporte gradual e orientação estruturada durante o processo de aprendizagem; (iii) aprendizagem significativa, operacionalizada por meio de analogias com situações do cotidiano das usuárias; (iv) microlearning, com lições curtas centradas em um único conceito seguidas de atividades práticas; e (v) representatividade histórica integrada, que associa o avanço no conteúdo ao desbloqueio de narrativas sobre mulheres pioneiras da Computação.

O percurso de aprendizagem ocorre de forma sequencial, dessa forma a usuária inicia acessando um módulo, realiza a lição correspondente e, em seguida, resolve exercícios de fixação. Ao concluir o módulo com êxito, desbloqueia uma conquista, obtém acesso à história de uma pioneira da Computação e libera o próximo módulo. Caso não conclua a etapa, o sistema verifica a disponibilidade de vidas: se houver tentativas restantes, a usuária pode repetir o desafio; caso contrário, é direcionada a exercícios livres para recuperar vidas antes de retornar ao fluxo principal.

A Figura 2 apresenta o fluxograma de interação que representa esse ciclo de progressão, o qual se repete até a conclusão do último módulo, encerrando o percurso formativo dentro da aplicação.

Figura 2. Fluxograma geral de interaç ão

## 5. Resultados e Discussões

O acesso ao HerCode inicia-se pela tela de apresentação (Figura 3), na qual são expostos o propósito da aplicação, seus objetivos educacionais e uma introdução aos conceitos básicos de lógica de programação. Essa etapa tem a função de contextualizar a usuária quanto à proposta pedagógica e ao funcionamento da plataforma. A mediação inicial é

realizada pela personagem Ada Lovelace, que atua como elemento de representatividade e introdução ao percurso formativo.

Concluída a etapa introdutória, a usuária é direcionada à tela principal (Figura 4), que centraliza a navegação da aplicação. Nessa interface são exibidas as vidas disponíveis, os módulos de aprendizagem organizados sequencialmente e as demais funcionalidades acessíveis por meio da barra inferior. Essa organização busca oferecer clareza estrutural e facilitar a progressão no conteúdo.

Cada módulo é composto por lições curtas (Figura 5) estruturadas em um ciclo pedagógico que envolve: apresentação do conceito, exemplificação por meio de analogias com situações cotidianas, realização de atividades interativas e fornecimento de feedback imediato. Essa organização busca favorecer a compreensão progressiva e reduzir a sobrecarga cognitiva durante o processo de aprendizagem.

O percurso formativo contempla os principais conceitos introdutórios da programação, distribuídos de forma sequencial: Lógica de Programação; Algoritmos e Sequência; Variáveis; Tipos de Informação; Entrada e Saída de Dados; Operadores e Comparações; Estruturas Condicionais; Repetições ( loops ); e, por fim, Combinação de Estruturas e Resolução de Problemas. Essa estrutura permite que o aprendizado ocorra de maneira gradual, prática e contextualizada.

Os exercícios (Figura 6) adotam um modelo de questões de múltipla escolha, direcionando o foco ao desenvolvimento do raciocínio lógico e à compreensão conceitual, ao mesmo tempo em que minimizam dificuldades relacionadas à sintaxe ou à escrita formal

de código.

Durante a interação com as lições, a usuária acessa a explicação do conceito e, ao prosseguir, realiza um exercício de fixação baseado em alternativas de resposta. Caso selecione uma alternativa incorreta, o sistema apresenta um feedback explicativo mediado por outra personagem, que esclarece o erro e oferece orientações complementares. A cada resposta incorreta, uma vida é descontada. As vidas podem ser recuperadas por meio da funcionalidade Praticar, destinada à realização de exercícios adicionais.

O sistema de recompensas é operacionalizado por meio da seção Conquistas (Figura 7), na qual são apresentadas as conquistas já obtidas e aquelas ainda disponíveis. Ao concluir um módulo, a usuária desbloqueia uma conquista vinculada ao conteúdo aprendido, que libera uma nova entrada no espaço denominado Hall da Fama, associando o avanço pedagógico à representatividade histórica.

O acompanhamento do desempenho ocorre na seção de progresso (Figura 8), onde a usuária pode visualizar sua pontuação acumulada, o número de atividades concluídas, as conquistas desbloqueadas e pendentes, bem como a quantidade de vidas disponíveis, módulos existentes e pioneiras já descobertas. Essa estrutura permite monitoramento contínuo do percurso formativo e reforça a motivação por meio da visualização do avanço alcançado.

O Hall da Fama (Figura 9) constitui o espaço dedicado à apresentação das mulheres pioneiras da Computação que podem ser desbloqueadas ao longo do percurso formativo. Cada personagem dispõe de uma tela individual (Figura 10), contendo uma síntese

de sua trajetória e de suas contribuições para a área.

Essa estrutura estabelece uma articulação entre o conteúdo técnico estudado e o contexto histórico da Computação, integrando progressão acadêmica e representatividade feminina. Ao associar o avanço nos módulos ao desbloqueio dessas narrativas, o aplicativo incorpora um mecanismo de incentivo que reforça o engajamento e contribui para a construção do sentimento de pertencimento na área.

Figura 9. Hall da Fama

Figura 10. Tela individual das pioneiras

Além dos módulos estruturados, o HerCode disponibiliza uma área de exercícios livres destinada à prática e consolidação dos conteúdos já abordados. Nesse espaço, a usuária pode realizar atividades adicionais sem penalização por erro, favorecendo a repetição e o aprofundamento dos conceitos em um ambiente de menor pressão avaliativa. Essa funcionalidade estimula a autonomia, fortalece a retenção do conhecimento e permite a recuperação de vidas quando esgotadas, possibilitando o retorno ao fluxo principal de aprendizagem.

## 6. Conclusão

O desenvolvimento do HerCode contribui para a discussão sobre estratégias voltadas à inclusão feminina na Computação ao propor uma ferramenta educacional gamificada que integra fundamentos introdutórios de programação a abordagens pedagógicas progressivas e acessíveis.

Como limitações, destaca-se que a ferramenta ainda se encontra em fase de testes, não tendo sido aplicada junto ao público-alvo para avaliação empírica de seus impactos no

aprendizado e na motivação das usuárias. Além disso, ainda não foram conduzidos testes formais de usabilidade e experiência do usuário para validação das escolhas de interface e das estratégias pedagógicas adotadas.

Como trabalhos futuros, propõe-se a finalização da etapa de testes e a realização de estudos experimentais com estudantes, visando analisar o impacto do HerCode no desenvolvimento do pensamento lógico e no interesse pela Computação. Pretende-se também conduzir avaliações de usabilidade e experiência do usuário, incluindo validação com especialistas, a fim de aprimorar e consolidar a proposta.

## Agradecimentos

Nosso agradecimento vai para o grupo de pesquisa TechThinkers, que nos deu apoio, colaborou e incentivou este trabalho. Agradecemos também ao Instituto Federal do Amazonas (IFAM), especialmente ao Campus Manaus Zona Leste, pelo suporte da instituição e pelos incentivos que fizeram esta pesquisa acontecer.

## Uso de Inteligência Artificial

Este trabalho utilizou ferramentas de Inteligência Artificial Generativa em duas etapas do processo de escrita. O ChatGPT (versão GPT-5.5) e o Claude (versão GPT-4.6) foram empregados para revisão gramatical e textual do artigo em todas as sessões. Além disso, o ChatGPT foi utilizado para a geração da imagem ilustrativa das etapas metodológicas (Figura 1).
