import tkinter as tk
import tkinter
import speech_recognition as sr
import random
import ComparingWordsV2
from PIL import Image, ImageTk
from tkinter import *
import datetime
import PIL.Image

WIDTH = 600
HEIGHT = 600
TEXT_SIZE = 15
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
        # List of wrong, right, unheard words.
        now = datetime.datetime.now()
        self.fileAppend = str(str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute))
        print(self.fileAppend)
        self.wrongList = []
        self.rightList = []
        self.unHeardList = []

        self.outCSVFile = "./outData/ErrorFile_" + self.fileAppend + ".csv"
        self.readPercPercentFile = "./outData/RightWrongUnheard.csv"
        self.readPercErrorFile = "./outData/TypeOfError.csv"

        # Percentages
        self.percentageOfRight = 0
        self.percentageOfWrong = 0
        self.percentageOfNothing = 0
        # number of right, wrong, unsaid words.
        self.numRight = 0
        self.numWrong = 0
        self.numUnSaid = 0

        # Given word and the said word.
        self.givenWord = ""
        self.saidWord = ""

        # The speech recognizer that we are using.
        self.recognizer = sr.Recognizer()

        # The devices index that we use, change the index if theres a error
        self.mic = sr.Microphone(device_index=0)

        # The file name that we use
        self.fileName = "foodtextv3"

        # Opening the file
        self.file = open(self.fileName, "r")

        # Creates a word list called wordList that has each word from the file.
        self.wordList = []

        self.addition = 0
        self.deletion = 0
        self.substitution = 0
        # Reads through each line of the word file appending the word to the wordList.
        for line in self.file:
            self.wordList.append(line.strip("\n"))

        super(GUI, self).__init__(master)

        # calls the pack
        self.pack()

        # Creates images
        self.appleImage1 = PIL.Image.open("../summer_work/images/Apple.png")
        self.appleImage = self.appleImage1.resize((125, 100))
        self.cheeseImage1 = PIL.Image.open("../summer_work/images/Cheese.png")
        self.cheeseImage = self.cheeseImage1.resize((135, 100))
        self.iceCreamImage1 = PIL.Image.open("../summer_work/images/IceCream.png")
        self.iceCreamImage = self.iceCreamImage1.resize((100, 100))
        self.mushroomImage1 = PIL.Image.open("../summer_work/images/Mushroom.png")
        self.mushroomImage = self.mushroomImage1.resize((150, 100))
        self.orangeImage1 = PIL.Image.open("../summer_work/images/Orange.png")
        self.orangeImage = self.orangeImage1.resize((125, 100))
        self.questionMarkImage1 = PIL.Image.open("../summer_work/images/QuestionMark.png")
        self.questionMarkImage = self.questionMarkImage1.resize((100, 100))
        self.breadImage1 = PIL.Image.open("../summer_work/images/Bread.png")
        self.breadImage = self.breadImage1.resize((150, 100))
        self.chickenImage1 = PIL.Image.open("../summer_work/images/Chicken.png")
        self.chickenImage = self.chickenImage1.resize((180, 100))
        self.eggImage1 = PIL.Image.open("../summer_work/images/Egg.png")
        self.eggImage = self.eggImage1.resize((130, 100))
        self.milkImage1 = PIL.Image.open("../summer_work/images/Milk.png")
        self.milkImage = self.milkImage1.resize((130, 100))
        self.waffleImage1 = PIL.Image.open("../summer_work/images/Waffle.png")
        self.waffleImage = self.waffleImage1.resize((100, 100))

        self.noRightImage1 = PIL.Image.open("../summer_work/images/noneRight.png")
        self.noRightImage = self.noRightImage1.resize((75, 150))
        self.oneRightImage1 = PIL.Image.open("../summer_work/images/oneRight.png")
        self.oneRightImage = self.oneRightImage1.resize((75, 150))
        self.twoRightImage1 = PIL.Image.open("../summer_work/images/twoRight.png")
        self.twoRightImage = self.twoRightImage1.resize((75, 150))
        self.threeRightImage1 = PIL.Image.open("../summer_work/images/threeRight.png")
        self.threeRightImage = self.threeRightImage1.resize((75, 150))
        self.fourRightImage1 = PIL.Image.open("../summer_work/images/fourRight.png")
        self.fourRightImage = self.fourRightImage1.resize((75, 150))
        self.fiveRightImage1 = PIL.Image.open("../summer_work/images/fiveRight.png")
        self.fiveRightImage = self.fiveRightImage1.resize((75, 150))

        self.noStarsImage1 = PIL.Image.open("../summer_work/images/zeroStars.png")
        self.noStarsImage = self.noStarsImage1.resize((500, 150))
        self.oneStarImage1 = PIL.Image.open("../summer_work/images/oneStar.png")
        self.oneStarImage = self.oneStarImage1.resize((500, 150))
        self.twoStarsImage1 = PIL.Image.open("../summer_work/images/twoStars.png")
        self.twoStarsImage = self.twoStarsImage1.resize((500, 150))
        self.threeStarsImage1 = PIL.Image.open("../summer_work/images/threeStars.png")
        self.threeStarsImage = self.threeStarsImage1.resize((500, 150))


        self.wordImageDict = {"apple": self.appleImage, "cheese": self.cheeseImage, "ice cream":self.iceCreamImage,
                            "mushroom":self.mushroomImage, "orange":self.orangeImage}

        self.wordImageDict2 = {"apple": self.appleImage, "cheese": self.cheeseImage, "ice cream":self.iceCreamImage,
                            "mushroom":self.mushroomImage, "orange":self.orangeImage, "bread":self.breadImage,
                               "chicken":self.chickenImage, "egg":self.eggImage, "milk":self.milkImage, "waffle":self.waffleImage}

        self.rightWrongImageList = [self.noRightImage, self.oneRightImage, self.twoRightImage, self.threeRightImage,
                                    self.fourRightImage, self.fiveRightImage]

        self.starImageList = [self.noStarsImage, self.oneStarImage, self.twoStarsImage, self.threeStarsImage]

        self.finishedIndex = 0
        self.starIndex = 0

        # Creates the starting front page:
        self.create_widgets()

        # Creates a instance of the comparingWords class so we can use it in later functions
        self.comparingWords = ComparingWordsV2.ComparingWordsV2()

    #     Create widgets:
    #           makes the start button.
    def create_widgets(self):

        # Creates the start button which then calls the start function.
        self.testButton = tk.Button(self, text="testButton", command=self.testFunction)
        self.testButton.grid(row=4)
        self.startButton = tk.Button(self, text="Start", command=self.startFunction)
        self.startButton.grid(row=1, column=0)

        self.analyticsButton = tk.Button(self, text="Analytics", command=self.AnalyticsFunction)
        self.analyticsButton.grid(row=3, column=0)

        # Exits the programs but does not call the write to file function.
        self.mainPageExit = tk.Button(self, text="Exit", command=lambda: self.master.quit())
        self.mainPageExit.grid(row=2, column=0)

        self.gameTitle = tk.Label(self, text="Well Spoken", bg="#f76363", font="Helvetica 35 bold")
        self.gameTitle.grid(row=10, column=0)

    # Is called on press of the start function
    def startFunction(self):
        # Destroys the startButton and the MainPageExit
        self.startButton.destroy()
        self.mainPageExit.destroy()
        self.analyticsButton.destroy()
        self.gameTitle.destroy()

        self.audioButton = tk.Button(self, text="Record Audio", command=self.audioFunction)
        self.audioButton.grid(row=1, column=0)

        self.nextButton = tk.Button(self, text="Next", command=self.nextFunction)
        self.nextButton.grid(row=2, column=0)

        self.exitButton = tk.Button(self, text="Exit", command=self.exitFunction)
        self.exitButton.grid(row=3, column=0)

        self.labelGivenWord = tk.Label(self, text="Say the Given Word")
        self.labelGivenWord.grid(row=5)
        # Creates a canvas for the given word
        self.canvasGivenWord = tk.Canvas(self.master, width=WIDTH / 4, height=40)
        self.canvasGivenWord.pack(side="top")

        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=WIDTH / 4, height=40)
        self.canvasSaidWord.pack(side="top")

        self.canvasGoodKeep = tk.Canvas(self.master, width=WIDTH, height=50, bg="#EB7DF5")
        self.canvasGoodKeep.pack(side="top")

        self.newGivenWord()
        self.printGivenWord()
        self.images()
        self.imageScale()

    def images(self):
        try:
            self.img = ImageTk.PhotoImage(self.wordImageDict2.get(self.givenWord))
            self.label1 = tkinter.Label(image=self.img)
            self.label1.image = self.img
            self.label1.place(x=10, y=10)
            self.label1.pack()
        except KeyError:
            # Will generate a "Exception ignored" warning
            self.img = ImageTk.PhotoImage(self.questionMarkImage)
            self.label1 = tkinter.Label(image=self.img)
            self.label1.image = self.img
            self.label1.place(x=10, y=10)
            self.label1.pack()

    def imageScale(self):
        self.scale = ImageTk.PhotoImage(self.rightWrongImageList[self.finishedIndex])
        self.label2 = tkinter.Label(image=self.scale)
        self.label2.image = self.scale
        self.label2.place(x=10, y=10)

        self.scale1 = ImageTk.PhotoImage(self.starImageList[self.starIndex])
        self.label3 = tkinter.Label(image=self.scale1)
        self.label3.image = self.scale1
        self.label3.place(x=10, y=10)
        self.label3.pack()

    def updateImageScale(self):
        if self.saidWord == self.givenWord:
            if self.finishedIndex < 5:
                self.finishedIndex += 1
            else:
                # Bar will restart and one star will light up
                self.finishedIndex = 0
                self.starIndex += 1
        elif self.finishedIndex > 0:
            self.finishedIndex -= 1

    def printGoodJob(self):
        self.canvasGoodKeep.delete("all")
        self.canvasGoodKeep.create_text(WIDTH/2, 25, fill="black", font="Helvetica " + str((TEXT_SIZE * 2)) + " bold",
                                        text="Good Job")
        self.canvasGoodKeep.update()

    def printKeepTrying(self):
        self.canvasGoodKeep.delete("all")
        self.canvasGoodKeep.create_text(WIDTH/2, 25, fill="black", font="Helvetica " + str((TEXT_SIZE * 2)) + " bold",
                                        text="Keep Trying")
        self.canvasGoodKeep.update()


    # Is called on the audioButton being pressed, starts the audio
    def audioFunction(self):
        with self.mic as source:
            audio = self.recognizer.listen(source)

        try:
            self.saidWord = self.recognizer.recognize_google(audio)
            self.saidWord = self.saidWord.lower()
            self.printSaidWord()
            print(self.saidWord)
            self.updateImageScale()

        except sr.UnknownValueError:
            self.saidWord = ""
            self.canvasSaidWord.create_text(WIDTH / 8, 15, fill="black",
                                            font="Times " + str(TEXT_SIZE) + " italic bold",
                                            text="Unheard")
            self.canvasSaidWord.update()

    # Is called on the nextButton being pressed, clears the current word and then creates a new word.
    def nextFunction(self):
        self.checkWord()
        self.readOutCSV()
        self.canvasSaidWord.delete("all")
        self.resetWords()
        self.newGivenWord()
        self.printGivenWord()
        self.label1.destroy()
        self.images()
        self.label2.destroy()
        self.label3.destroy()
        self.imageScale()


    def exitFunction(self):
        self.writeFilePerc()
        self.writePercOfError()
        self.master.quit()

    def writePercOfError(self):
        self.calcPercOfError()
        self.fileCreated1 = True
        try:
            self.sessions1 = open(self.readPercErrorFile, "r")
            self.fileList1 = self.sessions1.read().split("\n")
            self.sessions1.close()

            self.sessionNumber1 = len(self.fileList1) - 1

        except:
            self.sessionNumber1 = 1
            self.fileCreated1 = False

        self.fileHandle1 = open(self.readPercErrorFile, "a")
        if self.fileCreated1 == False:
            self.fileHandle1.write("Sessions; Deletion; Addition; Substitution" + "\n")
            self.fileCreated1 = True

        self.fileHandle1.write(str(self.sessionNumber1))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percOfDeletion))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percOfAddition))
        self.fileHandle1.write(";")
        self.fileHandle1.write(str(self.percOfSubstitution))
        self.fileHandle1.write("\n")
        self.fileHandle1.close()

    def calcPercOfError(self):
        try:
            self.percOfDeletion = (self.deletion) / (self.substitution + self.deletion + self.addition)
            self.percOfAddition = (self.addition) / (self.addition + self.deletion + self.substitution)
            self.percOfSubstitution = (self.substitution) / (self.addition + self.substitution + self.deletion)
        except ZeroDivisionError:
            return 0

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

    def readOutCSV(self):

        self.comparingWords.constructor(self.givenWord, self.saidWord)
        self.comparingWords.controller()

        self.fileCreated2 = True
        try:
            self.sessions2 = open(self.outCSVFile, "r")
            self.fileList2 = self.sessions2.read().split("\n")
            self.sessions2.close()

            self.sessionNumber2 = len(self.fileList2) - 1

        except:
            self.sessionNumber2 = 1
            self.fileCreated2 = False

        self.fileHandle2 = open(self.outCSVFile, "a")
        if self.fileCreated2 == False:
            self.fileHandle2.write(
                "NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        self.fileHandle2.write(str(self.sessionNumber2))
        self.fileHandle2.write(";")
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

        self.typeOfError(self.comparingWords.typeOfErrors)

        self.comparingWords.reset()
        self.fileHandle2.close()

    def AnalyticsFunction(self):
        img = Image.open("./Graphs/BME.png")
        img.show()

    def typeOfError(self, error):
        if (error == "Addition"):
            self.addition += 1
        elif (error == "Substitution"):
            self.substitution += 1
        elif (error == "Deletion"):
            self.deletion += 1

    def newGivenWord(self):
        self.givenWord = self.wordList[random.randrange(0, stop=len(self.wordList))]

    def resetWords(self):
        self.givenWord = ""
        self.saidWord = ""

    def printGivenWord(self):
        self.canvasGivenWord.delete("all")
        self.canvasGivenWord.create_text(WIDTH / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                         text=self.givenWord)
        self.canvasGivenWord.update

    def printSaidWord(self):
        self.canvasSaidWord.delete("all")
        self.canvasSaidWord.create_text(WIDTH / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold",
                                        text=self.saidWord)
        self.canvasSaidWord.update

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
            self.master.quit()

    def testFunction(self):
        # patientName = input("File Name:")
        # path  = "./data/"+patientName+".txt"
        path = "patient3.csv"
        file1 = open(path, "r")

        for line in file1:
            line = line.strip()
            line1 = line.split(";")
            print(line1)
            self.givenWord = line1[0]
            self.saidWord = line1[1]
            self.checkWord()
            self.readOutCSV()


main()
