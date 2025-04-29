from openai import OpenAI

client = OpenAI(
    base_url="https://api.sree.shop/v1",
    api_key="ddc-beta-lmfilgctuq-SVg0l6WxGuGcmdijAeoKfTWV2KQMfdoAdk2"  # Replace with your API key
)

response = client.chat.completions.create(
    model="Provider-2/o3-mini",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)