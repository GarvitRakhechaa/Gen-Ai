import os
from dotenv import load_dotenv

load_dotenv("../.env")

Api_key = os.getenv('GOOGLE_API_KEY')
Base_url = os.getenv('BASE_URL')

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    api_key = Api_key,
    dimesions=1024
)

print("made a text embedder")
# print("embedding model: ", embeddings)

text = "Hello, how are you? I am fine. Thank you. I am learning Langchain. It is a great library for building LLM applications. I am also learning about embeddings and vector stores. I am using Qdrant as my vector store. It is a great vector store for storing and retrieving embeddings. I am also learning about text splitters. They are used to split text into smaller chunks for better processing. I am also learning about document loaders. They are used to load documents into the system. I am also learning about retrievers. They are used to retrieve relevant documents from the vector store."

text_embeddings = embeddings.embed_query(text)
print("text embeddings: ", text_embeddings)