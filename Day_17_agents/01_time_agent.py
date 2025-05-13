from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
import datetime
from langchain.agents import tool
import requests
import os

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


@tool
def get_weather(city: str):
    """it takes input cityname as string and provide weather details"""
    print("🔨 Tool Called: get_weather", city)
    
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong"


@tool
def run_command(command: str):
    """Executes a system command. This is for Windows machines."""
    print("🔨 Tool Called: run_command", command)
    result = os.system(command=command)
    return result


# @tool
# def append_to_file(file_path: str, text: str):
#     """Appends text to a file. If the file doesn't exist, it will be created."""
#     try:
#         with open(file_path, "a") as f:
#             f.write(text + "\n")
#         return f"Successfully appended text to {file_path}"
#     except Exception as e:
#         return f"Error appending to file: {str(e)}"



model = GoogleGenerativeAI(model="gemini-2.0-flash")

query = input("what do you want to do or want to know ")

# prompt_template = PromptTemplate(query)  this is for when we want answer from ai

prompt_template = hub.pull("hwchase17/react")

tools = [get_system_time, get_weather,run_command, ]

agent = create_react_agent(model ,tools, prompt_template)

agent_executer = AgentExecutor(agent=agent, tools=tools , verbose=True)

agent_executer.invoke({"input": query})