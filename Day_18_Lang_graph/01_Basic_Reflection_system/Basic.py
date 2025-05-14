from typing import List, Sequence, Literal
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generation_chain, reflection_chain 

# we created chains now we will create nodes

GENERATE = "generate"
REFLECT = "reflect"

graph = MessageGraph()

def generate_node(state):
    return generation_chain.invoke({
        "messages": state
    })

# def reflect_node(state):
#     return reflection_chain.invoke(
#         {"messages": state }
#     ).content

# def reflect_node(messages):
#     response = reflection_chain.invoke({
#         "messages": messages
#     })
#     return [HumanMessage(content=response.content)]

# def reflect_node(state):
#     response = reflection_chain.invoke({
#         "messages": state
#     })
#     return [HumanMessage(content=response.content)]


# def reflect_node(messages):

#     response = reflection_chain.invoke({
#         "messages": messages
#     })

#     # Ab feedback ko HumanMessage ke roop me return karo
#     feedback_message = HumanMessage(
#         content=f"Critique:{response.content}"
#     )

#     return [feedback_message]

def reflect_node(messages):
    # Last message is AI's generated tweet
    last_tweet = messages[-1].content

    # Get critique from reflection chain
    response = reflection_chain.invoke({
        "messages": messages
    })

    # Combine both in one HumanMessage
    feedback_message = HumanMessage(
        content=f"Feedback on your tweet:\n\n{last_tweet}\n\nCritique:\n{response.content}"
    )

    return [feedback_message]


graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.set_entry_point(GENERATE)


def should_continue(state) -> Literal["REFLECT", "END"]:
    if len(state) > 4:
        return "END"
    return "REFLECT"

graph.add_conditional_edges(
    GENERATE,
    should_continue,
    path_map={
        "REFLECT": REFLECT,
        "END": END
    }
)

graph.add_edge(REFLECT, GENERATE)

app = graph.compile()

print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

response = app.invoke(HumanMessage(content=input("what do you want to tweet: ")))
# print(response)
for r in response:
    # if r.type == "ai":
    print(r.type," Message")
    print(r.content)
    print("\n")