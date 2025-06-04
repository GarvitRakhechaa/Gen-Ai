from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import pyttsx3

load_dotenv("../.env")

Api_key = os.getenv('GOOGLE_API_KEY')
Base_Url = os.getenv("GOOGLE_BASE_URL")

import speech_recognition as sr

def continuous_listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening continuously... Speak whenever you want!")

        while True:
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
                text = recognizer.recognize_google(audio)
                if text.strip() != "":
                    print("You said:", text)
                    return text
            except sr.UnknownValueError:
                # Ignore if speech not recognized, keep listening silently
                pass
            except sr.RequestError:
                # Ignore API errors silently (e.g. no internet)
                pass
            except KeyboardInterrupt:
                print("\nStopped by user")
                break

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Speed (default is around 200)
    engine.setProperty('volume', 1.0)  # Max volume
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can choose male/female voice
    engine.say(text)
    engine.runAndWait()

client = OpenAI(
    base_url= Base_Url,
    api_key= Api_key
)

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}

"""

Messsages = [
    {   "role": "system", "content": system_prompt },    
]

query = continuous_listen()
Messsages.append({"role": "user", "content": query})


while True:
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        response_format={ "type": "json_object" },
        messages = Messsages
    )

    parsed_response = json.loads(response.choices[0].message.content)
    Messsages.append({ "role": "assistant", "content": json.dumps(parsed_response) })

    if parsed_response.get("step") != "output":
        print(f"🧠: {parsed_response.get("content")}")
        continue
    
    print(f"🤖: {parsed_response.get("content")}")
    text = parsed_response.get("content")
    speak_text(text)
    
    break
