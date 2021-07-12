import pyaudio
import speech_recognition as sr

def record(givenWord):
    word_list = []
    recognizer = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    mic = sr.Microphone(device_index=0)
    print("Say", givenWord, ":")
    with mic as source:
        audio = recognizer.listen(source)
        recognized_dict = recognizer.recognize_google(audio, show_all=True)
        if recognized_dict != []:
            for index in range(len(recognized_dict.get("alternative"))):
                word = ((recognized_dict.get("alternative"))[index]).get("transcript")
                word_list.append(word)
        return word_list


if __name__ == "__main__":
    print(record("peace"))