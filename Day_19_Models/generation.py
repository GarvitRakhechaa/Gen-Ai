from openai import OpenAI

client = OpenAI(
    base_url="https:api.a4f.co/v1",
    api_key="ddc-a4f-97b8d103c44746cba9792a1528df440a",
)

img = client.images.generate(
    model="provider-2/flux.1-schnell",
    prompt="a girl in swim suit",
    n=1,
    response_format="url",
    size="1024x1024"
)

print(img.data[0].url)