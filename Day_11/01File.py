import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv("../.env")
groq_api_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1 ")

# Initialize model
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=groq_api_key,  # Directly pass API key
    base_url=groq_base_url,  # Directly pass base URL
)

# Messages
messages = [
    SystemMessage(content="You are a helpful assistant that explains programming concepts."),
    HumanMessage(content="Question: How do I create a function in Python?")
]

# Invoke model
try:
    response = llm.invoke(messages)
    print(response.content)
except Exception as e:
    print("Error:", str(e))