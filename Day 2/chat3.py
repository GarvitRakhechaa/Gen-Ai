from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv("../.env")
# Api_key = os.getenv('OPENAI_API_KEY')
# Base_Url = os.getenv("BASE_URL")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")



client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)

system_prompt = """
You are an Ai assistent who is expery in breaking down complex problems and then resolve the user query
For the given user input, analyse the input and break down the problem step by step.
Altest think 5-6 steps on how to solve the problem before solving it down 

the steps are you get a user input, you analyse, you think you again thikn for saveral time and then return output with explaination then finally you validate thee output as well before giving final result,

Follow the steps in sequnce that is "analyse", "think", "output", "validate", and fially "result" peovide one step st a time 

Rule

1. Follow the strict  JSON output as per Output schema 
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format: {{ step: "string", content: "string" }} 

Example:
Input: what is 2 + 2
Output: {{step: "analyse", content: "Alright! the user is interested in maths query and he asking a basic arthmatic operation}}
Output: {{step: "think", content: " To perform the addidtion i must go from left to right and following and add all the operands}}
Output: {{step: "output", content "4" }}
Output: {{step: "validate", content: "sees like 4 is correct ans for 2 + 2"}}
Output: {{step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers}}
"""

result = client.chat.completions.create(
    model="gemini-2.0-flash",
    temperature =0.9,
    response_format = {"type": "json_object"},
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "what is 3 + 4 * 5" },
        
        #
        { "role": "assistant", "content": json.dumps({"step": "analyse","content": "The user is asking for the result of a mathematical expression involving addition and multiplication. It's crucial to remember the order of operations (PEMDAS/BODMAS) to solve this correctly."})  },
        { "role": "assistant", "content": json.dumps({"step": "think","content": "According to the order of operations (PEMDAS/BODMAS), multiplication should be performed before addition. Therefore, I need to first calculate 4 * 5, and then add 3 to the result."}) },
        { "role": "assistant", "content": json.dumps({"step": "output","content": "23"}) },
        { "role": "assistant", "content": json.dumps({"step": "validate","content": "Let's verify: 4 * 5 = 20, and 3 + 20 = 23. The answer seems correct."}) }
     ]
    )

print(result.choices[0].message.content)
