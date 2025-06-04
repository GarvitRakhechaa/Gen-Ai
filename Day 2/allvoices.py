import requests

API_KEY = "ak_4f3a47222ad66843ef591da3710bd0fe8a1d"
url = "https://api.allvoicelab.com/v1/text-to-speech/create "

headers = {
    "ai-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "Hello from GPT-4",
    "voice_id": 1  # Try different values here
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved as output.mp3")
else:
    print("❌ Error:", response.status_code)
    print("Response:", response.text)