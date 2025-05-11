from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
loader = TextLoader("Phase 1 Foundations and Core Concep.txt")
documents = loader.load()
from langchain_ollama import OllamaEmbeddings
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)

texts = text_splitter.split_documents(documents)
# print(texts[0])

embeddings = OllamaEmbeddings(
    model="gemma:2b",
)

db = FAISS.from_documents(texts, embeddings)

query = " what is Foundations and Core Concepts"
docs = db.similarity_search(query)

# print("documents are",docs[0].page_content)

#retrivaer

retriver = db.as_retriever()
result_docs = retriver.invoke(query)
# print("retriever documents are",result_docs[0].page_content)

similarity_score = db.similarity_search_with_score(query)
print("similarity score are",similarity_score[0][1])

embeddings_vectors = embeddings.embed_query(query)

similarity_with_vector = db.similarity_search_by_vector(embeddings_vectors)
# print("similarity with vector are",similarity_with_vector[0].page_content)

similarity_with_score_by_vector = db.similarity_search_with_score_by_vector(embeddings_vectors)
print("similarity with score by vector are",similarity_with_score_by_vector[0][1])

# saving the faiss index
db.save_local("faiss_index")

# loading the faiss index
mew_df = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization= True)
docs = mew_df.similarity_search(query)
print("documents are",docs[0].page_content)