# from gtts import gTTS
# import pygame

# # Text to convert
# text = "Hello, I am your frontend interviewer. Tell me about yourself."

# # Convert text to speech
# tts = gTTS(text)
# tts.save("voice.mp3")  # Save the audio

# # Play the audio
# pygame.mixer.init()
# pygame.mixer.music.load("voice.mp3")
# pygame.mixer.music.play()

# # Wait till the audio finishes
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# from gtts import gTTS
# from playsound import playsound

# text = "Hello, I am your frontend interviewer. Tell me about yourself."
# tts = gTTS(text)
# tts.save("voice.mp3")

# playsound("voice.mp3")

# import pygame
# import time

# pygame.mixer.quit()
# pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# print("Mixer initialized")

# try:
#     pygame.mixer.music.load("output.mp3")
#     print("Loaded voice.mp3")
# except Exception as e:
#     print("Failed to load audio:", e)

# pygame.mixer.music.play()
# print("Playback started")

# time.sleep(0.5)

# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# print("Playback finished")

# pygame.mixer.init()
# pygame.mixer.music.load("output.mp3")
# pygame.mixer.music.play()


# time.sleep(0.5)

# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)





