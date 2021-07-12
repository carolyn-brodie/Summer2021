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
var = recognizer.recognize_google(audio, show_all=True)

for index in range(len(var.get("alternative"))):
     print(var.get("alternative")[index].get("transcript"))