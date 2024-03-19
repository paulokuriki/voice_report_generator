import io
import os
import time
import warnings

import pyperclip
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
from playsound import playsound
from pydub import AudioSegment

# Custom template for the prompt. Use this file to create your template
from template import TEMPLATE_PT

# Suppress deprecation warnings to clean up the console output
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Initialize OpenAI and pyttsx3 client
client = OpenAI()
engine = pyttsx3.init()

def main():
    print("Talk to GPT.")
    try:
        # Initialize speech recognition
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Start Reporting:")
            audio = recognizer.listen(source)  # Capture audio input from microphone

        # Convert captured audio to WAV format for processing
        wav_data = audio.get_wav_data()

        # Processing the audio file
        audio_segment = AudioSegment.from_file(io.BytesIO(wav_data), format="wav")
        file_location = "temp_audio.wav"
        if os.path.exists(file_location):
            os.remove(file_location)  # Delete existing file to prevent overlap
        audio_segment.export(file_location, format="wav")  # Save new audio file
        print(f'Saving to {file_location}')

        # Transcribing audio to text
        transcript_text = ""
        try:
            with open(file_location, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file, language="pt",
                                                                response_format="text")
                transcript_text = transcript
        finally:
            if os.path.exists(file_location):
                os.remove(file_location)  # Clean up temporary file

        print(f"You said: {transcript_text}")

        # Generate response using GPT
        print('Generating Report at GPT-4...')
        prompt = TEMPLATE_PT.replace('{phrases}', transcript_text)
        response = client.chat.completions.create(
            model="gpt-4",
            temperature=0,
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": transcript_text}]
        )
        gpt_response = response.choices[0].message.content
        pyperclip.copy(gpt_response)  # Copy response to clipboard
        print('--- GPT REPORT:\n')
        print(gpt_response)

        # Convert GPT response to speech
        print('\nConverting Report to Audio...')
        response = client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=gpt_response,
        )
        response.stream_to_file("output.mp3")
        time.sleep(5)  # Wait for file to finish saving

        print('\nReading out loud the report...')
        playsound('output.mp3')

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"SR Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
