import tkinter as tk
import WordQuizer
from summer_work.Classes import comparingWordsClass
from summer_work.Classes import LetterToCharactersClass


class PatientSimulator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.inPath = "../inData/patient4.csv"
        self.outPath = "../outData/test1"
        self.givenWord = ""
        self.saidWord = ""
        self.right = 0
        self.wrong = 0
        self.unanswered = 0
        self.comparingWords = comparingWordsClass.ComparingWordsC()

        self.runTest = tk.Button(self,text = "Run Test",command = lambda : self.runTestFunc())
        self.runTest.pack(side = "top")
    def runTestFunc(self):
        file1 = open(self.inPath, "r")

        for line in file1:
            line = line.strip()
            line1 = line.split(";")
            self.givenWord = line1[0]
            self.saidWord = line1[1]
            print(self.givenWord)
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

        except:
            self.sessionNumber2 = 1
            self.fileCreated2 = False

        self.fileHandle2 = open(self.outPath, "a")
        if self.fileCreated2 == False:
            self.fileHandle2.write("NumberOfWords;Word;WordSaid;WhereErrorOccurred;TypeOfError;LocationOfError;ExpectedLetterError;SaidLetterError" + "\n")
            self.fileCreated2 = True

        self.fileHandle2 = open(self.outPath,"a")
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




