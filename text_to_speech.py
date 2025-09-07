client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the text-to-speech request
response = client.audio.speech.create(
  model="gpt-4o-mini-tts",
  voice = "ballad",
  input="Hi! How's your day going?"
)

# Stream the response to an MP3 file
response.stream_to_file("output.mp3")