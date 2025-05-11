from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

loader = TextLoader("Phase 1 Foundations and Core Concep.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

texts = text_splitter.split_documents(documents)

embeddings = OllamaEmbeddings(
    model="gemma:2b",
)

vectordb = Chroma.from_documents(texts, embeddings)

query = " what is Foundations and Core Concepts"
docs = vectordb.similarity_search(query)

# print("documents are",docs)

#saving the chroma index
vectordb = Chroma.from_documents(texts, embeddings, persist_directory="chroma_index")

# loading the chroma index
db2 = Chroma(persist_directory="chroma_index", embedding_function=embeddings)
docs = db2.similarity_search(query)
# print("documents are",docs[0].page_content)


#retrivaer
retriver = vectordb.as_retriever()
result_docs = retriver.invoke(query)
print("retriever documents are",result_docs)