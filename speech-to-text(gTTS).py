from gtts import gTTS
import os

def audio_to_text(audio_file):
    # Load the audio file
    tts = gTTS(audio_file)

    # Save the audio file as a temporary .mp3 file
    temp_audio_file = "segment_11.mp3"
    tts.save(temp_audio_file)

    # Use the speech recognition library to convert audio to text
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.AudioFile(temp_audio_file) as source:
        audio = r.record(source)
    text = r.recognize_google(audio)

    # Remove the temporary audio file
    os.remove(temp_audio_file)

    return text

audio_file_path = "./123.mp3"
text = audio_to_text(audio_file_path)
print(text)