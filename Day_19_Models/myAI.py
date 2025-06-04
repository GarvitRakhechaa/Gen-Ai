from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json
import os

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17")

# Helper function to serialize messages
def serialize_messages(message_list):
    return [{"type": type(msg).__name__, "content": msg.content} for msg in message_list]

# Helper function to deserialize messages
def deserialize_messages(data):
    message_classes = {
        "SystemMessage": SystemMessage,
        "HumanMessage": HumanMessage,
        "AIMessage": AIMessage,
    }
    return [message_classes[item["type"]](content=item["content"]) for item in data]

# Load messages from JSON or start fresh
def load_messages():
    if os.path.exists("messages.json"):
        with open("messages.json", "r") as f:
            data = json.load(f)
        return deserialize_messages(data)
    else:
        return [
            SystemMessage(content="Sunn mere jigri, tu mera desi dost hai jo time management ka ustaad aur web dev, DSA, generative, aur agentic AI ka top coder hai! Jo bhi poochun, fatfat jawab dena hai, bilkul apne doston jaise. Aur haan, zyada lambi kahani tabhi sunana jab main bolun ki 'detail mein batao'.")
        ]

# Save messages to JSON
def save_to_json(message_list):
    with open("messages.json", "w") as json_file:
        json.dump(serialize_messages(message_list), json_file, indent=2)

# Main logic
messages = load_messages()

while True:
    query = input("You: ")
    messages.append(HumanMessage(content=query))
    save_to_json(messages)
    
    if query.lower() == "exit":
        print("Final Messages:", messages)
        break

    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    save_to_json(messages)
    print("AI: ", result.content)

    