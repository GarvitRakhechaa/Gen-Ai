import os
from dotenv import load_dotenv
# import openai


load_dotenv("../.env")

Groq_api_key = os.getenv('GROQ_API_KEY')
# print(Groq_api_key)
from langchain_groq import ChatGroq
# # from langchain_openai import ChatOpenAI

# # model=ChatGroq(model="Gemma2-9b-It",groq_api_key=Groq_api_key)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    groq_api_key=Groq_api_key,
    # other params...
)


# # print(model)
# from langchain_core.messages import HumanMessage, SystemMessage
# # messages = [
# #     SystemMessage(content="You are a helpful assistant that helps by answering the question ."),
# #     HumanMessage(content="Question: How do I create a function in Python?")
# # ]

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]

response = llm.invoke(messages)
print(response)