import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
import random
from GUIpackage.Classes import comparingWordsClass
import datetime
from GUIpackage.sysVar import application_path
import os
TEXT_SIZE = 12


class WordQuizer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # The speech recognizer that we are using.
        self.recognizer = sr.Recognizer()
        self.stars = 0
        self.bar = 0
        # The devices index that we use, change the index if theres a error
        self.mic = sr.Microphone(device_index=1)

        now = datetime.datetime.now()
        self.fileAppend = str(str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute))

        self.addition = 0
        self.deletion = 0
        self.substition = 0

        self.givenWord = ""
        self.saidWord = ""
        self.excluded = ["QuestionMark.png"]
        self.imageNameList = []
        self.dictImages= {}
        for x in os.listdir(application_path +"\\Images\\DisplayImages\\"):
            if x not in self.excluded:
                self.imageNameList.append( os.path.splitext(x)[0])
        self.imagePathList = []
        for x in self.imageNameList:
            self.imagePathList.append(application_path +"\\Images\\DisplayImages\\"+x+".png")
            self.dictImages[x.lower()] = application_path +"\\Images\\DisplayImages\\"+x+".png"
        self.questionMarkImage1 = Image.open(
            application_path+"\\Images\\DisplayImages\\QuestionMark.png")
        self.questionMarkImage = self.questionMarkImage1.resize((100, 100))

        self.outPath = application_path+"\\outData\\ErrorFileDir\\ErrorFile"+self.fileAppend+".csv"
        self.inPath = application_path+"\\inData\\WordFiles\\ThousandWords.txt"
        self.readPercPercentFile = application_path+"\\outData\\percentFile.csv"

        self.rightWrongImageList = []
        self.starImageList = []

        self.unHeardList = []
        self.rightList = []
        self.wrongList = []
        self.unHeard = []
        self.numRight = 0
        self.numWrong = 0
        self.numUnsaid = 0
        self.total = 0
        self.score = 0

        self.percentageOfNothing = 0
        self.percentageOfWrong = 0
        self.percentageOfRight = 0
        self.comparingWords = comparingWordsClass.ComparingWordsC()

        self.canvasGivenWord = tk.Canvas(self.master, width=600 / 4, height=20)
        self.canvasGivenWord.grid(row=1, sticky="n")
        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=600 / 4, height=20)
        self.canvasSaidWord.grid(row=2, sticky="n")

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

        self.fileList = os.listdir(application_path + "\\inData\\WordFiles\\")
        self.fileListRev = []
        for files in self.fileList:
            self.fileListRev.append(os.path.splitext(files)[0])
        self.selection = tk.StringVar(self)
        self.selection.set(self.fileListRev[0])  # default value

        self.optionMenu = tk.OptionMenu(self, self.selection, *self.fileListRev)
        self.optionMenu.pack(side="top")

        self.enterButton = tk.Button(self,text = "enter",command = lambda : self.enterFunction())
        self.enterButton.pack(side = "top")

        self.nextButton = tk.Button(self, text="Next", command=lambda: self.nextFunction())
        self.nextButton.pack(side="top")

        self.exitButton = tk.Button(self, text="exit", command=lambda: self.exitFunction())
        self.exitButton.pack(side="top")

        self.labelGivenWord = tk.Label(self, text="Say the Given Word")
        self.labelGivenWord.pack(side="top")
        self.img = ImageTk.PhotoImage(self.questionMarkImage)
        self.label1 = tk.Label(image=self.img)
        self.label1.image = self.img
        self.label1.place(x=10, y=10)
        self.label1.pack()
        self.images()
        self.barImage = Image.open(
            application_path + "\\Images\\GUIimages\\right0.png")
        self.barImage = self.barImage.resize((150, 125))
        self.scale = ImageTk.PhotoImage(self.barImage)
        self.label2 = tk.Label(image=self.scale)
        self.label2.image = self.scale
        self.label2.place(x=10, y=10)

        self.starImage = Image.open(
            application_path + "\\Images\\GUIimages\\stars0.png")
        self.starImage = self.starImage.resize((500, 150))
        self.scale1 = ImageTk.PhotoImage(self.starImage)
        self.label3 = tk.Label(image=self.scale1)
        self.label3.image = self.scale1
        self.label3.place(x=10, y=10)
        self.label3.pack()

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
            self.printGoodJob()
        elif self.saidWord == "":
            self.unHeardList.append(self.givenWord)
            self.numUnSaid += 1
            self.printKeepTrying()
        else:
            self.wrongList.append(self.givenWord)
            self.numWrong += 1
            self.printKeepTrying()

    def newGivenWord(self):
        self.file = open(self.inPath, "r")
        lines_in_file = self.file.readlines()
        self.givenWord = lines_in_file[random.randrange(0, stop=len(lines_in_file))].strip()
        self.file.close()

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
        self.label1.destroy()
        self.newGivenWord()
        self.printGivenWord()
        self.images()

    def checkWord(self):
        if self.saidWord.lower() != self.givenWord.lower():
            self.numWrong += 1
        elif self.saidWord.lower() == "":
            self.numUnsaid += 1
        else:
            self.numRight += 1
        self.updateImageScale()

    def resetWords(self):
        self.givenWord = ""
        self.saidWord = ""

    def readOutCSV(self):
        self.comparingWords.constructor(self.givenWord, self.saidWord)
        self.comparingWords.controller()

        self.fileCreated2 = True

        try:
            self.sessions2 = open(self.outPath, "r")
            self.fileList2 = self.sessions2.read().split("\n")
            self.sessions2.close()

            self.sessionNumber2 = len(self.fileList2) - 1
            self.fileHandle2 = open(self.outPath, "a")

        except:
            self.sessionNumber2 = 1
            self.fileCreated2 = False

            self.fileHandle2 = open(self.outPath, "w")
        if self.fileCreated2 == False:
            self.fileHandle2.write(
                "NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        if (self.saidWord != ""):

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
            self.fileHandle3 = open(self.readTOEFile, "a")
        except:
            self.sessionNumber3 = 1
            self.fileCreated3 = False

            self.fileHandle3 = open(self.readTOEFile, "w")
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
            self.fileHandle1 = open(self.readPercPercentFile, "a")
        except:
            self.sessionNumber = 1
            self.fileCreated = False

            self.fileHandle1 = open(self.readPercPercentFile, "w")
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
    def enterFunction(self):
        self.inPath = application_path + "\\inData\\WordFiles\\"+self.selection.get()+".txt"

    def imageScale(self):
        self.label2.destroy()
        self.barImage = Image.open(
            application_path+"\\Images\\GUIimages\\right"+str(self.bar)+".png")
        self.barImage = self.barImage.resize((150, 125))
        self.scale = ImageTk.PhotoImage(self.barImage)
        self.label2 = tk.Label(image=self.scale)
        self.label2.image = self.scale
        self.label2.place(x=10, y=10)

        self.label3.destroy()
        self.starImage = Image.open(
            application_path+"\\Images\\GUIimages\\stars"+str(self.stars)+".png")
        self.starImage = self.starImage.resize((500, 150))
        self.scale1 = ImageTk.PhotoImage(self.starImage)
        self.label3 = tk.Label(image=self.scale1)
        self.label3.image = self.scale1
        self.label3.place(x=10, y=10)
        self.label3.pack(side = "bottom")

    def updateImageScale(self):
        if self.saidWord == self.givenWord:
            if self.bar < 4:
                self.bar += 1

            else:
                # Bar will restart and one star will light up
                if self.stars != 3:
                    self.bar = 0
                    self.stars += 1
                else:
                    self.bar = 0

        elif self.bar > 0:
            self.bar -= 1
        self.imageScale()

    def printGoodJob(self):
        self.canvasGoodKeep.delete("all")
        self.canvasGoodKeep.create_text(600/2, 25, fill="black", font="Helvetica " + str((TEXT_SIZE * 2)) + " bold",
                                        text="Good Job")
        self.canvasGoodKeep.update()

    def printKeepTrying(self):
        self.canvasGoodKeep.delete("all")
        self.canvasGoodKeep.create_text(600/2, 25, fill="black", font="Helvetica " + str((TEXT_SIZE * 2)) + " bold",
                                        text="Keep Trying")
        self.canvasGoodKeep.update()

    def images(self):
        if self.dictImages.get(self.givenWord) != None:

            try:
                self.label1.destroy()
                self.tempImage = Image.open(str(self.dictImages.get(self.givenWord)))
                self.tempImage = self.tempImage.resize((125, 100))
                self.img = ImageTk.PhotoImage(self.tempImage)
                self.label1 = tk.Label(image=self.img)
                self.label1.image = self.img
                self.label1.place(x=100, y=100)
                self.label1.pack(side = "top")
            except KeyError:
                self.img = ImageTk.PhotoImage(self.questionMarkImage)
                self.label1 = tk.Label(image=self.img)
                self.label1.image = self.img
                self.label1.place(x=100, y=100)
                self.label1.pack(side = "top")
        else:
            self.label1.destroy()
            self.img = ImageTk.PhotoImage(self.questionMarkImage)
            self.label1 = tk.Label(image=self.img)
            self.label1.image = self.img
            self.label1.place(x=10, y=10)
            self.label1.pack(side = "top")

