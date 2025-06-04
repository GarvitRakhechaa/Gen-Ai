from gtts import gTTS
import pygame
from io import BytesIO

# Text to convert
text = "Hello, I am your frontend interviewer. Tell me about yourself."

# Convert text to speech and store in memory
tts = gTTS(text, lang="en-in", tld="co.in")
fp = BytesIO()
tts.write_to_fp(fp)
fp.seek(0)

# Initialize pygame and play from memory
pygame.mixer.init()
pygame.mixer.music.load(fp, "mp3")  # Second arg tells pygame it's mp3 format
pygame.mixer.music.play()

# Wait until playback finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
