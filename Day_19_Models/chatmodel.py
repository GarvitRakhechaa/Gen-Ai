from langchain.
# Initialize the ChatOllama model
# Ensure you have Ollama running locally and the desired model pulled (e.g., ollama pull llama2)
chat_model = ChatOllama(model="llama2")

# Example usage:
response = chat_model.invoke([
    HumanMessage(content="Hello, how are you?")
])

print(response.content)
