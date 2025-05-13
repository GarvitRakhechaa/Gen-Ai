from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages = [
    ("system", "you are comedian and tells a jokes on given topic"),
    ("human", "tell me {num_of_jokes} on {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt,middle=[invoke_model],last=parse_output)

response = chain.invoke({
    "num_of_jokes":4,
    "topic": "muslim pilot"
})

print(response)