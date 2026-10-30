# Bridging the Gap: A Data-Driven Analysis of How Traditional Software Engineering Productivity Metrics Overlook Women’s Performance

Lorena M. V. Seabra, Pamela T. L. Bezerra

1Centro de Estudos e Sistemas Avançados do Recife - CESAR School Avenida Cais do Apolo, n 77 – Recife – PE – Brazil

{ lmvs,ptlb } @cesar.school

Abstract. Traditional productivity metrics in software engineering, such as lines of code, commits, and task duration, often fail to capture essential subjective factors like collaboration and well-being. This gap disproportionately affects women, who face additional challenges including gender bias, microaggressions, and double workload. Based on a survey with 85 female software engineers in Brazil, this study analyzes how these challenges impact performance and reveals that conventional metrics undervalue women’s contributions. The findings highlight the need for a more inclusive framework that recognizes both technical and non-technical work.

Abstract. A produtividade em engenharia de software é geralmente medida por métricas como linhas de código, commits e tempo de execução de tarefas, mas essas métricas ignoram fatores subjetivos importantes, como colaboração e bem-estar. Isso afeta especialmente mulheres, que enfrentam vieses de gênero, microagressões e dupla jornada. Com base em uma pesquisa com 85 engenheiras de software no Brasil, este estudo mostra como esses desafios impactam o desempenho feminino e aponta que as métricas tradicionais não valorizam adequadamente suas contribuições. Os resultados reforçam a necessidade de um modelo mais inclusivo que reconheça tanto aspectos técnicos quanto não técnicos.

## 1. Introduction

Traditional metrics in software engineering (SE), such as lines of code (LOC), commit frequency, and task completion time, remain widely used to assess productivity [McConnell 2004]. However, such quantitative indicators often fail to reflect essential qualitative aspects like collaboration, creativity, and problem-solving, which are crucial to successful software development [Ford et al. 2017, Murphy-Hill et al. 2014, Storey et al. 2017].

Research also highlights the positive impact of gender diversity on team performance, innovation, and communication in SE [Rodríguez-Pérez et al. 2021, Rosser 2005, Williams et al. 2016, Storey et al. 2017]. Inclusive teams tend to demonstrate higher collective intelligence and better outcomes. Yet, despite these benefits, women remain underrepresented, occupying only 26% of computing-related roles in 2023 [for Women & Information Technology (NCWIT) 2023], and continue to face systemic barriers such as biased evaluations, reduced access to technical leadership,

and assignment to undervalued tasks [Gino and Coffman 2021, Wynn and Correll 2018, Rodríguez-Pérez et al. 2021]. These challenges are compounded by unequal domestic responsibilities [Roth and Green 2021, Williams et al. 2016] and physiological factors rarely considered in traditional assessments.

As a result, current productivity measures offer a narrow and often distorted view of performance, failing to capture the full scope of women’s contributions. By prioritizing output volume over the quality of collaboration, mentoring, emotional labor, and other invisible yet crucial activities, these frameworks not only undervalue key aspects of team success but also contribute to the invisibility of women’s work, perpetuating structural inequalities in recognition, career progression, and leadership opportunities.

Given this context, this study addresses this gap between metrics and contribution through a quantitative analysis of how conventional productivity metrics neglect gender-specific experiences and contributions. The research is based on a survey of 85 female software engineers across Brazil, collected via social media and professional networks. The instrument comprises 32 structured questions on productivity perception, gender bias, recognition, microaggressions, work-life balance, and physiological aspects. The goal is to reveal how existing metrics overlook collaborative and cognitive work, and to support the design of more equitable evaluation frameworks. This paper is structured as follows: Section 2 explores productivity factors in SE; Section 3 examines gender disparities; Section 4 details the methodology and results; and Section 5 presents conclusions and future directions.

## 2. Software Engineering Productivity Factors

### 2.1. Traditional Productivity Metrics in Software Engineering

In software engineering (SE), productivity is often measured through quantitative metrics that prioritize tangible outputs over cognitive, collaborative, and creative contributions. Common metrics include Lines of Code (LOC), which counts the number of lines written or modified; Commit Frequency, tracking how often changes are submitted; Sprint Velocity, measuring tasks completed in Agile sprints; and Defect Resolution Rate, assessing bug fixes within a given period.

While these metrics offer some insight, they don’t tell the full story. A high LOC count, for example, may indicate unnecessary verbosity rather than efficiency [McConnell 2004]. Similarly, commit frequency overlooks task complexity; a developer focused on refactoring or solving complex problems may push fewer commits but deliver greater value than one making frequent minor updates [Fenton and Pfleeger 1998]. Sprint velocity, although widely used in Agile environments, fails to consider the varying difficulties of tasks and assumes that all completed work has equal weight in contributing to project success [Cataldo et al. 2008]. Furthermore, research suggests that defect resolution rates can be influenced by external factors such as team collaboration, codebase maturity, and testing automation rather than individual developer effort [Zeller 2005].

These limitations highlight the need for a more nuanced approach to measuring productivity, incorporating qualitative aspects such as problem-solving, knowledgesharing, and maintainability, which are critical for long-term software quality and innovation [Storey et al. 2017, Murphy-Hill et al. 2014].

### 2.2. Challenges in Measuring Subjective Productivity Factors

Unlike industrial work, software development demands strategic thinking and collaboration. Many key contributions, such as mentoring, code reviews, and process improvements, are not directly reflected in the codebase but are vital to team success. Traditional metrics often overlook these qualitative aspects, resulting in incomplete evaluations. Studies recommend incorporating peer feedback and assessing long-term outcomes like team cohesion and reduced technical debt [Roth and Green 2021, Storey et al. 2017].

Research has consistently highlighted the shortcomings of conventional metrics. For example, [Terrell et al. 2017] showed that in open-source environments, contributions like documentation and community support are routinely undervalued. In corporate settings, these limitations disproportionately affect women, who are more likely to be assigned critical yet low-visibility tasks [Williams et al. 2016, Vasilescu et al. 2015]. Other studies show that vital activities such as code review, debugging, and architectural planning are also frequently overlooked in standard assessments [Murphy-Hill et al. 2014, Fenton and Pfleeger 1998].

In summary, traditional metrics fail to capture:

- Knowledge sharing and mentoring – Essential for team growth and knowledge retention, yet often invisible in evaluations.

- Code review and debugging – Crucial for quality and stability, but rarely accounted for.

- Architectural decisions and creative problem-solving – High-impact contributions with long-term value that LOC or commit counts can’t reflect.

- Collaboration and teamwork – Time spent planning, communicating, and aligning is vital but largely ignored by standard measures.

## 3. Women in Software Engineering

### 3.1. Overview of Women in the Technology Sector

Despite ongoing diversity efforts, women remain significantly underrepresented in technology globally. In 2023, women held only 26% of computing-related jobs, a proportion with minimal change over the last decade [for Women & Information Technology (NCWIT) 2023]. The Brazilian context mirrors this trend, with women comprising just 20% of technology professionals in 2022, highlighting persistent structural barriers to career entry and progression [das Empresas de Tecnologia da Informação e Comunicação 2022].

The disparity intensifies in leadership roles: only 13.6% of technology leadership positions in Brazil are occupied by women [na Tecnologia Brasil 2023]. This underrepresentation restricts women’s influence on decision-making and workplace policies, including productivity evaluation methods [Williams et al. 2016]. Additionally, the scarcity of female mentors reduces the visibility of clear career paths and successful role models.

Further illustrating these challenges, the Brazilian Institute of Geography and Statistics reports women represent only 22% of STEM graduates, revealing gender disparities from education through employment [Instituto Brasileiro de Geografia e Estatística (IBGE) 2021]. According to the World

Economic Forum’s Global Gender Gap Report, Brazil ranks 94th among 146 countries in women’s economic participation and opportunities, underscoring the structural barriers hindering women’s advancement in technological fields [World Economic Forum 2023].

### 3.2. Challenges in Productivity and Career Progression

Women in software engineering frequently encounter productivity and career advancement barriers, including biases in performance evaluations, microaggressions, and disproportionate assignments to undervalued tasks. Research indicates women’s technical contributions often go unrecognized or are attributed to male colleagues, while activities like documentation and coordination are disproportionately assigned to them and undervalued [Gino and Coffman 2021].

Common challenges identified by studies include:

- Bias in evaluations: Women receive less specific technical feedback, with achievements often credited to collective team efforts [Gino and Coffman 2021].

- Limited access to high-visibility projects: Assignment to tasks such as documentation and coordination reduces women’s career visibility and progression [Terrell et al. 2017].

- Workplace microaggressions: Frequent interruptions in meetings and code reviews diminish women’s contributions and visibility [Wynn and Correll 2018].

- Double workload: Domestic responsibilities disproportionately affect women’s productivity and professional growth, as Brazilian women spend nearly twice as many hours per week on household tasks compared to men (21.4 hours vs. 11 hours) [Instituto Brasileiro de Geografia e Estatística (IBGE) 2021].

### 3.3. How Current Productivity Metrics Undervalue Women’s Contributions

As previously explained (Section 2.1), SE traditional productivity metrics focus on quantifiable outputs, often ignoring key contributions like mentorship, documentation, collaboration, and sustainable coding—tasks frequently performed by women and undervalued in evaluations [Williams et al. 2016, Gino and Coffman 2021].

This pattern stems from a historical divide between “technical” and “supportive” work. Feminine-coded tasks such as mentoring and emotional support are viewed as auxiliary rather than strategic [Rosser 2005, Rodríguez-Pérez et al. 2021]. As Rosser highlights, societal norms associate care with women and technical authority with men [Rosser 2004]. These stereotypes persist, with women still disproportionately assigned low-visibility, non-promotable tasks [Capitolino et al. 2019].

Research shows that female engineers receive less recognition and face more scrutiny than their male peers, even when delivering equal or superior results [Wynn and Correll 2018, Gino and Coffman 2021]. To address these inequities, productivity frameworks must include qualitative and collaborative factors.

Some examples of factors that are often overlooked by the traditional methods are:

Collaboration and Team Dynamics: Women frequently engage in mentoring, knowledge sharing, and conflict resolution, activities essential for effective team dynamics and successful project outcomes. Nevertheless, these contributions typically remain unrecognized in traditional performance evaluations, exacerbating gender-based career advancement barriers [Terrell et al. 2017].

Long-Term Impact of Work: Conventional metrics prioritize immediate outputs, neglecting essential long-term contributions such as thorough documentation and maintainable code. Women commonly invest substantial effort into these areas, yet such contributions, critical for software sustainability, are routinely undervalued in productivity assessments [Williams et al. 2016].

Leadership and Coordination Efforts: Women often assume informal leadership roles, facilitating effective communication and project alignment within teams. However, these vital coordination efforts rarely translate directly into quantifiable metrics, limiting women’s recognition and opportunities for formal leadership positions [Roth and Green 2021].

## 4. Data Analysis

Given the limitations of traditional SE productivity metrics (Section 2) and the distinct structural and cultural challenges women face in technology (Section 3), this study addresses two research questions:

1. ”What are the limitations of existing productivity metrics in software engineering concerning female developers?”

2. ”What additional factors, based on female developers’ experiences, should be included in productivity measures?”

To answer these questions, this study uses a survey-based methodology to collect firsthand data from female software engineers in Brazil, allowing direct insight into their productivity challenges and experiences. Unlike theoretical reviews, the survey captures real-world perspectives and reveals nuances often absent from the literature. Given the lack of national studies, this Brazilian-focused research complements global discussions with culturally specific insights. The data exposes gaps in traditional metrics and supports more inclusive evaluation models.

Key aspects analyzed include: factors influencing women’s productivity; the effects of gender bias, recognition disparities, and structural barriers; the impact of worklife balance, hormonal cycles, and microaggressions; and how current metrics overlook collaborative and cognitive contributions—providing evidence for broader discussions on gender disparities in software engineering.

### 4.1. Data Collection Process

The survey collected a total of 85 valid responses from female software engineers across Brazil between January 20 and February 27, 2025. It was disseminated through multiple channels, including professional networks, online forums, and women-in-tech communities, leveraging platforms such as LinkedIn, WhatsApp groups, Telegram channels, GitHub, Stack Overflow, and regional tech communities. Participants ranged from junior developers to senior engineers and technical leaders, ensuring diverse professional experiences and geographic representation. This diversity allowed the collection of insights reflecting various professional backgrounds and regional contexts across Brazil.

The survey comprised both multiple-choice (quantitative) and open-ended (qualitative) questions organized into four categories:

- Demographics and Career Background – Information on age, years of experience, and current professional roles.

- Workplace Environment and Bias – Presence and frequency of gender bias, microaggressions, and inclusivity in decision-making processes.

- Productivity Challenges and Performance Evaluation – Methods used to measure productivity and perceptions of contribution recognition.

- Work-Life Balance and External Factors – Impact of double workload, family responsibilities, and physiological factors such as hormonal cycles.

The full list of survey questions is publicly available for verification at: Investigating Female Productivity in Software Engineering.

### 4.2. Quantitative Data Analysis

The quantitative analysis involved descriptive statistics derived from multiple-choice responses. Important findings included recognition disparities, with 68% of respondents feeling their contributions were less recognized compared to male colleagues. Regarding workplace microaggressions, approximately 74% of the participants indicated frequent interruptions during meetings and code reviews, significantly impacting their professional visibility. Responses concerning work-life balance indicated significant challenges, with about 82% of respondents affirming that domestic responsibilities considerably impact their professional productivity. These results highlight the inadequacy of traditional metrics in capturing relevant external productivity factors. A detailed analysis is described in the following sections.

### 4.2.1. Demographics and Career Background

The majority of respondents ( 59.7% ) were between the ages of 20 and 29, reflecting the trend that younger individuals are more likely to enter software engineering careers in Brazil. However, this sample may not fully capture the career progression challenges faced by older women in the field. Only 12% of respondents reported holding leadership positions, reinforcing the well-documented underrepresentation of women in decision-making roles within the software industry (Section 3).

Regarding professional experience, 42.4% had less than 3 years of experience (junior level), 35.3% were mid-level professionals (3–7 years of experience), and 22.3% had over 7 years of experience (senior level and above).

### 4.2.2. Workplace Environment and Bias

A significant portion of respondents ( 38.5% ) reported that their work was not recognized at the same level as that of their male colleagues, despite performing similar tasks. While this percentage represents a considerable portion, it is important to note that the question allowed multiple responses, reflecting different aspects of professional recognition disparities.

Regarding specific challenges in the environment, respondents reported:

- 41.2% experienced interruptions or were dismissed during technical discussions.

- 32.9% were excluded from major technical decisions.

### • 29.4% were assigned less challenging or lower-visibility tasks.

These findings align with research indicating that women in technology face more frequent interruptions in professional settings, which can undermine their authority and perceived technical expertise [Wynn and Correll 2018]. Additionally, it is important to consider the demographic profile of the survey respondents. As the majority were junior or mid-level professionals, some of the reported biases may reflect earlycareer experiences. However, studies suggest that even as women advance professionally, they continue to face systemic challenges, though in different forms, such as reduced access to leadership roles and sponsorship opportunities [Williams et al. 2016, Gino and Coffman 2021]. Together, these patterns reveal how gender biases shape not only the trajectory of career progression but also the ways in which professional performance and productivity are perceived and evaluated in software engineering environments.

### 4.2.3. Productivity Challenges and Performance Evaluation

When asked about the metrics used to assess their productivity, the majority of respondents indicated that their workplaces relied on traditional SE indicators such as Lines of Code (LOC), commit frequency, sprint velocity, and occasionally peer feedback. However, these metrics do not fully capture the range of contributions made by women in the field.

One key observation is that women are disproportionately assigned tasks that do not translate well into traditional productivity metrics. Many respondents reported frequently engaging in mentorship and onboarding activities, as well as contributing significantly to documentation and process improvements.

Despite being critical for the success of software projects, these contributions remain largely invisible in standard evaluation systems, leading to systematic undervaluation of women’s work. Several respondents highlighted that this misalignment affects their career progression, as traditional evaluation frameworks do not adequately recognize or reward these types of contributions. Many emphasized the need for more holistic assessment models that consider the broader impact of an engineer’s work beyond direct code output.

Table 1 shows the mismatch between how companies measure productivity and the tasks women developers most often perform.

Tabela 1. Comparison between evaluation criteria and frequently performed activities by women in software engineering

|Category|Metric or Activity|Percentage (%)|
|---|---|---|
|Evaluation Criteria Used by|Lines of Code (LOC) / Commit Frequency|58.8%|
|Companies|||
||Sprint Velocity|47.1%|
||Peer Feedback(Limited Scope)|35.3%|
|Tasks Frequently Performed by|Mentorship / Onboarding|52.9%|
|Women|||
||Documentation / Process Improvement|48.2%|

### 4.2.4. Work-Life Balance and External Factors

Work-life balance was another major area of concern. When asked about their ability to balance professional and personal responsibilities, respondents rated their satisfaction at an average of 3.78 out of 5, indicating moderate difficulties in managing both spheres. When asked about what factors affect their productivity, key points included:

- Double workload: 54.1% of respondents reported that domestic responsibilities significantly impacted their availability for extra professional development activities (e.g., learning new technologies and participating in conferences).

- Health-related factors: 42.3% indicated that hormonal variations (e.g., menstrual cycle, migraines) occasionally affected their ability to focus or maintain high levels of productivity.

### 4.3. Qualitative Data Analysis

The qualitative analysis consisted of the thematic evaluation of open-ended responses, providing deeper insights into participants’ experiences and perceptions. Respondents consistently indicated that existing productivity metrics inadequately measure crucial activities such as mentoring, documentation quality, and collaboration. Many emphasized the undervaluation of tasks frequently assigned to women, including documentation and project coordination.

These qualitative insights reinforce the need for inclusive productivity metrics that reflect women’s experiences in software engineering. Notably, 64.7% of respondents felt current metrics did not reflect their contributions, highlighting a persistent gap between female engineers’ work and how productivity is traditionally measured [Williams et al. 2016]. While issues like gender bias, task undervaluation, and limited recognition echo prior studies [Terrell et al. 2017, Wynn and Correll 2018, Gino and Coffman 2021], the survey adds new perspectives—especially the impact of double workload from domestic responsibilities and hormonal variations. These underexplored barriers, particularly relevant in the Brazilian context, emphasize the need for culturally and biologically informed evaluation frameworks.

Given that, participants proposed several additional productivity factors currently overlooked, including:

- Mentorship and knowledge sharing – Often cited as essential but rarely measured.

- Emotional labor and team support – Crucial for effective team dynamics but frequently overlooked.

- Quality and sustainability of delivered code – Emphasizing long-term maintainability.

- Physiological impacts – Acknowledging hormonal cycles and their potential effects on productivity.

### 4.4. Summary of Key Findings and Correlations

Several systemic barriers impacting productivity evaluation and career progression emerged from the survey responses. Table 2 summarizes the key findings and correlations obtained.

Tabela 2. Correlations and Key Findings on Gender and Productivity in SE

|Observation|Details|
|---|---|
|Workplace bias and undervaluation|38.5% of respondents reported bias, correlating with 64.7% who felt theirperformance was undervalued.|
|Non-technical task assignment and slower progression|52.9% were frequently assigned to documentation or mentorship, and 43.5% associated these roles with limited advancement.|
|Work-life balance and project exclusion|54.1% cited work-life conflicts, correlating with 32.9% being excluded from high-visibility projects.|
|Metrics limitations|Traditional indicators (LOC, commits, sprint velocity) overlook cognitive and collaborative contributions [Williams et al. 2016,Vasilescu et al. 2015].|
|Undervalued efforts|Tasks like documentation and mentoring, often assigned to women, remain unrecognized [Terrell et al. 2017, Williams et al. 2016].|
|Persistent gender bias|Reports of limited recognition, frequent interruptions, and exclusion from decision-making align with patterns in the literature[Gino and Coffman 2021,Wynn and Correll 2018].|
|Double workload|54.1% reported that household responsibilities limit professional development.|
|Physiological factors|42.3% indicated that hormonal variations affect productivity—an underexplored topic in SE.|

These findings reveal a clear misalignment between traditional productivity metrics and the actual contributions of women in software engineering. Workplace bias, reported by 38.5% of respondents, strongly correlates with feelings of being undervalued, echoing Williams et al. (2016). The frequent assignment to non-technical tasks (52.9%) aligns with studies indicating that such roles reduce visibility and hinder career progression [Terrell et al. 2017].

Exclusion from high-impact projects due to work-life balance challenges (54.1%) reflects how domestic responsibilities disproportionately impact women’s advancement in tech [Roth and Green 2021]. Metrics like LOC and sprint velocity continue to overlook collaborative and cognitive contributions, reinforcing structural bias [Vasilescu et al. 2015]. Reports of interruptions and exclusion from decision-making reaffirm persistent gender biases observed by Gino & Coffman (2021) and Wynn Correll (2018). Additionally, the impact of hormonal cycles, cited by 42.3%, introduces an important yet overlooked dimension to productivity evaluation in SE.

Altogether, these correlations reinforce the urgency of developing inclusive metrics that value both technical and non-technical work, enabling fairer evaluations and more equitable career growth for underrepresented professionals.

## 5. Conclusion and Future Work

This study presents an empirical analysis of the challenges women face in productivity assessment in software engineering. A survey of 85 female engineers in Brazil reveals critical gaps in traditional metrics, especially their inability to capture non-technical contributions such as mentorship, documentation, collaboration, and informal leadership. The findings also expose systemic barriers, including biased evaluations, unequal task allocation, microaggressions, and difficulties with work-life balance. These factors limit

visibility and hinder professional growth. Participants emphasized the need to recognize emotional labor, mentoring, and long-term efforts related to code sustainability, which are frequently overlooked by standard assessments.

This study’s limitations include its self-reported nature and the underrepresentation of senior professionals. To deepen the analysis, future research requires more interviews with female technical leaders to explore additional productivity factors and refine inclusive evaluation models. Expanding the survey to a more diverse audience will also improve the generalizability of findings and support the refinement of proposed metrics through real-world application, contributing to more equitable productivity assessments in software engineering.

For supporting organizations in adopting inclusive evaluation practices, in Table 3, we propose some preliminary guidelines based on the study’s findings. These guidelines are not a final framework but serve as a starting point for organizations seeking to make productivity assessments more inclusive and equitable. Future work should focus on validating these approaches through real-world testing and feedback from diverse technical teams.

Tabela 3. Preliminary Guidelines for Inclusive Productivity Evaluation

|Guideline|Description|
|---|---|
|Incorporate qualitative metrics|Recognize contributions beyond code, including mentoring, documentation,onboarding,and coordination.|
|Enable peer and team feedback|Implement regular feedback loops that capture collaborative and relational work.|
|Diversify performance criteria|Avoid relying solely on LOC, commits, or sprint velocity. Include indicators that account for context and impact.|
|Acknowledge non-promotable tasks|Formally recognize recurring but invisible tasks essential to team success,such as emotional labor and support.|
|Consider work-life dynamics|Factor in flexibility needs, caregiving responsibilities, and physiological aspects when settingexpectations.|
|Foster transparency and co-creation|Develop evaluation frameworks collaboratively to ensure fairness and contextual relevance.|

Ultimately, this discussion aims to drive a cultural shift in how performance is recognized and rewarded, transforming management and evaluation practices across technology companies.
