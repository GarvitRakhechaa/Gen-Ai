import os 
from dotenv import load_dotenv

load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    api_key = Api_key,
    dimesions=1024
)

from langchain_community.vectorstores import FAISS

newVectorDB = FAISS.load_local("ChaiCodeVectordb", embeddings,allow_dangerous_deserialization=True)
query = input("Enter your query: ")
response = newVectorDB.similarity_search(query)

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


from langchain_google_genai import ChatGoogleGenerativeAI

llm= ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.8,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
)

sources = list({doc.metadata["source"] for doc in response})
# print(sources)
prompt= ChatPromptTemplate.from_template(
    '''
    You are a helpful assistant. that answer every question but first priority is to give an answer based on the context provided below.
    Context: {context} 
    Question: {input}
    Answer:
    '''
)

document_chain = create_stuff_documents_chain(llm,prompt)

result = document_chain.invoke(
    {
        "input": query,
        "context": response # this is a document object not a string
    }
)
final_answer = f"{result}\n\nSource: ({sources})"
print(final_answer)
