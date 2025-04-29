import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("😕 Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ Error from Google API: {e}")

# Example usage
query = listen_and_transcribe()
print(query)
