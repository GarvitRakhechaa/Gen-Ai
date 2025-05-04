from pathlib import Path
import json
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
    
    # query = input("what you want to know: ")
    query = "what is pointer"
    if query == "bye":
        break


    
    
    System_prompt_query = f"""
    you are a helpful assistant that analuse the user query and provides 3 questions related to the query
    Follow the steps in sequnce that is think", "query", "query","query","query", "output" peovide one step step a time and follow the steps dont provide any other steps


    Rule
    Carefully analyse the user query
    think about what user want to know or ask
    Always perform one step at a time and wait for next input
    Output Format: {{ step: "string", content: "string" }}


    Example
    input: what is pointer in dsa
    Output: {{step: "think", content: "let me break it down and from users query i need to make 3 querys"}}
    Output: {{step: "query", content: "defination of pointers"}}
    Output: {{step: "query", content: "types of pointers"}}
    Output: {{step: "query", content: "definations and example on types of pointer"}}
    Output: {{step: "query", content: "use of pointers in different language"}}
    Output: {{step: "query", content: "explain pointers with defination and example"}}
    Output: {{step: "output", content: "here is all queries that user might want to ask "defination of pointers", "types of pointers", "definations and example on types of pointer", "use of pointers in different language", "explain pointers with defination and example"}}
    """

    Messages_query = [
            {"role": "system", "content": System_prompt_query},
    ]
    Messages_query.append({"role": "user", "content": query})
    user_queries = []

    from openai import OpenAI
    Base_Url = os.getenv("GOOGLE_BASE_URL")

    client = OpenAI(
        base_url= Base_Url,
        api_key= Api_key
    )

    while True:
        result = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages = Messages_query
        )

        # print(result.choices[0].message.content)
    
        parsed_response = json.loads(result.choices[0].message.content)
        Messages_query.append({"role": "assistant", "content": json.dumps(parsed_response)})
    
        if parsed_response.get("step") == "think":
                    print(f"🧠: {parsed_response.get("content")}")
                    continue
        if parsed_response.get("step") == "query":
                    print(f"🧠: {parsed_response.get("content")}")
                    user_queries.append(parsed_response.get("content"))
                    continue
        if parsed_response.get("step") == "output":
            print(f"🤖: {parsed_response.get("content")}")
            break

    # print("userqueries are : ",user_queries)

    all_relevent_chunks = []
    for user_query in user_queries:
        relevent_chunks = retriver.similarity_search(user_query)
        all_relevent_chunks.append(relevent_chunks)

    print(all_relevent_chunks)

    def flatten_unique(chunks):
        seen_ids = set()
        flattened = []

        for obj in chunks:
            for doc in obj:
                page_content = doc.page_content  # Extract page content
                page_number = doc.metadata['page'] 
                # print(f"page {page_number}") 
                if page_number not in seen_ids:
                    seen_ids.add(page_number)
                    flattened.append(doc)

        return flattened
    
    unique_relevent_chunks = flatten_unique(all_relevent_chunks)
    # print(unique_relevent_chunks)

    available_content = "\n".join([chunk.page_content for chunk in unique_relevent_chunks])

    # print(available_content)

    System_prompt = f"""
You are a helpful assistant that answers user queries based on the provided context.

Instructions:
1. Analyze the user query and the provided Context.
2. If the Context contains relevant information to answer the query, use ONLY the information from the Context.
3. Be concise and directly answer the question.

Context:
--- Start of Relevant Document Excerpts ---
{available_content}
--- End of Relevant Document Excerpts ---

Examples:
query: what is a pointer in DSA?
answer: According to the document, [answer based on context].

query: what is a pointer in C++?
answer: Based on the provided context, [answer based on context].

query: what is the capital of France?
answer: I cannot find information about the capital of France in the provided document. The capital of France is Paris.

query: Explain the concept of recursion.
answer: According to the document, recursion is [answer based on context].

query: What is a 'bag'?
answer: I cannot find information about 'bag' in the provided document.
"""

    Messages_for_result = [
            {"role": "system", "content": System_prompt},
            {"role": "user","content": query},
    ]

    result2 = client.chat.completions.create(
        model="gemini-2.0-flash",
        temperature =0.9,
        messages = Messages_for_result
    )

    print("answer: ",result2.choices[0].message.content)
    break


