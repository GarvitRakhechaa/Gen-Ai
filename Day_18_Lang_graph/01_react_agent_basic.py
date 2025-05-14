from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, tool
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
from langchain_community.tools import TavilySearchResults
# from langchain_google_community import GoogleSearchAPIWrapper
# from langchain_core.tools import Tool
from dotenv import load_dotenv
import datetime



load_dotenv("../.env")


search_tool = TavilySearchResults(search_depth="basic")
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]
agent = initialize_agent(tools=tools, llm=model, agent="zero-shot-react-description", verbose=True)
agent.invoke("what is time now and provide todays buletins news about india and pakistan")

# print(result.content)