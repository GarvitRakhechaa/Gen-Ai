import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st



from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import strOutputParser
from langchain_core.output_parsers import StrOutputParser


load_dotenv("../.env")

Api_key = os.getenv('GOOGLE_API_KEY')
Base_url = os.getenv('GOOGLE_BASE_URL')
Langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
Langchain_training_key = os.getenv('LANGCHAIN_TRACING_V2')
Langchain_project = os.getenv('LANGCHAIN_PROJECT')

prompt = ChatPromptTemplate.from_messages([
    {"role":"system","content":"you are a helpful assistant that helps with coding"},
    {"role":"user","content":"Question: {question}"}
])


st.title("ChaiDocs Api")

input_text = st.text_input("Enter your question here")

llms = Ollama(model="gemma:2b")
output_parser = StrOutputParser()

chain = prompt|llms|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))