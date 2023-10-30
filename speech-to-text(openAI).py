# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai


openai.api_key = ''
audio_file= open("./123.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

print(transcript)