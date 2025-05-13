from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",)

# result = llm.invoke("What is the capital of France?")


messages = [
    SystemMessage("you are an expert in social media content strategy"),
    HumanMessage("What are some tips for creating engaging content on Instagram?"),
    
]

result = llm.invoke(messages)

print(result.content)