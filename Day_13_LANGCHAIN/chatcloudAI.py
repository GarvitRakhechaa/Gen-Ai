from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
PROJECT_ID = "aichat-ffbc1"
SESSION_ID = "user1"
COLLECTION_NAME = "chat_history"

print("Initializing Firestore client...")
client = firestore.Client(project=PROJECT_ID)

print("Initializing Firestore client...")

chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

print("Chat history initialized.")

# print("Current chat History: ", chat_history.messages)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


while True:
    human_input = input("Enter your question: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    print("AI: ", ai_response.content)
    chat_history.add_ai_message(ai_response.content)
