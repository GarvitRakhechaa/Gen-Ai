import os
from dotenv import load_dotenv

load_dotenv("../.env")

Api_key = os.getenv('GOOGLE_API_KEY')
Base_url = os.getenv('GOOGLE_BASE_URL')
Langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
Langchain_training_key = os.getenv('LANGCHAIN_TRACING_V2')
Langchain_project = os.getenv('LANGCHAIN_PROJECT')

#data scrape using langchain

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.chaicode.com/youtube/chai-aur-git/terminology/")
#1. load data
data = loader.load()
# print("Data 0: ",data)
# for doc in data:
#     print(doc.page_content)

# load data --> Docs --> divide into chunks --> text --> vector --> vector embeddings -->vector store --> retriever --> LLM

#2. text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=600,chunk_overlap=50, )

docs = text_splitter.split_documents(data)
# i = 1
# for doc in docs:
#     print(f"{i}th doc = ",doc.page_content) 
#     print("--------------------------------------------------")
#     i+= 1


#3. embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    api_key = Api_key,
    dimesions=1024
)


#4. vector store
from langchain_community.vectorstores import FAISS
vectordb = FAISS.from_documents(docs, embeddings)

# print("vectordb: ",vectordb)
#5. retriever
query = "Git and people who use it talk in a different terminology"
retriver = vectordb.similarity_search(query)

# print("retriver: ",retriver)

# print(retriver[0].page_content)

# k =1
# for r in retriver:
#     print(f"{k}th content: ",r.page_content)
#     print("--------------------------------------------------")
#     k+=1

context = " ".join([r.page_content for r in retriver])
# print("Full context: ",context)


from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


from langchain_google_genai import ChatGoogleGenerativeAI

llm= ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


prompt= ChatPromptTemplate.from_template(
    '''

    You are a helpful assistant. Answer the question based on the context provided below.
    Context: {context}
    Question: {input}
    Answer:
    '''
)

document_chain = create_stuff_documents_chain(llm,prompt)
# print(document_chain)
# from langchain_core.documents import Document
result = document_chain.invoke(
    {
        "input": "how to Check your git repository",
        "context": retriver # this is a document object not a string
    }
)
print("answer is: ",result)