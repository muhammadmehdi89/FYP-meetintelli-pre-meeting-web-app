'''from django.shortcuts import render
from langchain.llms import Ollama
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain




ollama = Ollama(base_url='http://localhost:11434', model='meetintelli')


def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = Ollama(base_url='http://localhost:11434', model='meetintelli')

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


def user_input(request):
    if request.method == "POST":
        user_question = request.POST.get("question", "")
        uploaded_files = request.FILES.getlist("pdf_files")

        # Extract text from the uploaded PDF files
        context = get_pdf_text(uploaded_files)

        # Create the conversational chain
        chain = get_conversational_chain()

        # Generate the response
        response = chain(
            {"input_documents": [{"page_content": context}], "question": user_question},
            return_only_outputs=True
        )

        # Render the response to the user
        return render(request, "chatbot.html", {"reply": response["output_text"]})

    return render(request, "chatbot.html")



# Create your views here.
def home(request):
    #print(ollama('who are you'))
    
    context = {
        "title": "Welcome to MeetIntelli Chatbot",
        "description": "Upload your PDF documents and ask questions to get detailed answers from the content.",
    }
    return render(request, "index.html", context)'''


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatSession, ChatMessage
from langchain_community.llms import Ollama
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
from PyPDF2.errors import PdfReadError
from django.utils import timezone

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = Ollama(base_url='http://localhost:11434', model='meetintelli')

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

ollama = Ollama(base_url='http://localhost:11434', model='meetintelli')

@login_required
def home(request):
    # Get or create active session
    if request.method == "POST" and "switch_session" in request.POST:
        # Handle session switching
        session_id = request.POST.get("session_id")
        if session_id:
            active_session = ChatSession.objects.filter(
                id=session_id, 
                user=request.user
            ).first()
            if not active_session:
                active_session = ChatSession.objects.create(
                    user=request.user, 
                    title=f"Chat {timezone.now().strftime('%Y-%m-%d %H:%M')}"
                )
    else:
        active_session = ChatSession.objects.filter(user=request.user).order_by('-updated_at').first()
        if not active_session:
            active_session = ChatSession.objects.create(
                user=request.user, 
                title=f"Chat {timezone.now().strftime('%Y-%m-%d %H:%M')}"
            )
    
    # Rest of your view code remains the same...
    chat_sessions = ChatSession.objects.filter(user=request.user).order_by('-updated_at')
    
    if request.method == "POST":
        # Handle new chat creation
        if "new_chat" in request.POST:
            new_session = ChatSession.objects.create(
                user=request.user,
                title=f"Chat {timezone.now().strftime('%Y-%m-%d %H:%M')}"
            )
            return redirect('home')
        
        # Handle clear chat
        elif "clear_chat" in request.POST:
            ChatMessage.objects.filter(session=active_session).delete()
            return redirect('home')
        
        # Handle PDF removal
        elif "remove_pdf" in request.POST:
            request.session["uploaded_context"] = ""
            return redirect('home')
        
        # Handle normal chat message
        elif "question" in request.POST:
            user_question = request.POST.get("question", "")
            uploaded_files = request.FILES.getlist("pdf_files")
            uploaded_context = request.session.get("uploaded_context", "")

            if uploaded_files:
                uploaded_context = get_pdf_text(uploaded_files)
                request.session["uploaded_context"] = uploaded_context

            input_documents = [Document(page_content=uploaded_context, metadata={})] if uploaded_context else []
            chain = get_conversational_chain()
            response = chain(
                {"input_documents": input_documents, "question": user_question},
                return_only_outputs=True
            )

            ChatMessage.objects.create(
                session=active_session,
                question=user_question,
                response=response["output_text"]
            )
            
            if active_session.messages.count() == 1:
                active_session.title = user_question[:50] + ("..." if len(user_question) > 50 else "")
                active_session.save()
    
    # Get messages for active session
    chat_history = [
        {"question": msg.question, "response": msg.response, "timestamp": msg.timestamp}
        for msg in active_session.messages.all()
    ]
    
    return render(request, "index.html", {
        "chat_history": chat_history,
        "pdf_uploaded": bool(request.session.get("uploaded_context", "")),
        "chat_sessions": chat_sessions,
        "active_session_id": active_session.id
    })

# Keep your existing utility functions (get_pdf_text, get_conversational_chain)