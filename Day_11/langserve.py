from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

load_dotenv("../.env")
Groq_api_key = os.getenv('GROQ_API_KEY')

app = FastAPI()
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=Groq_api_key)