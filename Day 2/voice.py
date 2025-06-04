import requests

# Replace with your actual API key
API_KEY = "ak_4f3a47222ad66843ef591da3710bd0fe8a1d"

url = "https://api.allvoicelab.com/v1/text-to-speech/create"

headers = {
    "ai-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "The first move is what sets everything in motion.",
    "voice_id": 12345,  # Must be an integer per your API definition
    "model_id": "tts-multilingual",  # Optional: default used if not provided
    "language_code": "en"  # Optional
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("Audio saved as output.mp3")
else:
    print("Error:", response.status_code)
    print("Response:", response.json())