import os
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir , "db","chroma_db")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embeddings
)

query = "what is Foundations and Core Concepts?"

retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.1}, 
)


# result = db.similarity_search(query=query)
# i = 1
# for r in result:
#     print(f"{i}th document: ",r.page_content)
#     i+=1

relevent_docs = retriever.invoke(query)

print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevent_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")