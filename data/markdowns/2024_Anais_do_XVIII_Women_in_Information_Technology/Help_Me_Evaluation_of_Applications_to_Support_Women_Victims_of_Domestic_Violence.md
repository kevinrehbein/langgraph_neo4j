# Help Me: Evaluation of Applications to Support Women Victims of Domestic Violence

Cynthya Letícia Teles de Oliveira, Isadora Garcia Ferrão

> 1University of São Paulo (USP) – Ave. Trab. São Carlense, 400 – Parque Arnold Schimidt, São Carlos – SP, 13566-590

> 2Federal Institute of São Paulo (IFSP) – St. Doutor Aldo Benedito Pierri, 250 Jardim Paulo Freire, Araraquara – SP, 14804-296

cynthya@usp.br, isadoraferrao@usp.br

Abstract. Brazil, the fifth country with the most cases of femicide in the world, faces challenges both in its culture and in its public policies about supporting women who are victims of domestic violence. There are assistance programs, such as granting protective measures to ensure a minimum distance between the aggressor and the victim. Thus, different complementary initiatives emerged, such as applications that allow reporting incidents of violence and support for access. In this sense, this article proposes a technical evaluation of the five most popular brazilian applications on the Play Store dedicated to combating gender-based violence, considering technical metrics of usability and security.

## 1. Introduction

During the first year of the pandemic, every minute, eight women were victims of aggression in Brazil. During this same period, 2.1 million were threatened with knives or firearms, and 1.6 million were beaten or subjected to attempted strangulation [Bitencourt et al. 2021]. Additionally, according to data from the Brazilian Forum of Public Security (FBSP), cases of domestic violence continue to increase year after year [de Avila 2018]. Amidst this scenario, protective measures emerge as an essential strategy to remove battered women from their aggressors, aiming to protect and ensure the safety of the victims.

Different initiatives have been fundamental in combating violence against women, such as the Maria da Penha Law [Pasinato 2016], the creation of shelter homes, and the implementation of awareness campaigns. The Maria da Penha Law, in particular, plays a vital role in the Brazilian context by establishing protective measures for women experiencing violence. These measures include removing the aggressor from the home and prohibiting contact with the victim, as well as the creation of specialized courts and shelter homes to provide support to women in vulnerable situations. However, despite advancements, many women still face barriers to reporting cases of domestic violence. In this context, mobile applications emerge as an important additional tool in combating gender-based violence, offering a discreet and accessible way for women to report abuse, access information about their rights, and find support and assistance.

Reporting apps are mobile platforms developed to simplify the process of reporting cases of domestic and gender-based violence [Buehlow 2023, Adams et al. 2021,

Dragiewicz et al. 2018]. They provide an interface for victims or witnesses to communicate incidents of violence to the relevant authorities and seek assistance and support. Through these apps, victims can give details on the incident, such as date, time, location, and description of events. Additionally, they can attach photos, videos, or other evidence that may assist in investigating the case. Many apps use GPS technology to record the exact location of an incident, which is crucial for ensuring a rapid response from authorities. Additionally, some apps offer the functionality to send emergency alerts to trusted contacts or authorities in imminent danger.

When using a reporting app, it is crucial to recognize that victims may be in high vulnerability and stressful situations. Therefore, the app’s effectiveness depends on its ability to offer support quickly, easily, and safely. In this context, usability is essential to ensure that victims can use the app intuitively. A clear and user-friendly interface, accompanied by simple instructions and accessible navigation options, allows victims to report the incident quickly and accurately, minimizing any confusion or technical difficulty that may arise. Additionally, information security is a fundamental aspect of protecting the privacy and confidentiality of victims. Apps should implement robust security measures to protect the information victims provide against unauthorized access or leakage. This includes using encryption and advanced security protocols to protect transmitted data and adopting clear privacy policies and data protection measures.

Any failure in usability or security can impair victims’ ability to seek help and protection, putting them at greater risk. To the best of the authors’ knowledge, no studies specifically focused on the technical evaluation of usability and security of these apps, with most focusing on proposing new apps or functionalities. Therefore, this article proposes a technical review of the five most popular apps on the Play Store dedicated to combating gender-based violence. The analysis will focus on the highest-rated and most downloaded apps, emphasizing usability and information security criteria. The aim is to ensure these tools are effective and reliable in protecting victims.

This text is organized as follows. Section 2 presents the related works. Section 3 presents the methodology, including the stages for the development of this study. Section 4 presents the results of the usability technical evaluation. Section 5 presents the results of the security evaluation, Section 6 presents the discussion, and Section 7 presents the conclusions.

## 2. Related Work

Given the importance of the subject addressed, we could note a certain number of systematic reviews carried out in recent years. [Eisenhut et al. 2020] searched for apps on women’s safety about domestic violence from all world regions with more than 100 downloads and included 171 apps in the systematic review. The selected applications were classified into five categories: emergency, prevention, education, communication, construction of evidence, and support applications. Of these, 46.78% consisted of emergency apps, followed by education, notification and evidence building, support and prevention apps in descending order. The authors point out the need to develop preventive measures.

[Sumra et al. 2023] analyzed 136 applications on the Google Play and App Store (iOS) for women’s safety. They found that there were five categories of applications: emergency care (44.9%), prevention (21.3%), informational (3%), legal information

(7.4%), and self-assessment (5.1%). More than half of the apps (71%) were launched between 2020 and 2022. About half were from Northeast America (46.3%). Where emergency alerts existed, they required activation by the potential victim without any automatic activation. The authors indicate that current applications have many limitations and suggest that future applications should focus on automation, apply artificial intelligence and multimedia (voice, video, image capture, text, and sentiment analysis), speech recognition, and pitch detection to assist in live situation analysis and accurate generation of emergency alerts.

[Doria et al. 2021] identified that victims of sexualized violence are in a unique position to provide information to app creators about their specific priorities and needs, which can potentially change the way women use app technology for their security. Overall, the literature reviewed in this study concluded that security apps are a complete private resource for support, information, and emergency planning that are useful and easy to use. Furthermore, women believed that sexualized violence safety apps had the potential to reduce the overall risk of experiencing sexualized violence, which is not valid.

Regarding usability evaluation, [Sarkar et al. 2023] investigated the effectiveness of SOS applications in supporting victims of domestic violence, specifically examining the activation process through the visual user interface (UI) and physical UI. The authors noted that although there were no significant behavioral differences, participants expressed greater satisfaction and perceived effectiveness with the physical UI.

## 3. Methodology

This study was conducted in five distinct stages. Firstly, the (1) Selection of criteria for choosing the apps was performed. Next, the (2) Evaluation criteria to be considered were defined. In the third stage, the (3) Selection of the apps to be analyzed was carried out. Subsequently, the selected apps underwent (4) Testing to evaluate their usability and security. Finally, the results were compiled and used in the (5) Writing of the technical evaluation.

### 3.1. Selection of criteria for choosing the apps

Two main criteria were considered when selecting the apps to be evaluated: number of downloads and rating on the Play Store. These criteria were chosen because they are reliable indicators of popularity and perceived quality by users. The number of downloads reflects the public’s acceptance of the app, while the rating on the Play Store indicates users’ satisfaction with their user experience.

### 3.2. Evaluation criteria

The evaluation of the apps dedicated to combating gender-based violence in this study was primarily based on two fundamental criteria: usability and security.

### 3.2.1. Usability

Usability aimed to analyze the ease with which users can interact with the application. This included aspects such as the intuitiveness of the interface, the clarity of the instructions, the ease of navigation, and the efficiency in carrying out tasks such as making

a report or requesting help. To carry out the usability assessment, we used MATCH [Krone 2013], a tool in the form of a checklist based on heuristics to evaluate the usability of smartphone applications. MATCH was created by adapting Nielsen’s heuristics [Nielsen and Molich 1990]. It has 48 questions, and each has three answer options: yes, no, and not applicable.

The checklist classifies the app’s usability into five levels: very low usability (below 30 points), low usability (between 30 and 40 points), reasonable usability (between 40 and 50 points), high usability (between 50 and 60 points) and very high usability (above 60 points).

### 3.2.2. Security

Regarding security, the following criteria were considered: minimal user permission requests, ensuring that the app does not require more access than necessary for its functionality, the presence of a secure connection (HTTPS) for communication with servers, the presence of password and biometric authentication for access, the presence of easily accessible and understandable privacy policies, and compliance with data protection regulations, such as the General Data Protection Law (LGPD). Additionally, a brute force test was conducted on the apps. This test involved repeated attempts of unauthorized access to the system using random combinations of login and password to identify possible vulnerabilities related to authentication. This test aimed to verify if the system can detect and respond appropriately to unauthorized access attempts, thus ensuring the security of users’ information.

Additionally, we conduct brute force tests and assess the apps’ resistance to potential attacks of this nature. This test involved repeated attempts to access the apps using random combinations of login and password. The main objective was to identify potential vulnerabilities related to authentication and verify if the apps can detect and respond appropriately to these unauthorized access attempts. It is worth mentioning that emails were sent to the platform’s developers to alert them of the tests that would be carried out.

### 3.3. Selection of the apps

The five selected apps for evaluation were SP Mulher (+500 downloads), Rede Mulher (+10.000 downloads), Mulher Segura (+10.000 downloads), Salve Mulher (+1.000 downloads), and SOS Maria da Penha (+1.000 downloads).

### 3.3.1. SP Mulher

The SP Mulher is a public utility system primarily used by women in risk situations. The application allows for filing a police report, which the women’s police station will analyze. Women who have protective measures can send an emergency request through SP Mulher in case of any risk to their physical and/or psychological integrity. The police will use the victim’s location information to improve response to a potential incident.

### 3.3.2. Rede Mulher

The Rede Mulher app allows women who are victims of domestic violence to request help from the military police, register a protection network of friends and family, quickly access the occurrence registration service of the civil police, register a request for a protective measure, and access information about the entire network of protection for women in the State of Rio de Janeiro.

### 3.3.3. Mulher Segura

The Mulher Segura app allows women in Goiás direct access to public safety services. It provides the location and phone numbers of nearby battalions and police stations. It enables the registration of occurrences directly with the military police through communication with the attendant and patrol via chat. In addition to these functionalities, the tool offers access to services that bring the Government closer to the citizens.

### 3.4. Salve Mulher

Salve Mulher is an app from the Civil Police of the State of Tocantins, victims of aggression can make reports or request protective measures directly from their cell phones. Salve Mulher provides different services for women who are victims of domestic violence, allowing them to find information about the types of violence, such as physical, psychological, and financial. Through the application, women can clarify doubts about these types of violence and understand how each of them works. Additionally, it’s also possible to make reports, including anonymously, and expedite protective measure processes. Another essential tool available is the panic button. Women can activate it with a protective measure in case of its violation. When activated, the woman has direct contact with the Maria da Penha patrol of the Military Police, which will take the appropriate measures at that moment.

### 3.5. SOS Maria da Penha

The SOS Maria da Penha app is a tool designed to assist women in situations of domestic violence, with the primary objective of providing support and resources quickly and efficiently. Victims can access different functionalities, such as an emergency button, which instantly activates a security team, such as the police, with just one touch. Additionally, the app provides information about the Maria da Penha Law, which protects the rights of women victims of violence. Another essential feature is the ability to find nearby support networks. The app uses the user’s location to provide a list of available resources nearby, including safe shelters, counseling services, and specialized legal assistance.

### 3.6. Tests

During this stage, tests were effectively conducted in practice, employing the predefined criteria to assess the applications’ usability and security. Both tests were conducted on the Android operating system.

### 3.6.1. Usability

To carry out this analysis, we used a Samsung Galaxy S23 Ultra smartphone with an Android operating system, Snapdragon 8 Gen 2 Qualcomm SM8550-AC processor, 12 GB of RAM, a 6.8-inch screen, 3088x1440 pixel resolution, and dark mode configuration.

### 3.6.2. Security

For manual testing, we used a Samsung Galaxy S22 Ultra smartphone equipped with an Exynos 2200 or Qualcomm Snapdragon 8 Gen 1 processor, 16 GB of RAM, and 512 GB of internal storage.

For automated testing, we utilized the OWASP ZAP (Zed Attack Proxy), developed by the Open Web Application Security Project (OWASP), to conduct brute force tests and assess the apps’ resistance to potential attacks of this nature. This test involved repeated attempts to access the apps using random login and password combinations. The main objective was to identify potential vulnerabilities related to authentication and verify if the apps can detect and respond appropriately to these unauthorized access attempts.

### 3.7. Writing of the technical evaluation

At this stage, all applications were evaluated according to the definitions mentioned earlier. The following sections analyze the results obtained after the technical evaluation of usability and security.

## 4. Usability Evaluation

This section presents the results obtained based on our observation and the score obtained with MATCH. We do not finalize any report, request protective measures, or request help, as false reporting of a crime or misdemeanor is a crime under Brazilian law.

### 4.1. SP Mulher

When opening the application, we see three buttons.In the first, it is possible to register a Police Report with the Civil Police; the second button reads ”ask for help,”and the last gives the option to activate the location. When trying to register a police report, we see two buttons with the option ”yes”and ”no”.However, a question above the buttons indicates that the function is only for victims and asks for the user’s confirmation to proceed that, with the phone in dark mode, it’s almost impossible to read. Below the buttons is an information box with some text that cannot be read. When we continue filling out the form, some options are shown in the app, and at this stage, we notice problems viewing the questions on the form.

When we returned to the application’s home screen, this time, we clicked on the ”call for help”(SOS) button, and the application presented a message that no protective measure was registered. That is, the button only works for previously registered cases and with a minimum distance between the attacker and victim established by the judge.

The app obtained a score of 44.4 points in MATCH, being classified as reasonable usability, which means, according to the MATCH authors’ explanation, ”they offer

intuitive navigation and an aesthetically simple and clear menu, contain short titles and labels, have fonts, spacing between lines and alignment that favor reading, highlight more important content, have simple tasks to perform that make it clear what your next step is, offer immediate and adequate feedback on their status with each user action”.

### 4.2. Rede Mulher

In this application, we have some functions besides calling for help. We see the app’s home screen and its main functionalities (in Brazilian Portuguese); there, we find the option to find specialized support centers for victims of domestic violence; when clicked, the phone numbers and addresses of the centers are displayed. It is also possible to access the police station’s services online, which go beyond services for victims of domestic violence. On the home page, there is also the option to request a protective measure, which will be analyzed by the Civil Police and forwarded to a judge. Another option is called ”emergency guardians”, where the app user can register phone numbers of family and friends to be notified in cases of emergency.

Still, on the home page, there is a menu located at the bottom of the screen where you can see calls made through the app, create a report and call a vehicle, check emergency numbers (such as 190, the Military Police number in Brazil) and finally, it is possible to view the support network for victims. When we click on the megaphone icon, a map and a text box are displayed for the user to enter the address, and then the user must inform the type of violence suffered (physical, psychological, moral, sexual, and property) and information that helps in screening the complaint and identifying suspects during the police approach.The last option on the menu, ”support network,”shows a map with places that can support the user. However, this function is difficult to use, as the map pin starts in the middle of the ocean, and we had difficulty finding Brazil.

In the user profile section, it is possible to activate camouflaged mode, where the application keeps the name but changes the icon to lipstick and logs out of the session. Despite being extremely relevant and necessary, the application does not work correctly in this mode, crashing and often not opening. We reinforce that we conducted these analyses on a state-of-the-art smartphone with great configuration. The app achieved 47.5 points in the MATCH evaluation and was classified as reasonable usability.

### 4.3. Mulher Segura

The application has each button in a different color, but this does not affect usability. However, the buttons do not use icons but text, which impairs usability. The application was classified with high usability, with 56 points, which means that, in addition to the characteristics of applications with reasonable usability, they ”display small amounts of information on each screen, maintain menus and common functions of the application on all screens, show the number of steps required to perform a task, allow the user to cancel an action in progress.”

### 4.4. Salve Mulher

The Salve Mulher app has a large amount of information for users. However, the home page is divided into two and requires vertical scrolling; even the report button is on the secondary page. The buttons on the home page do not have markings, shadows, or any indication that they are buttons.

The videos on the app direct you to the app store even if the YouTube app has already been downloaded to your phone. In the tests we carried out, we were unable to access the videos because when we opened the application through the app store, it started other videos with standard topics recommended for the user. Salve Mulher obtained 59.8 points in the MATCH evaluation, with reasonable usability.

### 4.5. SOS Maria da Penha

This last application did not allow us to perform many tasks, as it only allows specific uses in places where they actually work (places that purchased the app). In addition, the application had many crashes. The application has reasonable usability, with 48.9 points.

## 5. Security Assessment

The SP Mulher app presents a partially practical approach regarding the privacy and security of its users. Although it only requests the minimum necessary permissions, such as access to phone and email data, its method requires users to re-enter all information when making a report, including sensitive details like name, document, and RG number, which raises concerns. This practice may be considered excessive and unnecessary, going beyond essential permissions for the application’s functionality, compromising convenience, and potentially discouraging users from using the service.

Furthermore, although the application uses HTTPS for all communications with servers and offers clear privacy policies, the lack of support for biometric authentication represents a gap. Implementing this functionality could provide an additional layer of protection, especially considering the sensitive nature of the data handled by the application.

The resilience of the SP Mulher app’s system against unauthorized access attempts, evidenced by its stability after a brute force test, is noteworthy. Hackers often employ this type of test to compromise the security of digital systems, exploiting combinations of login and password until they find the correct one. The fact that the system resisted these attempts suggests that robust security measures have been implemented, making it difficult for intruders to access confidential information or compromise the integrity of the application. Additionally, after the app underwent a brute force test using the OWASP ZAP tool, the system remained stable despite these intrusion attempts.

### 5.1. Rede Mulher

The Women’s Network app’s evaluation reveals several concerns regarding its users’ privacy and security. Firstly, the app requests excessive permissions, going beyond what is necessary for its basic functionality. This practice can increase the risks of exposing users’ data, such as names, email addresses, user IDs, addresses, and phone numbers, which are shared and collected for multiple purposes.

The app does not use HTTPS for communication with its servers, exposing users’ data to potential interceptions and espionage attacks. The absence of biometric authentication for access is also a significant flaw that needs to be highlighted.

Finally, after only 5 seconds of brute force testing, system instability was observed. This result reveals a severe vulnerability in the app’s security infrastructure. This weakness could severely compromise the security of users’ data and put them at risk of privacy violations.

### 5.2. Mulher Segura

The evaluation of the Mulher Segura app reveals some concerning practices. For example, although the app requests only essential permissions for its functionality and uses an HTTPS connection for communication with its servers, there are some security gaps. Firstly, the absence of biometric authentication for access represents a failure in implementing additional security measures. Additionally, although the app provides easily accessible and understandable privacy policies, it is concerning that it may collect sensitive data such as voice or sound recordings, photos, and location information without clearly specifying the purpose of this collection.

The lack of transparency regarding the use of this data and the absence of clear consent options compromise users’ privacy and raise ethical questions about using personal information. While it is positive that data is encrypted in transit, the app must adopt comprehensive measures to ensure user data’s protection and privacy at all processing stages. Finally, it is important to mention that the app demonstrated stability during the brute force test.

### 5.3. Salve Mulher

The Salve Mulher app takes a positive approach to protecting user privacy by limiting permission requests to the essentials for its functionality, avoiding unnecessary access to personal data. Additionally, it adopts an HTTPS connection for communication with servers. However, like the previous apps, it does not implement biometric authentication.

As stated by the developer, this app does not share user data with third parties. However, the collection of personal information such as email address, address, and phone number, along with the option to capture photos, videos, files, and documents, raises concerns about the extent of data collection and its potential use. Finally, the app remained stable after brute force testing.

### 5.4. SOS Maria da Penha

The SOS Maria da Penha app presents a series of issues related to the privacy and security of its users that deserve attention. Although it requests only the minimum necessary permissions, such as access to name, email address, and phone number, the sharing of data with third parties and the collection of a variety of personal information, such as app activities, photos, videos, files, and documents, are concerning. Additionally, there is a lack of transparency regarding how this data is used and shared.

Furthermore, the app uses an HTTPS connection to communicate with servers. However, there is a lack of biometric authentication. The app became unstable after a short period, precisely 34 seconds, regarding the brute force test. This suggests that the app may not be able to handle unauthorized access attempts effectively.

## 6. Discussion

When we analyzed the applications, we saw that we must pay attention to contexts in addition to practical and technical issues. In this study, we could not conduct studies with users in the context of use to better understand usability. However, even with studies on smartphone users, we still cannot evaluate it in an authentic context.

A situation of domestic violence can result in a risk to the victim’s life. A problem of this type must trigger reactions and nervousness, in addition to the impossibility of the victim needing to spend enough time with the device to carry out several steps to complete a report. In other cases, the victim may have children who are still young without the necessary knowledge to be able to perform the task of asking for help.

In the evaluation we carried out, we found that it is impossible to read with the cell phone in dark mode (SP Mulher). The Rede Mulher app, the only one with a camouflage option, does not work correctly when this function is activated. The Mulher Segura application, with high usability according to heuristic evaluation, has buttons containing only text. This approach makes it difficult for illiterate people to use the application. Although very good, some functions were not designed for emergencies, such as the Salve Mulher application, which even depends on other applications to display part of its content, in addition to the fact that the buttons do not refer to buttons. Finally, the SOS Maria da Penha app has an emergency button, which takes its name from the most important Brazilian law protecting domestic violence. Still, it only works (theoretically) in regions that have purchased the app.

In addition to having seen the need for an emergency button, which activates the cell phone’s location (with prior authorization) and directs a police vehicle to the area, we believe that a process of unification or sharing between platforms is necessary because, in the way that They work today, each application works in a tiny region, generally limited to one State of the Federation, which would make it challenging to request help in the event of a trip or move.

The main problem identified in the security analysis of the applications is the lack of prioritization and implementation of sophisticated and modern security measures, such as integrating biometric authentication and applying data encryption in some apps. This can be concerning, especially in applications that handle sensitive issues such as women’s protection. Additionally, the absence of these measures leaves the applications vulnerable to various cyber threats, including unauthorized access and leakage of personal information. This lack of security concern could undermine users’ trust in the applications and jeopardize the privacy and security of those who rely on them for support and assistance. Therefore, the developers of these applications must recognize the importance of prioritizing security from the outset of development and implementing sophisticated protection measures.

## 7. Final Remarks

This work presented a usability and security assessment of the five most downloaded women’s safety apps on the Google Play Store in Brazil. We saw that despite being useful, applications can still improve and one way to do this is by listening to the target audience: women survivors of domestic violence.

The main limitation of this work was not having carried out a case study with users. In future work, we intend to conduct studies with users, collect requirements from victims of violence, consider integrating police operation centers throughout Brazil, and develop safer models for these systems.
