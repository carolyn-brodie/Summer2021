import tkinter as tk
import speech_recognition as sr
import random
import comparingWordsClass
import PIL.Image
import datetime
import rpy2.robjects as ro
from tkinter import *


WIDTH = 600
HEIGHT = 600
TEXT_SIZE = 10
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
    def __init__(self,master):
        # List of wrong, right, unheard words.
        now = datetime.datetime.now()
        self.fileAppend = str(str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"-"+str(now.minute))
        print(self.fileAppend)
        self.wrongList = []
        self.rightList = []
        self.unHeardList = []

        self.outCSVFile = "ErrorFile_"+self.fileAppend+".csv"
        self.readPercPercentFile = "RightWrongUnheard1.csv"
        self.readPercErrorFile = "TypeOfError.csv"

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
        self.path = ""
        self.path1 = "../"

        # The speech recognizer that we are using.
        self.recognizer = sr.Recognizer()

        # The devices index that we use, change the index if theres a error
        self.mic = sr.Microphone(device_index=1)

        # The file name that we use
        self.fileName = "inData/ThousandWords"

        # Opening the file
        self.file = open(self.fileName, "r")

        # Creates a word list called wordList that has each word from the file.
        self.wordList = []

        self.addition = 0
        self.deletion = 0
        self.substitution = 0
        self.e = 0
        # Reads through each line of the word file appending the word to the wordList.
        for line in self.file:
            self.wordList.append(line.strip("\n"))

        super(GUI, self).__init__(master)

        # calls the pack
        self.pack()

        # Creates the starting front page:
        self.create_widgets()

        # Creates a instance of the comparingWords class so we can use it in later functions
        self.comparingWords = comparingWordsClass.ComparingWordsC()

    #     Create widgets:
    #           makes the start button.
    def create_widgets(self):

        # Creates the start button which then calls the start function.
        self.testButton = tk.Button(self,text = "testButton",command = self.testFunction)
        self.testButton.grid(row = 4)
        self.startButton = tk.Button(self,text = "Start",command = self.startFunction)
        self.startButton.grid(row = 1,column = 0)

        self.analyticsButton = tk.Button(self,text = "Analytics",command = self.AnalyticsFunction)
        self.analyticsButton.grid(row = 3,column = 0)

        # Exits the programs but does not call the write to file function.
        self.mainPageExit = tk.Button(self,text = "Exit",command =lambda :self.master.quit())
        self.mainPageExit.grid(row = 2,column = 0)
    # Is called on press of the start function
    def startFunction(self):
        # Destroys the startButton and the MainPageExit
        self.startButton.destroy()
        self.mainPageExit.destroy()
        self.analyticsButton.destroy()

        self.audioButton = tk.Button(self,text = "Record Audio", command = self.audioFunction)
        self.audioButton.grid(row = 1,column = 0)

        self.nextButton = tk.Button(self, text="Next", command=self.nextFunction)
        self.nextButton.grid(row=2, column=0)

        self.exitButton = tk.Button(self,text = "Exit",command = self.exitFunction)
        self.exitButton.grid(row = 3,column = 0)

        self.labelGivenWord = tk.Label(self,text = "Say the Give Word")
        self.labelGivenWord.grid(row = 5)
        # Creates a canvas for the given word
        self.canvasGivenWord = tk.Canvas(self.master, width=WIDTH / 4,height=40)
        self.canvasGivenWord.pack(side = "top")

        # Creates a canvas for the said word
        self.canvasSaidWord = tk.Canvas(self.master, width=WIDTH / 4,height=40)
        self.canvasSaidWord.pack(side = "top")

        self.newGivenWord()
        self.printGivenWord()

    # Is called on the audioButton being pressed, starts the audio
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
            self.percOfSubstitution = (self.substitution) / (self.addition+self.substitution+self.deletion)
        except ZeroDivisionError:
            return 0

    def checkWord(self):
        if self.saidWord == self.givenWord:
            self.rightList.append(self.givenWord)
            self.numRight+= 1
        elif self.saidWord == "":
            self.unHeardList.append(self.givenWord)
            self.numUnSaid += 1
        else:
            self.wrongList.append(self.givenWord)
            self.numWrong += 1

    def readOutCSV(self):

        self.comparingWords.constructor(self.givenWord,self.saidWord)
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
            self.fileHandle2.write("NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
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

    def PieChartFunction(self,input1,output1,filename):
        self.pieChartButton.destroy()
        r = ro.r
        print(self.path1 + "PieChart.R")
        r.source(self.path1 + "PieChart.R")
        try:
            r.percent_Of_Sessions(input1, output1, filename)
        except:
            print(input1)
        img = PIL.Image.open("/Users/zachg/PycharmProjects/Summer2021a/summer_work/Classes/PieChartSessionStatsExample.png")
        img.show()


    def getNumberOfSession(self):
        self.textBox = tk.Entry(self)
        self.textBox.pack(side='bottom')
        self.pieChartButton1.destroy()
        self.a = Button(self, text='Enter Number of Sessions', command=self.getE)
        self.a.pack(side='bottom')

    def getE(self):
        self.e = self.textBox.get()
        self.e = int(self.e)
        self.pieChartButton = Button(self, text='Pie Chart',
                                     command=lambda: self.PieChartFunction(self.i, self.e, "SessionStatsExample"))
        self.pieChartButton.pack(side='bottom')

    def OverallSessionsFunction(self,input1,output1,filename):
        self.sessionsButton.destroy()
        r = ro.r
        print(self.path1 + "Sessions.R")
        r.source(self.path1 + "Sessions.R")
        try:
            r.plotSessions(input1, output1, filename)
        except:
            print(input1)
        img = PIL.Image.open(
            "/Users/zachg/PycharmProjects/Summer2021a/summer_work/Classes/LineGraphSessionStatsExample.png")
        img.show()

    def getNumberOfSession1(self):
        self.textBox = tk.Entry(self)
        self.textBox.pack(side='bottom')
        self.sessionsButton1.destroy()
        self.a = Button(self, text='Enter Number of Sessions', command=self.getE1)
        self.a.pack(side='bottom')

    def getE1(self):
        self.e = self.textBox.get()
        self.e = int(self.e)
        self.sessionsButton = Button(self, text='Overall Progress',
                                     command=lambda: self.OverallSessionsFunction(self.i, self.e, "SessionStatsExample"))
        self.sessionsButton.pack(side='bottom')

    def AnalyticsFunction(self):
        self.startButton.destroy()
        self.mainPageExit.destroy()
        self.analyticsButton.destroy()
        self.testButton.destroy()

        self.i = 1

        self.pieChartButton1 = Button(self, text='Pie Chart', command=self.getNumberOfSession)
        self.pieChartButton1.pack(side='bottom')

        self.sessionsButton1 = Button(self, text='Overall Progress', command=self.getNumberOfSession1)
        self.sessionsButton1.pack(side='bottom')

    def typeOfError(self,error):
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
        self.canvasGivenWord.create_text(WIDTH / 8, 15, fill="black", font="Times " + str(TEXT_SIZE) + " italic bold", text=self.givenWord)
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
        file1 = open(path,"r")

        for line in file1:
            line = line.strip()
            line1 = line.split(";")
            print(line1)
            self.givenWord = line1[0]
            self.saidWord = line1[1]
            self.checkWord()
            if self.givenWord != self.saidWord:
                self.readOutCSV()

main()