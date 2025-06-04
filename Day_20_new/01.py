from typing import TypedDict, List, Union
class AgentState(TypedDict):
    """Represents the state of our agent this will be accessed by every node and they can update it """
    input: str
    intermediate_steps: List[str]
    tool_output = Union[str, None]
    final_response = Union[str,None]

from langgraph.graph import StateGraph

graph_builder = StateGraph(AgentState)

# def process_user_input_node(state: AgentState) -> dict:
#     """this node will take user input and convert it into uppercase and put it as 'processed_input' now simplified take a simplified state: {'input': str}"""
#     print("Processing input....")
#     current_input = state["input"] # accessed input value from state
#     processed_input = current_input.upper() #done some processing
#     return {
#     'intermediate_steps': f"Processed input: {processed_input}"   # this will add at intermediate_steps's value
#     }

# graph_builder.add_node("process_input", process_user_input_node) 

def update_input(state: AgentState) -> dict:
    


