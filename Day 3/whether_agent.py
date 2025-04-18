from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests
from simple_chalk import chalk

load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")


client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)

# def query_db(sql):
#     pass

def run_command(command):
    print("🔨 Tool Called: run_command", command)
    result = os.system(command=command)
    return result



def get_weather(city: str):
    # TODO!: Do an actual API Call
    print("🔨 Tool Called: get_weather", city)
    
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong"

def add(x, y):
    print("🔨 Tool Called: add", x, y)
    return x + y

avaiable_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as an input and returns the current weather for the city"
    },
    "run_command": {
        "fn": run_command,
        "description": "Takes a command as input to execute on windows system and returns ouput"
    }
}

system_prompt = """
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query
    use chalk module for better visual purpose

    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Output Code Format:
    {{
    '''
    num1 = 5
    num2 = 10
    product = num1 * num2
    print(product) 
    '''
    }}


    Available Tools:
    - get_weather: Takes a city name as an input and returns the current weather for the city
    - run_command: Takes a command as input to execute on windows system and returns ouput
    
   Example:
   User Query: What is the weather of new york?
   Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york" }}
   Output: {{ "step": "plan", "content": "From the available tools I should call get_weather" }}
   Output: {{ "step": "action", "function": "get_weather", "input": "new york" }}
   Output: {{ "step": "observe", "output": "12 Degree Cel" }}
   Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees." }}

   Example:
   User Query: create a file and add code ?
   Output: {{ "step": "plan", "content": "The user is interseted in creating a file and want to add code in that file" }}
   Output: {{ "step": "plan", "content": "From the available tools I should call run_command on windows system" }}
   Output: {{ "step": "action", "function": "run_command", "input": "command" }}
   Output: {{ "step": "action", "function": "run_command", "input": "command" }}
   Output: {{ "step": "observe", "output": "out will be created a file and added code" }}
   Output: {{ "step": "output", "content": "i have created a file and added code in that" }}

   
   """


Messages = [
        {"role": "system", "content": system_prompt},
]
user_query = input("> ")
Messages.append({"role": "user", "content": user_query})


while True:
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        response_format={"type": "json_object"},
        messages = Messages
    )
    parsed_response = json.loads(response.choices[0].message.content)
    Messages.append({"role": "assistant", "content": json.dumps(parsed_response)})

    if parsed_response.get("step") == "plan":
        print(f"🧠: {parsed_response.get("content")}")
        continue

    if parsed_response.get("step") == "action":
        tool_name = parsed_response.get("function")
        tool_input = parsed_response.get("input")

        if avaiable_tools.get(tool_name, False) != False:
            output =  avaiable_tools[tool_name].get("fn")(tool_input)  # this is a function call
            Messages.append({"role": "assistant", "content": json.dumps({"step": "observe", "output": output})})
            continue
          
    if parsed_response.get("step") == "output":
        print(f"🤖: {parsed_response.get("content")}")
        break
