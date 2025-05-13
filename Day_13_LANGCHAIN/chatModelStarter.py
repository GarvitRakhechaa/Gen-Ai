from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",)

result = llm.invoke("What is the capital of France?")

print(result.content)
