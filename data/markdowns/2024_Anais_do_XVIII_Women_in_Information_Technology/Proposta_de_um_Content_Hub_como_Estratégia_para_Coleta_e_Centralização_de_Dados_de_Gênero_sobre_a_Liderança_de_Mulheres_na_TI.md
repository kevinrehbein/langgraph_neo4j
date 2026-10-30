# Proposta de um Content Hub como Estratégia para Coleta e Centralização de Dados de Gênero sobre a Liderança de Mulheres na TI

Julia Milioranza Gomes, Melissa Maria Souza de Carvalho, Bruna Rocha Aguiar, Karen da Silva Figueiredo Medeiros Ribeiro

Instituto de Computação – Universidade Federal de Mato Grosso (UFMT) Cuiabá – MT – Brasil

`{julia.gomes1, melissa.carvalho, bruna.aguiar1}@sou.ufmt.br,`

`karen@ic.ufmt.br`

Abstract. This paper proposes the creation of a content hub as a strategy for collecting and centralizing gender data on women's leadership in the IT sector in Brazil. Tool development was based on the creation of user journey maps with the aim to better understand their goals and interaction needs. The initial version of the hub is already available for use and was populated with data from studies and news about Brazilian women's leadership in IT selected by academic curation. Additionally, the hub works as a landing page for discussing the importance of gender data and the topic of women's leadership in IT and also as an interface for collecting new data on the subject by hosting a survey focused on women leaders in this field.

Resumo. O presente artigo apresenta a criação de um hub de informações como estratégia para a coleta e a centralização de dados de gênero sobre a liderança de mulheres na TI no Brasil. O desenvolvimento do hub foi baseado na elaboração de jornadas de usuárias, buscando compreender melhor seus objetivos e suas formas de interação. A versão preliminar do hub encontra-se disponível para uso e foi inicialmente populada com o resultado de pesquisas e notícias sobre liderança de mulheres na TI, realizadas por meio de uma curadoria acadêmica. Além disso, o hub funciona como landing page para a discussão da importância de dados de gênero e da temática de liderança de mulheres na TI e como interface para a coleta de novos dados sobre o assunto, ao abrigar uma pesquisa voltada para mulheres líderes na área.

## 1. Introdução

Um dos desafios relacionados à equidade de gênero na área de Tecnologia da Informação (TI) é a ausência e dispersão de dados de gênero confiáveis sobre o tema para a conscientização social, tomada de decisões e criação de políticas embasadas em evidências sólidas [Fuentes e Cookson 2020].

Um content hub, ou hub de informações, é uma plataforma digital centralizada na qual é possível reunir, organizar e distribuir uma variedade de conteúdos relacionados a um tema. Esses conteúdos podem incluir artigos, blogs, vídeos, infográficos, podcasts, entre outros conteúdos hipermídia. O objetivo principal de um content hub é fornecer às pessoas usuárias um ponto de acesso conveniente e centralizado para consumir informações relevantes e de alta qualidade sobre um assunto [Chessell et al. 2015]. Quando se trata de centralização de dados de gênero, um content hub pode desempenhar um papel importante como uma fonte confiável e acessível de informações relacionadas

às questões de gênero, por oferecer a agregação de recursos, uma organização estruturada, de acesso facilitado e de atualização contínua.

Considerando o exposto, este artigo apresenta a criação de um hub de informações como estratégia para a coleta e a centralização de dados de gênero sobre a liderança de mulheres na TI no Brasil. O content hub funciona como landing page para a discussão da importância de dados de gênero e da liderança de mulheres na TI e como interface para a coleta de novos dados sobre o assunto, ao abrigar, inicialmente, uma pesquisa voltada para mulheres líderes na área. A partir desta introdução, o artigo traz as seções de trabalhos relacionados, metodologia, resultados e conclusão, na sequência descrita.

## 2. Trabalhos Relacionados

Realizou-se uma revisão dos trabalhos publicados nos anais do Women in Information Technology (WIT) referentes à produção de ferramentas web relacionadas à temática de mulheres na TI no Brasil e a sua liderança. O trabalho [Milson et al. 2020] apresenta um website com jogos que permitem a divulgação de personalidades femininas das Ciências. Este trabalho se assemelha a um hub de jogos, sendo esta a forma principal de obter informações sobre as mulheres cientistas. Já o artigo [Lima et al. 2023] traz o protótipo de um site para oferecer um espaço de maior representatividade feminina visando a divulgação de seus projetos. O protótipo apresenta perfis de mulheres profissionais da área, visando promover a interação entre elas no contexto dos seus projetos e carreiras, no entanto, não há iniciativas para coletar e centralizar dados sobre a liderança de mulheres em TI especificamente, funcionando mais como uma rede social de divulgação dos projetos de mulheres.

Dos trabalhos revisados, o que apresenta maior semelhança com relação ao presente trabalho é o artigo de [Berardi et al. 2023], que apresenta estratégias para desenvolver uma plataforma baseada em Web Semântica, destinada a estruturar e centralizar dados abertos do Brasil, Peru e Bolívia sobre mulheres em STEM ( Science, Technology, Engineering and Mathematics ). Este trabalho trata de uma plataforma e uma pesquisa muito maiores do que a proposta por este artigo, tanto em complexidade tecnológica, quanto em temática, visto que extrapolam os dados nacionais e a área de TI. Apesar do projeto citado ser de grande contribuição social, a plataforma ainda não está disponível. Desta forma, é possível que o hub aqui proposto apresente uma solução mais imediata para a obtenção de informações sobre o recorte escolhido por parte das pessoas usuárias, que poderão encontrar informações orgânicas de forma mais direta, junto com suas fontes originais.

## 3. Metodologia

Para realizar a análise e projeto do content hub, foi adotada a técnica de mapeamento da jornada do usuário [Endmann e Keßner 2016], aqui chamada de jornadas das usuárias. As jornadas das usuárias geram aprendizado sobre os processos que são relevantes para as pessoas usuárias, contribuindo para a elicitação de requisitos e no projeto de interação a partir de personas e seus objetivos, expectativas, atividades, oportunidades, pensamentos e emoções com relação ao sistema. Assim, foram elaboradas duas

personas: Frida e Laura, e suas jornadas de interação são mapeadas nas Figuras 1 e 2, respectivamente.

### Figura 1. Jornada da Usuária Frida

Na Figura 1, apresenta-se Frida, 45 anos, líder na área de TI, que deseja contribuir para reverter a falta de mulheres em TI. Suas expectativas incluem compreender melhor e se atualizar sobre a situação das mulheres na TI, apoiar programas para o avanço feminino na área e contribuir de forma construtiva para a causa. Sua jornada começa com pesquisas na internet, ela encontra o content hub com indicadores e notícias relevantes sobre o tema. Explorando a seção de notícias, busca atualizar-se e encontrar possíveis parcerias. Além disso, na plataforma ela encontra uma pesquisa que coleta dados de mulheres líderes na área, aproveitando a oportunidade, ela contribui compartilhando insights valiosos sobre a sua experiência. Ao concluir sua jornada, sente-se satisfeita por alcançar suas expectativas em um só lugar. Ademais, a possibilidade de entrar em contato com as pessoas responsáveis pelo site abre novas oportunidades para estabelecer novas parcerias.

Laura, 20 anos, Figura 2, é uma estudante de jornalismo que deseja redigir um artigo sobre a participação das mulheres na TI no Brasil. Nesse sentido, busca encontrar dados sobre mulheres na TI no Brasil para compreender mais profundamente o tema de maneira otimizada. Entretanto, inicialmente se depara com diversas informações espalhadas até encontrar o content hub. Assim sendo, descobre indicadores relevantes destacados no início da página sobre o tema, o que a direciona para outra página que

contém diversos artigos e documentos abordando questões de gênero, liderança e tecnologia, nos quais ela pode se inspirar e/ou obter mais dados sobre o tema. Adicionalmente, no rodapé da página, se depara com os dados de contato das responsáveis pelo site, possibilitando-a entrar em contato para possíveis entrevistas para seu artigo.

Figura 2. Jornada da Usuária Laura

Além das jornadas das usuárias, visando popular o hub adotou-se a curadoria de dados [Palmer et al. 2013] como técnica para seleção de notícias e de documentos de relatórios técnicos sobre o tema. A curadoria foi realizada em pares, pelas pessoas pesquisadoras autoras do trabalho conforme descrito em Ribeiro et al. (2024).

## 4. Resultados

A versão preliminar do content hub proposto, chamado LideraM, encontra-se disponível para acesso no endereço <u>https://lideram.tech/</u> e pode ser visualizada na Figura 3. Atualmente, esta versão possui oito seções distribuídas em quatro páginas para navegação, que foram elaboradas com base nas jornadas das usuárias.

A página inicial apresenta seis seções. A primeira oferece uma breve explicação sobre as vantagens da liderança feminina no setor de TI. Na segunda seção, são destacados indicadores alarmantes sobre a disparidade de gênero na liderança em TI, permitindo que as pessoas usuárias naveguem para outra página com documentos de estatísticas e de relatórios técnicos relacionados à liderança, gênero e tecnologia selecionados pela curadoria de dados [Ribeiro et al. 2024]. Esta página também pode ser acessada pelo cabeçalho. A terceira seção aborda a identidade do hub e fornece um

esclarecimento do propósito do site, direcionando as pessoas visitantes para a última seção, que apresenta um convite para participação em uma pesquisa destinada a mulheres líderes na área de TI, que visa compreender o cenário no Brasil. As quarta e quinta seções complementam o entendimento geral na temática, respectivamente, explicando a ausência de dados de gênero sobre o assunto e ressaltando a importância de sua obtenção.

No cabeçalho, há um acesso direto a uma página com notícias e outras matérias jornalísticas atualizadas sobre o tema, selecionadas pela curadoria de dados desde o ano de 2022 (início do projeto de pesquisa relacionado à ferramenta). No rodapé, além de informações sobre as organizações responsáveis pelo site e suas parcerias, é possível encontrar os contatos pertinentes para comunicação. O hub também possui uma ferramenta que permite a alteração do idioma para inglês ou espanhol.

Figura 3. Print screen da versão preliminar do content hub LideraM

## 5. Conclusão

Este artigo apresentou a versão preliminar de um hub de informações como estratégia para a centralização de dados de gênero sobre a liderança de mulheres na TI no Brasil e como possibilidade de coletar novos dados a partir da publicação de pesquisas. O hub proposto está disponível e pode ser acessado via navegadores web. Este trabalho oferece

contribuições tanto para a sociedade, no sentido de promover a conscientização sobre a equidade de gênero na TI no Brasil, quanto para a academia, ao preencher lacunas de pesquisa sobre dados de gênero, centralizando dados confiáveis e estimulando o debate acadêmico sobre a liderança em TI.

Atualmente, o hub aponta somente para dados previamente selecionados, mas publicados por outras fontes, tais como instituições governamentais, empresas de TI e sites de notícias. No futuro, pretende-se que os dados gerados por pesquisas publicadas no hub possam compor os dados disponíveis, e que a ferramenta possa ser estendida a partir do apoio de novas parcerias.

## Agradecimentos

Este trabalho foi desenvolvido a partir de recursos da Universidade Federal de Mato Grosso (UFMT), do Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) e do International Development Research Centre (IDRC) via projeto “The Latin American Open Data for Gender Equality Policies Focusing on Leadership in STEM”.
