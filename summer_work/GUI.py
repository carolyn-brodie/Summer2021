

import tkinter as tk
import speech_recognition as sr
import random

WIDTH = 600
HEIGHT = 600

# Window Size
WINDOW_STARTING_SIZE = str(WIDTH) + "x" + str(HEIGHT)
# Title
WINDOW_NAME = "Window"


def main():

    root = tk.Tk()
    root.title(WINDOW_NAME)
    root.geometry(WINDOW_STARTING_SIZE)

    app = GUI(root)
    root.mainloop()



class GUI(tk.Frame):
    def __init__(self, master):
        self.wrongWordSet = []
        self.rightWordSet = []
        self.nothingWordSet = []

        self.unsaid = 0
        self.correct = 0
        self.wrong = 0

        self.word = ""
        self.saidWord = ""

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=1)

        file = open("rWordsBeginning", "r")
        self.WordList = []

        for line in file:
            self.WordList.append(line.strip("\n"))

        super(GUI, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.startButton = tk.Button(self, text="Start", command=lambda: self.startFunc())
        self.startButton.grid(row=0, column=0)

        self.recordAudio = tk.Button(self, text="Record Audio", command=lambda: self.audioFunc())
        self.recordAudio.grid(row=1, column=0)

        self.nextButton = tk.Button(self, text="Next", command=lambda: self.nextFunc())
        self.nextButton.grid(row=2, column=0)

        self.exit = tk.Button(self, text="Exit", command=lambda :self.exitButtonFunc())
        self.exit.grid(row=10, column=0)

    def calcPercentages(self):

        try:
            self.percentageOfRight = (len(self.rightWordSet) / (len(self.rightWordSet) + len(self.wrongWordSet) + len(self.nothingWordSet)))
            self.percentageOfWrong = (len(self.wrongWordSet) / (len(self.rightWordSet) + len(self.wrongWordSet) + len(self.nothingWordSet)))
            self.percentageOfNothing = (len(self.nothingWordSet) / (len(self.rightWordSet) + len(self.wrongWordSet) + len(self.nothingWordSet)))
        except ZeroDivisionError:
            self.master.quit()

    def writeFilePerc(self):
        self.fileHandle = open("statsForExels.csv", "a")
        self.fileHandle.write(str(self.percentageOfRight))
        self.fileHandle.write(",")
        self.fileHandle.write(str(self.percentageOfWrong))
        self.fileHandle.write(",")
        self.fileHandle.write(str(self.percentageOfNothing))
        self.fileHandle.write("\n")

        self.fileHandle.close()

    def exitButtonFunc(self):
        self.calcPercentages()
        self.writeFilePerc()
        self.master.quit()
    def startFunc(self):
        self.startButton.destroy()

        self.lable1 = tk.Label(self, text="Say the Word:")
        self.lable1.grid(row=11, column=0)

        self.canvas1 = tk.Canvas(self.master,
                                 width=WIDTH / 4,
                                 height=40)
        self.canvas1.pack(side="top")

        self.canvas2 = tk.Canvas(self.master,
                                 width=WIDTH / 4,
                                 height=40)
        self.canvas2.pack(side="top")

        self.randomWord()
        self.printWord()

    def randomWord(self):
        self.word = self.WordList[random.randrange(0, stop=len(self.WordList))]
        self.WordList.remove(self.word)

    def printWord(self):
        self.canvas1.create_text(WIDTH / 8, 15, fill="black", font="Times " + str(10) + " italic bold",
                                 text=self.word)
        self.canvas1.update

    def nextFunc(self):
        if self.saidWord == "":
            self.unsaid += 1
            self.nothingWordSet.append(self.word)

        self.canvas2.delete("all")
        self.canvas1.delete("all")

        self.randomWord()
        self.printWord()

        self.saidWord = ""

    def audioFunc(self):

        with self.mic as source:
            audio = self.recognizer.listen(source)

        try:
            self.saidWord = self.recognizer.recognize_google(audio)
            self.saidWord = self.saidWord.lower()
            self.canvas2.create_text(WIDTH / 8, 15, fill="black", font="Times " + str(10) + " italic bold",
                                     text=self.saidWord)
            self.canvas2.update

            if self.saidWord == self.word:
                self.correct += 1
                self.rightWordSet.append(self.word)
            else:
                self.wrong += 1
                self.wrongWordSet.append(self.word)
        except:
            self.unsaid += 1
            self.nothingWordSet.append(self.word)



main()
