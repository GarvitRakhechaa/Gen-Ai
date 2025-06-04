from sarvamai import SarvamAI
from sarvamai.play import save

client = SarvamAI(api_subscription_key="fd8842fd-56ff-4c6c-9160-b51bf3e9ef35")
# Convert text to speech
audio = client.text_to_speech.convert(
      target_language_code="en-IN",
      text="Welcome to Sarvam AI!",
      model="bulbul:v2",
      speaker="anushka"
  )
save(audio, "output1.wav")
from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="fd8842fd-56ff-4c6c-9160-b51bf3e9ef35",
)

response = client.text.translate(
    input="hwllo how are you and whats your name who made you and one more thing what your origin",
    source_language_code="auto",
    target_language_code="en-IN",
    speaker_gender="Male"
)

print(response)


from sarvamai import SarvamAI
from sarvamai.play import save

client = SarvamAI(api_subscription_key="fd8842fd-56ff-4c6c-9160-b51bf3e9ef35")
# Convert text to speech
audio = client.text_to_speech.convert(
      target_language_code="en-IN",
      text=response,
      model="bulbul:v2",
      speaker="anushka"
  )
save(audio, "output1.wav")