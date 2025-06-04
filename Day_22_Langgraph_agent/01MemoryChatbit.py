from typing import TypedDict , List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    messages: list[Union[HumanMessage, AIMessage]]


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def process(state: AgentState) -> AgentState:
    """This node will solve the request you input"""
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    return state


graph_builder = StateGraph(AgentState)

graph_builder.add_node("process", process)
graph_builder.add_edge(START, "process")
graph_builder.add_edge("process", END)

graph =  graph_builder.compile()

conversation_history = []
while True:
    user_input = input("Enter your query: ")
    if user_input.lower() == "exit":
        break
    else:
        conversation_history.append(HumanMessage(content=user_input))
        result = graph.invoke({"messages":conversation_history})
        conversation_history = result["messages"]