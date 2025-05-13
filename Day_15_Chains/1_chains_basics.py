from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.output_parser import StrOutputParser
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages = [
    ("system", "you are comedian and tells a jokes on given topic"),
    ("human", "tell me {num_of_jokes} on {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

# prompt = prompt_template.invoke({
#     "num_of_jokes":4,
#     "topic": "muslim pilot"
# })
# print(prompt)

# result = model.invoke(prompt)

# print(result.content)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({
    "num_of_jokes":4,
    "topic": "muslim pilot"
})

print(result)

