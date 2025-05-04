from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
file_path = Path(__file__).parent/"tutorial.pdf" 
print("file upload done")


loader = PyPDFLoader(file_path=file_path)
print("made loader")

docs = loader.load()
print("using loader conversion of file is done")

print(docs[4].page_content)


from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,  # breaks into chucks with size of 1000
    chunk_overlap = 200 # chunk overlap menas thoda sa pichele se bhi le le taki context loose na ho
)
print("made a text_splitter")


split_docs = text_splitter.split_documents(documents=docs)
print("splitted the file in chunks")

print("docs ki length ", len(docs))

print("split_docs ki length ", len(split_docs))


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    api_key = Api_key  
)

print("made a text embedder")
from langchain_qdrant import QdrantVectorStore



try:
    vector_store = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333/",
        collection_name="learning_langchain",
    )
except:
        vector_store = QdrantVectorStore.from_documents(
        documents=[],
        url="http://localhost:6333/",
        collection_name="learning_langchain",
        embedding=embeddings
    )
        print("done collection in qdrant")

        vector_store.add_documents(documents=split_docs)
        print("injection done")
        

    
while True:
    retriver = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333/",
        collection_name="learning_langchain",
        embedding=embeddings
    )
    
    query = input("what you want to know: ")
    
    if query == "bye":
        break
    
    relevent_chunks = retriver.similarity_search(
        query = query,
    ) 

    # print("relevent chunks :", relevent_chunks[0].metadata['page'])

   

    available_content = "\n".join([chunk.page_content for chunk in relevent_chunks])

    # print("available content = ",available_content)
    System_prompt = f"""
    you are a helpful assistant that can answer any question but important is context if question is out of context then dont answer just book me nhi hai
    Context:
    {available_content}
    """

    from openai import OpenAI
    Base_Url = os.getenv("GOOGLE_BASE_URL")

    client = OpenAI(
        base_url= Base_Url,
        api_key= Api_key
    )

    Messages = [
            {"role": "system", "content": System_prompt},
    ]

    result = client.chat.completions.create(
        model="gemini-2.0-flash",
        temperature =0.9,
        messages = [
            {
                "role": "system",
                "content": System_prompt

                

            },
            {
                "role": "user",
                "content": query  
             }
        ]
    )

    print(result.choices[0].message.content)

