# from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="gemma:2b") 

# print(embeddings)

r1 = embeddings.embed_documents([
    "The quick brown fox jumps over the lazy dog.",
    "The rain in Spain stays mainly in the plain.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold."
])

print(len(r1[0]))

r2 = embeddings.embed_query("The quick brown fox jumps over the lazy dog.")
print(len(r2))