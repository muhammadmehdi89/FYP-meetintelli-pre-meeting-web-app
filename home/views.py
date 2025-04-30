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


from django.shortcuts import render
from langchain_community.llms import Ollama
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document  # Import the Document class

ollama = Ollama(base_url='http://localhost:11434', model='meetintelli')

from PyPDF2.errors import PdfReadError

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except PdfReadError:
            text += "\n[Error: Unable to read this PDF file. It might be corrupted or invalid.]\n"
    return text


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. 
    If the answer is not in the provided context, just say, "answer is not available in the context." Don't provide a wrong answer.

    Context:
    {context}?

    Question: 
    {question}

    Answer:
    """
    model = Ollama(base_url='http://localhost:11434', model='meetintelli')
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def home(request):
    # Retrieve chat history and uploaded PDF context from the session
    chat_history = request.session.get("chat_history", [])
    uploaded_context = request.session.get("uploaded_context", "")

    if request.method == "POST":
        # Check if the user clicked "Clear Chat"
        if "clear_chat" in request.POST:
            # Clear the chat history from the session
            request.session["chat_history"] = []
            chat_history = []  # Empty chat history in the current view

        elif "remove_pdf" in request.POST:
            # Clear uploaded PDF context
            request.session["uploaded_context"] = ""
            uploaded_context = ""  # Clear uploaded context in the current view

        else:
            # Otherwise, it's a normal chat, so process the user question
            user_question = request.POST.get("question", "")
            uploaded_files = request.FILES.getlist("pdf_files")

            # If new files are uploaded, extract text and update session
            if uploaded_files:
                uploaded_context = get_pdf_text(uploaded_files)
                request.session["uploaded_context"] = uploaded_context

            # Prepare the input documents for the chain
            input_documents = [Document(page_content=uploaded_context, metadata={})] if uploaded_context else []

            # Create conversational chain and generate response
            chain = get_conversational_chain()
            response = chain(
                {"input_documents": input_documents, "question": user_question},
                return_only_outputs=True
            )

            # Append new chat history entry and store it in session
            chat_history.append({"question": user_question, "response": response["output_text"]})
            request.session["chat_history"] = chat_history

    return render(request, "index.html", {"chat_history": chat_history, "pdf_uploaded": bool(uploaded_context)})



