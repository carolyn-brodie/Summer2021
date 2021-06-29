import tkinter as tk
import MainMenu
import speech_recognition as sr
import random
from summer_work.Classes import comparingWordsClass

TEXT_SIZE = 12
class WordQuizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.givenWord = ""
        self.saidWord = ""
        self.inPath = "../inData/ThousandWords"
        self.outPath = "../outData/WordQuizerTest"
        self.numRight = 0
        self.numWrong = 0
        self.numUnsaid = 0
        self.wordList = []

        self.comparingWords = comparingWordsClass.ComparingWordsC()

        inFile = open(self.inPath,"r")
        for line in inFile:
            line.strip()
            self.wordList.append(line)
        inFile.close()
    # Is called on the audioButton being pressed, starts the audio
        self.startButton = tk.Button(self,text = "Start",command = lambda: self.startFunction())
        self.startButton.pack(side = "top")

        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.pack(side = "top")

    def startFunction(self):
        self.startButton.destroy()
        self.audioButton = tk.Button(self,text = "Record Audio",command = lambda: self.audioFunction())
        self.audioButton.pack(side = "top")

        self.nextButton = tk.Button(self,text = "Next",command = lambda: self.nextFunction())
        self.nextButton.pack(side = "top")

        self.labelGivenWord = tk.Label(self,text = "Say the Given Word")
        self.labelGivenWord.pack(side = "top")
        # Creates a canvas for the given word
        self.canvasGivenWord = tk.Canvas(self.master, width=600 / 4,height=40)
        self.canvasGivenWord.grid(row = 2)

        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=600 / 4,height=40)
        self.canvasSaidWord.grid(row = 3)
        self.newGivenWord()
        self.printGivenWord()


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
        self.canvasGivenWord.update()

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(600 / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.saidWord)
        self.canvasSaidWord.update

    def nextFunction(self):
        self.checkWord()
        self.readOutCSV()
        self.canvasSaidWord.delete("all")
        self.resetWords()
        self.newGivenWord()
        self.printGivenWord()

    def newGivenWord(self):
        self.givenWord = self.wordList[random.randrange(0, stop=len(self.wordList))]

    def checkWord(self):
        if self.saidWord.lower() != self.givenWord.lower():
            self.numWrong += 1
        elif self.saidWord.lower() == "":
            self.numUnsaid += 1
        else:
            self.numRight += 1

    def resetWords(self):
        self.givenWord = ""
        self.saidWord = ""
    def printGivenWord(self):
        self.canvasGivenWord.delete("all")
        self.canvasGivenWord.create_text(600 / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold", text=self.givenWord)
        self.canvasGivenWord.update

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(600 / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.saidWord)
        self.canvasSaidWord.update

    def readOutCSV(self):
        self.comparingWords.constructor(self.givenWord, self.saidWord)
        self.comparingWords.controller()

        self.comparingWords.constructor(self.givenWord,self.saidWord)
        self.comparingWords.controller()

        self.fileCreated2 = True
        try:
            self.sessions2 = open(self.outPath, "r")
            self.fileList2 = self.sessions2.read().split("\n")
            self.sessions2.close()

            self.sessionNumber2 = len(self.fileList2) - 1

        except:
            self.sessionNumber2 = 1
            self.fileCreated2 = False

        self.fileHandle2 = open(self.outPath, "a")
        if self.fileCreated2 == False:
            self.fileHandle2.write("NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        self.fileHandle2 = open(self.outPath, "a")
        self.fileHandle2.write(str(self.comparingWords.givenWord))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.saidWord))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.whereErrorOccurred))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.typeOfErrors))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.revisedWrongIndexList))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.wrongLetterListOutput))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.wrongLetterListInput))
        self.fileHandle2.write("\n")

        self.comparingWords.reset()
        self.fileHandle2.close()
