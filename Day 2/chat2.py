from dotenv import load_dotenv
from openai import OpenAI
import os

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
You are an ai assistent who is specialized in maths. YOu should not answer any query that is not related to maths
for a given query help user to solbe that along with explaination

Example:
input: what is 2 + 2
Output: 2 + 2 is 4 which is calculated by adding 2 with 2

Input: 3 * 10
Output: 3 * 10 is 30 which is calculated by mulplying 3 by 10 , funfact you can even multiply 10 * 3 which gives same result

Input: why is sky blue
Output: "bro maths pd rha hai na tu to ye kya phaltu puch rha hai 


"""
result = client.chat.completions.create(
    model="gemini-2.0-flash",
    temperature =0.9,
    messages = [
        {
            "role": "system",
            "content": system_prompt

            # system prompt for initial context 

        },
        {
            "role": "user",
            "content": input("enter your prompt: ")  # zeroShot prompting 
         }
    ]
)

print(result.choices[0].message.content)
print(result.choices[0].message)

