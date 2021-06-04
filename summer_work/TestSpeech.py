import pyaudio
import speech_recognition as sr
#import pocketsphinx

print(sr.__version__)
print(sr.Microphone.list_microphone_names())
recognizer = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)
# ##If using an audio file
# # harvard = sr.AudioFile('harvard.wav')
# # with harvard as source:
# #     audio = recognizer.record(source)
print("Say a word or phrase: ")
with mic as source:
     audio = recognizer.listen(source)
print(recognizer.recognize_google(audio))
