import tkinter as tk
import speech_recognition as sr
import random
from Classes import comparingWordsClass
import datetime
import os
import inData.WordFiles
TEXT_SIZE = 12


class WordQuizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The speech recognizer that we are using.
        self.recognizer = sr.Recognizer()

        # The devices index that we use, change the index if theres a error
        self.mic = sr.Microphone(device_index=1)

        now = datetime.datetime.now()
        self.fileAppend = str(str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute))

        self.addition = 0
        self.deletion = 0
        self.substition = 0

        self.givenWord = ""
        self.saidWord = ""

        self.outPath = "../outData/ErrorFileDir/ErrorFile"+self.fileAppend+".csv"
        self.inPath = r"~\..\inData\WordFiles\ThousandWords.txt"
        self.unHeardList = []
        self.rightList = []
        self.wrongList = []
        self.unHeard = []
        self.numRight = 0
        self.numWrong = 0
        self.numUnsaid = 0
        self.total = 0
        self.wordList = []
        self.percentageOfNothing = 0
        self.percentageOfWrong = 0
        self.percentageOfRight = 0
        self.comparingWords = comparingWordsClass.ComparingWordsC()

        self.canvasGivenWord = tk.Canvas(self.master, width=600 / 4, height=20)
        self.canvasGivenWord.grid(row=1, sticky="n")
        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=600 / 4, height=20)
        self.canvasSaidWord.grid(row=2, sticky="n")
        inFile = open(self.inPath, "r")
        for line in inFile:
            line = line.strip()
            self.wordList.append(line)
        inFile.close()
        # Is called on the audioButton being pressed, starts the audio
        self.startButton = tk.Button(self, text="Start", command=lambda: self.startFunction(controller))
        self.startButton.pack(side="top")

        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.pack(side="top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

        self.newGivenWord()

    def startFunction(self, controller):
        self.startButton.destroy()
        self.Quit.destroy()


        self.audioButton = tk.Button(self, text="Record Audio", command=lambda: self.audioFunction())
        self.audioButton.pack(side="top")

        self.nextButton = tk.Button(self, text="Next", command=lambda: self.nextFunction())
        self.nextButton.pack(side="top")

        self.exitButton = tk.Button(self, text="exit", command=lambda: self.exitFunction())
        self.exitButton.pack(side="top")

        self.labelGivenWord = tk.Label(self, text="Say the Given Word")
        self.labelGivenWord.pack(side="top")
        # Creates a canvas for the given word

        self.printGivenWord()

    def audioFunction(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

        try:
            self.saidWord = self.recognizer.recognize_google(audio)
            self.saidWord = self.saidWord.lower()
            self.printSaidWord()

        except sr.UnknownValueError:
            self.saidWord = ""
            self.canvasSaidWord.create_text(600 / 2, 20, fill="black",
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
        self.canvasGivenWord.create_text(600 / 8, 10, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.givenWord)
        self.canvasGivenWord.update()

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(600 / 8, 10, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                        text=self.saidWord)
        self.canvasSaidWord.update

    def nextFunction(self):
        self.total += 1
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
        self.canvasGivenWord.create_text(600 / 8, 10, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.givenWord)
        self.canvasGivenWord.update

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(600 / 8, 10, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                        text=self.saidWord)
        self.canvasSaidWord.update

    def readOutCSV(self):
        self.comparingWords.constructor(self.givenWord, self.saidWord)
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
            self.fileHandle2.write(
                "NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        if (self.saidWord != ""):
            print(self.sessionNumer2)
            self.fileHandle2.write(str(self.sessionNumber2))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.givenWord))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.saidWord))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.whereErrorOccurred))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.typeOfErrors))
            self.typeOfError(self.comparingWords.typeOfErrors)
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.revisedWrongIndexList))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.wrongLetterListOutput))
            self.fileHandle2.write(";")
            self.fileHandle2.write(str(self.comparingWords.wrongLetterListInput))
            self.fileHandle2.write("\n")

        self.comparingWords.reset()

        self.fileHandle2.close()

    def typeOfError(self, error):
        if error == "Addition":
            self.addition += 1
        elif error == "Substitution":
            self.substitution += 1
        elif error == "Deletion":
            self.deletion += 1

    def writeTOE(self):
        try:
            self.sessions3 = open(self.readTOEFile, "r")
            self.fileList3 = self.sessions2.read().split("\n")
            self.sessions3.close()

            self.sessionNumber3 = len(self.fileList3) - 1

        except:
            self.sessionNumber3 = 1
            self.fileCreated3 = False

        self.fileHandle3 = open(self.readTOEFile, "a")
        if self.fileCreated3 == False:
            self.fileHandle2.write(
                "Sessions;Deletion;Addition;Substitution" + "\n")
            self.fileCreated2 = True
        self.totalDAS = self.addition+self.deletion+self.substition
        self.percentDeletion = self.deletion/self.totalDAS
        self.percentAddition = self.addition/self.totalDAS
        self.percentSubstition =self.substition/self.totalDAS
        self.fileHandle3.write(str(self.sessionNumber3))
        self.fileHandle3.write(";")
        self.fileHandle3.write(str(self.percentAddition))
        self.fileHandle3.write(";")
        self.fileHandle3.write(str(self.percentDeletion))
        self.fileHandle3.write(";")
        self.fileHandle3.write(str(self.percentSubstition))
        self.fileHandle3.write("\n")

    def writeFilePerc(self):

        self.calcPercentages()
        self.fileCreated = True
        try:
            self.sessions = open(self.readPercPercentFile, "r")
            self.fileList = self.sessions.read().split("\n")
            self.sessions.close()

            self.sessionNumber = len(self.fileList) - 1

        except:
            self.sessionNumber = 1
            self.fileCreated = False

        self.fileHandle1 = open(self.readPercPercentFile, "a")
        if self.fileCreated == False:
            self.fileHandle.write("Sessions;Correct;Incorrect;NoResponse" + "\n")
            self.fileCreated = True
        self.fileHandle1.write(str(self.sessionNumber))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percentageOfRight))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percentageOfWrong))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percentageOfNothing))
        self.fileHandle1.write("\n")
        self.fileHandle1.close()


    def calcPercentages(self):
        try:
            self.percentageOfRight = self.numRight/self.total
        except ZeroDivisionError:
            self.percentageOfRight = 0
        try:
            self.percentageOfWrong = self.numWrong/self.total
        except ZeroDivisionError:
            self.percentageOfWrong = 0
        try:
            self.percentageOfNothing = self.numUnsaid/self.total
        except ZeroDivisionError:
            self.percentageOfNothing = 0

    def backFunction(self, controller):
        self.calcPercentages()
        self.writeFilePerc()
        self.readOutCSV()
        self.readPercPercentFile

        from GUIpackage.MainMenuFrame import MainMenu
        self.canvasGivenWord.delete("all")
        self.canvasSaidWord.delete("all")
        controller.show_frame(MainMenu)

    def exitFunction(self):
        self.calcPercentages()
        self.writeFilePerc()
        self.readOutCSV()
        self.readPercPercentFile
        self.master.quit()


