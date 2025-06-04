from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START , END
from langgraph.prebuilt import ToolNode
import requests


# email = Annotated[str, "this has to be valid email format"]

# >print(email.__metadata__) 

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a:int , b:int):
    """this is an addition function that adds 2 numbers togrther"""
    return a + b

@tool
def subtract(a:int , b:int):
    """this is an subtaction function that subtract 2 numbers togrther"""
    return a - b

@tool
def multiply(a:int , b:int):
    """this is an multiplication function that multiply 2 numbers togrther"""
    return a * b

@tool
def divide(a:int , b:int):
    """this is an divider function that divides 2 numbers togrther"""
    return a / b

@tool
def average(a:int , b:int):
    """this is an average function that finds average 2 numbers togrther"""
    return (a + b)/2

@tool
def run_command(command: str):
    """Executes a system command. This is for Windows machines."""
    print("🔨 Tool Called: run_command", command)
    result = os.system(command=command)
    return result

@tool
def get_weather(city: str):
    """this tool finds weather of any city in the world"""
    # TODO!: Do an actual API Call
    print("🔨 Tool Called: get_weather", city)
    
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong"

tools = [add, subtract, multiply, divide, get_weather, average, run_command]

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash").bind_tools(tools)

def model_call(state:AgentState) -> AgentState:
    """ this is a model which gives answer to me if any tools want to use it can use"""
    system_prompt = SystemMessage(content="You are my AI assistant, please answer my query to the best of your ability.")
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]} # one more way to update state

def should_continue(state: AgentState):
    """this is a function that decides which node agent have to choose it is a decidive node"""
    messages = state["messages"]
    lastMessage = messages[-1]
    if not lastMessage.tool_calls:
        return "end"
    else:
        return "continue"
    
graph_builder = StateGraph(AgentState)
graph_builder.add_node("Agent", model_call)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("Tools", tool_node)

graph_builder.add_conditional_edges(
    "Agent",
    should_continue,
    {
        "continue": "Tools",
        "end": END
    }
)

graph_builder.add_edge("Tools","Agent")
graph_builder.set_entry_point("Agent")

graph = graph_builder.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

while True:
    query = input("what you want to ask to our agent: ")
    if query.lower() == "exit":
        break
    input = {"messages": [("user", query)]}
    print_stream(graph.stream(input=input, stream_mode="values"))