# Plataforma para Classificação da Amigabilidade de Gênero das Empresas de Tecnologia da Informação do Município de Belo Horizonte

Lara Cadar Cunha, Gabriel Novy,Carlos Alberto Severiano Júnior, Cristiane Targa, Daniel B. F. Conrado

1Instituto Federal de Minas Gerais - IFMG Campus Sabará Rod. MG-5 Km 10, Sobradinho – Sabará – MG – Brazil

lara ~~c~~ adar@yahoo.com.br, { gabriel.novy,carlos.severiano,

cristiane.targa,daniel.conrado } @ifmg.edu.br

Abstract. The area of Information Technology (IT) is mostly dominated by men professionals. This gender segmentation has cultural roots that still permeate workplaces and hinder the hiring of women. Since it’s urgent to promote gender equality, this work aims to help women professionals at finding organizations that are inclined to hire women and provide gender friendly workplaces. We are developing a platform to classify IT organizations from Belo Horizonte city based on their gender friendliness. We hope that this platform works as an indicator that helps evaluating work conditions and promotes the adoption of affirmative and inclusive policies.

Resumo. A área de Tecnologia da Informação (TI) é predominantemente dominada por profissionais homens. Essa segmentação de gênero possui raízes culturais que ainda permeiam ambientes de trabalho e dificultam a entrada de mulheres. Como promover a equidade de gênero é urgente, este trabalho pretende auxiliar as profissionais de TI a escolherem empresas receptíveis à contratação de mulheres e que forneçam um ambiente de trabalho amigável em relação a gênero. Para isso, está sendo desenvolvida uma plataforma que classifica as empresas de TI de Belo Horizonte de acordo com seu nível de amigabilidade de gênero. Espera-se fornecer um indicador para a avaliação das condições de trabalho e fomentar a adoção de medidas afirmativas e inclusivas nas empresas.

## 1. Introdução

Na sociedade brasileira, as diferenças sociais em relação ao gênero ocorrem em diversas frentes, dentre elas o ambiente de trabalho. Segundo o IBGE (Instituto Brasileiro de Geografia e Estatística), embora representem a maioria da população e têm ocupado cada vez mais espaço no mercado de trabalho [PORTAL BRASIL 2015], as mulheres compõem apenas 20% dos profissionais da área de TI [TV BRASIL 2015].

A reduzida representatividade feminina no mundo do trabalho pode ser explicada pelo conceito de segregação horizontal: “as mulheres são levadas a fazer escolhas e seguir caminhos marcadamente diferentes daqueles escolhidos ou seguidos pelos homens” [Olinto 2012]. No entanto, o desempenho escolar de mulheres e homens, em linhas gerais, foi relatado como equivalentes, reforçando que mulheres escolhem suas carreiras

menos por suas capacidades que pelos mecanismos sociais de segmentação por gênero. As empresas de TI podem combater essa segregação pela implantação de políticas afirmativas de gênero, fornecendo um ambiente de trabalho amigável às mulheres e gerando novas oportunidades. Porém, não é fácil encontrar empresas desse tipo pois, até onde pôde-se constatar, não há informação ou indicadores específicos disponíveis que permitam às mulheres direcionarem a entrega de seus currículos. Este trabalho pretende criar um esquema de classificação das empresas de TI do município de Belo Horizonte para servir como um possível indicador. O conceito foi inspirado no projeto Moda Livre [REP ORTER BRASIL 2013], que classifica as principais marcas de roupas em relação ao seu envolvimento com trabalho escravo bem como suas ações para combater a produção de peças de roupa com esse tipo de mão de obra. Assim como o Moda Livre quer fomentar o consumo consciente, pretende-se aqui promover a inclusão de mulheres na área de TI.

Plataformas voltadas para a avaliação de empresas são iniciativas de grande interesse para funcionários e aspirantes a uma colocação no mercado. Existe uma percepção de que a avaliação sobre como é trabalhar em uma determinada empresa é feita de maneira mais consistente por pessoas que vivenciaram o cotidiano do ambiente da mesma. Normalmente, as plataformas que oferecem esse tipo de serviço permitem aos usuários registrar de maneira anônima suas impressões sobre diferentes aspectos da empresa, como ambiente de trabalho, plano de carreira, salários, dentre outros. O Glassdoor é uma das iniciativas mais antigas no assunto. O site oferece alternativas para a avaliação de prós e contras da empresa, sugestões que os avaliadores gostariam de repassar para os gestores e um cadastro de salários por cargo desempenhado. A cada avaliação, o site abre espaço para que o usuário registre uma nota geral entre 0 e 5, a partir da qual é tirada uma média, a qual rotula o perfil da empresa. O site foi desenvolvido por uma empresa americana, mas também possui registros de empresas brasileiras. O Lovemondays foi criado por uma startup brasileira e se diferencia pelo foco no mercado brasileiro. Além de permitir avaliações diversas, também permite que os usuários cadastrem suas impressões sobre o processo seletivo que pelo qual passaram ao se candidatarem a uma vaga.

Os exemplos citados classificam aspectos das organizações com base principalmente em avaliações numéricas feitas pelos usuários em formulários específicos. Com o avanço das redes sociais e o consequente aumento de volume de dados proporcionado pelo registro das diferentes atividades dos usuários nessas plataformas, diversas iniciativas foram surgindo com o objetivo de permitir uma análise consistente de todo esse conteúdo. Um dos grandes desafios é o processamento de uma informação que não é produzida de maneira formatada, ou seja, que não foram obtidas p. ex. a partir de formulários com opções pré-definidas. Nesse contexto, técnicas de Análise de Sentimentos podem ser aplicadas, uma vez que possibilitam a extração de informações subjetivas de textos escritos em linguagem natural [Liu 2012].

Muitas das técnicas aplicadas atualmente na área de Análise de Sentimentos são fundamentadas no Aprendizado de Máquina. A ideia é definir uma base de conhecimento que contenha termos que possam indicar conotações p. ex. positivas ou negativas em relação ao texto em análise. Esse tipo de abordagem vem sendo muito utilizado por em-

> 1https://www.glassdoor.com

> 2https://www.lovemondays.com.br/

presas que desejam medir como seus produtos estão sendo avaliados pelos consumidores com base em comentários de usuários nas redes sociais. Cita-se como exemplo a platforma HugMe que, integrada com o site ReclameAqui e com as redes sociais, monitora comentários sobre produtos ou serviços de empresas aplicando Análise de Sentimentos.

## 2. Plataforma de Classificação

Neste trabalho, está em desenvolvimento um plataforma de classificação de amigabilidade de gênero de organizações de TI do município de Belo Horizonte. Seu abastecimento inicial se dará pela coleta de informações sobre ações jurídicas envolvendo essas empresas. Além disso, fazer-se-á proveito de dados estatísticos provenientes do Sistema Nacional de Informações de Gênero (SNIG) a respeito de empregabilidade de mulheres. Pretende-se também permitir às usuárias da plataforma dar feedback em relação à sua vivência como mulher nas empresas onde trabalham.

A classificação das empresas será indicada por cores, a saber: vermelho, para a empresa que foi condenada em um ou mais processos de assédio moral ou sexual; amarelo, para empresas que possuem processos dessa natureza em andamento; azul, caso não seja possível encontrar informação positiva ou negativa sobre a empresa; e verde, para a empresa que possuir políticas afirmativas de inclusão em seus ambientes de trabalho. Uma empresa pode ter sua classificação alterada caso revise suas políticas internas, tornando-se uma organização mais inclusiva. A plataforma prevê amplo direito de defesa às empresas classificadas e manterá um diálogo aberto para garantir a veracidade e atualidade das informações.

A metodologia utilizada para o desenvolvimento da plataforma consiste no uso de crawler para a coleta de dados na internet, na aplicação de Análise de Sentimentos para a construção de um modelo classificatório e na criação de um aplicativo para exibir os resultados.

O crawler a ser desenvolvido realizará uma busca na internet por processos jurídicos administrativos de assédio moral ou sexual envolvendo empresas de TI do município de Belo Horizonte. Escolheu-se essa fonte de dados por ser informação de acesso público. Os processos serão analisados para identificar conteúdos chaves que auxiliem na extração de características como: o resultado do processo, se houve ou não condenação, se houve acordo, dentre outros.

Para o desenvolvimento do aplicativo, serão conduzidas sessões de design conceitual para a elicitação e caracterização dos stakeholders, bem como a criação de Personas. Técnicas de prototipação serão executadas com o intuito de refinar os requisitos e a interação do usuário.

## 3. Considerações Finais

Ainda que existam fontes de informação sobre condições de trabalho em empresas, ainda não se tem notícia de plataformas que direcionam essa avaliação para a questão de gênero, especialmente o tratamento que é destinado para mulheres em empresas que oferecem vagas em Tecnologia da Informação. O presente trabalho se propõe a abordar essa questão

> 3https://www.hugme.com.br

> 4https://www.reclameaqui.com.br/

de modo que possa se posicionar como uma fonte relevante para mulheres que aspirem a cargos em empresas de TI.

Como contribuição social, o projeto auxiliará no combate a segregação de gênero e promoverá uma equidade entre homens e mulheres no mercado de trabalho. O desemprego afeta mais mulheres do que homens no Brasil, segundo o IBGE. Sendo assim, como contribuição econômica, o aplicativo auxiliará no combate ao desemprego, pois conduzirá a profissional a encontrar uma empresa que não irá gerar resistência em sua contratação. Mais do que isso, pretende-se que uma eventual avaliação negativa de uma empresa possa proporcionar uma reavaliação de suas políticas, de modo que esta possa se reposicionar como uma organização mais inclusiva.
