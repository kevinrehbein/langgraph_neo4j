# Gênero e Percurso Educacional: Evidências da Educação Básica à Graduação, com Enfase na Area de Tecnologia

Cláudia F. de Souza, Jaqueline U. Brito, Thalyta L. Rodrigues, Alice Nayara dos Santos, Carina Teixeira de Oliveira, Raquel Silveira

1Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE)

{ claudia.ferreira07, jaqueline.uchoa09, thalyta.lima08 } @aluno.ifce.edu.br,

{ alice.santos, carina.oliveira, raquel ~~s~~ ilveira } @ifce.edu.br

Abstract. Gender inequality in education has been widely discussed; however, most studies analyze only a single stage of the educational system. In this context, this work develops an interactive dashboard to analyze the educational trajectory of girls in Brazil, from Basic Education to Higher Education, using microdata from INEP. The results indicate a slightly lower number of enrollments of girls in Basic Education and higher performance in Portuguese in the 2023 Saeb, along with performance similar to boys in Mathematics. In Higher Education, female predominance is observed in admission, enrollment, and completion, although with concentration in health and education fields and low participation in technological areas.

Resumo. A desigualdade de gênero na educação tem sido amplamente discutida, porém analisando apenas uma etapa de ensino. Neste contexto, este trabalho desenvolve um painel interativo para analisar a trajetória educacional das meninas no Brasil, da Educação Básica ao Ensino Superior, a partir de microdados do INEP. Os resultados indicam quantidade de matrículas ligeiramente inferior das meninas na Educação Básica e desempenho superior em Língua Portuguesa no Saeb 2023, além de desempenho semelhante ao dos meninos em Matemática. No Ensino Superior, observa-se predominância feminina em ingresso, matrícula e conclusão, porém com concentração em áreas de saúde e educação e baixa participação em áreas tecnológicas.

## 1. Introdução

Nas últimas décadas, o sistema educacional brasileiro passou por um processo de expansão caracterizado pela ampliação do acesso à educação básica e pelo crescimento do ensino superior, em decorrência de políticas voltadas à universalização e à democratização das oportunidades educacionais [Nascimento et al. 2023]. A ampliação da oferta de vagas, a obrigatoriedade escolar e políticas de permanência reduziram barreiras históricas de acesso, especialmente para grupos socialmente vulneráveis [Roza 2023].

Contudo, a expansão do acesso não se converte automaticamente em equidade estrutural. Persistem desigualdades ao longo da trajetória educacional, associadas a fatores socioeconômicos, raciais e de gênero [INEP 2026, Ferreira and Prata 2025]. No caso do

> *O artigo foi desenvolvido no contexto do projeto DIVAS, com apoio financeiro da Rede Interset-CE da Sase/MEC.

gênero, observa-se um padrão aparentemente paradoxal: enquanto na educação básica as meninas apresentam, em média, maiores taxas de permanência e desempenho equivalente ou superior em diversas áreas, no ensino superior há forte segregação horizontal, com subrepresentação feminina nas engenharias, ciências exatas e tecnologia [Rocha et al. 2025].

Relatórios da [UNESCO 2017] e da [OCDE 2023] indicam que a subrepresentação feminina nas áreas de Science, Technology, Engineering and Mathematics (STEM) constitui fenômeno global, cuja explicação ultrapassa diferenças de desempenho acadêmico e envolve fatores socioculturais que influenciam escolhas educacionais ao longo da escolarização. No Brasil, embora as mulheres representem maioria entre ingressantes e concluintes do ensino superior, sua presença permanece concentrada em áreas tradicionalmente associadas às ciências humanas e ao cuidado, enquanto os cursos ligados à tecnologia seguem como espaços de menor representatividade feminina [INEP 2026].

Apesar da relevância do tema, a literatura nacional frequentemente aborda de forma segmentada o desempenho escolar por sexo ou a distribuição de matrículas em uma etapa de ensino, quer seja no ensino médio [Lima et al. 2022] ou no ensino superior [Nascimento et al. 2023]. São ainda limitados os estudos que conectam, de forma integrada, indicadores da educação básica às escolhas formativas e à distribuição por áreas no ensino superior. Essa fragmentação dificulta compreender como desigualdades se acumulam ou se transformam ao longo do percurso escolar.

Diante disso, o presente estudo tem como objetivo analisar desigualdades de gênero ao longo da trajetória educacional, articulando microdados do Censo Escolar da Educação Básica, do Sistema de Avaliação da Educação Básica (Saeb) e do Censo da Educação Superior, produzidos pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Por meio dessas bases, empregou-se o Power BI, ferramenta de Business Intelligence (BI), para construir um painel interativo e dinâmico que permite examinar como padrões de participação e proficiência na educação básica podem se associar à inserção feminina no ensino superior, considerando a distribuição por áreas do conhecimento e os indicadores de ingresso e conclusão por gênero, com ênfase na área de tecnologia. O painel destina-se a pesquisadores, gestores educacionais e formuladores de políticas públicas, oferecendo uma ferramenta de apoio à análise e à tomada de decisão.

Ao deslocar o foco de análises segmentadas para uma abordagem integrada do percurso formativo, o estudo contribui para o debate sobre desigualdades de gênero ao revelar como diferenças observadas na educação básica podem coexistir com padrões de sub-representação feminina no ensino superior. A ênfase na tecnologia decorre da compreensão de que a sub-representação feminina nesses cursos não deve ser tratada como fenômeno isolado do nível superior, mas analisada em articulação com diferenças já observáveis nas etapas anteriores da escolarização.

## 2. Trabalhos Relacionados

A literatura sobre desigualdades de gênero na educação investiga participação, desempenho e escolhas de áreas do conhecimento. Esta seção revisa estudos sobre inserção feminina, desafios em cursos de tecnologia e lacunas que motivam este trabalho.

O artigo [Mesquita et al. 2025] apresenta um mapeamento da representatividade feminina nos cursos de Tecnologia da Informação nos níveis técnico e de graduação do

Instituto Federal do Ceará (IFCE) a partir de dados abertos de matrículas presenciais de 2016 a 2022. O artigo mostra que a participação média feminina nos cursos técnicos era de 44,7%, caindo drasticamente para 17,4% na graduação, evidenciando uma expressiva redução da presença feminina ao avançar para o ensino superior.

Similarmente, [Santos et al. 2025] investigam a participação feminina no Instituto Federal de Pernambuco (IFPE) através dos dados do Censo da Educação Superior. Embora as mulheres apresentem, em média, maior nível de instrução, essa realidade não se reflete nos cursos de Computação e Tecnologias da Informação e Comunicação, onde permanecem em minoria. Os resultados indicam que, entre 2009 e 2022, o público feminino teve baixa participação nos ingressos, matrículas e conclusões, atingindo, por exemplo, 30,3% no curso de Análise e Desenvolvimento de Sistemas do campus Recife após a expansão dos campus em 2021.

Em contrapartida, [Marques et al. 2021] analisaram a participação feminina no curso Técnico em Informática Integrado ao Ensino Médio do Instituto Federal de São Paulo (IFSP) campus Hortolândia, construindo dashboards para visualizar o desempenho das alunas e o interesse na área. Os resultados mostraram que, em 2023, as mulheres representavam 86% das matrículas, apresentando desempenho superior aos alunos, mesmo quando relatavam baixo interesse pelo curso. No entanto, em disciplinas relacionadas à área de TI, como Algoritmos e Programação, as alunas registraram médias menores.

Apesar de amplamente discutida, a desigualdade de gênero na educação costuma ser analisada de forma isolada nos níveis de ensino, sem conectar o desempenho e a participação das alunas ao longo da trajetória escolar. Neste trabalho, são analisados os indicadores de participação e desempenho feminino desde a educação básica até o ensino superior, com ênfase em áreas de baixa representatividade feminina, como tecnologia.

## 3. Metodologia

Este estudo analisa dados do INEP para construir um painel interativo com visualizações sobre participação e desempenho por gênero ao longo da trajetória escolar, da Educação Básica ao Ensino Superior, com ênfase na área de tecnologia. As etapas adotadas neste estudo são descritas a seguir.

### 3.1. Elaboração das Questões de Pesquisa

Como delimitação do problema da análise das desigualdades de gênero ao longo da trajetória educacional, foram definidas Questões de Pesquisa (QP) específicas, estruturadas de modo a orientar a análise descritiva e a construção das visualizações no painel:

- QP1: Como se distribui o acesso à Educação Básica considerando variações regionais e diferenças de gênero?

- QP2: Existem diferenças de desempenho entre meninas e meninos nas áreas de Matemática e Língua Portuguesa no final da Educação Básica?

- QP3: De que forma fatores estruturais, como tipo de escola e nível socioeconômico, influenciam o desempenho educacional na Educação Básica?

- QP4: A participação feminina no Ensino Superior reflete o mesmo padrão observado na Educação Básica?

- QP5: As taxas de ingresso e conclusão na Ensino Superior diferem entre os gêneros?

20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

- QP6: Como se distribui a participação feminina nas diferentes áreas do conhecimento no Ensino Superior, com ênfase na área de Computação e TIC?

### 3.2. Coleta dos Dados

Os dados utilizados nesta pesquisa foram extraídos das bases de microdados disponibilizadas publicamente pelo INEP, que reúnem informações referentes a censos e avaliações da educação básica e superior no Brasil. Inicialmente, realizou-se um levantamento de todas as bases disponíveis no repositório do INEP. Para a seleção das bases de análise, foram adotados os seguintes critérios de inclusão: (i) bases contendo dados referentes ao ano de 2023 ou posterior; (ii) bases relacionadas à educação básica, à avaliação da educação básica ou à educação superior; e (iii) bases com dados segmentados por gênero. Assim, foram consideradas elegíveis para o estudo as seguintes bases: Censo Escolar da Educação Básica, Saeb e Censo da Educação Superior. A coleta ocorreu em setembro de 2025, sendo selecionadas os dados mais recentes de cada base no momento da coleta. Assim, coletou-se dados de 2024 para todas as bases, com exceção do Saeb, cujo ciclo mais recente correspondia ao ano de 2023, em razão de sua periodicidade de aplicação.

### 3.3. Análise Exploratória dos Dados

Após a seleção das bases, realizou-se uma análise exploratória dos dados para compreender sua estrutura e conteúdo. Foram examinados os dicionários de dados para identificar variáveis, esquemas de codificação e níveis de agregação, assim como avaliar a compatibilidade e a possibilidade de integração entre as bases. Esses resultados orientaram a seleção das variáveis e a estratégia de articulação dos dados nas etapas seguintes.

### 3.4. Pré-processamento dos Dados

Nesta etapa foi realizado o pré-processamento dos dados, com o objetivo de padronizar os dados e facilitar a interpretação das informações. Inicialmente, foram removidas colunas consideradas irrelevantes para os objetivos da pesquisa, como informações administrativas, dados detalhados de infraestrutura escolar e outros atributos que não contribuíam diretamente para as análises realizadas. Essa subetapa teve como objetivo reduzir a dimensionalidade da base e manter apenas os dados necessários para a investigação.

Em seguida, foi realizada a decodificação de variáveis categóricas originalmente representadas por códigos numéricos ou alfanuméricos, conforme os dicionários de dados. Para facilitar a interpretação e análise dos resultados, foram criadas novas colunas contendo as descrições correspondentes aos códigos. Esse procedimento foi aplicado, por exemplo, às variáveis relacionadas à rede de ensino (pública ou privada), unidades federativas e grau acadêmico dos cursos no ensino superior.

### 3.5. Construção do Painel

Com o intuito de auxiliar na visualização, exploração e interpretação dos dados analisados, foi desenvolvido um painel interativo utilizando a plataforma Power BI. A estrutura do painel foi concebida considerando as QP previamente definidas, organizando indicadores e visualizações segmentados por gênero, permitindo examinar padrões de participação e desempenho por gênero ao longo das diferentes etapas de ensino.

> 1https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/ microdados

O painel foi estruturado em três módulos, cada um dedicado a uma etapa ou dimensão específica da trajetória educacional. O módulo Educação Básica apresenta uma caracterização geral das matrículas na educação básica, com base nos dados do Censo Escolar. As visualizações contemplam a distribuição de estudantes por rede administrativa e unidade federativa. O segundo módulo, Saeb, analisa o desempenho nas proficiências em Língua Portuguesa e Matemática de estudantes da 3ª série do Ensino Médio com base no Saeb 2023, apresentando informações sobre distribuição dos participantes, desempenho por unidade federativa, rede de ensino e nível socioeconômico. Por fim, o módulo Educação Superior sistematiza indicadores de acesso, matrícula e conclusão, a partir do Censo da Educação Superior, além da distribuição por área do conhecimento, com ênfase na área de tecnologia.

## 4. Resultados e Discussões

As análises apresentadas nesta seção buscam responder às QP definidas anteriormente. As visualizações foram elaboradas com o objetivo de evidenciar diferenças e padrões entre gêneros ao longo da trajetória educacional.

### 4.1. QP1: Como se distribui o acesso à Educação Básica considerando variações regionais e diferenças de gênero?

De acordo com os dados do Censo Escolar, em 2024, a Educação Básica brasileira registrou aproximadamente 47,1 milhões de matrículas, abrangendo da pré-escola ao Ensino Médio. Desse total, 50,60% correspondem a estudantes do sexo masculino e 49,40% ao sexo feminino (Figura 1), indicando uma distribuição bastante equilibrada entre os gêneros no acesso à educação básica formal.

Em termos regionais, observa-se maior concentração de matrículas na região Sudeste, seguida pelas regiões Nordeste e Sul. As regiões Norte e Centro-Oeste apresentam menor número absoluto de estudantes matriculados, padrão que acompanha, de maneira geral, a distribuição populacional do país.

Esses resultados indicam que não há evidências de desigualdade significativa entre meninos e meninas no acesso à Educação Básica, sugerindo que a trajetória educacional feminina se inicia em condições quantitativamente semelhantes às masculinas.

### 4.2. QP2: Existem diferenças de desempenho entre meninas e meninos nas áreas de Matemática e Língua Portuguesa no final da Educação Básica?

Para analisar o desempenho acadêmico ao final da Educação Básica, foram utilizados os dados do Saeb 2023 referentes aos estudantes da 3ª série do Ensino Médio, etapa que antecede o ingresso no Ensino Superior. No total, cerca de 2,1 milhões de estudantes da 3ª série do Ensino Médio participaram da avaliação, dos quais 37,7% se autodeclararam do sexo feminino, 33,5% masculino e 28,8% não informaram. Considerando o objetivo deste estudo, a análise concentra-se nos estudantes que informaram gênero.

As proficiências do Saeb são expressas em uma escala contínua de 0 a 500 pontos e organizadas em níveis de desempenho [INEP 2020]. Em Língua Portuguesa, os níveis variam de 0 a 8, enquanto em Matemática variam de 0 a 10. Os resultados apresentados na

> 2Link para o Painel “Gênero e Percurso Educacional: Evidências da Educação Básica à Graduação”.

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

- 20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

Figura 1. Matrículas no Ensino Básico em 2024.

Figura 2 indicam padrões distintos de desempenho entre as áreas avaliadas. As estudantes do sexo feminino apresentaram média de 279 pontos em Língua Portuguesa (Nível 3) e os estudantes do sexo masculino obtiveram média de 268 pontos (Nível 2). Em Matemática, os estudantes do sexo masculino apresentaram média de 272 pontos, ligeiramente superior à média feminina de 265 pontos, embora ambos permaneçam classificados no Nível 2.

Figura 2. Desempenho no Saeb por gênero.

Esses resultados evidenciam uma assimetria de desempenho associada às áreas do conhecimento: vantagem feminina em Língua Portuguesa (+11 pontos) e vantagem masculina em Matemática (+7 pontos). Entretanto, a diferença observada em Matemática não é suficiente para deslocar os grupos para níveis distintos de proficiência, indicando que o desempenho feminino nessa área permanece relativamente próximo ao masculino.

A análise regional reforça esse padrão. Em todos os estados, as estudantes apresentaram médias superiores em Língua Portuguesa em relação à Matemática. Estados do Sul e Sudeste registraram os maiores desempenhos, enquanto estados do Norte e Nordeste apresentaram os menores, evidenciando desigualdades educacionais regionais.

### 4.3. QP3: De que forma fatores estruturais, como tipo de escola e nível socioeconômico, influenciam o desempenho educacional na Educação Básica?

A avaliação do Saeb 2023 foi realizada de forma censitária nas escolas públicas e amostral nas escolas privadas [INEP 2024]. Como consequência, entre os participantes da 3ª série do Ensino Médio no Saeb 2023, 98,15% dos participantes pertencem à rede pública de ensino, enquanto apenas 1,85% são oriundos de escolas privadas. Nas escolas públicas, as meninas participantes correspondem a 53% e nas escolas privadas correspondem a 51%.

Os resultados indicam diferenças entre os tipos de escola (pública e privada). As estudantes da rede privada obtiveram médias de 314 pontos em Língua Portuguesa e 307 pontos em Matemática, ambas correspondentes ao Nível 4. Já as estudantes da rede pública alcançaram médias de 278 pontos em Língua Portuguesa (Nível 3) e 264 pontos em Matemática (Nível 2). Esses resultados indicam uma vantagem das alunas da rede privada em ambas as áreas avaliadas.

Outro fator relevante é o nível socioeconômico. O Indicador de Nível Socioeconômico classifica os estudantes em oito níveis, com base na escolaridade dos pais, posse de bens e condições domiciliares [INEP 2025]. O nível 1 representa condições socioeconômicas muito baixas, enquanto o nível 8 indica maior acesso a bens, tecnologia e capital cultural familiar.

Aproximadamente 58% dos estudantes encontram-se nos níveis socioeconômicos 1 a 4, desse total, 62% de meninas e 38% de meninos, indicando maior concentração em camadas sociais de menor capital econômico. Os resultados indicam uma relação consistente entre nível socioeconômico e desempenho acadêmico. Observa-se que, tanto em Língua Portuguesa quanto em Matemática, as médias de proficiência tendem a aumentar conforme o nível socioeconômico dos estudantes, evidenciando a influência das condições sociais no desempenho escolar.

Esses resultados sugerem que desigualdades estruturais relacionadas a condições socioeconômicas e ao tipo de escola exercem influência mais significativa sobre o desempenho educacional do que as próprias diferenças de gênero.

### 4.4. QP4: A participação feminina no Ensino Superior reflete o mesmo padrão observado na Educação Básica?

Conforme Censo da Educação Superior, em 2024, aproximadamente 10,23 milhões de estudantes estavam matriculados em cursos de graduação no Brasil. Desse total, 59,53% são mulheres e 40,47% são homens (Figura 3). Esse resultado revela que, diferentemente da Educação Básica, na qual a distribuição entre os gêneros é praticamente equilibrada, no Ensino Superior as mulheres passam a constituir a maioria dos estudantes.

Esse padrão se mantém em todas as regiões do país. O Sudeste concentra o maior número absoluto de matrículas femininas, seguido pelo Nordeste e Sul. Mesmo nas regiões com menor número total de matrículas, como Norte e Centro-Oeste, as mulheres continuam predominando.

Nas instuitições de ensino superior públicas, observa-se uma distribuição relativamente equilibrada entre os estudantes do sexo masculino e feminino, com 965.432 homens e 1.099.635 mulheres matriculados. Em contraste, no setor privado, verifica-se predominância feminina mais expressiva, totalizando 4.988.967 matrículas de mulheres

46º Congresso da Sociedade Brasileira de Computação (CSBC 2026), Gramado/RS

- 20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

Figura 3. Matrículas no Ensino Superior em 2024.

frente a 3.173.232 de homens. Esse padrão indica que a maior participação feminina no Ensino Superior brasileiro está fortemente concentrada na rede privada, enquanto a rede pública apresenta distribuição mais próxima do equilíibrio entre os gêneros.

### 4.5. QP5: As taxas de ingresso e conclusão no Ensino Superior diferem entre os gêneros?

Entre os ingressantes no Ensino Superior em 2024, que totalizam aproximadamente 5 milhões de estudantes, 59,77% são mulheres e 40,23% são homens. Esse resultado indica que o fluxo de entrada no Ensino Superior já apresenta predominância feminina.

Esse padrão também se mantém entre os concluintes. Em 2024, cerca de 1,33 milhão de estudantes concluíram cursos de graduação, dos quais 59,46% são mulheres e 40,54% são homens. Esses resultados indicam que a maior participação feminina não ocorre apenas no acesso ao ensino superior, mas também se mantém ao longo da trajetória acadêmica, refletindo-se em maior proporção de mulheres entre os concluintes.

A pequena variação percentual entre ingressantes, matriculados e concluintes sugere que a participação feminina permanece relativamente estável ao longo da trajetória acadêmica, indicando que as mulheres não apenas ingressam em maior número, mas também concluem o Ensino Superior em proporção semelhante, o que reforça a maior participação feminina no ensino superior brasileiro.

### 4.6. QP6: Como se distribui a participação feminina nas diferentes áreas do conhecimento no Ensino Superior, com ênfase na área de Computação e TIC?

Em 2024, as matrículas femininas no Ensino Superior brasileiro concentraram-se principalmente nas áreas de Saúde e Bem-Estar (16,67%), Negócios, Administração e Direito (15,92%) e Educação (12,93%). Em contraste, a área de Computação e TIC apresentou baixa participação feminina (1,51%). Assim, embora as mulheres representem a maioria das matrículas no ensino superior, sua presença distribui-se de forma desigual entre as áreas do conhecimento, sendo mais reduzida nos campos tecnológicos.

Quando analisados em conjunto com os resultados da Educação Básica, observase que, no Saeb 2023, as estudantes apresentaram média superior em Língua Portuguesa, enquanto os homens obtiveram média ligeiramente maior em Matemática. Embora esse desempenho não determine, por si só, as escolhas profissionais, observa-se maior presença feminina em áreas associadas às ciências humanas, paralelamente ao desempenho mais elevado das estudantes em Língua Portuguesa, enquanto áreas das ciências exatas e tecnológicas apresentam maior participação masculina.

Em 2024, foram registradas 153.931 matrículas femininas (19,2%), enquanto as masculinas alcançaram 646.291 (80,8%), evidenciando forte predominância masculina. Entre os ingressantes, as mulheres representam 19,72% (Figura 4a), enquanto entre os concluintes esse percentual é de 17,59% (Figura 4b), indicando que a sub-representação feminina persiste ao longo da trajetória acadêmica (ingresso, permanência e êxito).

Figura 4. Ingresso e conclusão das estudantes na área de Computaç ão e TIC.

A análise regional mostra que esse padrão se mantém em todas as regiões. Entre os ingressantes, a participação feminina varia entre 19% e 22%, sendo ligeiramente maior no Sudeste (22,17%) e menor no Nordeste (19,72%), o que sugere que a sub-representação feminina na área de TIC é um fenômeno generalizado no país. A análise por unidade federativa reforça esse padrão. Mesmo nos estados com maior participação feminina entre ingressantes, como Piauí (30,6%), Amazonas (23,38%) e São Paulo (23,16%), os valores permanecem distantes da paridade de gênero. Em estados como Sergipe e Alagoas, a participação feminina fica abaixo de 16%, indicando presença ainda mais reduzida.

Entre os concluintes, observa-se padrão semelhante. No Sudeste, por exemplo, 20,19% dos concluintes são mulheres. A pequena diferença entre os percentuais de matriculadas (20,08%) e concluintes (20,19%) sugere que, apesar de serem minoria, as mulheres tendem a concluir os cursos em proporção semelhante à participação no curso.

Em relação aos cursos da área, Análise e Desenvolvimento de Sistemas (ADS) concentra o maior número absoluto de estudantes de ambos os gêneros. A desigualdade de gênero, entretanto, mantém-se entre as diferentes formações. Cursos como Gestão da Tecnologia da Informação, Banco de Dados e Sistemas de Informação apresentam participação feminina, com valores de ingressantes entre 30% a 27% e concluintes entre 27% a 25%. Enquanto o curso de Redes de Computadores apresenta a menor presença feminina, com 12,47% de ingressantes e 8,14% de concluintes em 2024.

Quando considerados os indicadores de desempenho educacional, observa-se que as estudantes apresentam média de proficiência em Matemática no Saeb ligeiramente inferior à dos estudantes do sexo masculino, sem alteração no nível de proficiência. Assim, a baixa participação feminina em cursos de Computação e TIC não parece estar associada a diferenças significativas de desempenho acadêmico, sugerindo a influência de outros fatores nas escolhas educacionais e profissionais.

De modo geral, os resultados indicam que a baixa participação feminina nos cursos de Computação e TIC não se restringe ao ingresso, mas caracteriza um padrão estrutural ao longo de todo o percurso formativo. Mesmo considerando diferentes cursos, regiões e estados, a presença masculina permanece predominante, evidenciando a necessidade de políticas e iniciativas que incentivem a participação feminina nas áreas tecnológicas.

## 5. Considerações Finais

Este estudo analisou a trajetória educacional das meninas no Brasil, da Educação Básica ao Ensino Superior, a partir de microdados do INEP, buscando compreender padrões de participação e desempenho ao longo da trajetória escolar, com ênfase em tecnologia.

Os resultados indicam que o acesso à Educação Básica ocorre de forma equilibrada entre gênero. Quanto ao desempenho acadêmico, as meninas apresentam desempenho superior em Língua Portuguesa e desempenho próximo ao dos meninos em Matemática, embora persistam desigualdades associadas ao nível socioeconômico e tipo de escola. Esses fatores estruturais demonstram exercer influência mais significativa sobre o desempenho acadêmico do que o próprio gênero.

No Ensino Superior, observa-se consolidação da maioria feminina em termos de ingresso, matrícula e conclusão, evidenciando avanços no acesso e permanência. Entretanto, a análise por área do conhecimento revela um padrão de concentração feminina em campos tradicionalmente associados ao cuidado e às ciências humanas, enquanto permanece reduzida a participação em áreas tecnológicas, como Computação e TIC. A baixa participação feminina nessas áreas não parece estar associada a diferenças de desempenho na Educação Básica, sugerindo a influência de outros fatores nas escolhas educacionais.

Dessa forma, os resultados indicam que a desigualdade de gênero na educação brasileira não se manifesta principalmente no acesso ao ensino, mas na distribuição desigual entre áreas de formação, especialmente nas áreas tecnológicas, além da influência de fatores socioeconômicos e do contexto escolar. Como trabalhos futuros, pretende-se ampliar a análise por meio de abordagens longitudinais, investigando os fatores que influenciam a participação feminina nas áreas de tecnologia ao longo do tempo.

- 20º Women In Information Technology (WIT 2026): Artigos de Pesquisa

## Uso de Inteligência Artificial

De acordo com as políticas do WIT 2026, um Large Language Model (LLM), mais especificamente, OpenAI ChatGPT (com o modelo GPT-5.3), foi utilizado exclusivamente para refinamento linguístico e revisão gramatical deste manuscrito. Nenhuma contribuição científica, incluindo metodologia, experimentos, resultados ou conclusões, foi gerada por IA. Todo o conteúdo foi revisado e validado pelos autores, que assumem total responsabilidade pela correção, originalidade e integridade do artigo.
