#import pyaudio

from getPhones import *
import speech_recognition as sr

def showSpeechRecognitionResults(recognizer, audio):
    results = recognizer.recognize_google(audio, show_all=True)
    print(results)
    try:
        print(results['alternative'][0]['transcript'])
    except TypeError:
        print("Could not understand audio")

def main():
    numberOfRepetitions = 5
    print("Start\n")

    print("SpeechRecognition version = " + sr.__version__)
    recognizer = sr.Recognizer()

    print("\nUsing File as Source:")
    for iteration in range(3):
        create_wav_file("voice.wav")
        test = sr.AudioFile('voice.wav')
        with test as source:
            audio = recognizer.record(source)
        showSpeechRecognitionResults(recognizer, audio)

    #print("\nMicrophone are " + str(sr.Microphone.list_microphone_names()))

    # mic = sr.Microphone(device_index=0)
    # print("\nUsing Default Microphone as Source:")
    #
    # for count in range(numberOfRepetitions):
    #     print("\nRepetition " + str(count+1) + " of " + str(numberOfRepetitions) + ". Say a word or phrase: ")
    #     with mic as source:
    #          audio = recognizer.listen(source)
    #     showSpeechRecognitionResults(recognizer, audio)

    print("\nEnd")

main()