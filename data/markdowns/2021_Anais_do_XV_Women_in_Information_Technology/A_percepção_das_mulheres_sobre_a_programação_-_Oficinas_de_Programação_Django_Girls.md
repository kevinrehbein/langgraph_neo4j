# A percepção das mulheres sobre a programação - Oficinas de Programação Django Girls

Myrian Noguera Salinas

1Girls Code

Asunción – Central – Paraguai

michinoguera@gmail.com

Abstract. Numerous initiatives have sought to attract girls and women to STEM (Science, Technology, Engineering and Mathematics) careers through different workshops. This paper aims to report on the experience of workshops developed with high school girls and adult women from Paraguay and Uruguay during the years 2018 and 2019. The workshops included the creation of a Web Blog with HTML/CSS, Python and Django Web Framework, as well as lectures and debates about prominent female personalities, as well as female insertion in technology. Perception questionnaires were applied where the data obtained is also presented, analyzed and discussed.

Resumo. Numerosas iniciativas têm buscado atrair meninas e mulheres para as carreiras STEM (Ciência, Tecnologia, Engenharia e Matemática) através de diferentes oficinas. Este trabalho têm como objetivo relatar a experiência das oficinas desenvolvidas com meninas do ensino médio e mulheres adultas do Paraguai e Uruguai durante os anos de 2018 e 2019. As oficinas incluíram a criação de um Blog Web com HTML/CSS, Python e Django Web Framework, além de palestras e debates sobre personalidades femininas proeminentes, bem como a inserção feminina na tecnologia. Foram aplicados questionários de percepção onde os dados obtidos também são apresentados, analisados e discutidos.

## 1. Introdução

Apenas uma fração das estudantes do sexo feminino escolhe campos relacionados a STEM no ensino superior. Segundo o World Economic Forum 3% dos alunos que ingressam nos cursos de tecnologia da informação e comunicação (TIC) em todo o mundo são mulheres. Essa ocorrência levou ao aumento da pesquisa sobre os fatores que promovem o interesse, a retenção e o sucesso das mulheres em carreiras relacionadas. Diversas ações são realizadas no mundo com o objetivo de eliminar a lacuna de gênero na tecnologia.

> Outras iniciativas são promovidas por organizações como Girls Who Code,

> 1STEM é a sigla em inglês de science, technology, engineering y mathematics.

> 2https://www.weforum.org/agenda/2020/02/stem-gender-inequality-researchers-bias/. Último acesso: 16/02/2021

> 3https://girlswhocode.com/. Último acesso: 16/02/2021

Girls Develop It, Django Girls, Chicas en Tecnología, Emili@s, entre outras. Alguns estudos no Brasil, como a análise de perfil [Oliveira et al. 2014], buscam despertar o interesse de mulheres jovens pelos cursos de informática. Estas iniciativas apresentam a computação por meio da perspectiva da programação. Além disso, algumas iniciativas desenvolvem atividades que exploram outras áreas da computação, como a interação humano-computador [Maciel et al. 2013] e na área de banco de dados [Martinhago et al. 2014] [Berardi et al. 2019].

O artigo descreve dois experimentos conduzidos no Paraguai e outro experimento no Uruguai no formato de oficinas de programação para alunas do ensino médio e mulheres adultas. Estas oficinas são parte de um projeto das Girls Code em parceria com a Django Girls, que visa apresentar a programação para as meninas e mulheres de uma forma positiva e empática. Por meio da experiência e dos dados deste estudo, mostramos a percepção das meninas e mulheres adultas sobre a programação e possíveis atividades que podem motivá-las e incentivá-las. O restante do artigo está definido da seguinte forma: na seção 2 descreve os trabalhos relacionados sobre iniciativas similares e seus resultados, a seção 3 apresenta a estrutura da oficina Django Girls, segue a descrição do cenário geral e os estudos de caso aplicados na seção 4. Na seção 5 menciona as ferramentas utilizadas nas oficinas e na seção 6 estão as observações e lições aprendidas. Por fim, nas seções 7 e 8 se descrevem a discussão e a conclusão respectivamente.

## 2. Trabalhos Relacionados

Existem várias iniciativas que têm como foco meninas do ensino médio ([Wang et al. 2012], [Bim et al. 2016], [Macedo et al. 2015]), estudantes universitárias ([Michell et al. 2017], [Cheryan et al. 2015], [Sax et al. 2017], [Amaral et al. 2017], [Wang et al. 2017]), crianças em idade escolar [Master et al. 2017] e mulheres na indústria ([Black et al. 2005] e [Rosenbloom et al. 2008]). [Sax et al. 2017] revelou fortes flutuações no interesse dos alunos em ciência da computação de 1971 a 2011 nos EUA, com tendências destacando uma desaceleração significativa entre o final dos anos 1990 e 2011, bem como uma sub-representação persistente e considerável de mulheres em todos os anos.

[Black et al. 2005] apresentam uma análise da situação das mulheres na computação a através de questionários e pesquisas realizadas com mulheres na China, Alemanha, Irlanda, Itália e Reino Unido. Os resultados evidenciaram a baixa participação feminina na computação em todos os países examinados e as semelhanças na percepção cultural das questões de tecnologia e gênero, mesmo com a distinção das realidades socioeconômicas de cada um dos países considerados.

Por outro lado [Rosenbloom et al. 2008] avaliaram a escolha da tecnologia como carreira e concentraram-se em entender por que existem tão poucas mulheres na tecnologia da informação. Os resultados apontaram que a discriminação ou diferenças de habilidades podem atuar como filtros que reduzem a entrada de mulheres em ocupações de

> 4https://girldevelopit.com/. Último acesso: 16/02/2021

> 5https://djangogirls.org/. Último acesso: 16/02/2021

> 6https://chicasentecnologia.org/. Último acesso: 16/02/2021

> 7https://emilias.dainf.ct.utfpr.edu.br/. Último acesso: 16/02/2021

tecnologia. Outros fatores mencionados em [Cheryan et al. 2015] são os estereótipos e a falta de representação.

[Amaral et al. 2017] discutiram quais fatores influenciam a entrada de uma mulher em um curso de computação, como ocorre sua permanência e o que incentiva a continuação. A pesquisa constatou que as alunas foram influenciadas, em sua maioria, pelos homens na escolha do curso e na carreira profissional a seguir. Todas as entrevistadas afirmaram que o contato com outras mulheres fortalece as questões de respeito ao gênero.

[Michell et al. 2017] sugeriram uma série de maneiras pelas quais as universidades australianas poderiam apoiar as meninas e mulheres a ampliação da participação na ciência da computação, podendo mudar a cultura masculina no campus mudando a decoração das salas de aula, usando bibliotecas como locais de encontro para mulheres da ciência da computação (e outras STEM) e garantindo que suas campanhas de marketing não reproduzam estereótipos.

Várias organizações promovem a participação feminina nas áreas relacionadas à informática. Entre os exemplos, podemos citar o Girls Who Code, Chicas en Tecnología, Django Girls, Tech Ladies, Mulheres na Computação, Meninas Digitais, Girls Code, entre outras.

Girls Code considerou a lacuna em relação a esse problema no Paraguai e mostrou uma das facetas da computação por meio do desenvolvimento de oficinas de programação para meninas do ensino médio e mulheres adultas em parceria com Django Girls.

## 3. Estrutura da Oficina de Programação

A estrutura das oficinas de programação da Django Girls é composta por 7 etapas desenvolvidas em dois dias (12 horas no total). Na Figura 1 mais embaixo é detalhada as etapas.

Figura 1. Estrutura das Oficinas Django Girls

- Boas-vindas e apresentação inicial: No primeiro dia foi realizado o cadastro das participantes e apresentação da oficina e os organizadores. Seguidamente foi ofe-

> 8https://pt-br.facebook.com/techladiesbr/. Último acesso: 16/02/2021

> 9https://mulheresnacomputacao.com/. Último acesso: 16/02/2021

> 10http://meninas.sbc.org.br/. Último acesso: 16/02/2021

> 11https://www.girlscode.com.py/. Último acesso: 16/02/2021

recido um lanche para as participantes. Esta etapa foi aproveitada para preencher o questionário inicial de percepção sobre a programação de computadores.

- Oficina de HTML / CSS: A oficina de HTML/CSS teve como conteúdo a contextualização sobre as ferramentas, a utilização e a arquitetura básica de sistemas Web. Além disso foram desenvolvidos exercícios de exemplo com as participantes. As participantes foram divididos em equipes (até 5 pessoas e 1 mentor) e seguiram as instruções para criar um aplicativo de Blog com sucesso e implementá-lo na Internet.

- Conversa com Mentores: Também foi preparado un momento de conversa com mentores, patrocinadores, profissionais da comunidade Python / Javascript e as participantes das equipes. Além disso, foram realizadas debates sobre personalidades femininas proeminentes, bem como a inserção feminina na tecnologia.

- Oficina de Python: Na oficina de Python foram discutidos o uso desta linguagem, a estrutura e sintaxe. Também foram desenvolvidos exercícios de exemplo com as participantes.

- Oficina de Django: Na oficina de Django teve a contextualização sobre as ferramentas de Framework Web e conceitos de banco de dados. Também foram desenvolvidos exercícios de exemplo com as participantes. Até aqui foram realizados no primeiro dia do evento.

- Oficina de Integração com o Front End: No segundo dia da oficina focamos a integração dos componentes Back End com o Front End e foram desenvolvidos exercícios de exemplo com as participantes.

- Fechamento: Nesta etapa foram apresentados os trabalhos realizados pelas equipes e fechamos as oficinas. Também foi aproveitada para preencher o questionário final de percepção sobre a programação de computadores e de avaliação sobre o evento.

## 4. Cenário e Casos de Estudo

Girls Code é uma ONG do Paraguai que realiza oficinas, cursos e mentoria para meninas e adolescentes paraguaios. Nasceu de um grupo de Programadores, Analistas e Engenheiros de Sistemas, que acreditam que as meninas e adolescentes merecem a oportunidade de entrar no mundo da computação, para gerar valor agregado digital por meio da programação.

Django Girls é outra organização sem fins lucrativos internacional que capacita e ajuda a organizar oficinas de programação gratuitas, fornecendo ferramentas, recursos e suporte. O seu principal objetivo é contribuir para trazer mais mulheres ao mundo da tecnologia, criando recursos projetados com empatia.

> 12HTML é a sigla para Hyper Text Markup Language, ou seja, linguagem de marcação de hipertexto. Ela é utilizada como marcação para desenvolver páginas e documentos eletrônicos para a internet.

> 13CSS é a sigla para Cascading Style Sheets, ou seja, Folhas de Estilo em Cascatas. É uma maneira de dar estilo ao código criado por linguagens como HTML, XML ou XHTML

> 14Framework Web é um conjunto de componentes que ajudam a desenvolver sites de forma mais fácil e rápida.

> 15As Organizações não Governamentais são organizações sem fins lucrativos, constituídas formalmente e autonomamente, caracterizadas por ações de solidariedade no campo das políticas públicas e pelo legítimo exercício de pressões políticas em proveito de populações excluídas das condições da cidadania.

Neste contexto, Girls Code fez uma parceria para realizar três oficinas de programação com o suporte da Django Girls em julho de 2018, maio e agosto de 2019. As estratégias de ensino, conteúdo e definição das atividades foram as mesmas nos 3 estudos de caso realizados.

### 4.1. Caso de Estudo 1

A primeira oficina foi realizada numa instituição de ensino médio para meninas, o Centro Educativo Mbaracayú localizado na Reserva Natural Florestal Mbaracayú, no departamento de Canindeyú.

O público alvo foram as meninas do ensino médio. O convite foi feito pelas redes sociais e os professores engajaram às meninas para participarem.

Esta primeira edição do evento teve a participação de 15 meninas e os conteúdos das oficinas foram desenvolvidos em 2 dias (Figura 2). Antes de iniciar as oficinas as participantes preencheram o questionário para identificar a percepção inicial sobre a programação. E importante destacar que as meninas são do interior e acessibilidade à informação e a exposição na tecnologia é reduzida pela falta de serviços de Internet e a falta de equipes como computador, tablets, laptops e outros.

Os principais desafios que as voluntárias tiveram que resolver foram:

- Problemas de conexão com a Internet: A qualidade de conexão com a Internet foi variável por causa da região. As voluntárias aplicaram algumas ações para enfrentar essa dificuldade como: baixar e instalar os aplicativos necessários antes do início das oficinas em cada computador, para que possam trabalhar sem conexão.

- Níveis variados de conhecimentos: No início das oficinas as voluntárias perceberam que algumas das participantes não possuíam o mesmo nível de conhecimento para o uso das ferramentas tecnológicas e dos termos de programação utilizados. Para isso, as voluntárias acharam adequado usar uma forma de comunicação mais simples baseada em exemplos do dia a dia e agrupar as equipes com pessoal de diferentes níveis de conhecimento para promover o aprendizado.

No final do evento as meninas preencheram novamente outro questionário para identificar a percepção sobre a programação. Na comparação entre as nuvens de palavras construídas a partir das percepções das participantes sobre programação, percebe-se a ausência de palavras negativas na segunda nuvem, quando comparada com a primeira.

Uma observação interessante foi a reação positiva das meninas com a presença das voluntárias e a criação de um vínculo de confiança. Por exemplo, demonstraram interesse na decisão das voluntárias de seguir carreiras em STEM, também como foi a sua experiência e onde se formaram.

### 4.2. Caso de Estudo 2

Esta edição do Django Girls foi focado para mulheres adultas e foi realizado com o apoio da organização Global Shapers e as empresas de tecnología CODIUM S.A. e MUV. O convite foi feito pelas redes sociais e também pela imprensa.

> 16http://www.mbertoni.org.py/. Último Acesso: 16/02/2021

> 17https://www.globalshapers.org/. Último Acesso: 16/02/2021

> 18https://codium.com.py/. Último Acesso: 16/02/2021

> 19https://muv-app.co/. Último Acesso: 16/02/2021

Figura 2. Oficinas de programaç ão Django Girls no Centro Educativo Mbaracayú

As oficinas foram realizadas nos dias 24 e 25 de maio em Asunción e contaram com a presença de 33 mulheres de 19 a 64 anos. As participantes deste evento são de diferentes lugares da cidade em comparação com o evento anterior. Isso representa maior acessibilidade à informação e exposição na tecnologia.

Antes de iniciar as oficinas as participantes preencheram o questionário para identificar a percepção inicial sobre a programação. O desenvolvimento dos conteúdos foram bem aplicados pelas participantes. A Figura 3 mostra um dos momentos da oficina de programação.

Figura 3. Oficinas de programaç ão Django Girls no Asunción

As equipes formadas apresentaram seus trabalhos com sucesso. No final do evento as pasticipantes preencheram novamente outro questionário para identificar a percepção sobre a programação.

Na comparação entre as nuvens de palavras construídas a partir das percepções das participantes sobre programação, percebe-se a ausência de palavras negativas na segunda nuvem, quando comparada com a primeira.

### 4.3. Caso de Estudo 3

Nesta edição, as oficinas foram desenvolvidas no Uruguai, no Centro Educativo Providencia da cidade de Montevideo, por conta de uma parceria com a IBM Montevideo.

O público alvo foram meninas do ensino médio. O convite foi feito pelas redes sociais e os professores engajaram às meninas para participarem.

O evento teve a participação de 18 meninas e a colaboração de 10 facilitadores para desenvolver o conteúdo das oficinas. As meninas são de diferentes lugares da cidade de Montevideo. Isso representa maior acessibilidade à informação e exposição na tecnologia.

Antes de iniciar as oficinas as participantes preencheram o questionário para identificar a percepção inicial sobre a programação e continuaram com as oficinas planejadas.

No final do evento as equipes formadas apresentaram seus trabalhos com sucesso e preencheram novamente outro questionário para identificar a percepção sobre a programação.

Na comparação entre as nuvens de palavras construídas a partir das percepções das participantes sobre programação, percebe-se a ausência de palavras negativas na segunda nuvem, quando comparada com a primeira.

## 5. Ferramentas Utilizadas

A equipe de Girls Code adaptou o instrutivo das Django Girls para facilitar a experiência das participantes. O instrutivo estabelece ferramentas de Software disponíveis gratuitamente para facilitar o acesso das participantes fora das oficinas para aprimorar seus conhecimentos. As ferramentas utilizadas são as seguintes:

- Google Colaboratory: Esta ferramenta é um ambiente Jupyter Notebook gratuito que não requer configuração e é executado inteiramente na nuvem. E um documento que contém código executável (por exemplo, Python) e também elementos de rich text (links, figuras, etc.).

- Sublime Text 3: Sublime Text na sua versão gratuita, é um editor de texto e editor de código-fonte utilizado para o desenvolvimento de aplicativos baseada em Windows que permite às empresas editar texto em códigos de programação, marcação e prosa.

- Python Versão 3.6: Python é uma linguagem de programação de alto nível, dinâmica, interpretada, modular, multiplataforma e orientada a objetos.

- Django: Django é uma Framework de desenvolvimento web de código aberto,

> 20http://www.providencia.org.uy/. Último Acesso: 16/02/2021

> 21https://www.ibm.com/uy-es. Último Acesso: 16/02/2021

> 22http://bit.ly/django-tuto. Último Acesso: 16/02/2021

> 23https://colab.research.google.com. Último Acesso: 16/02/2021

> 24Ambiente de computação interativo projetado para facilitar o trabalho com a linguagem Python e seus dados. Contém todo o conteúdo para a sessão do aplicativo da web do Jupyter Notebook, incluindo entrada e saída para cálculos, matemática, imagens e texto explicativo.

> 25https://www.sublimetext.com/. Último Acesso: 16/02/2021

> 26https://www.python.org/. Último Acesso: 16/02/2021

> 27https://www.djangoproject.com/. Último Acesso: 16/02/2021

escrita em Python, que respeita o padrão de design conhecido como model-viewcontroller (MVC).

## 6. Observações e Lições Aprendidas

Durante a concepção e implementação das oficinas, foram incluídas várias decisões importantes para garantir o sucesso das atividades:

- A utilização de ferramentas de Software disponíveis gratuitamente. Além disso, os materiais de aprendizagem foram disponibilizados online e podiam ser acessadas independentemente fora das oficinas para que os alunos pudessem continuar a aumentar sua proficiência;

- A aplicação de estratégias de comunicação como exemplos do dia a dia e agrupar as equipes com pessoal de diferentes níveis de conhecimentopara facilitar o aprendizado das meninas no Caso de Estudo 1 na seção 4.1.

Os responsáveis do Centro Educativo Mbaracayú acharam realmente valiosa a iniciativa e solicitaram um plano de longo prazo para continuar as oficinas de programação. No caso do Centro Educativo Providencia, as oficinas de programação foram o incentivo para incluir a programação como disciplina opcional para os alunos e oferecer serviços de programação para o mercado.

Outro fator para destacar foi o interesse das empresas e instituições em colaborar neste tipo de iniciativa.

Outra observação importante foi o tempo de desenvolvimento das oficinas, para que o conteúdo seja aprofundado adequadamente será necesario aumentar o tempo proposto de 12 horas ao dobro e testar.

## 7. Discussão

Nos questionários aplicados no inicio e no final das oficinas, solicitamos às participantes escrever em texto livre uma palavra ou sentimento que vem à sua mente quando pensa em programação de computador. Apresentamos as respostas no formato de nuvem de palavras ou nuvem de etiquetas nas Figuras 4 e 5. Na comparação entre as nuvens de palavras construídas a partir das percepções das participantes sobre programação, percebe-se a ausência de palavras negativas na segunda nuvem, quando comparada com a primeira. Como menciona [Macedo et al. 2015] nos resultados do seu estudo, que a “falta de conhecimento” é um motivo para as alunas evitarem à área de Computação/TI.

Além disso, algumas meninas e mulheres mencionaram seu interesse na programação como carreira e outras falaram de continuar com o desenvolvimento do seu próprio Blog focado no interesse particular delas (gastronomia, maquiagens, animais de estimação, esportes, etc.). Considerando o estudo de [Berardi et al. 2019] que fala qeue através da análise da compreensão dos conceitos e da percepção sobre a área é possível obter resultados promissores.

Outro fator interessante é o perfil das voluntárias na sua maioría estudantes e formadas de carreiras de Computacao como o estudo conduzido pelo [Wang et al. 2012]

> 28Nuvem de palavras (também conhecida como nuvem de tags ou texto) é uma representação visual da frequência e do valor das palavras. Quanto mais vezes uma palavra-chave estiver presente em um conjunto de dados, maior e mais forte será a palavra-chave.

Figura 4. Percepç ão inicial das participantes sobre a programaç ão

Figura 5. Percepç ão final das participantes sobre a programaç ão

sobre o evento de divulgação do ensino médio feminino em ciência da computação, que foi conduzido e organizado quase exclusivamente por estudantes de graduação e pósgraduação na Escola de Ciência da Computação. Os resultados obtidos foram muito animadores, indicando uma influência positiva nos alunos participantes.

## 8. Conclusão

Este trabalho apresentou um relato de experiência sobre as oficinas de programação Django Girls para meninas e mulheres adultas realizado no Paraguai e Uruguai. Nas oficinas foram desenvolvidos conceitos básicos sobre programação Web e conteúdo práctico para criar um blog web na Internet.

Uma importante contribuição com esta experiência é mostrar que as oficinas de programação Django Girls poderiam mudar a percepção sobre programação de computador para as meninas e mulheres sem conhecimento inicial. Além disso, mostrar representatividade através da figura das voluntárias.

Como trabalho futuro planejaremos as oficinas com o tempo de desenvolvimento adequado e aplicaremos algum método para levantar outros fatores que determinam as escolhas de carreiras das participantes. Outra proposta é investigar se essas meninas e mulheres que participaram das oficinas continuaram algum curso da área da computação.
