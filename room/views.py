from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

import os
import google.generativeai as genai
# from langchain.vectorstores import FAISS 
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
# from langchain_community.vectorstores import FAISS

# Create your views here.
@login_required
def rooms(request):
    return render(request, 'room/rooms.html')

@login_required
def room(request):
    return render(request, 'room/room.html')

@login_required
def room_books(request):
    return render(request, 'room/room_books.html')

def search_pyqs(question):
    # embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
    
    database = FAISS.load_local("full_pyqs", embeddings,allow_dangerous_deserialization=True)
    docs = database.similarity_search(question,k=10)

    # chain = start_conversation()

    prompt_template = """
        you are an expert teacher of computer science and your job is to explain the students whatever they ask about related to computer science (CSE).
        The students are trying to prepare for exams so make sure to give answers in detail and  correct as possible . 

        To pepare for GATE exam which is a MCQ type exam , students are trying to find and solve previously asked question in the exams . The context contains those
        questions along with their solutions .

        sudents can either ask for questions related to a particular topic or time and you should show those qustions to them along with answers 
        and detailed explanation. 

        students can also directly give a previous year question and ask for solutions . 

        make sure that your tone is explanatory .

        


        Context:\n {context}?\n
        Question: \n{question}\n

         Answer:

    """

    # model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)


    
    response = chain({"input_documents":docs,"question": question}, return_only_outputs=True)

    # print(response["output_text"])
    return question, response["output_text"]


def search_book(question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
    
    database = FAISS.load_local("full_books_embedding", embeddings,allow_dangerous_deserialization=True)
    docs = database.similarity_search(question,k=20)

   

    prompt_template = """

        you are an expert teacher of computer science and your job is to explain the students whatever they ask about related to computer science (CSE).
        The students are trying to prepare for exams so make sure to give answers in detail and  correct as possible . 

        you know everything about the things mentioned in context .

        your tone should always be explanatory so that students could understand well .


        Context:\n {context}?\n
        Question: \n{question}\n

         Answer:

        
    """
    
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.3)

   

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)


    
    response = chain({"input_documents":docs,"question": question}, return_only_outputs=True)

    # print(response["output_text"])
    return question, response["output_text"]

@login_required
def chat(request):
    if request.method == 'POST':
        query = request.POST.get('content')
        # google api key : AIzaSyBWaGzJb8mHU_QQS-XldHcnc1GgOtSyxDQ
        os.environ["GOOGLE_API_KEY"] = "AIzaSyAiI9HLb4GA7Zm6bi4oeLCEDs5EFai0q9s"
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        question, answer = search_pyqs(query)

        # Process the query as needed

        return JsonResponse({'question': question, 'answer': answer})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
@login_required
def chat_book(request):
    if request.method == 'POST':
        query = request.POST.get('content')
        # google api key : AIzaSyBWaGzJb8mHU_QQS-XldHcnc1GgOtSyxDQ
        os.environ["GOOGLE_API_KEY"] = "AIzaSyAiI9HLb4GA7Zm6bi4oeLCEDs5EFai0q9s"
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        question, answer = search_book(query)

        # Process the query as needed

        return JsonResponse({'question': question, 'answer': answer})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)