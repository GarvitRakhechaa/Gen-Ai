from openai import OpenAI

a4f_api_key = "ddc-a4f-97b8d103c44746cba9792a1528df440a"
a4f_base_url = "https://api.a4f.co/v1"

client = OpenAI(
    api_key=a4f_api_key,
    base_url=a4f_base_url,
)

completion = client.chat.completions.create(
  model="provider-1/chatgpt-4o-latest",
  messages=[
    {"role": "user", "content": "who made you?"}
  ]
)
print(completion.choices[0].message.content)