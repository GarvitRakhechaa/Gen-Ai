from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import AnswerOuestion
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.messages import HumanMessage
pydentic_parser = PydanticToolsParser(tools=[AnswerOuestion])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

actor_messages = [
    ("system", """you are expert AI researcher
        current time: {time}
     
     1. {first_instruction}
     2. Reflect and critique your answer. Be severe to maximize improvement.
     3. After the reflection, 1-3 search queries separately** for
        researching improvements. Do not include them inside the reflection.
      """),MessagesPlaceholder(variable_name="messages"),
      ("system", "Answer the user's question above using the required format")
]
actor_prompt_template = ChatPromptTemplate.from_messages(actor_messages).partial(time= lambda: datetime.datetime.now().isoformat())

first_responder_prompt_template = actor_prompt_template.partial(first_instruction = "provide a detailed ~250 word answer")

first_responder_chain = first_responder_prompt_template | llm.bind_tools(
    tools=[AnswerOuestion], tool_choice="AnswerOuestion") | pydentic_parser


response = first_responder_chain.invoke({
    "messages": [HumanMessage(content="write me a blog post on 100 line of is better than 3 line of code ")]
})

for r in response:
    print("answer is: ",r.answer)
    print("\n")
    print("\n")
    for search in r.search_queries:
        print("search query is: ",search)
        print("\n")
    print("\n")
    print("\n")
    print("\n")