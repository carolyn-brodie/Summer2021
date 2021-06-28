import tkinter as tk
import MainMenu
import speech_recognition as sr
import random

TEXT_SIZE = 12
class WordQuizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.givenWord = ""
        self.saidWord = ""


        self.numRight = 0
        self.numWrong = 0
        self.numUnsaid = 0

    # Is called on the audioButton being pressed, starts the audio
        self.audioButton = tk.Button(self,text = "Record Audio",command = lambda: self.audioFunction())
        self.audioButton.pack(side = "top")

        self.nextButton = tk.Button(self,text = "Next",command = lambda: self.nextFunction())
        self.nextButton.pack(side = "top")

        self.labelGivenWord = tk.Label(self,text = "Say the Give Word")
        self.labelGivenWord.pack(side = "top")
        # Creates a canvas for the given word
        self.canvasGivenWord = tk.Canvas(self.master, width=600 / 4,height=40)
        self.canvasGivenWord.grid(row = 2)

        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=600 / 4,height=40)
        self.canvasSaidWord.grid(row = 3)

    def audioFunction(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

        try:
            self.saidWord = self.recognizer.recognize_google(audio)
            self.saidWord = self.saidWord.lower()
            self.printSaidWord()
            print(self.saidWord)

        except sr.UnknownValueError:
            self.saidWord = ""
            self.canvasSaidWord.create_text(600/ 8, 15, fill="black",
                                             font="Times " + str(TEXT_SIZE) + " italic bold",
                                             text="Unheard")
            self.checkWord()
            self.canvasSaidWord.update()

    def checkWord(self):
        if self.saidWord == self.givenWord:
            self.rightList.append(self.givenWord)
            self.numRight += 1
        elif self.saidWord == "":
            self.unHeardList.append(self.givenWord)
            self.numUnSaid += 1
        else:
            self.wrongList.append(self.givenWord)
            self.numWrong += 1

    def newGivenWord(self):
        self.givenWord = self.wordList[random.randrange(0, stop=len(self.wordList))]

    def printGivenWord(self):
        self.canvasGivenWord.delete("all")
        self.canvasGivenWord.create_text(600 / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold", text=self.givenWord)
        self.canvasGivenWord.update

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(600 / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.saidWord)
        self.canvasSaidWord.update

    def nextFunction(self):
        pass
