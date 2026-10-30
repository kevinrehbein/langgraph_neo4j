# A Digital Educational Game to Promote Inclusive Programming Education for Refugee Girls

Alexya Silva, Ana Clara Laredo, Pedro Henrique Valle, Alessandreia Oliveira

1Departamento de Ciência da Computação - UFJF, Juiz de Fora – MG – Brasil

2Universidade de São Paulo - USP – São Paulo, SP – Brasil

alessandreia.oliveira@ufjf.br,alexya.jesus@estudante.ufjf.br ana.laredo@estudante.ufjf.br, pedrohenriquevalle@usp.br

Abstract. Digital Educational Games (DEGs) have been widely used to support teaching in several areas, especially in contexts that require inclusion and engagement. This work presents a DEG to introduce programming concepts to refugee girls aged 12–14, fostering interest in Computing and promoting gender equality. The tool incorporates accessible language, culturally representative narrative, and puzzle-based challenges aligned with programming concepts. We conducted a heuristic evaluation and a cognitive walkthrough, and the results identified usability issues and highlighted aspects related to engagement, representativeness, and educational potential. The DEG contributes to Sustainable Development Goals by promoting digital inclusion and empowering women.

## 1. Introduction

The global crisis of forced displacement has worsened in recent years. In 2023, the number of forcibly displaced people reached 117.3 million, and in April 2025, approximately 122 million people were displaced. In Brazil, although there are public policies focused on welcoming approximately 710 thousand refugees, significant challenges related to integration and social vulnerability still persist, especially among women and children [Fernandes and Onuma 2024]. This scenario highlights the need for accessible educational technologies to support inclusion and skill development.

In this scenario, the United Nations (UN) Sustainable Development Goals (SDGs) highlight the relevance of initiatives that promote gender equity, access to quality education, and the reduction of social inequalities, as established in SDGs 4, 5, and 10. Specifically, the city of Juiz de Fora and its region host approximately 3 thousand refugees, predominantly women and girls. Despite this, it is estimated that approximately 68% of refugees remain outside the labor market in host countries, largely due to linguistic and social barriers that disproportionately affect women. In this context, educational tools that combine accessibility, engagement, and skill development become particularly relevant.

From another perspective, Brazil faces a growing demand for technology professionals, with an estimated annual deficit of 106 thousand unfilled positions. In this context, digital educational tools that integrate learning and inclusion, such as those support-

> 1https://www.unhcr.org/global-trends

> 2https://news.un.org/pt/story/2024/01/1825912

> 3https://brasil.un.org/pt-br/sdgs

> 4https://www.pjf.mg.gov.br/noticias/view.php?modo=link2&idnoticia2= 82673

> 5https://www.cnnbrasil.com.br/tudo-sobre/imigrantes/pagina/26/

> 6https://tiinside.com.br/01/12/2021/

ing Computing Education for socially vulnerable populations, play a key role in promoting equity and social transformation [Gottschalk and Weise 2023, UNESCO IITE 2025].

Considering the challenges faced by refugee girls and the opportunities for inclusion in Information Technology (IT), this work presents Jogando para o Amanhã, a Digital Educational Game (DEG) designed as an educational tool to support programming education for refugee girls aged 12 to 14. The tool integrates accessible language, a culturally representative narrative, and puzzle-based challenges aligned with programming concepts, enabling engagement, digital inclusion, and the development of computational skills. The tool is publicly available for research and educational purposes. License information is provided in the repository metadata.

This work is organized as follows: Section 2 presents the theoretical foundation and discusses related works. Section 3 describes the development process of the proposed DEG. Section 4 details the architecture, design, and main features of the tool, and Section 5 presents the evaluations conducted, including heuristic evaluation and cognitive walkthrough. Some threats to validity are discussed in Section 6. Finally, Section 7 presents final considerations and future perspectives.

## 2. Background and Related Work

In Brazil, the National Common Core Curriculum (BNCC) [Brasil 2022] incorporated Computing more explicitly through a supplement published in 2022, which organizes the area into three axes: Computational Thinking (CT), Digital World, and Digital Culture. In middle school, CT includes skills such as data classification, algorithm development, and problem-solving strategies. However, teaching CT remains challenging due to the abstraction required to understand logical structures [Robins 2019], highlighting the need for educational tools that support the gradual development of these concepts.

Digital Educational Games (DEGs) have been explored as a strategy to bridge the gap between concrete experiences and abstract Computing concepts [Petri et al. 2017]. By combining interactive environments with active learning, these games can increase engagement and support learning retention [Prensky and Yamagute 2021]. In addition, DEGs can strengthen girls’ confidence and sense of belonging in Computing. From a tool perspective, DEGs provide interactive environments that operationalize pedagogical strategies through game mechanics and user interaction. These principles guided the design of the DEG proposed in this work, which integrates CT learning into a narrative centered on refugee protagonists and uses accessible language and progressive challenges to reduce cognitive barriers [Robins 2019].

Several DEGs have been proposed to support programming education. Codeland [Silva et al. 2022] and Hello Food [Macena et al. 2022] introduce programming concepts through interactive challenges. Although these games show positive learning results, as tools, they lack adaptations for specific user groups, such as the sociocultural context of refugees and linguistic or accessibility support for girls in lower secondary education.

Other games aim to promote female engagement in Computing. ProgramADAs [Yamashita et al. 2024] uses RPG elements to teach programming to women entering Computing degree programs, while Thinking Girls [Santos et al. 2024] teaches computational thinking through logic challenges supported by characters inspired by historical

> 7https://github.com/alexya09/JogandoParaOAmanha

figures in Computing. However, these tools are designed for older audiences and do not address the needs of younger refugee girls.

Other educational games explore narrative and social contexts to stimulate interest in Computing, such as Sucesso4me [Duarte et al. 2021], Peg.Ada [Vinhal and Odakura 2024], and FemQuest [Holly et al. 2024]. These tools use storytelling and logical challenges to promote identification and motivation, but do not provide structured support for introductory programming learning in younger audiences.

In the context of refugee populations, The Rights Hero [Dima et al. 2022] and Project Hope [Sirin et al. 2018] use digital games to promote awareness, language learning, and programming skills among refugee children. However, these tools are not specifically designed for girls and do not provide structured support for introductory programming in the Brazilian context, highlighting a gap that the proposed DEG aims to address.

Unlike existing tools such as Codeland, Hello Food, and ProgramADAs, Jogando para o Amanhã combines introductory programming activities with culturally sensitive design and a specific focus on refugee girls in lower secondary education.

## 3. Methodology and Action Strategies

This work presents the development of a DEG for teaching programming to refugee girls in lower secondary education (ages 12 to 14), as part of the ongoing project Jogando para o Amanhã. The proposed DEG is designed as an educational tool that supports introductory programming learning through interactive and accessible game-based activities. The game was designed to run in the computer laboratories of public schools serving this audience, with the technical limitations of available equipment taken into account from the outset. This approach opted for a lightweight, accessible solution with minimal hardware requirements. In addition, the DEG is being developed in Portuguese, following the plain-language guidelines of [BRASIL 2019]. The adoption of this language model aims to reduce comprehension barriers by prioritizing short sentences, direct order, and familiar vocabulary. It also relies on a visual glossary and tutorials with icons and examples. The system architecture allows future translations into Spanish and English.

To develop the DEG in accordance with the real needs of refugee girls, a development process was established to guide the design and implementation of the tool, structured into five stages: initial research, review and definition, DEG development, evaluation, and improvement. The initial research stage was exploratory, aimed at understanding the target audience and its context. To this end, observations and informal conversations with refugees identified preferences for logic and puzzle games, as well as challenges such as linguistic barriers, limited access to technology, and varying levels of familiarity with games. These findings were translated into design requirements for the tool, guiding decisions about the game’s language, interaction, and complexity.

In the review and definition stage, a bibliographic survey of related works and DEGs focused on teaching programming and computational thinking was conducted to identify best practices, limitations, and adopted pedagogical strategies. In parallel, an analysis of candidate game engines was carried out, considering criteria such as accessibility, ease of use in school environments, and technical feasibility. In this stage, the pedagogical foundations of programming teaching and computational thinking were also reviewed, particularly those grounded in decomposition, abstraction, algorithms, and pattern recognition [Wing 2006]. This analysis culminated in defining the DEG’s scope,

phases, game mechanics, educational objectives, and functional requirements of the tool, strategically structured to mitigate abstraction challenges and the high cognitive load inherent to learning Computing concepts [Robins 2019]. Therefore, the tool requirements were defined based on three sources: (1) The BNCC [Brasil 2022], (2) a literature review of DEGs for programming education, and (3) technical constraints of school computer laboratories that serve the target audience.

The DEG development stage involved implementing the game using the chosen engine, including core functionalities such as programming mechanics, puzzle-based challenges, and progression systems, as well as creating art and visual elements. An effort was made to adopt a simple, intuitive aesthetic aligned with the target audience and the constraints of public school computer laboratories. The DEG was evaluated using two methods, heuristic evaluation (HE) and cognitive walkthrough, focusing on player actions, clarity of objectives, and the adequacy of interactions. These evaluations enabled the identification of issues related to the interface, mechanics, and task comprehension. It is worth noting that the initial evaluations involved only adult participants, with voluntary participation, prior clarification of objectives, respect for applicable ethical principles, and assurance of data anonymity.

The improvement stage consisted of analyzing the evaluation results and applying the identified recommendations, adjusting the mechanics, interface, and information presentation accordingly. This stage aimed to refine the DEG, increasing its usability, accessibility, and effectiveness as a tool for supporting programming instruction.

## 4. Digital Educational Game

In light of social and educational inequalities, the DEG Jogando para o Amanhã aims to promote programming education for refugee girls in lower secondary education (ages 12 to 14). The DEG aims to promote the development of basic programming skills, foster interest in Computing, and encourage autonomy in solving everyday problems. The main challenges of the project include gaining direct access to refugee girls, ensuring respectful cultural representation, and adapting DEG content to make it more engaging and dynamic.

### 4.1. Technical aspects of the DEG

The DEG is being developed with the support of the GameMaker game engine, which enables the creation of 2D games with lightweight executables. To define the visual style, criteria such as attractiveness to refugee girls, low computational cost, and feasibility of production with limited resources were considered. Thus, the pixel art style was adopted, as it simultaneously meets these criteria.

The game narrative unfolds around two fictional characters, Cármen and Camila, refugees from Venezuela. While exploring an abandoned house (Figure 1.a), they are transported through an old computer (Figure 1.b), to a virtual world (Figure 1.c) controlled by a villain who tries to prevent them from learning programming. The story emphasizes the importance of overcoming difficulties and resilience, thereby reinforcing the identity and rights of refugee girls. The character design reflects Venezuelan ethnic diversity, featuring diverse skin tones, hairstyles, and elements that promote identification, such as simple clothing and accessories that convey personality.

> 8https://gamemaker.io/pt-BR

(a) House

Figure 1. Central elements of the DEG narrative.

### 4.2. DEG Architecture

The architecture of Jogando para o Amanhã follows a modular design organized into three layers: input systems, game core, and output systems, as illustrated in Figure 2. This structure separates user interaction, game logic processing, and feedback presentation, improving maintainability and extensibility. Player interactions are captured through input devices, currently including keyboard and mouse, which detect commands and translate them into events sent to the game’s internal processing layer.

Figure 2. DEG Architecture.

The game core manages the game’s internal logic and execution and is composed of three modules: object systems, activities, and game flow. Object systems control the state and behavior of interactive entities such as characters and puzzles. The activities module implements the educational challenges of each phase, supporting the learning of introductory programming concepts. The game flow module coordinates player progression, controlling state transitions and task sequencing.

Finally, the output systems present the results of game processing through a visual module (images and text) and a sound module. These components provide immediate visual and auditory feedback to player actions, reinforcing interaction and engagement. This layered architecture promotes separation of concerns and supports the implementation of mechanics aligned with the DEG’s pedagogical objectives.

### 4.3. Phase Mapping

The DEG is structured into phases with progressively increasing difficulty, using a puzzlebased approach (Table 1) to introduce fundamental programming concepts in a playful manner, including variables, conditional structures, and loops. Each phase combines interactive mechanics and contextualized narrative to facilitate understanding of concepts and increase player engagement.

Table 1. DEG phases, game elements, and programming contents

|Phases|Description of the dynamics|Game elements|Programming contents|
|---|---|---|---|
|1 – Variables|Classification of variables into portals corresponding to their types|Categorical portals, immediate visual feedback, association challenge|Data types: integer, boolean, float, and character|
|2 – Algorithms|Guiding a character through a maze usingsequential instructions|Maze, cooperative characters, directional commands|Algorithms and instruction sequencing|
|3 – Turing Tumble|Assembly and connection of pieces inspired by Turing Tumble to simulate logic circuits and activate mechanisms|Logic puzzle, interactive modular pieces, doors, and mechanisms|Control structures: sequence and repetition|
|4 – Debugging|Correction of a speech containing logic errors to confront the villain|Final narrative, review challenge, narrativeprogression|Integration of data types, algorithms,and logic;debugging|

In Phase 1, players classify integer, boolean, and character variables into corresponding portals. The mechanics of this phase aim to promote an initial understanding of data types in programming, stimulating the ability to recognize and categorize information based on their semantic and structural characteristics. This playful approach encourages players to practice abstraction, the ability to deal with complexity by ignoring irrelevant details [Wing 2006]. In this stage, the player ignores the literal value of the block (whether it is 10 or 100) and focuses on its categorical nature (integer type).

Phase 2 (Figure 3.a) introduces the concept of algorithms through a maze. One character is accidentally thrown into the structure and cannot escape alone. The other, with a complete view of the path, must guide her by giving instructions such as “right,” “down,” or “up.” This dynamic stimulates planning of logical sequences and spatial reasoning, reinforcing the idea that an algorithm is an ordered set of steps to achieve a goal. This dynamic reinforces the view of [Wing 2006] that CT is not about the computer itself, but about formulating of logical processes to achieve goals.

In Phase 3 (Figure 3.b), the DEG presents an interactive reinterpretation of the physical game Turing Tumble [Boswell and Boswell 2017]. Players must position and connect pieces that simulate logic circuit components to activate mechanisms that open doors. This challenge reinforces understanding of control structures, such as sequences and repetitions, promotes decomposition [Wing 2006], and internalizes execution flows typical of programming languages. The visual representation and manipulation of logical elements contribute to meaningful, contextually relevant learning.

Finally, Phase 4 (Figure 3.c) proposes an integrative challenge: confronting the villain requires the player to review and correct a text with logical inconsistencies. This stage consolidates previous contents by requiring the combined application of knowledge about data types, algorithms, programming logic, and textual structure. The activity reinforces debugging skills, attention to detail, pattern recognition, and critical evaluation.

b) Algorithms

c) Turing Tumble

d) Debugging

Figure 3. DEG phases

It is worth noting that each phase is preceded by an introduction that provides context for the concepts explored. Following the principles of plain language, all game texts were developed with brevity, direct sentence structure, and concrete terms as priorities. This design choice aims to reduce cognitive load, ensuring that the players’ mental effort is directed toward solving the challenges rather than understanding the instructions and narrative. These design choices ensure engagement and promote a gradual learning curve.

In a typical usage scenario, the player begins exploring the narrative and progresses through increasingly complex phases, interacting with puzzle-based challenges using keyboard and mouse. The system provides immediate visual and textual feedback, supporting task completion and guiding progression. Additional resources, such as tutorials and a visual glossary, support understanding instructions and game elements.

## 5. Evaluation

This section presents the two evaluations conducted to verify the effectiveness of the DEG, namely: the heuristic evaluation and the cognitive walkthrough.

### 5.1. Heuristic Evaluation (HE)

Heuristic evaluation (HE) [Nielsen 1995] is widely used to efficiently identify usability problems, especially in early stages of software development, including digital games [Pinelle et al. 2008]. In this context, we evaluate Jogando para o Amanhã using the AHJED heuristics [Azevêdo et al. 2018], aiming to identify issues that could hinder algorithm learning in refugee girls and affect their interest in Computing. The AHJED acronym refers to five dimensions: (i) A – Learning Aspects: analyze whether the game supports knowledge construction, promotes motivation, and aligns with learning objectives; (ii) H – Gameplay Heuristics: related to fun, appropriate challenge, and clear rules that foster engagement; (iii) J – Game Interface and Interaction: verify command clarity, interface consistency, immediate feedback, and experience fluency; (iv) E – Educational Interaction Elements: consider instructional feedback, support for learner autonomy, and encouragement of reflection; (v) D – Instructional Design and Accessibility: evaluate graphical adequacy, language use, and accessibility for different audiences and contexts.

Three women participated in the evaluation. Regarding educational background, one evaluator completed undergraduate studies, another is pursuing higher education, and the third is a doctoral student. Before the activity, they received introductory training on DEG and HE, enabling them to analyze the DEG in a guided manner. The research question that guided the evaluation was: “Does Jogando para o Amanhã present relevant characteristics to support the teaching and learning of basic programming notions for refugee girls in middle school (ages 12 to 14) and stimulate interest in Computing?”

To conduct the evaluation, the following instruments were used: the DEG itself, a participant profile form, a game exploration guide, a form containing the AHJED heuristics, and a report template for logging issues.

Although DEGs are promising teaching tools, they often face usability challenges and player experience. The evaluators identified issues ranging from aesthetic aspects to more complex gameplay difficulties. For instance, the lack of supporting materials and a well-contextualized narrative compromised understanding of the plot and objectives. A critical issue was the inconsistency in control mechanisms: while most interactions occur via keyboard, at one moment, the mouse is required to activate a lever without prior

notice. This unexpected change caused confusion and frustration, particularly among players with limited familiarity with DEGs, compromising the experience flow.

Despite these limitations, the evaluation also revealed positive aspects of representativeness. The evaluators highlighted the game’s visual design, color palette, scenery, and character representation. These elements were seen as welcoming, appealing, and culturally sensitive, promoting identification and engagement among refugee girls. The content’s relevance and the adequacy of the examples reinforced the DEG’s potential as an inclusive and motivating tool for bringing this audience closer to Computing.

Table 2 summarizes the results obtained. The first column lists the AHJED heuristic identifiers used to classify the problems. The second column presents the severity level assigned by the evaluators according to the impact on gameplay and learning. The third column describes the identified problems, while the fourth proposes possible solutions. Finally, the last column shows the percentage of evaluators who identified each problem.

Table 2. Problems identified through HE.

|ID|Sev.|Problem Description|Possible Solution|%|
|---|---|---|---|---|
|AE2|4|Lack of feedback|Provide feedback for each activity|100|
|AE4|3|Does not show the result|Celebrate each correct action or provide feedback|66|
|CN1|3|No execution flow|Improve execution flow|33|
|CN2|3|Few instructional materials|Include basic reference points|66|
|CN3|3|Lack of help elements|Include attractive help elements|100|
|CN5|3|No phases|Divide into stages|100|
|ED3|3|No different levels|Create learning levels|66|
|ED4|3|No progress indicator|Implement a progress indicator|66|
|ED5|3|No level adjustment|Implement difficulty adjustment|100|
|ED6|3|The game does not adapt to player performance|Adapt phases to successes and errors|100|
|ED7|3|No personalization|Allow users to edit information|100|
|ED8|3|No history of previous actions|Allow users to view previous actions|100|
|HJ1|3|Lack of game contextualization|Add animated prologue/story|33|
|IN1|3|No location indicator|Indicate on-screen location|33|
|IN4|3|NNo initial hints in the room|Allow hints to be viewed at any time|33|
|IN5|3|No hints on how to execute tasks|Provide task execution hints|66|
|IN6|3|Difficulty performing tasks|Provide task execution hints|66|
|IN8|3|No information about errors|Provide error hints and possible solutions|66|
|JG1|3|What to do when starting the game|Show a story|66|
|JG2|3|No start button|Implement start button and login|100|
|JG3|3|No save option|Implement save/pause button|100|
|JG4|3|Does not show task result|Provide feedback to users|100|
|JG5|3|Nopositive reinforcement|Implementpositive reinforcement for errors|100|

AE - educational agent, CN - content, ED - educational elements, HJ - game story, IN - interface, JG - gameplay

In future versions, visual elements and contextual hints will be added to signal changes in interaction modes, increasing predictability and ensuring continuity in the user experience. Narrative contextualization will also be expanded, and complementary materials will be made available to strengthen support for the learning process.

### 5.2. Cognitive Walkthrough

The cognitive walkthrough is a usability inspection method focused on evaluating design in terms of ease of use [Wharton et al. 1994]. We used to verify whether a novice user can learn to use the DEG by exploring the interface without external guidance. The method includes: (i) preparation: user identification, task definition, and action sequence; (ii) data collection and analysis: exploration of predefined tasks while answering the four questions in Table 3; (iii) results consolidation: synthesis of findings and improvement suggestions; and (iv) results reporting: documentation of problems and solutions.

Three specialists participated in the evaluation: two university professors in Computing and one master’s student working on educational games. They were selected for

#### Table 3. Traditional questions used in the cognitive walkthrough

Description of the Questions

- (Q1) Would the user try to achieve the correct effect?

- (Q2) Would the user notice that the correct action is available?

- (Q3) Would the user be able to associate the correct action with the intended effect?

<u>(Q4) If the correct action were performed, would the user perceive progress toward task completion?</u>

their experience in Computing and game development, enabling them to conduct critical analysis of usability aspects and to adhere to the DEG proposal. The evaluation used an online form containing the four original cognitive walkthrough questions (Table 3).

The results were summarized in Table 4 to facilitate comparison. The table presents the level of agreement of each evaluator (Yes, Partial, No), allowing visualization of divergences across phases. This supports objective analysis of the data and identification of satisfactory or problematic DEG aspects.

Table 4. Summary of CW results

|Task|Evaluator|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
||Evaluator 1|Yes|Partial|Yes|Yes|
|Phase 1|Evaluator 2|Yes|No|Yes|No|
||Evaluator 3|Partial|Yes|Yes|Yes|
||Evaluator 1|Yes|Yes|Yes|Yes|
|Phase 2|Evaluator 2|Yes|No|Yes|Yes|
||Evaluator 3|Yes|Yes|Partial|Yes|
||Evaluator 1|Yes|Partial|Yes|Yes|
|Phase 3|Evaluator 2|No|No|No|No|
||Evaluator 3|Yes|Yes|Partial|Yes|
||Evaluator 1|Yes|Yes|Yes|Yes|
|Phase 4|Evaluator 2|Yes|Yes|Yes|Yes|
||Evaluator 3|Yes|Yes|Yes|Yes|

The evaluation identified issues ranging from aesthetic aspects to more complex gameplay difficulties. In Phase 1, although two evaluators completed the walkthrough, partial and negative responses revealed difficulties predicting the effects of actions. Evaluators highlighted issues with the use of levers, indicating that this resource is unnecessary for task execution and that it causes confusion among users, compromising usability.

In Phase 2, greater divergence among evaluators indicated the need for clearer instructions. The main complaint was the excessive amount of information, which hindered understanding of the storyline and objectives. Phase 3 showed the worst performance, with all evaluators reporting difficulties; therefore, it was considered the most challenging phase, requiring technical adjustments and simplification of actions. Phase 4 achieved the best performance, indicating that specialists understood the tasks. However, it was criticized for emphasizing Portuguese-language elements over logic, thereby partially diverting from the experience’s core educational objective. Despite these limitations, the evaluation revealed improvements compared to the HE. Evaluators highlighted the game’s design, narrative, and pedagogical proposal. The content was considered appropriate for the target age group and aligned with CT education principles. The addition of visual hints and guidance improved DEG fluency and reduced confusion. Narrative elements also strengthened identification and engagement, improving gameplay.

However, evaluators noted the need to provide support materials and tutorials to

help the target audience perform the activities effectively. The relevance of the content and the results obtained reinforced the potential of the DEG as a motivating, inclusive tool that can bring this audience closer to the field of Computing.

## 6. Threats to Validity

The validity of the results must be considered throughout the study design to ensure that the evidence represents the population of interest [Wharton et al. 1994]. In this work, the analysis focused on threats to external validity, particularly the possibility of generalizing the findings to contexts different from those in which the study was conducted.

In the case of the DEG Jogando para o Amanhã, external validity may be affected by difficulties in reaching the target audience, language barriers, and practical constraints in school environments. Direct contact with refugee girls can be limited due to integration challenges and the social vulnerability of this population. To mitigate this issue, the project relies on partnerships with the Cátedra Sérgio Vieira de Mello at the Federal University of Juiz de Fora and the Municipal Secretariat of Juiz de Fora, which facilitate access to public schools where the activities can be conducted.

Another limitation is language barriers, as many refugee girls speak Spanish as their mother tongue. To reduce this impact, we adopt simplified language, visual glossaries, and tutorials, and future versions are expected to include Spanish and English versions. Finally, integrating the DEG into school environments may impose technical and pedagogical constraints. To address this issue, we provide support materials for players and plans to develop instructional resources for teachers to support classroom use.

## 7. Final Considerations

The global scenario of forced displacement and gender inequality highlights the need for actions that promote social inclusion through education. In this context, the project Jogando para o Amanhã seeks to transform Computing into an accessible and welcoming learning opportunity for refugee girls. Thus, this work presented the stages of conception and development of a DEG for teaching programming to girls aged 12 to 14. The proposal was grounded in updated curricular guidelines, accessibility strategies, and a culturally representative narrative. In particular, the work described a HE that revealed important limitations, which were subsequently addressed, indicating the DEG’s potential as a motivating and inclusive tool. It is worth noting that the DEG is in a refinement phase, incorporating improvements suggested during the cognitive walkthrough evaluation. The next steps involve its application in public schools that serve refugee girls, followed by an experimental study to assess its effectiveness in teaching programming and stimulating interest in Computing.

Jogando para o Amanhã already includes support materials for players and, as future work, aims to develop specific instructional materials for teachers, expanding classroom use possibilities. Another expansion perspective is a Spanish version, considering the relevance of this adaptation for the Venezuelan refugee girls’ population. As a tool, contributes a culturally sensitive, lightweight DEG designed to support introductory programming for refugee girls. It is also worth noting that by promoting digital inclusion for a historically marginalized audience, the project Jogando para o Amanhã reaffirms the transformative potential of Computing in social and educational contexts, contributing to achieving the SDGs through sustainable and inclusive technological solutions.

### Use of Artificial Intelligence

To support linguistic revision, grammatical correction, and the adaptation of this work to academic standards, generative AI tools such as ChatGPT and Gemini were used. These tools were employed exclusively as auxiliary support for text revision, clarity, and language improvement. They were not used for data collection, analysis, or decision-making; these processes were entirely carried out by the authors. Therefore, the use of AI does not affect the scientific content or the article’s contributions.
