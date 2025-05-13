import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
# import openai


load_dotenv("../.env")

Groq_api_key = os.getenv('GROQ_API_KEY')
Groq_base_url = os.getenv('GROQ_BASE_URL')
from groq import Groq
client = Groq(
    api_key= Groq_api_key,
    base_url=Groq_base_url,
)
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    client=client,
)




print(llm)
messages = [
    SystemMessage(content="You are a helpful assistant that helps by answering the question ."),
    HumanMessage(content="Question: How do I create a function in Python?")
]



response = llm.invoke(messages)
print(response.content)