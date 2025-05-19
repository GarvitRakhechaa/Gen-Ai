from typing import List, Dict
from langgraph.graph import START,END,StateGraph
# from langchain_ollama.llms import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI

# Step 1 Define state
class State(Dict):
    messages:List[Dict[str, str]]

#Step 2 Initialize StateGraph
graph_builder = StateGraph(State)

#step 3 initialize llm
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

#Step 4 define chatbot function
def chatbot(State:State):
    response = llm.invoke(State["messages"])
    State["messages"].append({"role":"assistant", "content":response.content})
    return {"messages": State["messages"]}

#step 5 Add Nodes and edges
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot", END)

#Step 6 Compile the graph
graph = graph_builder.compile()

#Step 7 Stream update
def stream_graph_updates(user_input: str):
    state = {"messages": [{"role":"user", "content": user_input}]}
    for event in graph.stream(state):
        for value in event.values():
            print("Assistant:",value["messages"][-1]["content"])

# step 8 run chatbot in a loop

if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit","q"]:
                print("goodbye")
                break
            
            stream_graph_updates(user_input)
        except Exception as e:
            print(f"An error occurec: {e}")
            break