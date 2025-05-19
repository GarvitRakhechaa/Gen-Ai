from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from langchain_google_genai import ChatGoogleGenerativeAI

api_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=4000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)  

# result = wiki_tool.run({"query":"Jaitaran"})
# print(result)
tools = [wiki_tool]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm_with_tools = llm.bind_tools(tools)

# User's query
query = "hwllo how are you"
print(f"User Query: {query}\n")

response = llm_with_tools.invoke(query)


print(response.content)


# creating agent

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

agent_executor = create_react_agent(llm,tools)

response2 = agent_executor.invoke({"messages": [HumanMessage(content="tell me about jaitaran")]})
print(response2["messages"][-1].content)