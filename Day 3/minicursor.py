from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests
import time

load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")


client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)



def run_command(command):
    print("🔨 Tool Called: run_command", command)
    result = os.system(command=command)
    return result

def write_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


HISTORY_FILE = "conversation_history.json"

# Load existing conversation history or initialize new
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return [{"role": "system", "content": system_prompt}]

# Save conversation history
def save_history(messages):
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f)


avaiable_tools = {
    "run_command": {
        "fn": run_command,
        "description": "Takes a command as input to execute on windows system and returns ouput"
    },
    "write_to_file": {
        "fn": write_to_file,
        "description": "Writes given content to a file."
    }
}



system_prompt = """
    
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - in react dont use create react app it already deprecated
    - always create folder on that project and inside that folder preform all task in that directory
    - Follow the Output JSON Format. but if output is code then it shoud be code format
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query break it into small pieces as many you can 
    
    Available Tools:
    - run_command: Takes a command as input and carefully analyse and then execute on windows system and returns ouput 
    this is how code added in file
    - - write_to_file: Takes a file path and content as input, and writes the content to the specified file. or we can say add code in file 

    
   Example:
   User Query: create a snake game in python
   Output: {{ "step": "plan", "content": "The user is interseted in creating a snake game " }}
   run time.sleep(10) after every step
   Output: {{ "step": "plan", "content": "user provided language python if user didnt provided then i have to ask user what language you want" }}
   Output: {{ "step": "plan", "content": "break it into parts " }}
   Output: {{ "step": "plan", "content": "create a snake_game folder " }}
   Output: {{ "step": "plan", "content": "From the available tools I should call run_command on windows system" }}
   Output: {{ "step": "action", "function": "run_command", "input": "command" }}
   Output: {{ "step": "plan", "content": "folder created" }}
   Output: {{ "step": "plan", "content": "create a python file snake.py in snake_game folder" }}
   Output: {{ "step": "plan", "content": "From the available tools I should call run_command on windows system" }}
   Output: {{ "step": "action", "function": "run_command", "input": "command" }}
   Output: {{ "step": "plan", "content": "file created now add snake game code in snake.py file" }}
   Output: {{ "step": "plan", "content": "From the available tools I should call write_to_file on windows system" }}
   Output: {{ "step": "action", "function": "write_to_file", "input": "command" }}
   Output: {{ "step": "observe", "output": "folder and file created and code also added " }}
   Output: {{ "step": "output", "content": "your game created" }}
   
   

    
    {{ "step": "plan", "content": "The user is interested in creating a Vite React project for a tic-tac-toe game." }}
    {{ "step": "plan", "content": "User provided framework/build tool (Vite React). No need to ask for language or framework." }}
    {{ "step": "plan", "content": "Break it into parts: initialize project, implement game logic and UI." }}
    {{ "step": "plan", "content": "Initialize the Vite React project using npx/npm/yarn/pnpm create." }}
    {{ "step": "plan", "content": "From the available tools I should call run_command." }}
    {{ "step": "action", "function": "run_command", "input": "command" }}
    {{ "step": "observe", "output": "Vite project directory 'tic-tac-toe' created with initial React template." }}
    {{ "step": "plan", "content": "Add tic-tac-toe game logic and components to the project files (e.g., src/App.jsx, new components, CSS)." }}
    {{ "step": "plan", "content": "From the available tools I should call write_to_file." }}
    {{ "step": "action", "function": "write_to_file", "input": "command" }}
    {{ "step": "observe", "output": "Game code added to project files." }}
    {{ "step": "observe", "output": "Vite React project initialized and game code added." }}
    {{ "step": "output", "content": "Your Vite React tic-tac-toe project has been created." }}
   """

Messages = load_history()

Messages = [
        {"role": "system", "content": system_prompt},
]

while True:
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
            time.sleep(5)
            print("sleeped for 7 seconds")
            
            continue

        if parsed_response.get("step") == "action":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            if avaiable_tools.get(tool_name, False) != False:
                if tool_name == "write_to_file":
                    output = avaiable_tools[tool_name].get("fn")(tool_input.get("file_path"), tool_input.get("content"))
                    time.sleep(7)
                    Messages.append({"role": "assistant", "content": json.dumps({"step": "observe", "output": output})})
                    print("sleeped for 7 seconds")
                    continue
                else:
                    output =  avaiable_tools[tool_name].get("fn")(tool_input)  # this is a function call
                    time.sleep(7)
                    Messages.append({"role": "assistant", "content": json.dumps({"step": "observe", "output": output})})
                    print("sleeped for 7 seconds")
                    continue
          
        if parsed_response.get("step") == "output":
            print(f"🤖: {parsed_response.get("content")}")
            break
