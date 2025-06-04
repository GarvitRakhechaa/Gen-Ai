from typing import TypedDict , List
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    messages: list[HumanMessage]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    print(f"\nAI: {response.content}")
    return state

graph_builder = StateGraph(AgentState)

graph_builder.add_node("process", process)
graph_builder.add_edge(START, "process")
graph_builder.add_edge("process", END)

graph =  graph_builder.compile()
while True:
    user_input = input("Enter your query: ")
    if user_input.lower() == "exit":
        break
    else:
        graph.invoke({"messages":[HumanMessage(content=user_input)]})