from pydub import AudioSegment

# Load your MP3 file
audio = AudioSegment.from_mp3("./output.mp3")

# Export as WAV
audio.export("output1.wav", format="wav")
