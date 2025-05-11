from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
class State(TypedDict):
    user_message: str
    is_coding_question: bool

def detect_query(state: State):
    user_message = State.get("user_message")

    #OpenAI Call

    state.is_coding_question = True
    return state


def solve_coding_question(state: State):
    user_message = state.get("user_message")

    #OpenAI call {coding question gpt-4.1}

    state.ai_message = "Here is your coding question answer"

    return state

def solve_simple_question(state: State):
    user_message = state.get("user_message")

    #OpenAI call {coding question gpt-3.5}

    state.ai_message = "please ask coding question"

    return state


graph_builder = StateGraph(State)

graph_builder.add_node("detect_query", detect_query)
graph_builder.add_node("solve_coding_question", solve_coding_question)
graph_builder.add_node("solve_simple_question", solve_simple_question)

graph_builder.add_edge(START, )

