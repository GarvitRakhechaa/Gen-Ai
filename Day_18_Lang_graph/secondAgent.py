from IPython.display import Image, display
from langgraph.graph import MessagesState,StateGraph, START
from langchain_google_genai import ChatGoogleGenerativeAI
import requests
from langchain_core.messages import SystemMessage,HumanMessage
from langgraph.prebuilt import ToolNode, tools_condition

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]



from langchain_community.tools import DuckDuckGoSearchRun

def search_duckduckgo(query: str):
    """Searches DuckDuckGo using Langchain's DuckDuckSearchRun tool."""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)


# print(search_duckduckgo("what happend on 7 and 8 may 2025 in india and pakistaan "))

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

tools = [search_duckduckgo]

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return  {"messages":[llm_with_tools.invoke(state["messages"])]}


from langgraph.prebuilt import tool_node, tools_condition
graph_builder = StateGraph(State)

graph_builder.add_node("assistant", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

#define edges
graph_builder.add_edge(START, "assistant")
graph_builder.add_conditional_edges("assistant", tools_condition)
graph_builder.add_edge("tools", "assistant")
react_graph = graph_builder.compile()

display(Image(react_graph.get_graph().draw_mermaid_png()))

response = react_graph.invoke({"messages": [HumanMessage(content="what is weather in jaitaran")]})
for m in response["messages"]:
    m.pretty_print()