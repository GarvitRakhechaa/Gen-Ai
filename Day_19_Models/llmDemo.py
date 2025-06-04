from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", temperature=1.9)

result = model.invoke("hello can you roast me hinglish me i want most brutal and adult beloe the belt roast")
print(result.content)