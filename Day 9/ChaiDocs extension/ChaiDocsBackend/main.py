# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# LangChain imports
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv("../../../.env")
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize embeddings and vector DB
try:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        api_key=API_KEY,
        dimensions=1024
    )
    vector_db = FAISS.load_local("ChaiCodeVectordb", embeddings, allow_dangerous_deserialization=True)
except Exception as e:
    raise RuntimeError(f"Error loading vector database: {e}")

# LLM and Prompt
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.8)

prompt = ChatPromptTemplate.from_template('''
You are a helpful assistant. Prioritize answering based on the context provided. if you find question is not related to any context just say "sorry I cannot answer this question".
if someone greets you can greet them back. IF question is related to greeting or chit chat you can answer it based on your knowledge.
you are made by Chai and you are a part of ChaiDocs. and you are a helpful assistant. you can answer every question but first priority is to give an answer based on the context provided below.
user can ask about you or docs then answer your self 
answer should be in a json if user is asking for a code or json.
Context: {context} 
Question: {input}
Answer:
''')

document_chain = create_stuff_documents_chain(llm, prompt)

# FastAPI Setup
app = FastAPI()

# Allow CORS for your browser extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    print("QueryRequest model initialized")

@app.post("/api/ask")
async def ask_bot(request: QueryRequest):
    try:
        query = request.query
        response_docs = vector_db.similarity_search(query)
        sources = list({doc.metadata["source"] for doc in response_docs})

        result = document_chain.invoke({
            "input": query,
            "context": response_docs
        })

        return {
            "answer": result,
            "sources": sources
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))