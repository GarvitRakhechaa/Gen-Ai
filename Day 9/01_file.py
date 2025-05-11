import os
from dotenv import load_dotenv

load_dotenv("../.env")

Api_key = os.getenv('GOOGLE_API_KEY')
Base_url = os.getenv('GOOGLE_BASE_URL')
Langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
Langchain_training_key = os.getenv('LANGCHAIN_TRACING_V2')
Langchain_project = os.getenv('LANGCHAIN_PROJECT')
# print("API Key:", Api_key)
# print("Base URL:", Base_url)
# print("Langchain API Key:", Langchain_api_key)
# print("Langchain Training Key:", Langchain_training_key)
# print("Langchain Project:", Langchain_project)

from langchain_google_genai import ChatGoogleGenerativeAI

llm= ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

#simple query
# print(llm.invoke("whats happening 22 april 2025 in pahalgaam ?").content)

# chat template 
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers every  questions .",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
result = chain.invoke(
    {
        "input": "bro do you have real time knowledge",
        
    }
)
# print(result.content)

#stroutput parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

print(chain.invoke({"input": "is pok part of india ?"}))