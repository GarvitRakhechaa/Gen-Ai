import os
from openai import OpenAI
import speech_recognition as sr
import requests
import urllib.parse
import pygame
import tempfile

# Initialize pygame mixer once
pygame.mixer.init()

Base_url = os.getenv("GOOGLE_BASE_URL")
Api_Key = os.getenv("GOOGLE_API_KEY")

client = OpenAI(base_url=Base_url, api_key=Api_Key)

conversation_history = [
    {"role": "system", "content": "You are a helpful AI interviewer who asks questions and listens carefully."}
]

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        print("Speech recognition API unavailable.")
        return ""

def get_gpt_response(conversation):
    print("\nConversation going to GPT API:")
    for i, msg in enumerate(conversation):
        print(f"{i}: role={msg['role']} content={repr(msg['content'])}")

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=conversation,
        temperature=0.7,
        max_tokens=150,
        n=1,
    )
    text = response.choices[0].message.content.strip()  # <-- dot notation here
    print(f"\nGPT says: {text}")
    return text


def generate_audio_from_pollinations(text, voice="echo"):
    base_url = "https://text.pollinations.ai/"
    encoded_prompt = urllib.parse.quote(text)
    url = f"{base_url}{encoded_prompt}?model=openai-audio&voice={voice}"
    print(f"Requesting audio from Pollinations...")
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Pollinations audio request failed:", response.status_code)
        return None

import os

def play_audio(audio_bytes):
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    try:
        tmpfile.write(audio_bytes)
        tmpfile.flush()
        tmpfile.close()  # Close so pygame can access file on Windows

        pygame.mixer.music.load(tmpfile.name)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    finally:
        pass  # Delete the temp file manually


def main():
    print("AI Interviewer started. Say 'exit' to quit.")
    while True:
        user_text = speech_to_text()
        if user_text.lower() == "exit":
            print("Exiting program.")
            break
        if user_text.strip() == "":
            continue

        # Append user message only if non-empty
        conversation_history.append({"role": "user", "content": user_text})

        ai_text = get_gpt_response(conversation_history)

        # Append AI response only if non-empty
        if ai_text:
            conversation_history.append({"role": "assistant", "content": ai_text})
        else:
            print("Empty response from GPT, skipping append.")

        audio_response = generate_audio_from_pollinations(ai_text)
        if audio_response:
            play_audio(audio_response)
        else:
            print("Could not generate audio.")

if __name__ == "__main__":
    main()
