from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests

load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")


client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)

def get_whether(city: str):
    print("⛏️ Tool Called: get_weather", city)
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"the weather in {city} is {response.text},"
    return "somthing went wrong"

    
def run_command(command):
    print("⛏️ Tool Called: run_command")

    result = os.system(command=command)
    return result


availavle_tools = {
        "get_whether": {
            "fn": get_whether,
            "description": "takes a city name as an input and return the current whether for the ciry"
        },
        "run_command": {
            "fn": run_command,
            "description": "takes a command as an input and run it on windows machine and return output"
        }
}


system_prompt = """

    initial context

    you are helpfull AI assitent who is specialized in resolving user query
    you work on start plan action observe mode
    for the given user query and available tools plan the step by step execution based on the planning  select the releveant
    tool from the available tool, and based on the tool selection you perform an action to call the tool
    wait for the observation from the tool call resolve the user query

    rules:
    - Follow the strict JSON output as per Output schema.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    output JSON format: 
    {{
        "step": "string",
        "content": "steing"
        "function: "the name of function if the step is action"
        "input": "the input parameters for the function
        "output": "string"
    }}

    Available tools
    - get_whether takes a city name as an input and returns the current whether for the city
    - run_command takes a command as an input and run it on windows machine and return output
    Example:

    user Query: What is the whether of new york?
    Output: {{ "step" : "plan", "content" : "the user is interested in whether of new york"}}
    Output: {{ "step" : "plan", "content" : "from the available tool i should call get whether"}}
    Output: {{ "step" : "action", "function" : "get_whether", "input" : "new york"}}
    Output: {{ "step" : "observe", "output" : "12 degree celsious"}}
    Output: {{ "step" : "output", "content" : "the whether of new york is seems to be 12 degree celsious"}}

    
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

        if availavle_tools.get(tool_name, False) != False:
            output =  availavle_tools[tool_name].get("fn")(tool_input)
            Messages.append({"role": "assistant", "content": json.dumps({"step": "observe", "output": output})})
            continue
          
    if parsed_response.get("step") == "output":
        print(f"🤖: {parsed_response.get("content")}")
        break

# wttr.in/jaitaran?format=%C+%t"