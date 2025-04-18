from pathlib import Path
import speech_recognition as sr 
from langchain_community.document_loaders import PyPDFLoader
# file upload 
import pyttsx3
file_path = Path(__file__).parent/"tutorial.pdf"
print("file upload done")


# adding loader on file 
loader = PyPDFLoader(file_path=file_path)
print("loader ban gya")

# convert in docs 
docs = loader.load()
print("file ko docs me convert kar diya")


# print(docs)
# print(docs[0].metadata)

#text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter

#creating a text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,  # breaks into chucks with size of 1000
    chunk_overlap = 200 # chunk overlap menas thoda sa pichele se bhi le le taki context loose na ho
)
print("text splitter bna gya hai")

# spliting docs into chunks
split_docs = text_splitter.split_documents(documents=docs)
print("file ke text ko chunks me split kar diya")

# print("docs ki length ", len(docs))
# print()
# print("split_docs ki length ", len(split_docs))


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/text-embedding-004",
    api_key = Api_key  
)

print("text embedder bna gya")
from langchain_qdrant import QdrantVectorStore

collection_loaded = False

try:
    vector_store = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333/",
        collection_name="learning_langchain",
        embedding=embeddings
    )
except:
        vector_store = QdrantVectorStore.from_documents(
        documents=[],
        url="http://localhost:6333/",
        collection_name="learning_langchain",
        embedding=embeddings
    )

    
print("collection bhi ban gya qdrantdb me")

if collection_loaded:
    print("Existing collection was loaded.")
else:
    print("New collection was created.")
    

vector_store.add_documents(documents=split_docs)
print("spitted docs ko qdrant db me save kiya hai means: ")
print("injection done")

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speed (default is around 200)
    engine.setProperty('volume', 1.0)  # Max volume
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can choose male/female voice

    engine.say(text)
    engine.runAndWait()
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
        query=query
    ) 

    # print("relevent chunks :", relevent_chunks)

   

    available_content = "\n".join([chunk.page_content for chunk in relevent_chunks])

    System_prompt = f"""
    you are a helpful assistant that can answer any question but important is context if question is out of context then use your brain and answer 
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

                # system prompt for initial context 

            },
            {
                "role": "user",
                "content": query  # zeroShot prompting 
             }
        ]
    )

    print(result.choices[0].message.content)
    speak_text(result.choices[0].message.content)