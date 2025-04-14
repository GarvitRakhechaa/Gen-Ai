from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv("../.env")
Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")



client = OpenAI(
  base_url= Base_Url,
  api_key= Api_key
)


text = "The Statue of Unity is a monumental statue located in Gujarat, India, dedicated to Sardar Vallabhbhai Patel, Standing at 182 meters (597 feet), it is the world's tallest statue and is situated on Sadhu Bet island, facing the Sardar Sarovar Dam. "



prompt = f"Summarize the following in simple words: {text}"

completion = client.chat.completions.create(
  model="gemini-2.0-flash",
  messages=[
    {
      "role": "user",
      "content": prompt
    }
  ]
)
print(completion.choices[0].message.content)