
 
 
  
MeetIntelli  
  
Project Team: 
 Mr. Muhammad Mehdi
 Mr. Saad Khan 
 
 
 
July 06th, 2025 
 
Declaration of Authorship


We, the undersigned, hereby declare that the project titled MeetIntelli is our original work and has been completed in accordance with the academic standards of SZABIST University under the supervision of Syed Hassan Ali.
We confirm that all sources and references used during the research and development of this project have been properly cited and acknowledged. The content of this report is original and has not been copied or plagiarized from any external source. 
We further declare that this project has not been previously submitted for the award of any degree, diploma, or other qualification at any other university or institution.



Project Description

Developed as a final year project to simplify and improve the general meeting experience via three connected phases: pre-meeting, meeting, and post-meeting, MeetIntelli is an AI-powered intelligent meeting helper. Users can interact with a customized chatbot designed to help prepare for meetings by offering pertinent direction, answering questions, and assisting structure ideas beforehand in the pre-meeting stage. A Chrome extension records the audio, converts it into text in real time, and keeps it in the system for quick reference during the meeting phase. The user may also engage with the chatbot live during the meeting to get recommendations, pose questions, or monitor main topics. During the post-meeting phase, the stored text is used to create a full transcript of the meeting with the added capability of bilingual assistance that lets the user produce the transcript or summary in English or Urdu. Meeting management from MeetIntelli provides a full answer to ensure thorough preparation, real-time assistance, and timely follow-up. 
Acknowledgement

In the name of ALLAH, the Most Beneficent, the Most Merciful - who blessed us with the ability, wisdom, and perseverance to undertake and complete this research project.
We would like to express our heartfelt gratitude to our supervisor, Sir Hassaan Ali, from the Department of Computer Science at SZABIST, for his unwavering support, insightful guidance, and constant encouragement throughout the development of our final year project, MeetIntelli. His expertise and direction were instrumental in helping us stay focused and overcome the challenges we faced during this journey.
We are also deeply thankful to all our respected teachers, whose knowledge and mentorship have laid the foundation of our academic and personal growth. Their guidance has empowered us to approach this project with clarity and confidence.
A special note of appreciation goes to our loving parents and families for their endless prayers, patience, and support. Their belief in us and their constant motivation served as a pillar of strength throughout this journey.
We extend our sincere thanks to SZABIST for providing us with a supportive academic environment and the resources essential to successfully execute this project. The institute’s commitment to innovation and excellence has been a significant influence on our learning experience.
Lastly, we are grateful to everyone who contributed to the development and testing of MeetIntelli, especially those who provided valuable feedback and encouragement, making this project both meaningful and successful.


Introduction

Designed to improve the general meeting experience through smart automation and real-time assistance, MeetIntelli is an artificial intelligence-powered meeting assistant platform. Pre-Meeting, In-Meeting, and Post-Meeting are the three main phases of the system. Users engage with a customized chatbot in the Pre-Meeting phase that offers agenda related direction, responds to questions, and recommends important discussion topics to help with meeting preparation. A Chrome extension captures live audio during the Meeting phase, which is then transcribed into text and kept inside the platform. This stage keeps the chatbot available so it can offer real-time support and engagement. The retained chat is used during the Post-Meeting phase to create a thorough meeting transcript with multilingual output assistance in English and Urdu. Especially for business and academic applications, MeetIntelli is meant to increase meeting effectiveness, guarantee better preparation, boost participation, and simplify follow-up.
Objective

With the goal of increasing productivity and communication, an AI-based assistance platform supporting users before, during, and after meetings by means of customized preparation tools, live meeting assistance, automated audiototext translation, and multilingual transcript generation is developed.
Problem Description

In academic and professional contexts, people sometimes struggle to prepare for meetings, maintain attention during talks, and precisely reflect major outcomes post-meeting. There aren’t coordinated tools providing customized preparation, real-time support, and planned follow-up in a smooth workflow. Conventional notetaking is time-consuming and susceptible to human error. Users also lack easy access to tools offering real-time summaries and linguistic flexibility. MeetIntelli tackles these obstacles by providing a sophisticated, all-inclusive platform that directs participants across every stage of the meeting, records essential information, and produces organized bilingual transcripts. It improves the general quality of meetings, eliminates manual notetaking, and lessens cognitive load.

Feasibility Study
Delays in model training, browser extension compatibility problems, or erroneous transcription in noisy surroundings are among potential dangers. Modular design, failover mechanisms, and intensive testing helped to reduce these risks. Better milestone and bottleneck tracking was made possible by agile methodology.
Resource Requirements:
For strong development, the project called for Figma for UI design, access to Python libraries for NLP and speech processing, Google Chrome APIs and Whisper AI (or equivalent) for speechtotext conversion, firebase or other backend systems for storage and authentication.
Solution Application Areas
MeetIntelli provides actual worth in academic and professional settings with common, time-sensitive, content-rich meetings. The platform simplifies pre-meeting preparation, enhances focus during discussions, and guarantees no important detail is missed post-meeting. It promotes better communication, saves time, and encourages more efficient meetings. Particularly in the Pakistani environment, its bilingual features enhance its usability and accessibility.
Tools/Technology
•	Web Development: Django, FastAPI, Flask
•	Chatbot/NLP: Langchain, Ollama, Meta llama 2.0 7B, Python
•	Speech-to-Text: Speech Recognition
•	UI/UX Design: Figma
•	Browser Extension: JavaScript, Chrome APIs
•	Project Management:  Google Sheets
Expertise of the Team Members
Saad Khan:
•	UI/UX Design and Front-End Development
•	AI Chatbot Integration
•	Documentation
Muhammad Mehdi:
•	Research and development
•	Audio Processing and Text Generation Logic
•	Chrome Extension Development
•	Backend API Design and Integration
•	Fine-Tuning Llama 2 (7B) with LoRA and QLoRA
•	End-to-end system building
Milestones
Phase 1: Requirements Gathering and Planning
1.	Identify core meeting challenges
2.	Analyze functional and non-functional requirements
Phase 2: Design
1.	Design wireframes and UI mockups
2.	Finalize chatbot flow and Chrome extension behavior
Phase 3: Development
1.	Implement pre-meeting chatbot
2.	Develop Chrome extension for in-meeting recording
3.	Integrate audio-to-text conversion pipeline
4.	Enable real-time chatbot use during meetings
5.	Store and structure meeting text
6.	Implement bilingual transcript generation
Phase 4: Testing and QA
1.	Test speech recognition accuracy
2.	UI and usability testing
3.	Bug fixing and performance tuning
Phase 5: Deployment and Feedback
1.	Deploy web app and extension
2.	Collect user feedback
3.	Implement final improvements
Data Flow Diagrams of Multiple phases
Requirements & Planning (P0)
No data flow – planning is internal. Skip for DFD.
Pre-Meeting Phase (P1)
Processes:
•	P1.1: User inputs meeting details
•	P1.2: Chatbot engages with user
•	P1.3: Agenda suggestions and refinement
Data Stores:
•	D1: Meeting Configuration DB
Data Flows:
•	User → (Meeting Info) → P1.1
•	P1.1 → D1 (Store Meeting Info)
•	User ↔ P1.2 (Chatbot Q&A)
•	P1.2 → P1.3 (Context Analysis)
•	P1.3 → D1 (Agenda Recommendations)

 
In-Meeting Phase (P2)
Processes:
•	P2.1: Audio Capture via Chrome Extension
•	P2.2: Speech-to-Text Engine
•	P2.3: Real-time NLP Chatbot
•	P2.4: Engagement Tracking
Data Stores:
•	D2: Meeting Transcript DB
•	D3: User Interaction Logs
Data Flows:
•	Meeting Platform → P2.1 (Audio Stream)
•	P2.1 → P2.2 (Captured Audio)
•	P2.2 → D2 (Live Transcript)
•	P2.2 → P2.3 (Text for NLP)
•	User ↔ P2.3 (Chatbot Suggestions)
•	P2.3 → D3 (Interaction Logs)
•	P2.4 → D3 (Engagement Scores)
 
Post-Meeting Phase (P3)
Processes:
•	P3.1: Summarization & Keyword Extraction
•	P3.2: Translation Module
•	P3.3: Insights & Summary Generation
Data Stores:
•	D4: AI Summaries DB
•	D5: Translated Reports DB
Data Flows:
•	D2 → P3.1 (Transcripts)
•	P3.1 → D4 (Summary, Keywords)
•	P3.1 → P3.2 (Summary)
•	P3.2 → D5 (Urdu Report)
•	User → P3.3 → (Final Output View)

 
Testing & QA (P4)
Processes:
•	P4.1: Speech Accuracy Testing
•	P4.2: UI Testing
•	P4.3: Bug Fixing
Data Flow (Internal):
•	Testers provide feedback → Developers improve modules
(Not typically detailed in DFD-supporting process only)




Preview of the project
Pre-Meeting Phase

Login Interface:
Ensuring that only approved users have access to the functions of the MeetIntelli web application, the login page serves as the main entryway into the system. It has a user interface displaying two basic input fields: one for the password and the other for the username. Before being able to access the three main modules of the system: Pre-Meeting, In-Meeting, and Post-Meeting, users have to provide valid credentials to authenticate themselves. This implementation isolates access to sensitive information and interactions behind a login barrier, therefore adhering to conventional security procedures. Form data is transmitted to the backend when the login button is pressed, where user authentication is confirmed usually against a database of registered users. The user is allowed access and sent to the home or dashboard screen if the credentials supplied match a valid entry. Should authentication fail, suitable feedback like “Invalid username or password” is displayed. This secure authentication process guarantees that every user session is uniquely linked to an authorized identification, so enabling customized access and improved data security throughout the application.

Pre Meeting customized chatbot
Users are sent to a customized interface after logging into the MeetIntelli web application successfully that highlights a meeting specific chatbot created only to help consumers with every facet of meeting preparation and participation. Trained and refined to answer intelligently questions about business meetings, this chatbot is not meant for general use. Users of this module may ask any meeting-related questions, including clarifications on the agenda, participants’ roles, predicted outcomes, or advised participation techniques, therefore driving its essential function. This chatbot’s ability to accept and read PDF files, particularly the meeting agenda, sets it apart. Users can upload the agenda document directly into the interface; the system then uses Natural Language Processing (NLP) techniques to extract important information from the PDF. Once uploaded, the chatbot analyzes the content and lets users ask context aware questions such as “What is my responsibility in the meeting?” or “Summarize the major issues from the agenda. “Based on the uploaded file, the chatbot then offers brief and correct responses. This smart interaction provides instant clarity and ideas on meeting materials, hence streamlining and effectively preparing the user; this helps to increase user confidence and productivity prior to the commencement of the meeting.

Meeting Phase

google chrome extension:
During the actual meeting, MeetIntelli introduces a robust and user-friendly Google Chrome extension designed to seamlessly integrate into live online meeting environments such as Zoom, Google Meet, or Microsoft Teams. This extension provides five essential buttons each contributing to a smoother, more productive meeting experience.
1.	Ask Button: During the meeting, this button lets users engage with the integrated chatbot. Users may enter any query or prompt relevant to the current conversation by clicking Ask. For instance, if a user is unclear about a term being debated or wants to know the definition of a corporate idea, they can just type the query and the chatbot offers a real-time, context-aware response. This guarantees that consumers remain informed and do not overlook critical elements of the discussion.
2.	Start Recording: Clicking this button starts real-time audio recording of the meeting. Starting immediately, the recording procedure logs all verbal material from participants in the background. This is especially useful for anyone who wants to go back to the meeting later or for latecomers who missed early discussions. The tool guarantees correct recording with time stamps for future reference.
3.	Stop Recording: This button stops the recording process at any specified moment. Once compressed, the system closes the ongoing recording session and arranges the audio data for transcription. This is essential to guarantee that particularly during breaks or off-topic conversations, unneeded segments are not recorded.
4.	Languages Button (English/Urdu): With the special capability to alternate between English and Urdu, this toggle button makes MeetIntelli bilingual and inclusive for a varied audience. Both the meeting transcript and the chatbot responses change depending on the chosen language. The important thing is that this is an essential tool in situations where bilingual communication is a key factor because it enhances inclusivity and comprehension on the part of the attendees.
5.	Download Transcript: This button lets users download a full transcript of the meeting in their preferred language after the meeting ends and the system has analyzed the recorded data. All important conversations, speaker sections, and timestamps are found in the transcript. Apart from being an official record of meetings, this helps in task follow-ups, post-meeting evaluations, and compliance papers.
Each of these buttons plays a critical role in ensuring that the meeting phase is interactive, efficient, and accessible, giving users the tools they need to stay engaged, document information accurately, and interact intelligently in real time.

Post meeting phase
transcripts

The Post-Meeting phase of MeetIntelli turns on one of its most potent and sophisticated tools-automated transcript creation with bilingual help after the end of a corporate gathering.-This capability guarantees that everything covered in the session is recorded, processed, and returned to the user as readable, premium transcripts in English and Urdu. Using sophisticated speech recognition and natural language processing (NLP), the system listens to the audio recordings taken during the meeting (using the “Start Recording” and “Stop Recording” buttons) and automatically transforms the spoken conversation into properly formatted text.
The English transcript offers a crisp, accurate, chronologically arranged account of the whole debate. Each participant’s speech is separated, properly punctuated, and presented to resemble natural language for readability. Retaining even subtle conversations and technical terminology guarantees the transcript accurately captures the mood and detail of the meeting. For expert documentation, distribution of meeting minutes, or task follow-up, this is perfect.
MeetIntelli is among the few AI-driven meeting assistants created with cultural and linguistic variety in mind since it also produces a fluid Urdu transcript. The Urdu version is a contextually changed transcription capturing meaning, tone, and sentiment, not merely a literal translation. This guarantees that Urdu native speakers get a transcription as natural, conversational, and meticulously structured as the English equivalent. Correct grammar, diacritics (when necessary), and an easy flow in the Urdu text allow for smooth understanding for a larger user base.
These records dynamically narrate what occurred during the meeting rather than merely static logs. Whether rereading a chat, writing a post-meeting summary, or distributing important points to absent team members, users can completely rely on MeetIntelli’s accuracy, simplicity, and linguistic flexibility. Reflecting the platform’s dedication to inclusiveness, accuracy, and modern workplace needs, the smooth creation of both English and Urdu transcripts makes it a remarkable instrument in intelligent meeting management systems.
