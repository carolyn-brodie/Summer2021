import tkinter as tk
import speech_recognition as sr
import random
from summer_work.Classes import comparingWordsClass

TEXT_SIZE = 12
class WordQuizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The speech recognizer that we are using.
        self.recognizer = sr.Recognizer()

        # The devices index that we use, change the index if theres a error
        self.mic = sr.Microphone(device_index=1)
        self.addition = 0
        self.deletion = 0
        self.substition = 0

        self.givenWord = ""
        self.saidWord = ""
        self.inPath = "../inData/ThousandWords"
        self.outPath = "../outData/WordQuizerTest"
        self.readPercPercentFile = "../outData/percentFile"

        self.unHeardList = []
        self.rightList = []
        self.wrongList = []
        self.unHeard = []
        self.numRight = 0
        self.numWrong = 0
        self.numUnsaid = 0
        self.wordList = []
        self.percentageOfNothing = 0
        self.percentageOfWrong = 0
        self.percentageOfRight = 0
        self.comparingWords = comparingWordsClass.ComparingWordsC()

        inFile = open(self.inPath,"r")
        for line in inFile:
            line = line.strip()
            self.wordList.append(line)
        inFile.close()
    # Is called on the audioButton being pressed, starts the audio
        self.startButton = tk.Button(self,text = "Start",command = lambda: self.startFunction(controller))
        self.startButton.pack(side = "top")

        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.pack(side = "top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

    def startFunction(self,controller):
        self.startButton.destroy()
        self.Quit.destroy()

        self.audioButton = tk.Button(self,text = "Record Audio",command = lambda: self.audioFunction())
        self.audioButton.pack(side = "top")

        self.nextButton = tk.Button(self,text = "Next",command = lambda: self.nextFunction())
        self.nextButton.pack(side = "top")

        self.exitButton = tk.Button(self,text = "exit",command = lambda: self.exitFunction())
        self.exitButton.pack(side = "top")

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

        if(self.saidWord != ""):
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

    def typeOfError(self,error):
        if (error == "Addition"):
            self.addition += 1
        elif (error == "Substitution"):
            self.substitution += 1
        elif (error == "Deletion"):
            self.deletion += 1

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

        self.fileHandle = open(self.readPercPercentFile, "a")
        if self.fileCreated == False:
            self.fileHandle.write("Sessions; Correct; Incorrect; NoResponse" + "\n")
            self.fileCreated = True
        self.fileHandle.write(str(self.sessionNumber))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.percentageOfRight))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.percentageOfWrong))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.percentageOfNothing))
        self.fileHandle.write("\n")

        self.fileHandle.close()

    def calcPercentages(self):
        try:
            self.percentageOfRight = (len(self.rightList) / (
                    len(self.rightList) + len(self.wrongList) + len(self.unHeardList)))
            self.percentageOfWrong = (len(self.wrongList) / (
                len(self.rightList) + len(self.wrongList) + len(self.unHeardList)))
            self.percentageOfNothing = (len(self.unHeardList) / (
                    len(self.rightList) + len(self.wrongList) + len(self.unHeardList)))
        except ZeroDivisionError:
            if len(self.unHeardList) != 0:
                if len(self.wrongList) != 0:
                    self.percentageOfNothing= (len(self.unHeardList) / (
                        len(self.wrongList) + len(self.unHeardList)))
                    self.percentageOfWrong = (len(self.wrongList) / (
                            len(self.wrongList) + len(self.unHeardList)))
                elif len(self.rightList) != 0:
                    self.percentageOfRight = (len(self.rightList) / (
                            len(self.rightList)+ len(self.unHeardList)))
                    self.percentageOfNothing = (len(self.unHeardList) / (
                            len(self.rightList) + len(self.unHeardList)))
                else:
                    self.percentageOfNothing = 0

            elif len(self.wrongList) != 0:
                if len(self.unHeardList) != 0:
                    self.percentageOfNothing= (len(self.unHeardList) / (
                        len(self.wrongList) + len(self.unHeardList)))
                    self.percentageOfWrong = (len(self.wrongList) / (
                            len(self.wrongList) + len(self.unHeardList)))
                elif len(self.rightList) != 0:
                    self.percentageOfRight = (len(self.rightList) / (
                            len(self.rightList) + len(self.wrongList)))
                    self.percentageOfWrong = (len(self.wrongList) / (
                            len(self.rightList) + len(self.wrongList)))
                else:
                    self.percentageOfWrong = 0
            elif len(self.rightList) != 0:
                if len(self.wrongList) != 0:
                    self.percentageOfRight= (len(self.rightList) / (
                        len(self.wrongList) + len(self.rightList)))
                    self.percentageOfWrong = (len(self.wrongList) / (
                            len(self.wrongList) + len(self.rightList)))
                elif len(self.unHeardList) != 0:
                    self.percentageOfRight = (len(self.rightList) / (
                            len(self.rightList)+ len(self.unHeardList)))
                    self.percentageOfNothing = (len(self.unHeardList) / (
                            len(self.rightList) + len(self.unHeardList)))
                else:
                    self.percentageOfNothing = 0

    def backFunction(self,controller):
        from summer_work.Classes.GUI.MainMenu import MainMenu1
        self.canvasGivenWord.delete("all")
        self.canvasSaidWord.delete("all")
        controller.show_frame(MainMenu1)
    def exitFunction(self):
        self.calcPercentages()
        self.writeFilePerc()
        self.master.quit()