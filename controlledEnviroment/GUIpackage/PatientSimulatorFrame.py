import tkinter as tk
from GUIpackage.Classes import comparingWordsClass
import datetime
import os
from GUIpackage.sysVar import application_path
class PatientSimulator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        now = datetime.datetime.now()
        self.fileAppend = str(str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute))

        self.givenWord = ""
        self.saidWord = ""
        self.right = 0
        self.wrong = 0
        self.unanswered = 0
        self.comparingWords = comparingWordsClass.ComparingWordsC()

        self.runTest = tk.Button(self,text = "Run Test",command = lambda : self.runTestFunc())
        self.runTest.pack(side = "top")

        self.fileList = os.listdir(application_path+"\\inData\PatientFiles\\")
        self.fileListRev = []
        for files in self.fileList:
            self.fileListRev.append(os.path.splitext(files)[0])
        self.selection = tk.StringVar(self)
        self.selection.set(self.fileListRev[0])  # default value

        self.optionMenu = tk.OptionMenu(self, self.selection, *self.fileListRev)
        self.optionMenu.pack(side="top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side = "top")

    def runTestFunc(self):
        self.patient = self.selection.get()
        self.inPath = application_path+"\\inData\\PatientFiles\\"+self.patient+".csv"
        self.outPath = application_path+"\\outData\\ErrorFileDir\\"+self.patient+"ErrorFile"+".csv"
        file1 = open(self.inPath, "r")

        for line in file1:
            line = line.strip()
            line1 = line.split(";")
            self.givenWord = line1[0]
            self.saidWord = line1[1]
            self.readOutCSV()

    def checkWord(self):
        if self.saidWord.lower() != self.givenWord.lower():
            self.wrong += 1
        elif self.saidWord.lower() == "":
            self.unanswered += 1
        else:
            self.right += 1

    def readOutCSV(self):
        self.comparingWords.constructor(self.givenWord,self.saidWord)
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
            self.fileHandle2.write("NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        self.fileHandle2 = open(self.outPath,"a")
        self.fileHandle2.write(str(self.sessionNumber2))
        self.fileHandle2.write(";")
        self.fileHandle2.write(str(self.comparingWords.givenWord))
        print(self.comparingWords.givenWord)
        print(self.comparingWords.saidWord)
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

    def backFunction(self,controller):
        from GUIpackage.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)




