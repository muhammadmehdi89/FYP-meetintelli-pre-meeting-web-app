
 
 
  
MeetIntelli  
  
Project Team: 
 Mr. Saad Khan
 Mr. Muhammad Mehdi 
 
 
 
July 06th, 2025 
 
Submitted in partial fulfillment of the requirements for the degree of 
Bachelor of Science in Artificial Intelligence 
in the
Faculty of Computing and Engineering Sciences  
Shaheed Zulfiqar Ali Bhutto Institute of Science and Technology University
Karachi Campus

Declaration of Authorship


We, the undersigned, hereby declare that the project titled MeetIntelli is our original work and has been completed in accordance with the academic standards of SZABIST University under the supervision of Syed Hassan Ali.
We confirm that all sources and references used during the research and development of this project have been properly cited and acknowledged. The content of this report is original and has not been copied or plagiarized from any external source. 
We further declare that this project has not been previously submitted for the award of any degree, diploma, or other qualification at any other university or institution.



Project Description

Developed as a final year project to simplify and improve the general meeting experience via three connected phases: pre-meeting, meeting, and post-meeting, MeetIntelli is an AI-powered intelligent meeting helper. Users can interact with a customized chatbot designed to help prepare for meetings by offering pertinent direction, answering questions, and assisting structure ideas beforehand in the pre-meeting stage. A Chrome extension records the audio, converts it into text in real time, and keeps it in the system for quick reference during the meeting phase. The user may also engage with the chatbot live during the meeting to get recommendations, pose questions, or monitor main topics. During the post-meeting phase, the stored text is used to create a full transcript of the meeting with the added capability of bilingual assistance that lets the user produce the transcript or summary in English or Urdu. Meeting management from MeetIntelli provides a full answer to ensure thorough preparation, real-time assistance, and timely follow-up. 
Acknowledgement

In the name of ALLAH, the Most Beneficent, the Most Merciful – who blessed us with the ability, wisdom, and perseverance to undertake and complete this research project.
We would like to express our heartfelt gratitude to our supervisor, Sir Hassaan Ali, from the Department of Computer Science at SZABIST, for his unwavering support, insightful guidance, and constant encouragement throughout the development of our final year project, MeetIntelli. His expertise and direction were instrumental in helping us stay focused and overcome the challenges we faced during this journey.
We are also deeply thankful to all our respected teachers, whose knowledge and mentorship have laid the foundation of our academic and personal growth. Their guidance has empowered us to approach this project with clarity and confidence.
A special note of appreciation goes to our loving parents and families for their endless prayers, patience, and support. Their belief in us and their constant motivation served as a pillar of strength throughout this journey.
We extend our sincere thanks to SZABIST for providing us with a supportive academic environment and the resources essential to successfully execute this project. The institute’s commitment to innovation and excellence has been a significant influence on our learning experience.
Lastly, we are grateful to everyone who contributed to the development and testing of MeetIntelli, especially those who provided valuable feedback and encouragement, making this project both meaningful and successful.
 
Contents
Declaration of Authorship	1
Project Description	2
Acknowledgement	3
Table of Figures	9
Table of Tables	10
Project Proposal	11
Introduction	12
Objective	12
Problem Description	12
Target Industry	12
Methodology	12
Project Scope	13
Out of Scope:	13
Feasibility Study	13
Resource Requirements:	13
Solution Application Areas	13
Tools/Technology	14
Expertise of the Team Members	14
Milestones	14
Phase 1: Requirements Gathering and Planning	14
Phase 2: Design	14
Phase 3: Development	14
Phase 4: Testing and QA	15
Phase 5: Deployment and Feedback	15
Data Flow Diagrams of Multiple phases	15
Requirements & Planning (P0)	15
Pre-Meeting Phase (P1)	15
In-Meeting Phase (P2)	16
Post-Meeting Phase (P3)	17
Testing & QA (P4)	18
Deployment & Feedback (P5)	19
Preview of the project	20
Pre-Meeting Phase	20
Pre Meeting customized chatbot	21
Meeting Phase	22
Post meeting phase	23
Pseudocode of the project	26
Pre meeting phase:  BEGIN PreMeetingPhase	27
Meeting phase:	30
Post meeting phase:	34
Overall Workflow summary:	38
Software Requirements Specification	40
Introduction	41
Purpose	41
Overall Description	43
Product Perspective	43
External Interface Requirements	45
User Interfaces	45
Hardware Interfaces	46
Software Interfaces	46
Communications Interfaces	46
System Features	47
Pre-Meeting Evaluation	47
Meeting Assistance	47
Post-Meeting Summary	48
Software Quality Attributes	48
Business Rules	49
Other Nonfunctional Requirements	49
Performance Requirements	49
Safety Requirements	49
Security Requirements	49
Software Quality Attributes	50
Business Rules	50
Other Requirements	50
Appendix A: Glossary	50
Software Design Specification	52
Introduction	53
Purpose	53
Definitions, Acronyms, and Abbreviations	56
Core Components	57
AI and Processing Modules	58
System Characteristics	59
Strategic Impact	59
3. Architectural Design	59
System Components	59
Table 3 : Components utilized in the project	60
3.2 Data Flow Diagram (DFD)	60
3.3 Architectural Layers and Deployment View	61
Detailed Design	63
Pre-Meeting Phase	63
Meeting Phase	65
Post-Meeting Phase	67
Security Considerations	69
Performance Requirements	71
Conclusion	73
Conclusion	73
Future Scope	74
8. References	74
9. Appendices	74
9.1 Glossary	74
Test cases	76
Test Case Name: User Registration Test Case	77
Description:	77
Prerequisites:	77
Initial Execution Test Scenario:	77
Test Case Name: Login (User) Test Case	78
Description:	78
Prerequisites:	78
Initial Execution Test Scenario:	78
Test Case Name: Admin User Role Assignment Test Case	79
Description:	79
Initial Execution Test Scenario:	79
Test Case Name: Edge Case: Meeting with No Audio	80
Description:	80
Initial Execution Test Scenario:	80
Test Case Name: Load Testing for Live Transcription	80
Description:	80
Prerequisites:	80
Initial Execution Test Scenario:	80
Test Case Name: Pre-Meeting Chatbot Interaction Test Case	81
Description:	81
Initial Execution Test Scenario:	81
Test Case Name: In-Meeting Chrome Extension Recording Test Case	82
Description:	82
Initial Execution Test Scenario:	82
Test Case Name: Post-Meeting Transcript Generation Test Case	83
Description:	83
Initial Execution Test Scenario:	83
Test Case Name: Knowledge Base Upload Test Case	83
Description:	83
Initial Execution Test Scenario:	83
Test Case Name: Email Summary Export Test Case	84
Description:	84
Initial Execution Test Scenario:	84
Test Case Name: Bilingual Summary Toggle Test Case	85
Description:	85
Initial Execution Test Scenario:	85
User manual	86
Introduction	87
Key Features Overview:	88
Target Audience:	89
Getting Started	90
User Login & Authentication	90
Becoming a MeetIntelli User	90
Features and Functionalities	91
Pre-Meeting Phase	91
Chatbot Preparation	91
Preparing for the Meeting	92
In-Meeting Phase	92
Post-Meeting Phase	93
FAQs	95
General Platform Questions	95
Technical Support	96
Support Information	97
Contact Emails	97
Response Time	97
Community Guidelines	97
Responsible Usage	97
Content Security	98

 


Table of Figures


Figure 1: P1 Data Flow Diagram	15
Figure 2: P2 Data Flow Diagram	16
Figure 3: P3 Data Flow Diagram	17
Figure 4: P4 Data Flow Diagram	18
Figure 5: P5 Data Flow Diagram	19
Figure 6: Login Interface	20
Figure 7: Pre- Meeting Chatbot	21
Figure 8: In-Meeting Google Chrome Extension	23
Figure 9 :Post-Meeting Transcript Generated in Urdu	25
Figure 10 :Post-Meeting Transcript Generated in English	25
Figure 11: Data Flow Diagram of the Overall Workflow	63


 

Table of Tables


Table 1 : Intended Audience	58
Table 2 : Full Form of the given Acronyms	59
Table 3 : Components utilized in the project	63
Table 4 :  Description of the Given Components	69
Table 5 : Description of the Given Components	71
Table 6 : Description of the Given Components	73
Table 7 : Test Case 1	84
Table 8 : Test Case 2	85
Table 9 : Test Case 3	87
Table 10 : Test Case 4	87
Table 11 : Test Case 5	88
Table 12 : Test Case 6	89
Table 13 : Test Case 7	90
Table 14 : Test Case 8	91
Table 15 : Test Case  9	92
Table 16 : Test Case 10	93
Table 17 : Test Case 11	93
 







Project Proposal
 
Introduction

Designed to improve the general meeting experience through smart automation and real-time assistance, MeetIntelli is an artificial intelligence-powered meeting assistant platform. Pre-Meeting, In-Meeting, and Post-Meeting are the three main phases of the system. Users engage with a customized chatbot in the Pre-Meeting phase that offers agenda related direction, responds to questions, and recommends important discussion topics to help with meeting preparation. A Chrome extension captures live audio during the Meeting phase, which is then transcribed into text and kept inside the platform. This stage keeps the chatbot available so it can offer real-time support and engagement. The retained chat is used during the Post-Meeting phase to create a thorough meeting transcript with multilingual output assistance in English and Urdu. Especially for business and academic applications, MeetIntelli is meant to increase meeting effectiveness, guarantee better preparation, boost participation, and simplify follow-up.
Objective

With the goal of increasing productivity and communication, an AI-based assistance platform supporting users before, during, and after meetings by means of customized preparation tools, live meeting assistance, automated audiototext translation, and multilingual transcript generation is developed.
Problem Description

In academic and professional contexts, people sometimes struggle to prepare for meetings, maintain attention during talks, and precisely reflect major outcomes post-meeting. There aren’t coordinated tools providing customized preparation, real-time support, and planned follow-up in a smooth workflow. Conventional notetaking is time-consuming and susceptible to human error. Users also lack easy access to tools offering real-time summaries and linguistic flexibility. MeetIntelli tackles these obstacles by providing a sophisticated, all-inclusive platform that directs participants across every stage of the meeting, records essential information, and produces organized bilingual transcripts. It improves the general quality of meetings, eliminates manual notetaking, and lessens cognitive load.

Target Industry
MeetIntelli targets the corporate, educational, and professional services sectors, with a focus on productivity, communication, and meeting automation.
Methodology
MeetIntelli grew in stages. Through investigation, user demands and gaps in current meeting tools were first discovered. User flows and interfaces were created using Figma following this to guarantee a seamless user experience. Built and tested during development were core features like speech-to-text processing, Chrome extension for audio capture, and chatbot integration. To guarantee correctness, performance, and usability, the platform went through ongoing feedback and testing loops. To enable iterative enhancements, agile development techniques were implemented.
Project Scope
MeetIntelli aims to deliver a complete meeting assistant experience through three key features:
•	A pre-meeting chatbot for preparation.
•	An in-meeting Chrome extension for recording and real-time text conversion.
•	Post-meeting transcript generation with bilingual output.
•	The platform will focus on business and academic use cases, providing structured, AI-supported meeting workflows.
Out of Scope:
At this phase, the initiative omits advanced calendar integration, voice or video calling, mobile app creation, emotional or sentimental analysis, and live language translation. It does not have document cooperation tools or real-time speaker diarization capabilities.
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
•	Chrome Extension Development
•	AI Chatbot Integration
•	Backend API Design and Integration
Muhammad Mehdi:
•	UI/UX Design and Front-End Development
•	Research and Documentation
•	Audio Processing and Text Generation Logic
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

 
Figure 1: P1 Data Flow Diagram
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
 
Figure 2: P2 Data Flow Diagram
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

 
Figure 3: P3 Data Flow Diagram
Testing & QA (P4)
Processes:
•	P4.1: Speech Accuracy Testing
•	P4.2: UI Testing
•	P4.3: Bug Fixing
Data Flow (Internal):
•	Testers provide feedback → Developers improve modules
(Not typically detailed in DFD—supporting process only)


 
Figure 4: P4 Data Flow Diagram
Deployment & Feedback (P5)
Processes:
•	P5.1: Deploy Web App & Extension
•	P5.2: Collect User Feedback
•	P5.3: Continuous Improvements
Data Stores:
•	D6: Feedback Logs
Data Flows:
•	P5.1 → Users (App Availability)
•	Users → P5.2 (Feedback)
•	P5.2 → D6
•	D6 → P5.3 (Refinements)
 
Figure 5: P5 Data Flow Diagram


Preview of the project
Pre-Meeting Phase

Login Interface:
Ensuring that only approved users have access to the functions of the MeetIntelli web application, the login page serves as the main entryway into the system. It has a user interface displaying two basic input fields: one for the password and the other for the username. Before being able to access the three main modules of the system—Pre-Meeting, In-Meeting, and Post-Meeting—users have to provide valid credentials to authenticate themselves. This implementation isolates access to sensitive information and interactions behind a login barrier, therefore adhering to conventional security procedures. Form data is transmitted to the backend when the login button is pressed, where user authentication is confirmed—usually against a database of registered users. The user is allowed access and sent to the home or dashboard screen if the credentials supplied match a valid entry. Should authentication fail, suitable feedback like “Invalid username or password” is displayed. This secure authentication process guarantees that every user session is uniquely linked to an authorized identification, so enabling customized access and improved data security throughout the application.
Figure 6: Login Interface


Pre Meeting customized chatbot
Users are sent to a customized interface after logging into the MeetIntelli web application successfully that highlights a meeting specific chatbot created only to help consumers with every facet of meeting preparation and participation. Trained and refined to answer intelligently questions about business meetings, this chatbot is not meant for general use. Users of this module may ask any meeting-related questions, including clarifications on the agenda, participants’ roles, predicted outcomes, or advised participation techniques, therefore driving its essential function. This chatbot’s ability to accept and read PDF files, particularly the meeting agenda, sets it apart. Users can upload the agenda document directly into the interface; the system then uses Natural Language Processing (NLP) techniques to extract important information from the PDF. Once uploaded, the chatbot analyzes the content and lets users ask context aware questions such as “What is my responsibility in the meeting?” or “Summarize the major issues from the agenda. “Based on the uploaded file, the chatbot then offers brief and correct responses. This smart interaction provides instant clarity and ideas on meeting materials, hence streamlining and effectively preparing the user; this helps to increase user confidence and productivity prior to the commencement of the meeting.
Figure 7: Pre- Meeting Chatbot


Meeting Phase

google chrome extension:
During the actual meeting, MeetIntelli introduces a robust and user-friendly Google Chrome extension designed to seamlessly integrate into live online meeting environments such as Zoom, Google Meet, or Microsoft Teams. This extension provides five essential buttons—each contributing to a smoother, more productive meeting experience.
1.	Ask Button: During the meeting, this button lets users engage with the integrated chatbot. Users may enter any query or prompt relevant to the current conversation by clicking Ask. For instance, if a user is unclear about a term being debated or wants to know the definition of a corporate idea, they can just type the query and the chatbot offers a real-time, context-aware response. This guarantees that consumers remain informed and do not overlook critical elements of the discussion.
2.	Start Recording: Clicking this button starts real-time audio recording of the meeting. Starting immediately, the recording procedure logs all verbal material from participants in the background. This is especially useful for anyone who wants to go back to the meeting later or for latecomers who missed early discussions. The tool guarantees correct recording with time stamps for future reference.
3.	Stop Recording: This button stops the recording process at any specified moment. Once compressed, the system closes the ongoing recording session and arranges the audio data for transcription. This is essential to guarantee that particularly during breaks or off-topic conversations, unneeded segments are not recorded.
4.	Languages Button (English/Urdu): With the special capability to alternate between English and Urdu, this toggle button makes MeetIntelli bilingual and inclusive for a varied audience. Both the meeting transcript and the chatbot responses change depending on the chosen language. The important thing is that this is an essential tool in situations where bilingual communication is a key factor because it enhances inclusivity and comprehension on the part of the attendees.
5.	Download Transcript: This button lets users download a full transcript of the meeting in their preferred language after the meeting ends and the system has analyzed the recorded data. All important conversations, speaker sections, and timestamps are found in the transcript. Apart from being an official record of meetings, this helps in task follow-ups, post-meeting evaluations, and compliance papers.
Each of these buttons plays a critical role in ensuring that the meeting phase is interactive, efficient, and accessible, giving users the tools they need to stay engaged, document information accurately, and interact intelligently in real time.
Figure 8: In-Meeting Google Chrome Extension

Post meeting phase
transcripts

The Post-Meeting phase of MeetIntelli turns on one of its most potent and sophisticated tools—automated transcript creation with bilingual help—after the end of a corporate gathering.-This capability guarantees that everything covered in the session is recorded, processed, and returned to the user as readable, premium transcripts in English and Urdu. Using sophisticated speech recognition and natural language processing (NLP), the system listens to the audio recordings taken during the meeting (using the “Start Recording” and “Stop Recording” buttons) and automatically transforms the spoken conversation into properly formatted text.
The English transcript offers a crisp, accurate, chronologically arranged account of the whole debate. Each participant’s speech is separated, properly punctuated, and presented to resemble natural language for readability. Retaining even subtle conversations and technical terminology guarantees the transcript accurately captures the mood and detail of the meeting. For expert documentation, distribution of meeting minutes, or task follow-up, this is perfect.
MeetIntelli is among the few AI-driven meeting assistants created with cultural and linguistic variety in mind since it also produces a fluid Urdu transcript. The Urdu version is a contextually changed transcription capturing meaning, tone, and sentiment, not merely a literal translation. This guarantees that Urdu native speakers get a transcription as natural, conversational, and meticulously structured as the English equivalent. Correct grammar, diacritics (when necessary), and an easy flow in the Urdu text allow for smooth understanding for a larger user base.
These records dynamically narrate what occurred during the meeting rather than merely static logs. Whether rereading a chat, writing a post-meeting summary, or distributing important points to absent team members, users can completely rely on MeetIntelli’s accuracy, simplicity, and linguistic flexibility. Reflecting the platform’s dedication to inclusiveness, accuracy, and modern workplace needs, the smooth creation of both English and Urdu transcripts makes it a remarkable instrument in intelligent meeting management systems.
Figure 9 :Post-Meeting Transcript Generated in Urdu
Figure 10 :Post-Meeting Transcript Generated in English
 








Pseudocode of the project
 
Pre meeting phase:

BEGIN PreMeetingPhase
    DISPLAY “Welcome to MeetIntelli - Pre-Meeting Assistant”
    // Step 1: User Login
    PROMPT “Enter Username:”
    INPUT username
    PROMPT “Enter Password:”
    INPUT password
    IF AuthenticateUser(username, password) == TRUE THEN
        DISPLAY “Login successful. Redirecting to Pre-Meeting Dashboard...”
    ELSE
        DISPLAY “Invalid credentials. Please try again.”
        TERMINATE PreMeetingPhase
    ENDIF
    // Step 2: Launch Meeting Chatbot Interface
    INITIALIZE MeetingChatbot()

    DISPLAY “Chatbot Ready. You can now ask meeting-related questions or upload a meeting agenda.”
    WHILE UserInChatbotInterface == TRUE DO
        DISPLAY “Choose an option: (1) Ask a Question, (2) Upload Agenda PDF, (3) Exit Chatbot”
        INPUT userOption

        IF userOption == 1 THEN
            PROMPT “Enter your meeting-related query:”
            INPUT userQuery
            chatbotResponse ← GenerateChatbotResponse(userQuery)
            DISPLAY chatbotResponse
        ELSE IF userOption == 2 THEN
            PROMPT “Upload Meeting Agenda PDF:”
            INPUT pdfFilePath
            IF ValidatePDF(pdfFilePath) == TRUE THEN
                extractedText ← ReadPDF(pdfFilePath)
                summarizedContent ← SummarizePDFContent(extractedText)
                DISPLAY “PDF processed. Summary:”
                DISPLAY summarizedContent
                DISPLAY “You may now ask questions related to the uploaded agenda.”
            ELSE
                DISPLAY “Invalid or corrupt PDF file. Please try again.”
            ENDIF
        ELSE IF userOption == 3 THEN
            DISPLAY “Exiting Chatbot. Proceed to the Meeting Phase.”
            BREAK
        ELSE
            DISPLAY “Invalid option. Please choose 1, 2, or 3.”
        ENDIF
    END WHILE
END PreMeetingPhase
Explanation:

The Pre-Meeting Phase is designed to prepare users before their scheduled meetings by assessing their readiness and equipping them with necessary tools such as a meeting-specific chatbot and document understanding features. The pseudocode outlines the logical steps followed by the system to carry out this process efficiently.
 
Meeting phase:
BEGIN MeetingPhase
    DISPLAY “Welcome to MeetIntelli - In-Meeting Assistant via Chrome Extension”
    // Step 1: Initialize Chrome Extension UI
    DISPLAY “Chrome Extension UI Loaded with the following options:”
    DISPLAY “[1] Ask”
    DISPLAY “[2] Start Recording”
    DISPLAY “[3] Stop Recording”
    DISPLAY “[4] Language Selection (English / Urdu)”
    DISPLAY “[5] Download Transcript”
    // Step 2: Main Interaction Loop
    WHILE MeetingInProgress == TRUE DO
        PROMPT “Select an option (1 to 5):”
        INPUT userChoice
        // Ask: Interact with the assistant during the meeting
        IF userChoice == 1 THEN
            PROMPT “Enter your meeting-related query:”
            INPUT meetingQuery
            assistantReply ← ProcessQuery(meetingQuery)
            DISPLAY “Assistant: “, assistantReply
        // Start Recording: Begins audio capture of the live meeting
        ELSE IF userChoice == 2 THEN
            IF recordingStatus == FALSE THEN
                StartAudioCapture()
                recordingStatus ← TRUE
                DISPLAY “Recording started successfully.”
            ELSE
                DISPLAY “Recording is already in progress.”
            ENDIF
        // Stop Recording: Ends audio capture and processes audio
        ELSE IF userChoice == 3 THEN
            IF recordingStatus == TRUE THEN
                StopAudioCapture()
                recordingStatus ← FALSE
                DISPLAY “Recording stopped. Processing transcript...”
                meetingTranscript ← GenerateTranscript(capturedAudio, selectedLanguage)
                STORE meetingTranscript
                DISPLAY “Transcript successfully generated and saved.”
            ELSE
                DISPLAY “No active recording to stop.”
            ENDIF
        // Language Selection: Toggle between English and Urdu
        ELSE IF userChoice == 4 THEN
            DISPLAY “Select Transcript Language: [1] English, [2] Urdu”
            INPUT languageChoice
            IF languageChoice == 1 THEN
                selectedLanguage ← “English”
            ELSE IF languageChoice == 2 THEN
                selectedLanguage ← “Urdu”
            ELSE
                DISPLAY “Invalid language selection. Defaulting to English.”
                selectedLanguage ← “English”
            ENDIF
            DISPLAY “Language set to: “, selectedLanguage
        // Download Transcript: Save transcript to user’s system
        ELSE IF userChoice == 5 THEN
            IF transcriptExists == TRUE THEN
                PROMPT “Enter file name for download:”
                INPUT fileName
                SaveTranscript(meetingTranscript, fileName, selectedLanguage)
                DISPLAY “Transcript downloaded successfully as “, fileName
            ELSE
                DISPLAY “No transcript available. Please record the meeting first.”
            ENDIF
        ELSE
            DISPLAY “Invalid option. Please choose between 1 to 5.”
        ENDIF
    END WHILE
    DISPLAY “Meeting concluded. You may now proceed to the Post-Meeting phase.”
END Meeting Phase
Explanation:
Using a custom-built Google Chrome extension, the Meeting Phase concentrates on recording, analysis, and helping real business meetings. This extension combines several interactive features including language support, real-time prompt assistance, audio recording, and transcript generation. The pseudocode clarifies how every function is activated and controlled in a real meeting.
 
Post meeting phase:
BEGIN PostMeetingPhase
    DISPLAY “Welcome to MeetIntelli - Post-Meeting Transcript Assistant”
    // Step 1: Load transcript data generated during the Meeting Phase
    IF TranscriptExists() THEN
        DISPLAY “Transcript found for the recent meeting session.”
    ELSE
        DISPLAY “No transcript found. Please complete the Meeting Phase first.”
        TERMINATE
    ENDIF
    // Step 2: Offer language selection for transcript review
    DISPLAY “Select the language in which you want to view the transcript:”
    DISPLAY “[1] English”
    DISPLAY “[2] Urdu”
    PROMPT “Enter language choice:”
    INPUT languageChoice
    IF languageChoice == 1 THEN
        selectedLanguage ← “English”
    ELSE IF languageChoice == 2 THEN
        selectedLanguage ← “Urdu”
    ELSE
        DISPLAY “Invalid choice. Defaulting to English.”
        selectedLanguage ← “English”
    ENDIF
    // Step 3: Fetch and display the transcript
    meetingTranscript ← LoadTranscript(selectedLanguage)
    DISPLAY “----- Meeting Transcript (“ + selectedLanguage + “) -----”
    DISPLAY meetingTranscript
    // Step 4: Highlight intelligent narration
    DISPLAY “MeetIntelli has segmented the conversation into clear dialogue blocks.”
    DISPLAY “Speaker labels, timestamps, and coherent context formatting have been applied.”
    DISPLAY “Natural language understanding was used to enhance clarity and accuracy.”
    // Step 5: Offer additional features
    WHILE TRUE DO
        DISPLAY “Post-Meeting Options:”
        DISPLAY “[1] Summarize Meeting”
        DISPLAY “[2] Translate Transcript”
        DISPLAY “[3] Download Transcript”
        DISPLAY “[4] Exit”
        PROMPT “Choose an option:”
        INPUT userOption
        // Option 1: Generate Meeting Summary
        IF userOption == 1 THEN
            summary ← GenerateSummary(meetingTranscript)
            DISPLAY “----- Meeting Summary -----”
            DISPLAY summary

        // Option 2: Translate Transcript to the alternate language
        ELSE IF userOption == 2 THEN
            IF selectedLanguage == “English” THEN
                translatedTranscript ← Translate(meetingTranscript, targetLanguage=“Urdu”)
                DISPLAY “----- Translated Transcript (Urdu) -----”
            ELSE
                translatedTranscript ← Translate(meetingTranscript, targetLanguage=“English”)
                DISPLAY “----- Translated Transcript (English) -----”
            ENDIF
            DISPLAY translatedTranscript
        // Option 3: Download the final transcript
        ELSE IF userOption == 3 THEN
            PROMPT “Enter filename for download:”
            INPUT fileName
            SaveTranscript(meetingTranscript, fileName, selectedLanguage)
            DISPLAY “Transcript saved as “, fileName
        // Option 4: Exit
        ELSE IF userOption == 4 THEN
            DISPLAY “Exiting Post-Meeting Phase. Thank you for using MeetIntelli!”
            BREAK
        ELSE
            DISPLAY “Invalid option. Please choose from 1 to 4.”
        ENDIF
    END WHILE
END PostMeetingPhase
Explanation:
Post-Meeting Phase emphasizes the automatic producing, presenting, and downloading of transcripts derived from the recorded conference audio. Additionally, supporting bilingual output (English and Urdu), it helps users to better grasp and record the results of a meeting. This stage guarantees that consumers leave with understandable transcripts, useful insights, and improved grasp of events.

 
Overall Workflow summary:

Three clearly related but interconnected phases—Pre-Meeting, Meeting, and Post-Meeting—assist to simplify and maximize the whole meeting experience thanks to the AI-powered assistant MeetIntelli. The system starts by validating the user via a login interface during the Pre-Meeting phase, so guaranteeing a safe environment before sensitive meeting features are accessed. Once verified, the user is presented to an intelligent chatbot designed especially for meeting preparation. This chatbot enables the user to submit a PDF with the meeting agenda, as well as answering inquiries about general meetings. The system analyzes and reads the document using natural language processing methods upon arrival, pulling important points, summaries, and possible action items. this context-aware support guarantees that users are well-informed and confidently ready for the approaching session, and it does by removing the necessity of hand review and notetaking. The chatbot will still be available for ongoing engagement, and will offer tailored references or descriptions which will depend on both the user’s questions and the submitted agenda content.
The system enters into a live interaction mode during the Meeting phase through a custom created Google Chrome extension, which proves to be instrumental in capturing and controlling the meeting’s flow. There are five major buttons on the extension interface, and each button has a different function, which is very important for improving the live meeting experience. The “Ask” button will allow users enter prompts during the meeting, hence allowing real-time aid or clarification from the artificial intelligence assistant. The “Start Recording” button starts the audio recording operation, which captures the entire chat flawlessly in the background. It enables the audio recording functions of the browser upon clicks, and retains every spoken conversation for subsequent analysis. This process is stopped and the captured file is kept safely in the memory of the machine with the help of the “Stop Recording” button. The MeetInteli extension’s language toggle, titled “Languages,” is a critical feature that allows the bilingual users or multilingual teams switch between English and Urdu in real time, therefore promoting inclusivity and access. At last, once the conference is over, the “Download Transcript” button lets customers get a complete written transcription. This all-encompassing suite lets attendees remain involved throughout the presentation without concern about notetaking and also allows live interaction with the artificial intelligence and linguistic agility.
Once the meeting ends, the Post-Meeting stage starts, concentrating on transforming the taped audio into significant, well-organized documentation. First, the system grabs the saved audio file and runs sophisticated speech-to-text algorithms to convert the content. catering to the user’s preferred language, the result is a very accurate transcript created in Urdu and English. These transcripts are carefully organized by speaker, timestamped when appropriate, and formatted for readability and simplicity; they are not just basic speech dumps. Allowing the user to easily examine or compare them, the interface presents transcripts either side by side or sequentially. Moreover, the user is given the chance to download either version in several formats including PDF or simple text, which simplifies archiving or sharing. The sophisticated of the transcription module comes from its capacity to clearly describe the dialogue, capturing subtleties, tone, and context, in addition to its linguistic complexity. By post-meeting automation, nothing is missed, hence strengthening the efficiency of the whole meeting lifecycle. MeetIntelli converts meetings from regular responsibilities into clever, informed, and structured corporate interactions overall—that is, it serves as a full spectrum digital assistant.
 








Software Requirements Specification


 

Introduction
Purpose
For the AI Meeting Assistant project—an original system under development as part of a final year academic effort at SZABIST University Karachi—this paper details the exacting software requirements. Designed to drastically enhance the way business meetings are run and handled, the MeetIntelli system is meant to be a thorough AI-powered meeting assistant. Three key phases of a meeting—pre-meeting planning, in-meeting help, and post-meeting summarization—the assistant supports users through these. This paper specifies the entire range of functional and nonfunctional demands specifying the behavior and limits of the system. Furthermore, it helps to guarantee smooth development and deployment by clarifying system expectations, technological terminology, and system restrictions. For documentation purposes, the SRS stresses user interaction mechanisms, real-time performance criteria, AI-driven decision-making skills, and transcription generation. These specifications guarantee that the MeetIntelli initiative fulfills its technical, operational, and usability objectives by matching both industry standards and academic criteria.
Document Conventions
Bold Text: Indicates key sections, requirements, or development priorities.
Italic Text: Denotes supplementary explanations, examples, or optional recommendations.
All requirements within this document are labeled using unique identifiers for effortless referencing and traceability throughout the software development lifecycle.
Priorities assigned to high-level requirements will be automatically inherited by their respective detailed requirements unless explicitly redefined. This convention promotes consistency and clarity during requirement analysis, design, testing, and implementation phases.
Intended Audience and Reading Suggestions
This document is intended to be reviewed by a diverse set of stakeholders involved in the MeetIntelli project, ensuring alignment across all development phases:
●	Head of Department (HoD): To gain a thorough understanding of the project’s design, scope, technical complexity, and resource requirements.
●	Final Year Project (FYP) Supervisors: To track project milestones, validate alignment with academic standards, and ensure the project delivers functional, technically sound, and innovative outcomes.
●	Testers and Quality Assurance Teams: To utilize the defined requirements as the basis for test planning, case development, and validation of system functionality and performance benchmarks.
●	End-Users (Students, Faculty, or Business Professionals): To comprehend the system’s intended features, capabilities, and operational behavior, fostering user readiness and informed usage of the assistant.
For optimal understanding, it is recommended that readers familiarize themselves with basic AI concepts, natural language processing, and web-based application workflows. Technical terms, acronyms, and system references are explained in the Glossary and throughout the document where first introduced.
Product Scope
The AI Meeting Assistant, branded as MeetIntelli, is an AI-driven system engineered to revolutionize the preparation, execution, and follow-up of business meetings. The system addresses common challenges such as lack of preparation, inefficient meeting management, and inadequate record-keeping by providing intelligent assistance across all phases of a meeting lifecycle:
●	Pre-Meeting: The system offers a personalized chatbot interface capable of handling user queries and guiding meeting preparation based on the shared agenda and key discussion points. Through AI-driven dialogue, users can clarify meeting objectives, review relevant materials, and align their expectations before joining the session.
●	During Meeting: A Google Chrome Extension seamlessly integrates with the meeting platform, acting as an AI-powered agent. It captures real-time meeting audio, generates accurate transcripts, and provides live, context-aware recommendations to enhance decision-making and participation. All conversational data and AI suggestions are securely stored in a database for real-time access and post-meeting analysis.
●	Post-Meeting: Upon meeting conclusion, the assistant automatically generates comprehensive transcripts, extracts key discussion points, and provides summaries with bi-lingual support (English and Urdu). This feature enhances accessibility, improves documentation accuracy, and aids in future meeting follow-ups.
The MeetIntelli system aims to increase productivity, boost user confidence during meetings, facilitate inclusive communication, and ensure reliable record-keeping. It leverages advanced AI models, natural language processing, and cutting-edge web technologies to deliver an intuitive, efficient, and highly effective meeting management experience.

References
●	IEEE Software Engineering Standards and SRS Documentation Guidelines.
●	Internal Vision and Scope document for the AI Business Assistant project.
●	Python libraries and frameworks including Hugging Face Transformers, Langchain conversational AI tools, Django web framework, FastAPI, and relevant NLP and LLM models.
●	Technical documentation for Chrome Extension development and Speech-to-Text integration APIs.
●	Academic resources on AI, speech recognition, natural language processing, and meeting management systems.
Overall Description
Product Perspective
Designed as a modular, standalone software product, the AI Meeting Assistant uses cutting-edge natural language processing (NLP), real-time evaluation, and machine translation to change how people approach commercial meetings. Through a specific browser extension and behind-end services, although the product works as an independent system, its architecture guarantees easy integration with popular web conferencing platforms. To improve user experience and help meeting production, the assistant provides thorough multi-language transcription assistance, real-time recommendations, and clever summarizing tools.
Context Diagram:
Inputs to the system comprise user responses, loaded meeting agendas, and live audio streams from current conferences.
The outputs that are generated by the system are real-time follow up suggestions, meetings in entire transcripts, translations in various languages (now supporting translation between English and Urdu), and automatic evaluations about the user responses.
Product Functions
MeetIntelli system offers intelligent support throughout the meeting lifecycle with the following key functionalities:
●	Pre-Meeting Phase:
○	Accept well-structured meeting information and input of agenda entries by users.
○	Deploy personalized AI-enabled conversations to enable the user to ask preliminary questions.
○	Graduate reactions based on fine tuned NLP models to check and evaluate relevance and readiness.
○	Offer user-persona-specific guidance and suggestions as and when required by the user.
●	Meeting Phase:
○	Record in-room discussions, through integrated audio recording and speech recognition.
○	Produce instant transcripts of dialogs.
○	Provide smart suggestions of follow up questions using current discussions.
○	Ensure that all transcripts, conversation logs and AI-generated recommendations are securely stored in a relational database (MySQL) to be accessed and analyzed in future.
●	Post-Meeting Phase:
○	Automatically generate a detailed, structured transcript and summary of the meeting.
○	Provide translation of meeting summaries into Urdu, enhancing accessibility and inclusivity for diverse user groups.
User Classes and Characteristics
The target audience for MeetIntelli spans multiple user groups with distinct roles and technical proficiencies:
●	Business Professionals: Primary users expected to interact with all system features to prepare for, participate in, and review meetings effectively.
●	Developers: Responsible for maintaining, updating, and extending the system’s technical components.
●	Testers: Tasked with validating system functionalities, performance benchmarks, and user experience during development and deployment cycles.
●	Managers/Project Leads: Oversee project execution, resource allocation, and alignment of system development with organizational goals and project deliverables.
Operating Environment
The MeetIntelli system operates within the following hardware and software environment specifications:
●	Minimum Hardware Requirements:
○	Dual-core processor
○	4GB RAM
○	Microphone for audio input
●	Recommended Hardware Specifications:
○	Quad-core processor
○	8GB RAM or higher
●	Software Requirements:
○	Supported Operating Systems: Windows 10+, macOS, or major Linux distributions
○	Software Dependencies: Python 3.9+, Langchain library, Django framework, Flask for web interfaces, and additional NLP/AI toolkits
Design and Implementation Constraints
●	The system design prioritizes compliance with international data privacy regulations such as GDPR to protect user information.
●	Functionality must remain robust under low-bandwidth or unstable internet connections.
●	System development is restricted to open-source tools, APIs, and frameworks to adhere to project budget limitations.
●	Translation services within the system currently support English to Urdu language pairs exclusively.
User Documentation
Comprehensive user support materials will be provided, including:
●	User Manual: Step-by-step instructions for system installation, setup, and operation.
●	Online Help Resources: Integrated FAQs and troubleshooting guides accessible within the application.
●	Video Tutorials: Interactive, phase-specific visual guides to facilitate user onboarding and efficient system usage.
Assumptions and Dependencies
1.	Reliable internet connectivity is assumed for seamless real-time processing, translation services, and cloud-based functionalities.
2.	System performance and AI-driven suggestions depend on the availability and accuracy of pre-trained NLP models for tasks such as question generation, response evaluation, and summarization.
External Interface Requirements
User Interfaces
The AI Meeting Assistant provides a modern, user-friendly interface for optimal interaction and system usability:
●	Graphical User Interface (GUI):
○	Clean, responsive design compatible with major web browsers (Chrome, Edge, etc.).
○	Features include a dedicated web application for pre-meeting and post-meeting phases, and a specialized Chrome extension for in-meeting operations.
○	Error notifications with clear, actionable recovery instructions (e.g., “Meeting audio is not audible, please check your microphone settings”).
○	Real-time language translation options for generating meeting transcripts in Urdu.
○	Consistent interface design with standardized navigation controls such as Submit, Next, and Help across all screens.
Hardware Interfaces
●	Input Devices:
○	Microphone for capturing live audio inputs during meetings.
○	Laptop or compatible computing device for system access.
●	Output Devices:
○	Display screen for engaging with the graphical interface.
○	Optional speakers or headphones for enhanced audio feedback.
Software Interfaces
●	Dependencies and Integrations:
○	Python-based libraries and frameworks including Django, PyPDF for document processing, Langchain for conversational AI, Flask for web interfaces, and SR for speech recognition functionalities.
Communications Interfaces
●	Protocols and Standards:
○	HTTP/HTTPS protocols for secure system communication and cloud service integration.
○	WebSocket technology for delivering real-time, low-latency suggestions during active meetings.
○	Data encryption standards utilizing TLS (Transport Layer Security) for securing transmitted information.
○	UTF-8 character encoding to support multilingual capabilities within the system.

System Features
Pre-Meeting Evaluation
Description and Priority:

The system provides AI-driven preparatory assistance to users based on meeting-related queries submitted during the pre-meeting phase. Through interactive dialogues, the assistant evaluates user readiness, suggests relevant questions, and boosts confidence prior to the meeting.
Priority: High
Stimulus/Response Sequences:
●	User accesses the system and selects the “Pre-Meeting” mode.
●	Personalized chatbot engages the user, providing meeting-specific guidance.
●	Users utilize the chatbot for clarifications, agenda reviews, and preparation tips.
Functional Requirements:
●	REQ-1: The system must provide a fully functional, AI-powered chatbot interface.
●	REQ-2: A stable internet connection is required to ensure fast response times and seamless AI interaction.
Meeting Assistance
Description and Priority:
The system operates as an AI-enabled Chrome extension during meetings, capable of recording discussions, generating real-time transcripts, and suggesting context-aware follow-up questions based on ongoing conversations.
Priority: High
Stimulus/Response Sequences:
●	User activates the Chrome extension to initiate the “Meeting” phase.
●	The system captures audio, transcribes speech to text in real time, and monitors meeting progress.
●	AI-generated suggestions and relevant questions are displayed to enhance engagement.
Functional Requirements:
●	REQ-1: Capture live audio and accurately convert speech to text.
●	REQ-2: Identify and highlight critical discussion points during the meeting.
●	REQ-3: Generate relevant, real-time follow-up questions based on conversation flow.
Post-Meeting Summary
Description and Priority:
Upon meeting conclusion, the system produces a comprehensive summary, including an English transcript and a translated Urdu version for broader accessibility and understanding.
Priority: High
Stimulus/Response Sequences:
●	The next step is the start of the phase by the user i.e. the Post-Meeting.
●	The full-scale meeting summary and translations of the same are generated by the net.
Functional Requirements:
●	REQ-1: Get to have a correct meeting summary generated through in-built AI models.
●	REQ-2: The Urdu-speaking population will need to be supported with multilingual facilities such as providing reliable translation of transcripts.
Performance Requirements
●	The system has to process objects in such a procedure inputted at the end user to need feedback true real – time interval of five second.

Safety Requirements
●	Ensure all data is stored securely with access restricted to authenticated users.
●	Provide warnings for unsupported or faulty hardware (e.g., microphone).

Security Requirements
●	Encrypt all user data in transit and at rest using AES-256.
●	Implement user authentication via username and password.
●	Comply with GDPR for data privacy.
Software Quality Attributes
●	Usability: Simple, intuitive interface with minimal learning curve.
●	Reliability: Ensure the system operates without crashing for continuous 3-hour sessions.
●	Scalability: Support multiple concurrent users without noticeable lag.
Business Rules
●	Only registered users can access system features.
●	Meeting data will be archived automatically after 30 days unless deleted by the user.
Other Nonfunctional Requirements
Performance Requirements
The meetIntelli runs designed to operate in the real-time environment with requirements relating to high performance. The processing needs to be low-latency in order to offer smooth user experiences when participating in live meetings. In 5 seconds of receiving the data the system must provide accurate transcripts, artificial intelligence recommendations and summaries of the meetings using real-time speech inputs. Back end services such as the NLP and translation modules are expected to be highly fault tolerant and highly available to meet the current operational requirements.
A potentially more significant factor is resource efficiency and low computational overhead during the times when real-time ideation, and speech-to-text translations synchronize with each other and during the meeting phase. The frontend Chrome extension is not expected to trigger much instability in the browser and system performance.
Safety Requirements
●	The operations on the device should not disrupt the device safety, user data integrity or stability of the system.
●	Strong error processing mechanisms should be available to avoid crashes on important operations.
●	Updates to systems must go through stringent testing to ensure deployment does not expose systems to vulnerabilities and even performance degradation.
Security Requirements
●	All API communication should go through secure communication channels (TLS) to guard the data of the user and avoid unauthorized access.
●	The authorized users of the system should be able to have access control and authentication to limit functionality of the system.
●	Transcripts, stored meeting content, and user data should be encrypted during transmission and when it is stored so that the privacy of data is respected and privacy regulations like GDPR.
●	Input validation needs to be done in the system to eliminate attacks or malicious data submissions through injection.
Software Quality Attributes
●	Reliability: The system must have good performance with reliability at every stage of use.
●	Usability: The systems should be obviously easy to use, have good interfaces that do not require extensive technical expertise to operate.
●	Scalability: System design must be able to support larger user communities and more data processing needs as they arise without affecting performance in a negative way.
●	Maintainability: The codebase is to be built with best practices, be modular and have an extensive documentation of the code so as to provide an easier maintenance and troubleshooting.
●	Portability: The system must have an ability to work or be adaptable on other platforms and operating systems based on requirements defined.

Business Rules
●	The system should be regulated strictly by the organizational policies concerning involving the privacy of data, consent of the users, and ethical use of AI.
●	In order to meet the immediate requirement of the users and the resource gap, translation functionality is currently restricted to English-to-Urdu.
●	AI suggestions made on meetings are made in order to guide users, but are not final, and they are left with the decision making capacity.
Other Requirements
●	Internationalization: The system supports multilingual to allow translation of meeting transcripts; it will start with English and Urdu. Yet to come additions could see the version extend to accommodate additional languages, depending on need and availability.
●	Analytics and Logging: System operations, errors as well as user interactions should be logged in to support performance tracking, debugging and continual upgrading.

Appendix A: Glossary

●	NLP: Natural Language Processing Natural Language Processing (A branch of AI) is concerned with how machines can understand, interpret and generate human language.
●	GDPR: General Data Protection Regulation -A legislative framework that governs the privacy and protection of data of individuals in the European Union.
●	GUI: Graphical User Interface - Visuals that enable the user to operate a system in an intuitive manner including buttons, menus and forms.
●	LLM: Large Language Model Gustavo Diamantino Simoes
●	TLS: Transport Layer Security - Protocol that ensures secured communication between the systems over the networks is encrypted.
●	SR: Speech Recognition - Technology to translate oral speech to texts in realtime.
 










Software Design Specification

 
Introduction
Purpose
This Software Design Specification (SDS) aims to present a clear and systematic technical path toward the development and the deployment of the MeetIntelli software an artificial intelligence (AI) based meeting assistant that can revolutionize the manner in which individuals manage commercial meetings. This specification is an extension of the functional requirements defined in the Software Requirements Specification (SRS) and gives a viable and comprehensive view of the aspects of the interior design, logic and interaction of the parts required to develop the system.
The combination of innovative technologies such as:
•	Real-Time Transcription: Capturing and converting spoken content during meetings into accurate, timestamped text using speech-to-text services and real-time audio processing.
•	Natural Language Processing (NLP): Enabling intelligent chatbot interactions both before and during meetings, facilitating context-aware responses and meaningful assistance to users.
•	Post-Meeting Analytics: Automatically summarizing discussions, identifying key decisions, extracting action items, and offering multilingual (e.g., English and Urdu) transcription and summaries.
This document defines:
•	The system’s architectural design including component breakdown, modular responsibilities, and communication protocols.
•	Data flow between front-end interfaces, backend servers, and AI models to ensure smooth and scalable performance.
•	Integration strategy for external tools and services, including Chrome extensions, speech recognition APIs, and NLP libraries.
•	Design considerations related to performance, maintainability, security, and extensibility.
The SDS serves as a reference for developers, testers, and system architects during the implementation phase and helps ensure that every part of the system aligns with the original objectives. This document will thus aid the objective of making the meeting process more productive, eye-opening and intuitive with the aid of intelligent automation and interaction.
This Software Design Specification covers the end-to-end design and development of MeetIntelli which will be a full stack AI-based meeting assistant platform. The system is designed in a manner that facilitates the productivity levels and the overall efficiency of the professional and academic users through three key phases of the meetings lifecycle namely Pre-Meeting, In-Meeting and Post-Meeting. All the phases are driven by smart automation, sophisticated machine learning models, and on-demand interaction capabilities and are built to deliver a seamless and responsive user experience.
Pre-Meeting Phase
This step is aimed at preconditioning the users of the forthcoming meetings via an intelligent and contextual-aware chatbot interface. Major features are:
•	Changeling one-on-one Chatbot communication: Users interact with a well trained CHATBOT and can have natural conversations to help answer meeting related queries, build context, and conduct pre-briefings.
•	Agenda Structuring: Constructing agenda agendas automatically according to the input of the user, previous discussions or uploaded resources.
•	Document Curation: Uploading and processing of follow-on documents, notes or files and other documents used by the AI to give contextual responses or suggestions.
•	Contextual Setup: The system leverages knowledge relevant to the area and information presented by the user to either simulate questions / answer or can be used to present strategic ideas before the meeting.
In-Meeting Phase
In-Meeting is the phase that allows in-session support and real-time intelligence via a browser extension, so people remain connected and up to date regardless of the meeting session. The key features are:
•	Chrome Extension Integration: A specific MeetIntelli Chrome extension records conversation in live meetings and communicates with backend resources to process.
•	Real-Time Speech Transcription: Spoken data are converted to text in almost real-time with low latency through the use of speech-to-text algorithms.
•	Conversational AI: Users are able to ask the chatbot questions during the meeting about contextual clarification, or mentions of prior discussions, or real-time suggestions.
•	Suggestions: The system can provide recommendations in real-time using live transcriptions and NLP inference, such as proposing real-time insights, identifying action items or illuminating decision points.
Post-Meeting Phase
After a meeting concludes, MeetIntelli automatically processes the collected data to generate meaningful, digestible outcomes for the user. Key outputs include:
•	Automated Summarization: NLP-based summary generation that highlights key takeaways, discussion topics, and conclusions.
•	Multilingual Translation: Support for generating transcripts and summaries in both English and Urdu, ensuring accessibility across user demographics.
•	Keyword and Entity Extraction: Identification of critical entities, dates, decisions, or responsibilities mentioned during the meeting.
•	Sentiment Analysis: Interpretation of speaker tone or sentiment trends to assess meeting atmosphere or emotional context.
•	Actionable Insights: Automatic generation of follow-up tasks, deadlines, and decision logs for enhanced productivity.
System-Level Scope
The technological scope of the work consists of:
•	Frontend Development: A user interface developed in a web application with the latest front end technologies (e.g., React.js) that is not only responsive but also experience friendly among different devices following a natural user flow.
•	Back-End Development: RESTful APIs + WebSocket communication to manage real-time transcription + the chatbot interaction, CORDA data persistence, and user management.
•	Integration of AI Models: Interpretation of pre-trained transformer models will be used (i.e., LLaMA 2 7B via quantized deployment or QLoRA) to implement intelligent conversations and summarization.
•	Database Design: A robust MySQL relational database schema that supports user profiles, chat history, transcript storage, file uploads, and analytics.
•	Security and Authentication: Implementation of secure login mechanisms, token-based authentication (e.g., JWT), and encrypted storage of sensitive data.
This document strictly defines the boundaries of what the initial version of MeetIntelli will support. Future expansions (e.g., integration with calendar systems, task management apps like Notion or Trello, and advanced analytics dashboards) are outside the immediate development scope but are noted for scalability.
 Intended Audience
Stakeholder	Description
Developers	Refer to the SDS to build modular, scalable components based on the architecture.
Project Managers	Use this document to manage timelines, assess risks, and evaluate progress.
QA Engineers	Use the technical specifications to plan and execute test cases for functionality and performance.
External Evaluators	Reference for understanding the project design and technical feasibility.
AI/ML Researchers	May review the NLP integration and model fine-tuning aspects for academic value.
Table 1 : Intended Audience

Definitions, Acronyms, and Abbreviations
Term	Definition
NLP	             Natural Language Processing
DFD	            Data Flow Diagram
ERD	            Entity-Relationship Diagram
LORA / Q-LORA	            Low-Rank Adaptation methods for model       fine-tuning
Ollama	            Lightweight local AI model runtime and inference engine
LangChain	            Framework for integrating language models with custom logic
SR	             Speech Recognition
K
Table 2 : Full Form of the given Acronyms
MeetIntelli is a comprehensive and modular AI-powered meeting assistant designed to transform the traditional meeting lifecycle through the application of advanced computational intelligence. By leveraging state-of-the-art technologies—including Natural Language Processing (NLP), real-time speech recognition, machine translation, and intelligent summarization—the system enables users to prepare, participate in, and analyze meetings with heightened efficiency and insight.
The architecture is client-server-based with cloud-enabled functions to accommodate scalability, and multi-user concurrency at low latency. MeetIntelli is custom-designed to support the requirements of modern business and academic facilities working in distributed or hybrid work conditions. It is designed as adaptable, extensible, and reliable, which makes it versatile in terms of performance sustainability per the different user demonstrations.
 Core Components
MeetIntelli consists of three main system components--Frontend, Backend, and Database--working coordinately to provide a smart and real-time experience of meetings.
Frontend
The frontend acts as the main user interaction component which allows problem free interactions with the backend delivered in form of a visual intuitive and friendly accessible component. It comprises of the following:
•	Web Application Interface: Created with the flask framework, in order to make the page light and quick to load. The framework allows communication with a chatbot, uploading files and scheduling meetings as well as seeing results.
•	Chrome Browser Extension:
o	Direct integration with platforms like Google Meet and Zoom.
o	Live transcription overlay and interaction panel during meetings.
o	Enables users to trigger AI suggestions, bookmark important segments, and ask real-time queries to the chatbot during live discussions.
•	Accessibility Features:
o	Designed with responsiveness in mind to support desktops, tablets, and mobile devices.
o	Incorporates contrast modes, screen-reader compatibility, and scalable text options to accommodate users with varying needs.
Backend
The backend provides the computational and logical backbone of MeetIntelli. Built using a hybrid of Django (for administrative control and session management) and FastAPI (for high-performance APIs), it manages core operations such as:
•	API Management: Robust endpoints for user authentication, chatbot interaction, file and transcript storage, and AI integration.
•	AI/NLP Execution:
o	Real-time question answering
o	Agenda and action point extraction
o	Context-aware recommendations based on meeting history and current content
•	Session and Task Orchestration: Maintains efficient communication between the frontend, AI modules, and persistent storage, enabling seamless user experience even under high concurrency.
•	Reliability Features:
o	Asynchronous processing of heavy AI tasks
o	Logging, error handling, and failover mechanisms to ensure uptime and recoverability
Database
The database is implemented using a MySQL relational schema, responsible for managing structured and unstructured data generated throughout the meeting lifecycle. It ensures:
•	Persistent Storage:
o	User accounts, profiles, and authentication tokens
o	Uploaded documents, meeting agendas, and chatbot query logs
o	Real-time and historical transcripts
o	Summarized insights, emotional tone metrics, and translated versions
•	Data Security and Integrity:
o	Role-based access control and hashed credentials
o	Scheduled backups and support for disaster recovery scenarios
•	Scalable Querying:
o	Optimized indexing for fast retrieval of transcript segments and chatbot interactions
o	Normalized schema to prevent redundancy while maintaining flexibility for future expansion (e.g., analytics dashboards)
 AI and Processing Modules
In addition to its core components, MeetIntelli integrates several specialized modules to support intelligent behavior:
•	Speech Recognition Module:
o	Captures and transcribes live audio using real-time processing algorithms.
o	Lays the foundation for NLP and summarization engines.
•	Natural Language Processing (NLP) Engine:
o	Powered by LLaMA 2 7B models, fine-tuned using QLoRA for efficient deployment.
o	Uses Langchain and Ollama to enhance dynamic chaining, context maintenance, and multi-query response flow.
o	Delivers advanced reasoning capabilities for generating summaries, agendas, and contextual recommendations.
•	Translation Module:
o	Integrates with the Google Translate API to convert English meeting data into Urdu, promoting bilingual accessibility and user inclusivity.
o	Supports real-time and post-meeting translation features.
•	Summarization and Sentiment Analysis:
o	Utilizes OpenAI’s language models to create coherent, concise, and action-oriented summaries.
o	Implements emotional tone detection to provide users with feedback on engagement levels, conversational tone shifts, and potential areas of improvement.
System Characteristics
MeetIntelli’s intelligent design supports the following system-wide capabilities:
•	Modularity: Components are loosely coupled and easily maintainable, supporting integration with new APIs, AI models, or data pipelines.
•	Real-Time Processing: Enables in-meeting features such as transcription, response generation, and live feedback within milliseconds of audio input.
•	Cross-Platform Accessibility: Accessible via web browser and Chrome extension, ensuring wide usability without needing heavy client-side installation.
•	Cloud-Enabled Scalability: The backend and AI services are deployable on cloud infrastructure (e.g., AWS, GCP), enabling auto-scaling and horizontal distribution under load.
•	Security-First Design: Adheres to best practices in data handling, encryption, and user authentication to protect sensitive information.
Strategic Impact
MeetIntelli offers a transformative solution for modern businesses and institutions aiming to:
•	Minimize administrative burdens during meetings
•	Improve knowledge capture and documentation accuracy
•	Foster inclusivity through multilingual support
•	Enhance decision-making through intelligent post-meeting insights
As a fully integrated, AI-driven assistant, MeetIntelli sets the foundation for future automation in professional collaboration.
3. Architectural Design
System Components
Component	Description
Frontend (Flask)	Provides user interaction interfaces, including the web app and Chrome extension for live meetings.
Backend (Django, FastAPI)	Processes NLP tasks, AI recommendations, and facilitates communication between system modules.
Speech Recognition	Converts live meeting audio into accurate, real-time transcripts.
NLP Engine	Utilizes LLaMA 2.7B with fine-tuning (LORA/Q-LORA) for contextual understanding and recommendations.
Translation Module	Integrates Google Translate API to convert meeting summaries into Urdu.
Database (MySQL)	Securely stores user data, transcripts, recommendations, summaries, and AI logs.

Table 3 : Components utilized in the project
3.2 Data Flow Diagram (DFD)
User → Pre-Meeting Chatbot → AI Preparation Assistance  
User → Meeting Phase (Chrome Extension) → Real-Time Transcription & AI Suggestions  
System → Post-Meeting Phase → Summary Generation & Translation  
All interactions and data → MySQL Database for storage and analysis 


Figure 11: Data Flow Diagram of the Overall Workflow
3.3 Architectural Layers and Deployment View
The architecture of MeetIntelli is designed with a layered and modular structure to ensure scalability, maintainability, and smooth integration of system components. Each layer of the architecture is responsible for a distinct set of functionalities, allowing for efficient development, debugging, and system updates. The following outlines the system’s architectural layers and deployment strategy:
1. Presentation Layer
•	Technologies Used: Flask (web application), Chrome Extension (JavaScript/HTML/CSS)
•	Responsibilities:
o	Serves as the user interface (UI) through which end users interact with the MeetIntelli system.
o	The web-based GUI is built using Flask, providing an intuitive dashboard for accessing transcripts, summaries, translations, and chatbot interactions.
o	The Chrome Extension facilitates in-meeting functionalities, including:
	Live meeting audio recording
	Real-time transcript visualization
	Access to AI-generated prompts and responses
	Seamless integration with platforms like Google Meet and Zoom
o	Offers cross-device compatibility and accessibility features for broader user support.
2. Application Layer
•	Technologies Used: Django (core backend), FastAPI (API gateway and async processes)
•	Responsibilities:
o	Acts as the central coordinator between the frontend, database, and AI models.
o	Manages core business logic, including:
	Processing user requests (e.g., chat prompts, transcription queries)
	Authentication and session management
	Meeting lifecycle management (start/stop recording, save data)
o	FastAPI handles high-performance, low-latency RESTful APIs and event-based triggers.
o	Django serves as the main controller for integrating long-running backend workflows such as summarization, data storage, and analytics computation.
AI/NLP Layer
•	Technologies & Tools Used:
o	LLaMA 2.7B fine-tuned with LORA/Q-LoRA
o	Langchain and Ollama for orchestrating prompt chaining and contextual decision-making
o	OpenAI APIs for summarization and sentiment analysis
•	Responsibilities:
o	Provides intelligent features for contextual understanding and generation:
	Generating responses to user queries during meetings
	Recommending follow-up actions and discussion recaps
	Summarizing key discussion points and extracting insights
o	Langchain enables multi-step prompt handling, improving coherence in chatbot replies.
o	NLP models are optimized for speed and relevance using lightweight quantization techniques like Q-LoRA.
Data Layer
•	Technology Used: MySQL (Relational Database)
•	Responsibilities:
o	Acts as the persistent storage for all structured and semi-structured data, including:
	User profiles and login sessions
	Historical transcripts and chatbot interactions
	Generated summaries, sentiment scores, and translation data
o	Implements ACID-compliant transactions to ensure data reliability.
o	Supports backup, recovery, and scaling mechanisms for long-term system growth and robustness.
o	Enables efficient querying and retrieval of historical meetings for analytics and insights.
Deployment View
•	Deployment Strategy:
o	Hosted on a cloud infrastructure (e.g., AWS, GCP, or Azure) to ensure high availability and fault tolerance.
o	All components are containerized using Docker, enabling isolated, portable, and replicable deployments across:
	Development
	Staging
	Production environments
o	Uses Docker Compose or Kubernetes for orchestration, auto-scaling, and service health monitoring.
o	Incorporates CI/CD pipelines for automated build, test, and deployment cycles.
Summary of Architectural Benefits:
•	Modularity: Each layer is independently developed and tested, allowing for isolated upgrades and maintenance.
•	Scalability: Cloud-based deployment and containerization ensure rapid scaling as usage increases.
•	Performance: Low-latency APIs and asynchronous processing support real-time interactions and fast feedback loops.
•	Security: Data encryption, Secure authentication, Container isolation increases the system’s security posture.
•	Extensibility: New features (for example 3rd party integrations with task management tools) may be easily layered in topper of gracile API of the adapter.

This layering brought with it the characteristics that individual modules could be independently developed and that individual units could be maintained; at the same time it allowed easy interaction between the modules. MeetIntelli provides scalable cloud infrastructure to support both current use and future growth to make the system versatile to changing business needs, and changing demand of users.
Detailed Design
Pre-Meeting Phase
The Pre-Meeting Phase of MeetIntelli allows users to effectively prepare the business meetings by using the potential of conversational AI and contextual understanding. This stage allows participants in the meeting to come into the session with the right ideas, mental preparation and the agenda set in a clear manner.

Functional Overview
1.	User Input Interface:
o	The users initiate this step through the web dashboard
o	Particular preparatory data is recorded in input fields
	Meeting title and agenda
	Participant names and roles
	Some discussion points Preliminary
	Meeting objectives or goals
2.	AI-Driven Chatbot Assignation:
o	A personalized chatbot initiates a structured dialogue with the user to:
	Clarify ambiguous agenda points
	Suggest reorganization of topics for flow and clarity
	Recommend missing elements (e.g., stakeholder input, key documents)
o	The chatbot operates using the LLaMA 2.7B model, fine-tuned for conference settings using LORA/Q-LoRA,Fine-Tuning techniques ensuring inconsequential presentation and related accurateness.
3.	Contextual Analysis and Suggestion Engine:
o	AI evaluates the inputs against past meeting patterns and fine-tuned Q/A datasets to:
	Offer relevant resources or articles for pre-reading
	Identify potentially unclear objectives
	Suggest modifications in agenda phrasing for precision
4.	Proactive Preparation Support:
o	Recommends additional data, such as:
	Past meeting notes
	Conflict alerts based on overlapping topics or unclear roles
	Clarification prompts based on linguistic cues
Technological Components
Component	Description
Django API	Backend logic handling input processing, API calls to AI models, and session management.
LLaMA 2.7B	The core language model, fine-tuned on meeting-specific dialogues using the HuggingFace MeetingBank Q/A dataset.
LORA/Q-LoRA	Lightweight fine-tuning and quantization techniques to reduce computational load during inference.
Ollama	Used for model deployment and runtime quantization, enabling low-latency inference.
Langchain	Manages complex AI interactions such as multi-turn conversations and conditional prompt flows for more accurate responses.
Table 4 :  Description of the Given Components
Data Flow (High-Level)
1.	User submits agenda input →
2.	Django backend processes input and forwards to Langchain pipeline →
3.	Langchain formats context-aware prompt for LLaMA 2.7B →
4.	Ollama executes quantized model inference →
5.	Chatbot response returned to user via Django API
Example Interaction
•	User Input: “Meeting to discuss Q3 performance and marketing strategies.”
•	AI Output:
“Would you like to include the sales team in this discussion? Also, would you prefer to break the marketing segment into paid ads and organic reach for clarity?”
Key Benefits
•	Ensures users are better prepared and more confident before meetings.
•	Reduces vagueness and improves agenda alignment.
•	Saves time by offering context-specific suggestions without manual search.
Meeting Phase
The Meeting Phase of MeetIntelli is designed to function as a real-time companion during live meetings, offering seamless speech transcription, conversational support, and intelligent suggestions. This component is activated through a custom Chrome extension that integrates with popular video conferencing platforms such as Google Meet.
Functional Overview
1.	Chrome Extension Activation:
o	The user enables the MeetIntelli Chrome Extension during live virtual meetings.
o	The extension automatically detects the active meeting platform (e.g., Google Meet) and initializes the real-time recording and transcription pipeline.
2.	Audio Capture and Processing:
o	An Audio Capture Module interfaces directly with the browser tab to:
	Record incoming and outgoing voices.
	Maintain low-latency streaming for real-time analysis.
o	The audio data is streamed to the backend in small frames to ensure minimal delay.
3.	Real-Time Speech Recognition:
o	Captured audio is processed through a real-time speech-to-text engine.
o	The transcribed text is streamed live into the system’s NLP pipeline, allowing instant contextual analysis.
4.	Contextual AI Interaction During Meeting:
o	A conversational AI chatbot, built on the fine-tuned LLaMA 2.7B model, continuously monitors the live transcript.
o	It provides:
	Real-time prompts and follow-up questions
	Clarification suggestions
	Summary bullets of ongoing discussions
o	This enables dynamic and context-aware feedback, supporting more focused and productive conversations.
5.	Engagement and Highlight Tracking:
o	The system tracks user activity and conversational dynamics:
	Speaker activity
	Turn-taking patterns
	Frequency of keyword usage
o	Key highlights are flagged for post-meeting insights and future reference.
6.	Data Persistence and Logging:
o	All live transcripts, chatbot interactions, user prompts, and AI responses are:
	Logged in real time
	Stored securely in the MySQL backend database
	Tagged with metadata (timestamps, speaker ID, topic category)
Technological Components

Component	Description
Chrome Extension	Frontline interface capturing audio and relaying browser context to the backend.
Real-time Speech Recognition	Transcribes speech to text with minimal delay, using an ASR model or streaming API.
FastAPI	Handles high-frequency API requests from the Chrome extension for real-time processing.
Ollama	Executes quantized LLaMA 2.7B model queries for fast and efficient AI response generation.
MySQL Database	Stores transcripts, AI responses, user interactions, and engagement data in a structured manner.
Table 5 : Description of the Given Components

Data Flow (High-Level)
1.	User joins meeting and activates Chrome extension →
2.	Audio is captured and streamed to the backend →
3.	Speech recognition transcribes audio in real-time →
4.	Transcripts passed to AI/NLP module via FastAPI →
5.	Ollama + LLaMA 2.7B generate real-time responses →
6.	Suggestions and highlights returned to the user during the meeting →
7.	All logs stored in MySQL for later access
Key Features and Benefits
•	Provides real-time meeting support through intelligent AI interaction.
•	Enables immediate contextual assistance, reducing the need for manual note-taking.
•	Enhances user engagement tracking, ensuring that important points are not missed.
•	Seamlessly connects with the Post-Meeting Phase for continuity in analysis and summary generation.
Post-Meeting Phase
The Post-Meeting Phase of MeetIntelli is dedicated to transforming raw meeting data into structured, actionable insights. Leveraging state-of-the-art NLP tools, this phase provides multilingual summaries, detects discussion sentiment, and highlights key takeaways, empowering users with precise and personalized meeting documentation.
Functional Overview
1.	Automated Summarization:
o	The system ingests the full meeting transcript stored during the in-meeting phase.
o	An OpenAI-powered summarization module:
	Extracts key discussion points
	Identifies action items
	Highlights major decisions made
o	Summaries are generated in a human-readable, bullet-style format for quick review.
2.	Multilingual Support (Urdu Translation):
o	The final English summary is passed through a translation module built on Google Translate API or transformer-based language models.
o	Users receive summaries in both English and Urdu, enhancing accessibility and retention across diverse linguistic backgrounds.
3.	Keyword Extraction and Sentiment Analysis:
o	Advanced NLP models perform:
	Keyword extraction to highlight recurring or emphasized topics.
	Sentiment analysis to evaluate the tone of conversation and participant engagement.
	Topic classification to group content into themes (e.g., finance, strategy, feedback).
4.	Highlighting Critical Insights:
o	The system flags:
	Controversial or emotionally charged segments
	Repeated topics or unresolved issues
	Tasks and deadlines mentioned
o	These insights help managers and participants follow up effectively after the meeting.
5.	User Notification and Access:
o	After processing, users are notified through the dashboard or email.
o	Summaries and insights are available for download or integrated into organizational documentation workflows.
Technological Components
Component	Description
OpenAI Summarization API	Generates condensed summaries from raw transcripts with a focus on clarity and relevance.
Transformers / Google Translate API	Converts summaries into Urdu while retaining contextual accuracy.
Keyword Extraction Module	Identifies high-frequency and context-relevant terms across the conversation.
Sentiment Analysis Engine	Evaluates emotional tone of the meeting, providing feedback on team morale and engagement.
MySQL Database	Stores summaries, keywords, sentiment tags, and user feedback for long-term analysis.
Table 6 : Description of the Given Components
Data Flow (High-Level)
1.	Transcript stored from in-meeting phase →
2.	Summarization module processes and condenses content →
3.	Translation module generates Urdu version →
4.	NLP tools perform keyword extraction and sentiment analysis →
5.	All outputs stored in database and displayed on dashboard
Key Features and Benefits
•	Time-saving summaries allow users to instantly review what happened and what needs to be done.
•	Multilingual output ensures inclusivity and better communication in culturally diverse teams.
•	Sentiment and keyword insights provide an added layer of intelligence for evaluating team dynamics.
•	AI-driven post-meeting documentation replaces manual note-taking, improving productivity and decision-making.



Security Considerations

Security is a critical component of the MeetIntelli system, given its role in handling sensitive business information, user data, and real-time meeting content. The security layer is built with a formidable security framework which takes care of security during communication, access control, protection of data and resilience of the system. The most important security mechanisms incorporated in the system are stated below:
1. Encrypted Communication
•	The cyber-security of all data transfers between the client interfaces (web app and Chrome extension) and the backend services is fortified with the using of the TLS (Transport Layer Security) and the SSL (Secure Sockets Layer) protocols.
•	This encryption will remove the possibility of a man-in-the-middle (MITM) attack, and makes any and all interactions including logins, chatbot messages, and meetings recording vulnerable to eavesdropping and manipulation.
2. Secure Authentication and Authorization
•	User authentication is performed according to the OAuth 2.0 standard which is safe, widely used, and allows managing access to data through tokens.
•	Access tokens are short-lived and securely stored, reducing the risk of credential leakage.
•	Multi-factor authentication (MFA) can be integrated optionally to enhance security for admin or enterprise-level accounts.
3. Role-Based Access Control (RBAC)
•	The platform incorporates RBAC policies to assign permissions based on user roles (e.g., admin, meeting organizer, regular user).
•	This prevents unauthorized access to sensitive operations such as data export, analytics review, or model retraining.
•	RBAC helps maintain principle of least privilege, ensuring users can only perform actions relevant to their roles.
4. Data Encryption and Protection
•	MySQL database encryption mechanisms protect stored data, including user credentials, meeting transcripts, and chat logs.
•	Sensitive data fields (e.g., passwords, summaries, participant names) are encrypted at rest using AES-256 encryption.
•	Passwords are hashed using secure algorithms like bcrypt, further preventing exposure in case of a data breach.

5. Security Against Web Vulnerabilities
•	The system is fortified against common web application threats using:
o	SQL Injection prevention through use of ORM and parameterized queries.
o	Cross-Site Scripting (XSS) prevention through input-validation and output-sanitization.
o	Cross-Site Request Forgery (CSRF) protection using secure tokens in all form-based and API interactions.
•	Frontend and backend code undergo regular static and dynamic security testing.
6. Privacy Compliance and Data Governance
•	MeetIntelli complies with data protection standards including the General Data Protection Regulation (GDPR), ensuring transparency, user consent, and data minimization.
•	Users are empowered with data rights, such as:
o	The right to access and download their data.
o	The right of the user to to request deletion of personal information.
•	Logs and audit trails are maintained for accountability and traceability of user actions.
7. Security Audits and Vulnerability Testing
•	Regular penetration testing and security audits are performed to evaluate system defenses against evolving cyber threats.
•	A vulnerability management system is in place to log, categorize, and remediate any identified issues within predefined SLA timelines.
8. Backup and Disaster Recovery
•	A daily backup routine is scheduled, storing encrypted snapshots of the database in secure cloud storage.
•	A disaster recovery plan (DRP) ensures that services can be quickly restored in case of system failure, ransomware attack, or natural disaster.
•	System uptime and recovery objectives (RTO/RPO) are defined and monitored to ensure business continuity.
Conclusion
MeetIntelli is designed to support confidentiality, integrity, and availability of user information with a multi-protective layer of security protections implemented at the network, application, and data level. Not only do these considerations make the system technically secure, but they also ensure the regulatory compliance and give the user trust.

Performance Requirements
System performance demands are meant to meet and exceed the demand where the system provides a seamless, real time experience in the three phases (Pre-Meeting, Meeting, Post-Meeting) even at its heaviest user load or sessional complexity. These requirements specify the anticipated performance in terms of speed, reliability, scale and responsiveness at both regular and peak times.
1. Real-Time Responsiveness
•	The system should be able to offer real interaction, in particular live meetings.
•	The AI chatbot responses, transcript updates, or user prompt-responses must take no more than 5 seconds; no delay should be noticeable.
•	It is within this constraint that components like the speech recognition engine and the in-meeting chatbot must operate in providing the input and output to the users to ensure satisfaction.
2. Scalable Architecture
•	MeetIntelli is implemented on a microservice-based, cloud-native system and therefore horizontally scalable.
•	It has to support hundreds of concurrent users and many sessions without a detectable performance loss.
•	Such technologies as Docker, Kubernetes (op.), and cloud-based load balancers allow auto-scaling and streamlined distribution of resources.
3. Backend Optimization
•	In the backend, services such as chatbot engine, transcription and summarization functions are tuned to require the least number of CPU and RAM.
•	Where feasible, batch processing and asynchronous task queues (e.g. using Celery and Redis) are deployed to promote throughput and low latency.
4. High Availability
•	The system must maintain an uptime of at least 99.5%, ensuring it remains operational and accessible with minimal disruption.
•	Redundancy is achieved through cloud-based infrastructure (e.g., AWS or Azure), with failover instances and automatic recovery protocols in place.
•	Scheduled downtimes (if any) are communicated in advance and occur during off-peak hours.

5. Low-Latency AI Operations
•	AI-powered features such as chatbot recommendations, in-meeting prompts, and transcript analysis must operate with minimal perceived delay.
•	Average latency for these tasks should remain under 2–3 seconds, with a hard ceiling of 5 seconds during high traffic.
6. System Health Monitoring
•	Continuous monitoring tools (e.g., Prometheus, Grafana, New Relic) are integrated to track system metrics including:
o	CPU/memory usage
o	Response time
o	API request success/failure rates
o	Session volume
•	Automated scaling policies are in place to respond to spikes in usage patterns by provisioning additional instances or containers.
7. Efficient Data Retrieval
•	MYSQL database performance tuning by:
o	Normalized schema design
o	Indexed columns for frequently queried fields
o	Caching mechanisms (e.g., Redis) for high-speed access to recent chat or transcript data
•	These enhancements ensure fast query responses even during data-intensive operations like summary generation or report retrieval.
8. Transcription Accuracy
•	The real-time speech-to-text engine must maintain a transcription accuracy of ≥ 95%, assuming recommended input conditions (e.g., noise-cancelled microphones and stable internet).
•	Models are trained on business conversation datasets to improve performance across accents and professional vocabulary.
Post-Meeting Processing Time
•	After a meeting concludes, summarization and translation modules must complete their tasks within 10 seconds for a meeting duration of up to 60 minutes.
•	The system ensures this by using pre-allocated compute instances, lightweight transformer models, and background job execution.

Load Testing and Stress Validation
•	Regular load testing using tools like JMeter or Locust is conducted to simulate high concurrency and validate:
o	System throughput
o	Memory leaks
o	Recovery time after overload
•	Reports from these tests are analyzed to make further improvements in code efficiency and infrastructure configuration.
Conclusion
Such performance needs will guarantee that MeetIntelli will provide a stable, real time and responsive user experience to all users, whether preparing, in-the-meeting, or post-meeting. The system is designed with robust, intelligent and scalable framework at the forefront of its performance excellence.
Conclusion
MeetIntelli is an end-to-end AI-based meeting assistant tailored to optimize the meeting lifecycle starting with before meeting, during the meetings and after the meetings. By the integration of real-time speech recognition, natural-language processing (NLP) and smarter clouds artificial intelligence into one sleek system, the manual workload is substantially reduced, and the effectiveness of business communications is even enhanced.
The modular, scalable design of the system, based upon cloud-native technologies, allows the system to effectively integrate into collaborative tools like Google Meet, and provides real-time multi-lingual support with speech-to-text transcription and in-line translation capabilities. MeetIntelli runs on a solid backend infrastructure, minimal latency and a high availability platform that can be used under challenging enterprise environments without performance degradation.
The combination of contextual Q&A preparation ahead of the meeting, AI-based suggestions during the meeting and summarization after the meeting, help the platform to automate some of the most significant productivity bottlenecks. This does not only increase user interest and active participation in decisions but also ensures knowledge retention with proper storage of transcripts, keywords and sentiment based feedback.
Moreover, the platform has adopted observed security practices in the industry, such as data encryption, role-based access control, GDPR compliance, and ongoing vulnerability testing, and as such user data and organizational content are safe.


Future Scope
Future versions of MeetIntelli could be directed at:
•	Expanding language support to a variety of languages to collaborate with people all over the world.
•	Incorporating analytical dashboards to establish how participants are engaged, whether there is a trend in the direction of sentiment, and the rate at which action items are being completed.
•	Powering up AI-models to gain deeper contextual insights, emotional analysis, speaker identification, and meeting proactive support.
•	Minimising platform integrations such as support of Microsoft Teams, Zoom and enterprise applications like CRM or project management system.
In essence, MeetIntelli is more than a meeting assistant—it is a smart productivity enabler, built to transform how modern organizations plan, conduct, and reflect on meetings. By combining cutting-edge AI with user-centric design and secure data handling, it lays the groundwork for intelligent, automated collaboration in the workplace of the future.
8. References
●	IEEE Software Engineering Standards
●	Vision and Scope Document for MeetIntelli (Internal)
●	Python Libraries: Django, FastAPI, Flask, Langchain, HuggingFace, Ollama
●	Google Translate API Documentation
●	OpenAI Text Summarization and Sentiment Analysis Resources
●	LLaMA 2.7B Model Documentation
●	GDPR Data Protection Guidelines
9. Appendices
9.1 Glossary
●	NLP: Natural Language Processing
●	GUI: Graphical User Interface
●	DFD: Data Flow Diagram
●	RBAC: Role-Based Access Control
●	TLS: Transport Layer Security
●	API: Application Programming Interface
●	AI: Artificial Intelligence
●	LLM: Large Language Model
●	LORA/Q-LORA: Techniques for optimizing AI model performance
●	CSRF/XSS: Common web vulnerabilities
●	GDPR: General Data Protection Regulation
●	SR: Speech Recognition
 






Test cases
 
Test Case Name: User Registration Test Case
Description:
Verifies the process of user registration, including validations, error messages, and successful account creation.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Prerequisites:
1.	Registration service and database must be functional.
2.	Email verification system (if applicable) should be active.
3.	The registration page must be accessible.
Initial Execution Test Scenario:
New user registers with valid credentials and receives confirmation of account creation.
Table 7 : Test Case 1
Step No.	Step Details	Expected Results	Actual Results	Status
1	Navigate to meetintelli.live/register	Registration form is displayed	Registration page displayed	Pass
2	Enter only name and submit form	Validation error for missing email and password	Validation messages shown	Pass
3	Enter invalid email format and click Register	Error: “Enter a valid email address”	Email format error displayed	Pass
4	Enter mismatching passwords	Error: “Passwords do not match”	Mismatch error displayed	Pass
5	Submit valid name, email, and matching passwords	Account created, redirect to login or confirmation	Redirected to login	Pass
6	Try registering with an already used email	Error: “Email already registered”	Duplicate email error shown	Pass





Test Case Name: Login (User) Test Case
Description:
Verifies the login functionality using various valid and invalid credentials, covering authentication, error handling, and redirection to the main interface.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Prerequisites:
1.	User must already be registered in the system.
2.	The login page of the MeetIntelli platform must be accessible.
3.	The database and authentication service must be functional.
Initial Execution Test Scenario:
User logs in successfully using valid credentials and is redirected to the MeetIntelli dashboard.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Navigate to meetintelli.live/login	System displays the login page	Login page displayed	Pass
2	Enter an unregistered email and any password	Displays error: “Account does not exist”	Error message displayed	Pass
3	Enter a valid email but incorrect password	Displays error: “Incorrect password”	Error message displayed	Pass
4	Leave both fields empty and click “Login”	Displays validation errors: “Email is required”	Validation errors displayed	Pass
5	Enter a valid email in an invalid format	Displays error: “Enter a valid email address”	Email format error displayed	Pass
6	Enter valid email and correct password	User is authenticated and redirected to chatbot/dashboard	Successfully logged in	Pass
7	Click on “Forgot Password” (if available)	Redirects to password recovery/reset page	Page not implemented	Not Executed / Optional
8	Refresh the login page after entering credentials	Fields reset and session not affected	Fields reset	Pass
9	Attempt login with a deactivated or blocked account	Displays error: “Account is deactivated”	No such case in DB	Not Executed
Table 8 : Test Case 2
Test Case Name: Admin User Role Assignment Test Case
Description:
Validates the admin’s ability to assign or revoke user roles and view user activity logs.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Prerequisites:
•	Admin panel accessible
•	At least 1 registered user
Initial Execution Test Scenario:
Admin assigns moderator rights and views activity logs.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Login as admin	Admin dashboard is shown	Dashboard visible	Pass
2	Select a user and assign “Moderator” role	User role updated successfully	Confirmation message shown	Pass
3	Try assigning role to non-existent user	Error message: “User not found”	Error displayed	Pass
4	View activity logs for a user	List of login and meeting activities shown	Logs visible	Pass
5	Revoke moderator rights	Role reverted to standard user	Success message	Pass
Table 9 : Test Case 3


Test Case Name: Edge Case: Meeting with No Audio
Description:
Tests how the system handles a recorded meeting where no one speaks.
Created By: Muhammad Mehdi
Version: 1.0
Date: 19 July 2025
Initial Execution Test Scenario:
Record a meeting with 0 seconds of voice activity.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Start live meeting recording	Recording starts normally	Recorder active	Pass
2	Do not speak for 1 full minute	Transcription shows “No voice detected” or similar	Message shown	Pass
3	End recording	No transcript generated	Empty or “No content” noted	Pass
4	Try exporting empty meeting transcript	Export disabled or generates blank file	Blank PDF downloaded	Pass
5	Ask chatbot about summary of the empty meeting	Message: “No meeting content available”	Accurate message shown	Pass
Table 10 : Test Case 4
Test Case Name: Load Testing for Live Transcription
Description:
Tests the system’s ability to handle transcription during simultaneous meetings.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Prerequisites:
•	Chrome extension installed
•	Server connected to speech-to-text backend
Initial Execution Test Scenario:
Start transcription in multiple concurrent sessions and monitor system performance.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Start 1 meeting and initiate transcription	Transcription runs smoothly	Success	Pass
2	Start 10 meetings from different accounts simultaneously	System handles all sessions, no crash	Acceptable latency	Pass
3	Monitor memory/CPU usage during transcription	Resource usage within threshold	CPU at 70%, memory 62%	Pass
4	Simulate poor network during transcription	Warn user or queue audio locally	Warning displayed	Pass
5	Run transcription for 1+ hour session	Session completes without interruption	Transcription completed	Pass
Table 11 : Test Case 5
Test Case Name: Pre-Meeting Chatbot Interaction Test Case
Description:
This test case verifies that the user can interact with the AI chatbot before a meeting for preparation, and that relevant suggestions and prompts are provided.
Created By: Saad Khan
Version: 1.0
Date: 16 July 2025
Initial Execution Test Scenario:
User interacts with the chatbot to get agenda-based suggestions and guidance before the meeting.
Step No.	Step Details	Expected Results	Actual Results	Status
1	User logs into MeetIntelli and navigates to Pre-Meeting	Chatbot interface is displayed	Chatbot interface shown	Pass
2	User types “How should I prepare for tomorrow’s meeting?”	Chatbot provides structured suggestions and key points	Suggestions displayed	Pass
3	User uploads meeting agenda	Chatbot analyzes and provides relevant questions and tips	Relevant tips and questions shown	Pass
4	User asks an off-topic question	Chatbot informs the question is not related to meeting context	Off-topic handling displayed	Pass
5	User exits the chatbot session	Chatbot session ends and returns to dashboard	Returned to dashboard	Pass
Table 12 : Test Case 6
Test Case Name: In-Meeting Chrome Extension Recording Test Case
Description:
This test case verifies that the Chrome extension records audio during a meeting, transcribes it to text, and allows the chatbot to respond during the session.
Created By: Muhammad Mehdi
Version: 1.0
Date: 16 July 2025
Initial Execution Test Scenario:
User records a meeting session using the Chrome extension and interacts with the chatbot in real-time.
Step No.	Step Details	Expected Results	Actual Results	Status
1	User opens Chrome and activates the MeetIntelli extension	Extension activates and starts listening	Extension active	Pass
2	User clicks “Start Recording”	Recording starts, UI shows active session	Recording starts successfully	Pass
3	User speaks during meeting	Audio is captured and transcribed to live text	Text transcription displayed	Pass
4	User asks chatbot “What did I just say?”	Chatbot summarizes or repeats the last captured sentence	Chatbot repeats accurately	Pass
5	User turns off the internet mid-session	System pauses or shows offline message	Recording paused, offline message shown	Pass
6	User ends meeting and stops recording	System saves text to database for post-meeting use	Audio saved and converted	Pass
Table 13 : Test Case 7
Test Case Name: Post-Meeting Transcript Generation Test Case
Description:
This test case verifies that after a meeting, the system generates a complete transcript in both English and Urdu, and presents it in a readable format.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Initial Execution Test Scenario:
User accesses meeting transcripts and requests summaries in either English or Urdu.
Step No.	Step Details	Expected Results	Actual Results	Status
1	User logs in and navigates to Post-Meeting section	List of recent meetings is displayed	Meeting list displayed	Pass
2	User selects a completed meeting	Transcript is generated and displayed in English by default	Transcript shown in English	Pass
3	User selects “View in Urdu”	Transcript switches to Urdu translation	Urdu version displayed	Pass
4	User clicks “Download Transcript”	System downloads transcript as a PDF file	PDF downloaded successfully	Pass
5	User finds incomplete or missing transcript	System shows error or fallback message	No such error occurred	Not Executed
6	User requests meeting summary instead of full transcript	Summary generated with bullet points or key insights	Summary displayed	Pass
Table 14 : Test Case 8
Test Case Name: Knowledge Base Upload Test Case
Description:
Verifies whether users can upload documents and notes for chatbot training in the Pre-Meeting phase.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Initial Execution Test Scenario:
User uploads relevant meeting documents, and chatbot is enhanced with the uploaded context.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Navigate to Pre-Meeting > Upload Section	File upload section is displayed	Upload interface visible	Pass
2	Upload supported file format (PDF/DOCX)	File successfully uploaded	Upload successful	Pass
3	Upload unsupported file (e.g., .exe or .zip)	Error: “Unsupported file format”	Error message displayed	Pass
4	Upload large file >10MB	Error or loading indicator, depending on size support	Upload successful	Pass
5	Ask chatbot something from uploaded file	Chatbot responds with context-aware answer	Context-based answer provided	Pass
Table 15 : Test Case  9
Test Case Name: Email Summary Export Test Case
Description:
Tests the functionality of sending post-meeting summaries via email to registered users.
Created By: Muhammad Mehdi
Version: 1.0
Date: 19 July 2025
Initial Execution Test Scenario:
User exports a summary of a completed meeting via email.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Navigate to Post-Meeting dashboard	List of completed meetings is shown	Meeting list displayed	Pass
2	Select a meeting and click “Email Summary”	Email dialog box appears	Dialog displayed	Pass
3	Enter invalid email address and click Send	Error: “Enter a valid email address”	Error shown	Pass
4	Enter a valid recipient email and click Send	Confirmation: “Email sent successfully”	Email confirmation shown	Pass
5	Internet is disconnected before sending email	Error or retry option shown	Retry button displayed	Pass
6	Send email without selecting any summary	Error: “Please select a summary first”	Validation error shown	Pass
Table 16 : Test Case 10
Test Case Name: Bilingual Summary Toggle Test Case
Description:
Validates the toggle feature between English and Urdu summaries in the Post-Meeting phase.
Created By: Saad Khan
Version: 1.0
Date: 19 July 2025
Initial Execution Test Scenario:
User switches between languages and verifies that content is displayed correctly in both.
Step No.	Step Details	Expected Results	Actual Results	Status
1	Navigate to Post-Meeting summary view	English summary displayed by default	Summary in English shown	Pass
2	Click “Toggle Language” button	Summary switches to Urdu	Urdu translation shown	Pass
3	Toggle back to English	Reverts to English summary	English displayed again	Pass
4	Refresh page after toggle	Default language (English) is restored	English restored	Pass
5	View a summary that hasn’t been translated	System shows fallback message	“Translation not available”	Pass
Table 17 : Test Case 11


























User manual












Introduction
MeetIntelli is an intelligent meeting assistant platform that has been painstakingly designed to transform how academic and professional users oversee the full virtual meeting lifecycle. Effective meeting management is now a need rather than a luxury in today’s fast-paced digital environment, where virtual collaboration is commonplace. AI-powered solution guarantees that meetings are not only fruitful but also perceptive, well-structured, and significant, and by providing a strong, MeetIntelli fills this urgent need.
Primarily, MeetIntelli functions are categorized in three carefully planned stages: pre-meeting, in-meeting, and post-meeting. Every step concentrates on a certain step of the meeting process that can bring the most advantages and involvement. Pre-Meeting phase helps users prepare fully as it gives a special chatbot where they can ask questions related to the meeting, decode agenda documents that may be attached and make valuable analysis.
MeetIntelli functions in three strategically delivered phases trained within its core- Pre-Meeting, In-Meeting and Post-Meeting phases, each of which focus on a particular phase of the meeting application in order to provide optimum utility and interaction. The Pre-Meeting phase enables the users to be thorough by providing them with a specialized chatbot that engages in meeting-related queries, interprets attached agenda document and also offers smart insights that assist its users in attaining alignment of their goals to that of the meeting purpose. This training will ensure that the MeetIntelli users are equipped to face the meetings with ease, purpose and pertinent information.
On the In-Meeting part, MeetIntelli is a real-time supportive tool through the Chrome extension. Its Users have the ability to initiate or terminate live audio recordings and can also communicate with the AI by providing questions, and possess the option of choosing between the English and the Urdu language to present diverse oral demands. This is so that important moments are not missed. users can also request clarifications, take notes or summarize discussions during meetings, and it is supported by AI in real time.
The meeting ends and leads to the Post-Meeting stage, whereby the meeting automatically advances to transcribing detailed accounts of what went on in the meeting in both English and Urdu. Transcripts provided by MeetIntelli can ensure that the words spoken could be recorded, and they could assist the user in extraction of action items and follow-up, and decisions that are critical. This last step can be valuable in the area of continuity so that it is not hard to revisit the discussions and to sustain momentum either outside of the virtual room or after online meetings are concluded.
MeetIntelli is user-friendly and uncluttered in its navigation and interface as well as in its intelligent PDF reading capabilities, bi-lingual translation, and many other features. MeetIntelli can be customized to your needs and ensuring that no part of the meeting process remains untouched, be it the meeting between a managing/manager and a client, a team lead preparing to have a strategic planning discussion, or a student preparing to defend his/her thesis, MeetIntelli will work to suit your needs.
In conclusion, covering all of the above, MeetIntelli is no longer a tool, it is an intelligent meeting management system. It offers a streamlined solution that will ensure its users to be prepared in advance before the meeting, strong during it, and enlightened thereafter replaces fragmented processes. MeetIntelli’s AI-powered methodology will improve communication, increase output, and also change the virtual meeting process into a more methodical, perceptive, and goal-oriented procedure.

Key Features Overview:
Pre-Meeting Chatbot:
MeetIntelli is prepared for its support journey before the meeting can even start, it uses an intelligent, personalized chatbot. The AI assistant of MeetIntelli is trained to assist users in a variety of different tasks. It can also guide its users through different meeting scenarios and also ensures that they feel confident. The chatbot is somewhat beneficial to its users who require clarification on the topics of the meetings or who wish to brainstorm ideas on what can be discussed in the meeting. The users will also be able to upload the agenda documents (in PDF format) that would be read by the chatbot and analyzed quickly and intuitively.
Chrome Extension Integration:
MeetIntelli power is elegantly incorporated into live meetings through a custom Google Chrome extension that features recording live audio, pausing and pausing recordings and real-time synchronization chatbot. This allows context-aware responses and support from the system during the actual meeting. The users of MeetIntelli can run a high-quality experience of meetings via a few clicks, which means that it could become an ideal tool to be used through teamwork, academic defense, and enterprise conversations. This ability reduces the task of writing things down, as well as eliminates the chances of missing important information when communicating face to face.
In-Meeting Assistant:
The chatbot has continued to provide contextual assistance even during the meeting, by affording the user an opportunity to input prompts or questions relating to the ongoing discussion. As an example, a participant can request the chatbot to explain a technical term in very simple words, without disrupting the interaction of the meeting. It ensures that users stay informed and engaged especially in a scenario involving a great deal of information or a high-stakes situation. MeetIntelli comes in handy to those who should attend cross functional meetings / sessions that are not in their area of expertise where real time understanding is a necessity.
Post-Meeting Dashboard:
MeetIntelli goes further to post-meeting management after meeting. The Post-Meeting Dashboard provides many types of outputs including: bilingual summaries (in Urdu and English), downloadable transcript of the entire conversation, and AI-generated decisions or action items based on the conversation. This attempts to ensure that the momentum of the meeting is not lost or that no one has different modalities when addressing the next line of action. The interface design is intuitive, so one can access, review, and share important results. Also, MeetIntelli frees graphics labor-intensive documentation that saves time and clarity in post-meeting operations.

Bilingual Support:
MeetIntelli has a robust bi-lingual support to all of its features in the awareness of the multi-lingual nature of modern workplaces and classrooms. The user can choose an Urdu and English option in their outputs as they communicate with the chatbot, read the transcripts, or downloading the summary. This one makes the platform more accommodative and accessible to non-english users, so that it works well in bilingual language settings, particularly in the case of teams or students.
Target Audience:
Corporate Professionals and Teams:
MeetIntelli has the potential to fulfill the needs of professional users across various industries who rely on regular virtual meetings to coordinate strategies, share updates, and make critical decisions. the platform simplifies preparation, enhances real-time decision-making, and automates follow-up documentation from project managers and HR leads to client-facing roles and C-suite executives— making each meeting more efficient and result-oriented.
University Students and Research Groups:
Academic users, including students involved in thesis work, group projects, or faculty-supervised research, can benefit immensely from MeetIntelli. The chatbot helps with research alignment and presentation preparation, while the Chrome extension and post-meeting transcripts support the recording and documentation of study group discussions, mock presentations, and advisor meetings.
Remote Workers and Project Managers:
With remote work becoming a permanent fixture, teams often face challenges around time zones, collaboration clarity, and meeting documentation. MeetIntelli supports distributed teams by ensuring real-time transcription, language flexibility, and organized post-meeting summaries. Project managers can use the platform to maintain consistency across meetings, align team members, and ensure accountability.
Individuals Conducting Interviews or Research Discussions:
Researchers, journalists, and interviewers who frequently conduct recorded discussions can use MeetIntelli to their advantage. The real-time capture and transcription of conversations — along with downloadable summaries — simplifies content analysis and improves record-keeping. Its bilingual capabilities make it a valuable tool for professionals working in multilingual environments or with diverse participant groups.

Getting Started
User Login & Authentication
Logging In
•	Begin by navigating to the official MeetIntelli web portal using any modern browser such as Chrome, Firefox, or Edge. Make sure your internet connection is stable for a smooth login experience.
•	On the homepage, locate the “Login” button typically found in the top-right corner of the screen. Click it to open the login interface.
•	You will be prompted to enter your registered email address and password. Ensure that you use the same email you provided during registration. The password field is case-sensitive, so be mindful of capitalization.
•	Once you’ve entered your credentials, click the “Login” or “Sign In” button. The system will verify your credentials through its authentication service. If the credentials are correct, you’ll be redirected to your personalized dashboard, where you can access pre-meeting tools, start new sessions, and view your meeting history and transcripts.

Becoming a MeetIntelli User
Whether for personal, professional, or academic purposes, using MeetIntelli is an easy and effective way to change the way you conduct meetings. Users are immediately given access to the entire range of MeetIntelli’s intelligent meeting assistant features, which are arranged into three functional phases: pre-, in-, and post-meeting. This is after successfully registering and logging in through the secure web portal.
Users can start by navigating the Pre-Meeting section of the platform, where the customized AI chatbot is available to help with meeting setup. The process includes reviewing of previous transcripts, assisting with agenda drafting, responding to research questions, and also partially simulating meetings for clarity or rehearsal. The chatbot will analyze and know PDFs that users upload, like meeting agendas or documents, in order to offer support.
Users of MeetIntelli are advised to use the Chrome Extension to access real-time capabilities during live meetings. Live audio recording, this small yet effective tool offers English and Urdu speech-to-text transcription, and immediate access to the in-meeting chatbot, that connects straight to the web platform. Users can record meetings, ask questions in real time, and create multilingual transcripts from within their browser window after installing the extension.
To summarize it all, MeetIntelli users who join its ecosystem instantly have access to a comprehensive set of tools designed to boost efficiency and simplify the meeting process. There is no complicated learning curve or need for extra sign-ups—just a user-friendly system that is set up to work for you from the beginning and eas your entire user experience.
Features and Functionalities
Pre-Meeting Phase
MeetIntelli’s Pre-Meeting phase’s goal is to make sure that its users are confident, informed, and ready for any upcoming meeting. This phase makes use of a clever, AI-powered chatbot that serves as a digital assistant, in order to help its users efficiently and easily navigate the complexities of meeting preparation.
Chatbot Preparation
Tailored Communication: users can influence its responses by giving the chatbot thorough contextual information beforehand. This entails entering details like the meeting’s topic, attendees, anticipated discussion topics, and any pertinent goals. The chatbot learns to understand context and can adjust its responses appropriately by doing this, and provides a customized experience that look like that of a real assistant that has subject-matter expertise.
• Schema Help: Amongst many abilities of MeetIntelli, one is to intelligently create well-structured and ordered meeting agendas. The chatbot can generate a clear, time-blocked agenda based on user input, such as the meeting’s objectives or important subjects to cover. This results in reducing time waste and increase productivity by enabling meeting hosts to arrive with a well-thought-out plan.
• Information Base Incorporation: MeetIntelli Users can upload relevant documents, that includes presentations, internal memos, notes from prior meetings, and any other background information. these documents are parsed and saved in the chatbot’s internal context in order to use them intelligently when responding to queries, creating briefs, or assisting users in simulating conversations. This integration guarantees continuity throughout meetings by utilizing institutional memory for more intelligent planning.
Preparing for the Meeting
AI-Driven Data Combining: Users ask the chatbot with specific questions like “What are the key discussion points from our last meeting?” or “What do we know about Project’s status?” The chatbot uses its trained context to generate precise, applicable replies that helps its users with saving time searching through files or emails.
• Replicated Q&A Meetings: MeetIntelli users can participate in simulated Q&A sessions with its chatbot to get assistance with public speaking or preparing answers to questions they might encounter in the upcoming meetings. Presenters, interviewers, and students getting ready for oral exams or research defenses will find this especially helpful.
• Conference Minutes Generation: MeetIntelli can also create briefing notes that are clear and informative, it summarizes the user’s goals, important topics of discussion, roles of participants, and any unfinished business. These notes are produced based on previous sessions and current input, which function as a customized briefing document that users can review just before their meetings.
The goal of the pre-meeting phase is to give the user the confidence to feel informed, prepared, and in charge. MeetIntelli creates the conditions for a successful meeting by fusing human inputs and machine intelligence, which in result turns what is usually a stressful process into a smooth and even joyful one.
In-Meeting Phase
MeetIntelli’s In-Meeting phase has the ability to combines sophisticated audio transcription technology with an intelligent chatbot that runs in the background to provide smooth, real-time support during live meetings. This stage can prove to be essential for guaranteeing that significant insights are recorded, prompt clarifications are given, and users can remain completely involved in the conversation without worrying about taking notes or retrieving data.
Chrome Extension Setup
Users must first install the MeetIntelli Chrome Extension, which acts as the entry point for real-time communication, in order to access the in-meeting features. The setup procedure is simple:
1.	 You can get the MeetIntelli Chrome Extension straight from the Chrome Store. The lightweight extension is specifically designed to easily integrate with any browser-based meeting platform, including Microsoft Teams, Zoom Web, and Google Meet.
2.	 User can start the Extension before the meeting they have planned. This guarantees that it will have enough time to establish a connection with the browser tab where their meeting will take places.
3.	To begin the real-time audio capture, click “Start Recording” in the extension. When enabled, the extension passively listens to the audio of the meeting, uses integrated AI models to process speech, and accurately transcribes it in real time.
Real-Time Chatbot Use
MeetIntelli’s intelligent chatbot remains accessible during the meeting, allowing users to interact with it without disrupting the session. This feature is particularly beneficial for users who need to recall prior information or seek clarifications during complex discussions.
•	Contextual Assistance: Users can ask real-time questions, such as “What was discussed about the budget in the last meeting?” or “What action items were assigned to Alex last week?” The chatbot leverages historical transcripts, uploaded notes, and ongoing transcription data to provide immediate, context-aware responses.
•	Non-Disruptive Queries: Since the chatbot operates via the MeetIntelli dashboard or extension pop-up, users can silently communicate with it during meetings without interrupting the speaker. This is ideal for multitasking or discreetly accessing information mid-discussion.
Live Transcription
Automated Speech-to-Text: As the meeting progresses, the Chrome extension captures spoken audio and automatically converts it into text. This live transcription is synced in real-time with the user’s dashboard and the chatbot’s memory, allowing all interactions to remain aligned and up-to-date.
•	Secure Storage: All transcription data is securely stored and encrypted to ensure user privacy and data protection. Transcripts are indexed and organized chronologically, allowing users to review them easily once the meeting concludes.
•	Synced Knowledge Base: The transcribed text is also made available for post-meeting summarization, action tracking, and multilingual processing, this shows MeetIntelli’s follow-up capabilities.
By eliminating the need for manual note taking, enabling dynamic assistance, and guaranteeing that no important detail is missed, these tools collectively revolutionize the in-meeting experience. Every meeting is made more effective and efficient by the In-Meeting phase, which guarantees that users remain present, informed, and supported in real time.
Post-Meeting Phase
MeetIntelli’s Post-Meeting phase is intended to make sure that meetings continue after the call concludes. Rather, it gives users the ability to consider, condense, follow up, and take action on the conclusions and choices reached during the meeting. This stage gives users access to thorough documentation, insightful summaries, and useful follow-up items, all of which are displayed on an easy-to-use dashboard with lots of features.
Dashboard Features
Upon the completion of a meeting, users are directed to their personalized Post-Meeting Dashboard, where the following capabilities are available:
•	Transcripts
o	The complete, time-stamped transcript of the meeting is automatically generated and saved.
o	Users can view it line by line, filter by speaker (if identifiable), and copy or highlight key sections.
o	Transcripts remain stored in the user’s archive for future reference and project tracking.
•	AI-Generated Summaries
o	MeetIntelli’s AI models analyze the full meeting transcript to produce a concise, readable summary.
o	The summary includes categorized segments such as:
	Key discussion points
	Final decisions
	Unresolved questions
	Assigned action items
o	These summaries help users quickly recall and review the meeting outcomes without rereading the entire transcript.
•	Bilingual Translation
o	All transcripts and summaries can be instantly translated between English and Urdu.
o	Users can toggle the language view at any time, making the platform accessible to diverse teams and bilingual users.
o	Translation maintains formatting and semantic accuracy for both languages.
•	Follow-Up Tasks
o	The platform scans the transcript for actionable statements (e.g., “Ali will send the proposal by Friday”) and converts them into follow-up tasks.
o	Each task includes:
	Task description
	Responsible person
	Due date (if mentioned or inferred)
o	Tasks are automatically categorized and displayed in a checklist or timeline format for easy tracking.
Export Options
MeetIntelli understands the importance of flexibility and interoperability when it comes to sharing and utilizing meeting content. Users can export or share meeting outcomes in the following ways:
•	Multi-Format Exports
o	Export the full transcript, AI summary, or both in common file formats such as:
	PDF – Ideal for formal sharing and archiving
	DOCX – Editable document format for collaborative editing
	Plain Text (TXT) – Lightweight version for quick reads or integration with custom workflows
•	Email Summaries
o	Send the meeting summary and key takeaways directly to participants via email.
o	Customize recipients, subject lines, and additional notes before sending.
•	Task Management Integration
o	(Upcoming Feature) Integration with productivity platforms such as:
	Trello
	Notion
	Asana
	ClickUp
o	This will allow direct export of action items into project boards or to-do lists for seamless continuity between meetings and task execution.
The Post-Meeting Phase bridges the gap between conversation and execution. By transforming raw discussions into structured outputs and actionable next steps, MeetIntelli ensures that every meeting ends with clarity, continuity, and concrete deliverables.
FAQs
General Platform Questions
Q: Is MeetIntelli free to use?

A: MeetIntelli offers free access with limited transcript generation. Premium plans offer unlimited usage and more advanced features.
Q: Can I use MeetIntelli without the Chrome extension?

A: Yes, the chatbot is available independently, but the extension is required for live audio capture and real-time transcription.
Q: What languages are supported?

A: Currently, MeetIntelli supports English and Urdu for all chatbot interactions and transcripts.
Q: Do I need an account to use MeetIntelli?

A: Yes, you need to sign in with a registered account to access all phases of the platform, including personalized chat history and transcript storage.
Q: Can I upload documents other than PDFs for meeting preparation?

A: Currently, MeetIntelli supports PDF files for agenda analysis. Future updates may include support for DOCX, TXT, and other formats.
Q: Is my meeting data and transcript private?

A: Absolutely. All meeting recordings and transcripts are securely stored and accessible only by the account holder. MeetIntelli does not share or sell user data.
Q: Can MeetIntelli summarize meetings for me?

A: Yes, in the post-meeting phase, MeetIntelli not only generates transcripts but also provides concise summaries and key takeaways if requested.
Q: What happens if I lose internet connection during a meeting?

A: If the connection is lost during recording, the Chrome extension saves the locally recorded audio. Once reconnected, transcription resumes from the saved data.
Q: Is there mobile support for MeetIntelli?

A: While the chatbot is accessible on mobile browsers, the Chrome extension is currently supported only on desktop Chrome for optimal performance.
Q: How accurate is the voice-to-text transcription?

A: MeetIntelli uses state-of-the-art speech recognition models, ensuring high accuracy in both English and Urdu, even in moderately noisy environments.
Technical Support
Q: The extension isn’t recording my meeting. What should I do?

A: Ensure microphone permissions are enabled in Chrome. Refresh your browser and restart the extension.
Q: I see inaccurate transcript results.

A: Check your audio input quality. Low-quality microphones or excessive background noise can affect accuracy.
Q:  What can I do in so far the chatbot does not answer or remains unresponsive?
A:  In a case where chatbot is silent, the user should refresh the page or clear his or her browser cache. In the event the problem continues, log out and log back in to reset the session.
Q: Some measures to take when the chatbot is not reading the uploaded PDF.
A: make sure that the file you are uploading as PDF is not a scanned file, otherwise not readable. OCR (optical character recognition) support is not introduced yet but will be in future scope.
Q: When the buttons in the Chrome extension are not clickable, what to do?

A:   In the event that the buttons are not clickable, this may be an issue of browsers compatibility. Make sure that you are updated on the latest version of Chrome and that the extension is also the latest and is correctly installed and turned on.
Q: I am unable to download transcript after recording please help me.

A: you need to ensure that your browser can support downloading of extensions. It is also important to look at system downloading folder permission and available storage space.
Q: How to proceed in the case that I clicked the button Start Recording and nothing happens.

A: You should sure that your microphone is correctly selected in your system settings. Restart the browser or reloading the extension.
Q: Why the language switch is not working inside the extension.

A: You can do this by refreshing the extension popup, and also make sure both the language and recording permissions are granted. In case the problem continues, reinstall the extension.
Q: Why my audio cuts out during transcription.

A: The reason behind this is usually unstable internet or hardware issues. You should lose background apps that may interfere with microphone access and test again.
Q: What is the reason behind facing frequent disconnections during live meetings.

A: Make sure to check your internet stability and avoid using VPNs or proxies while recording. Most of the disconnections can interrupt real-time transcription and reduce accuracy.
Support Information
Contact Emails
•	General Inquiries: saadkalizai@gmail.com
•	Technical Help: bscs21108116@szabist.pk
•	Feature Requests: bsai21108133@szabist.pk
Response Time
•	General Support: 24–48 hours
•	Chrome Extension Help: 1–2 business days
•	Transcription Issues: 24 hours
Community Guidelines
Responsible Usage
• Get Member Consent Before Recording:
MeetIntelli is based on the moral values and honors of each meeting participant’s privacy and independence. Therefore, users must get the express and unambiguous consent of all parties, before recording any conversation using the system. The unauthorized recording may also results in trust violations and legal repercussions. The MeetIntelli is not intended to cross organizational or personal boundaries; but rather, it is intended to promote limpidity and teamwork. Users are to ensure that they are not violating any national or international privacy regulations, including the GDPR or similar standard when recording.
• Forbidden Use for Hateful or Illusory Activities:
MeetIntelli use should never be malicious, deceptive, or scheming. Writing false minutes of a meeting, posing as another person, engaging in corporate espionage or attempting to gain unauthorized access to confidential discussions are just some examples of this. Users will make honesty, integrity and professionalism in every engagement facilitated with the platform. The consequence of violating this policy may include a permanent account suspension and a lawsuit by the affected parties and damaging the reputation of MeetIntelli.
Content Security
Encryption and Protected Data Storage:
MeetIntelli applies industry standard encryption standards. Audio, uploaded docs and transcripts are encrypted using secure technologies such as HTTPS and AES-256 encryption when the files are created or uploaded to protect all recorded audio, user-uploaded documents and generated transcripts. This reduces chances of interception or intrusion by ensuring that only users sharing permissions with the data can access their data. Another data integrity-protection mechanism the system employs in the deployment in the organisation setting is role-based access controls.
No Distribution with Other Involvers:
The construction of MeetIntelli is based on user data privacy. The user-generated content (chat logs, agenda PDF, and recordings, or transcripts) are never distributed amongst advertisers, unauthorized internal personnel, or external third parties. MeetIntelli ensures that the users that they have full control of their content and that it is held privately and in utter respect of privacy laws. The privacy, trust, and openness are the principles to be followed throughout the user journey since tight internal policies govern all data handling processes.
Ending Notes
Our vision is to revolutionalize the way professionals organize, conduct and follow up on meetings using the intelligent end-to-end meeting assistant platform, MeetIntelli. MeetIntelli is a customized tool to fit students, teams, educators, business professionals and coworkers of any industry. It was constructed using the latest AI-oriented features and rich knowledge of the contemporary needs of communication. The MeetIntelli platform effectively incorporates many tools and applications into one particular system that offers clear, orthodox, and reformed guidance to its users in all phases of an assembly, ranging through from assembly planning to post-analysis.
Pre-Meeting Phase of  MeetIntelli assists the user achieve readiness in a timely fashion, before the meeting begun. The pre-meeting phase allows to use the dedicated chatbot of MeetIntelli to analyze the uploaded documents, such as agendas or project briefs, interaction with which is also possible during the pre-meeting phase, as well as answer the questions which are specific to the meeting. This guarantees that attendees arrive at meetings with a solid understanding of the background, objectives, and standards. During the meeting, the In-Meeting Phase is activated by a vigorous Google Chrome extension that will provide a real-time voice recording, speech-to-text conversion, support for both English and Urdu, and a prompt input interface that allows the users to engage with the AI assistant of MeetIntelli without interfering with the conversation. this intelligent in-meeting assistant facilitates real-time concept clarification, facilitating more seamless conversations and minimizing misunderstandings, and in addition to recording information.
The Post-Meeting Phase provides an analytical advantage, by automatically creating well-structured meeting transcripts from the recorded audio in both English and Urdu. These transcripts can be downloaded for future research or record-keeping. These transcripts provide a clear, structured account of the meeting’s content, emphasizing key points of discussion. This simplifies the task follow-up, decision review, and dissemination of results to stakeholders or team members who were unable to attend the meeting.
MeetIntelli fosters trust through its dedication to user privacy, unambiguous ethical standards, and prohibition of sharing user data with outside parties, and also increases the productivity. MeetIntelli guarantees that you are always organized, focused, and knowledgeable, transforming every meeting into a significant and influential event, whether you’re managing client relationships, conducting academic research, leading a business team, or holding strategy sessions.





