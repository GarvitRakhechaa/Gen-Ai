from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",)

# result = llm.invoke("What is the capital of France?")

chat_history = []

system_message = SystemMessage("you are an expert in Mathematics and donw phd in Mathematics")
chat_history.append(system_message)

while True:
    query = input("Enter your question: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    result = llm.invoke(chat_history)
    print("AI: ", result.content)
    chat_history.append(AIMessage(content=result.content))

