from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")


client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)

result = client.chat.completions.create(
    model="gemini-2.0-flash", 
    messages = [
         {
      "role": "user",
      "content": "what is 2 + 2 explain with example"  # zeroShot prompting
    }
    ]
)

print(result.choices[0].message.content)

