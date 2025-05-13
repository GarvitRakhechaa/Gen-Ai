from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages = [
    ("system", "you are comedian and tells a jokes on given topic"),
    ("human", "tell me {num_of_jokes} on {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})



chain = prompt_template | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser()

result = chain.invoke({
    "num_of_jokes":4,
    "topic": "muslim pilot"
})

print(result)

