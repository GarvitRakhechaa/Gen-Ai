import requests
import urllib.parse
import pygame
from pydub import AudioSegment
import speech_recognition as sr
import os

def generate_audio_from_pollinations(prompt, voice="echo", filename="output.mp3"):
    base_url = "http://text.pollinations.ai/conversation?model=openai-audio&voice=" + voice
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{base_url}&prompt={encoded_prompt}"

    print(f"Requesting audio from: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {filename}")
    else:
        print("Failed to get audio:", response.status_code, response.text)

def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    print(f"Converted {mp3_path} to {wav_path}")

def audio_file_to_text(wav_path):
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data)
        print("Recognized text (interviewer):", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def continuous_listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening continuously... Speak whenever you want!")

        while True:
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                if text.strip() != "":
                    print("You said:", text)
                    return text
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
            except KeyboardInterrupt:
                print("\nStopped by user")
                break

def main():
    conversation = ""
    # current_prompt = "act like frontend development interviewer and you will take interview of person act a formal interviwer and start the interviwer and one more thing if user goes out of context of your domain 'frontend developement' then you have to take conversation on your domain again ok start inteviwe with asking name and so on"
    current_prompt = "Hello, I am ready for the interview. Please begin interview on frontend developement."
    conversation += " " + current_prompt

    while True:
        # Step 1: Generate audio from conversation prompt
        generate_audio_from_pollinations(conversation, voice="echo", filename="output.mp3")

        # Step 2: Play generated audio
        play_audio("output.mp3")

        # Step 3: Convert MP3 to WAV
        mp3_to_wav("output.mp3", "output1.wav")


        # Step 4: Extract text from audio (interviewer response)
        interviewer_text = audio_file_to_text("output1.wav")
        if interviewer_text:
            conversation += "\ninterviewer: " + interviewer_text
        else:
            print("No interviewer text recognized, continuing...")

        # Step 5: Listen to user answer continuously
        user_text = continuous_listen()
        if user_text:
            conversation += "\nuser: " + user_text
        else:
            print("No user input detected, stopping.")
            break

if __name__ == "__main__":
    main()
