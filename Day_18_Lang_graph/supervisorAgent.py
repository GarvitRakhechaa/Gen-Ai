from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph_supervisor import create_supervisor
from langgraph.prebuilt import create_react_agent

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_community.tools import DuckDuckGoSearchRun

def search_duckduckgo(query: str):
    """Searches DuckDuckGo using Langchain's DuckDuckSearchRun tool."""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)

def add(a: float, b: float) -> float:
    """Add two numbers ."""
    return a + b

def multiply(a: float, b: float) -> float:
    """ Multiply two numbers """
    return a * b


math_agent = create_react_agent(
    model=model,
    tools=[add, multiply],
    name="Math_expert",
    prompt="You are a math expert. Always use onetool at a time"    
)

research_agent = create_react_agent(
    model=model,
    tools=[search_duckduckgo],
    name="research_expert",
    prompt="You are a world class researcher with access to web search. Do not do any math"    
)


workflow = create_supervisor(
    [research_agent, math_agent],
    model=model,
    prompt=(
         "You are a team supervisor managing a research expert and a math expert. "
        "For current events, use research_agent. "
        "For math problems, use math_agent."
    )
)

app = workflow.compile()

result = app.invoke({
    "messages": [{
        "role":"user",
        "content":"what is weather in jaipur and what is 2 multiply by 50 adding 5 and then multiply 30"
    }]
})

# print(result["messages"])
for r in result["messages"]:
    r.pretty_print()