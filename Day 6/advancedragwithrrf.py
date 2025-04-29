from pathlib import Path
import speech_recognition as sr 
from langchain_community.document_loaders import PyPDFLoader
# file upload 
import pyttsx3
import json
file_path = Path(__file__).parent/"tutorial.pdf"
print("file upload done")
# ---------------------------------------------------------------------
# speech to text 

import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("😕 Could not understand audio.")
        listen_and_transcribe()
    except sr.RequestError as e:
        print(f"❌ Error from Google API: {e}")




# adding loader on file 
loader = PyPDFLoader(file_path=file_path)
print("made loader")

# convert in docs 
docs = loader.load()
print("using loader conversion of file is done")


# print(docs)
# print(docs[0].metadata)

# text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter

#creating a text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,  # breaks into chucks with size of 1000
    chunk_overlap = 200 # chunk overlap menas thoda sa pichele se bhi le le taki context loose na ho
)
print("made a text_splitter")

# spliting docs into chunks
split_docs = text_splitter.split_documents(documents=docs)
print("splitted the file in chunks")

# print("docs ki length ", len(docs))
print()
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

print("made a text embedder")
from langchain_qdrant import QdrantVectorStore

# collection_loaded = False

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

    
print("done collection in qdrant")

# if collection_loaded:
#     print("Existing collection was loaded.")
# else:
#     print("New collection was created.")
    

vector_store.add_documents(documents=split_docs)
print("injection done")

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speed (default is around 200)
    engine.setProperty('volume', 1.0)  # Max volume
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can choose male/female voice

    engine.say(text)
    engine.runAndWait()
    

retriver = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333/",
    collection_name="learning_langchain",
    embedding=embeddings
)
while True:
    # query = listen_and_transcribe()
    query = input("what you want to know: ")
    # query = "pointers in dsa"


    from openai import OpenAI
    Base_Url = os.getenv("GOOGLE_BASE_URL")

    client = OpenAI(
        base_url= Base_Url,
        api_key= Api_key
    )
    system_prompt_for_query = """
    you are an helpful assistant that helps to understand what user want to say or ask 
    you will process the user query and breakit down and create 2-3 another query based on user query
    Follow the steps in sequnce that is "analyse", "think", "query", "output" peovide one step st a time 

    Rule
    1. Follow the strict  JSON output as per Output schema 
    2. Always perform one step at a time and wait for next input
    3. Carefully analyse the user query
    Output Format: {{ step: "string", content: "string" }} 

    Example
    input: what is pointer in dsa
    Output: {{step: "analyse", content: "Alright! the user is interested in pointers and he asking what is pointers in dsa}}
    Output: {{step: "think", content: "let me break it down and from users query i nedd to make 2-3 query }}
    Output: {{step: "think", content: "here is 3 queries }}
    Output: {{step: "query", content: "defination of pointers}}
    Output: {{step: "query", content: "types of pointers}}
    Output: {{step: "query", content: "definations and example on types of pointer}}
    Output: {{step: "query", content: "use of pointers in different language}}
    Output: {{step: "query", content: "explain pointers with defination and example}}
    Output: {{step: "output", content: "here is all queries that user might want to ask}}
    """
    Messages_for_query = [
            {"role": "system", "content": system_prompt_for_query},
    ]
    Messages_for_query.append({"role": "user","content": query})
    user_queries = []

    while True:
        result1 = client.chat.completions.create(
            model="gemini-2.0-flash",
            temperature =0.9,
            response_format={"type": "json_object"},
            messages = Messages_for_query
        )

        parsed_response = json.loads(result1.choices[0].message.content)
        # print(parsed_response)

        Messages_for_query.append({"role": "assistant", "content": json.dumps(parsed_response)})
        if parsed_response.get("step") == "query":
                print(f"🧠: {parsed_response.get("content")}")
                user_queries.append(parsed_response.get("content"))
                continue
        if parsed_response.get("step") != "output":
                print(f"🧠: {parsed_response.get("content")}")

                continue
        print(f"🤖: {parsed_response.get("content")}")
        break

    print("userqueries are : ",user_queries)

    all_relevent_chunks = []
    for user_query in user_queries:
        relevent_chunks = retriver.similarity_search(
            query=user_query
        )
        all_relevent_chunks.append(relevent_chunks)

    print("all releventchunks are", all_relevent_chunks)
    def reciprocal_rank_fusion(rankings, k = 60):
        result = []
        scores = {}
        content_map = {}
        for ranking in rankings:
            for rank , doc in enumerate(ranking):
                doc_id = doc.metadata['_id']
                scores[doc_id] = scores.get(doc_id,0) + 1 / (k + rank + 1)
                content_map[doc_id] = doc.page_content
                
        for doc_id, score in scores.items():
            result.append({
                'content': content_map[doc_id],
                'score': score
            })
        result = sorted( result, key = lambda x: x["score"], reverse= True)
        return result
   

    unique_relevent_chunks = reciprocal_rank_fusion(all_relevent_chunks)
    # print(unique_relevent_chunks)
    print("relevent chunks :", unique_relevent_chunks)
    

    
    
    available_content = "\n".join([chunk["content"] for chunk in unique_relevent_chunks])

    System_prompt = f"""
    you are a helpful assistant that can answer any question but important is context if question is out of context then use your brain and answer if question is out of context then say naa ye to nhi hai pdf 
    if question under context then you will answer of any question
    example :
    context = pointers
    input: joke on pointer
    output: you will tell joke 
    
    example 
    context = pointers
    input: why sky is blue
    output: ye to out of syllabus hai 
    Context:
    {available_content}
    """





    Messages_for_result = [
            {"role": "system", "content": System_prompt},
            {"role": "user","content": query},
    ]

    result = client.chat.completions.create(
        model="gemini-2.0-flash",
        temperature =0.9,
        messages = Messages_for_result
    )

    print("answer: ",result.choices[0].message.content)
    speak_text(result.choices[0].message.content)