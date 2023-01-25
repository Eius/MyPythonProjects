from configparser import ConfigParser

from google.cloud import speech
from google.cloud import storage
from google.cloud import translate

import speech_recognition as sr

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


# Instantiates ConfigParser
config = ConfigParser()
config.read("config.ini")

# Instantiates a Google speech, translate and storage client
speech_client = speech.SpeechClient()
storage_client = storage.Client()
translate_client = translate.TranslationServiceClient()


# Initialize speech recognition
r = sr.Recognizer()

# obtain audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to RAW file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

upload_blob("voice_assistant_raw", "microphone-results.wav", "audio_wav")

audio_uri = "gs://voice_assistant_raw/audio_wav"
audio = speech.RecognitionAudio(uri=audio_uri)

speechConfig = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="sk-SK"
)

# Detects speech in the audio file
response = speech_client.recognize(config=speechConfig, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))

