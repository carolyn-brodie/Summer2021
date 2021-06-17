import tkinter as tk
import speech_recognition as sr
import random
import ComparingWordsV2

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
        self.wrongList = []
        self.rightList = []
        self.unHeardList = []

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
        self.mic = sr.Microphone(device_index=1)

        # The file name that we use
        self.fileName = "rWordsBeginning"

        # Opening the file
        self.file = open(self.fileName, "r")

        # Creates a word list called wordList that has each word from the file.
        self.wordList = []

        # Reads through each line of the word file appending the word to the wordList.
        for line in self.file:
            self.wordList.append(line.strip("\n"))

        super(GUI, self).__init__(master)

        # calls the pack
        self.pack()

        # Creates the starting front page:
        self.create_widgets()

        # Creates a instance of the comparingWords class so we can use it in later functions
        self.comparingWords = ComparingWordsV2.ComparingWordsV2()

    #     Create widgets:
    #           makes the start button.
    def create_widgets(self):

        # Creates the start button which then calls the start function.
        self.startButton = tk.Button(self,text = "Start",command = self.startFunction)
        self.startButton.grid(row = 1,column = 0)
        # Exits the programs but does not call the write to file function.
        self.mainPageExit = tk.Button(self,text = "Exit",command =lambda :self.master.quit())
        self.mainPageExit.grid(row = 2,column = 0)
    # Is called on press of the start function
    def startFunction(self):
        # Destroys the startButton and the MainPageExit
        self.startButton.destroy()
        self.mainPageExit.destroy()

        self.audioButton = tk.Button(self,text = "Record Audio", command = self.audioFunction)
        self.audioButton.grid(row = 1,column = 0)

        self.nextButton = tk.Button(self, text="Next", command=self.nextFunction)
        self.nextButton.grid(row=2, column=0)

        self.exitButton = tk.Button(self,text = "Exit",command = self.exitFunction)
        self.exitButton.grid(row = 3,column = 0)

        self.labelGivenWord = tk.Label(self,text = "Say the Give Word")
        self.labelGivenWord.grid(row = 4)
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
        self.calcPercentages()
        self.writeFilePerc()
        self.master.quit()

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

        self.fileHandle = open("excelFile1.csv", "a")
        self.fileHandle.write(str(self.comparingWords.givenWord))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.comparingWords.saidWord))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.comparingWords.whereErrorOccurred))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.comparingWords.typeOfErrors))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.comparingWords.wrongIndexList))
        self.fileHandle.write(";")
        self.fileHandle.write(str(self.comparingWords.wrongLetterList))
        self.fileHandle.write("\n")

        self.comparingWords.reset()
        self.fileHandle.close()

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
            self.sessions = open("statsForExcels.csv", "r")
            self.fileList = self.sessions.read().split("\n")
            self.sessions.close()

            self.sessionNumber = len(self.fileList) - 1

        except:
            self.sessionNumber = 1
            self.fileCreated = False

        self.fileHandle = open("statsForExcels.csv", "a")
        if self.fileCreated == False:
            self.fileHandle.write("Sessions, Correct, Incorrect, NoResponse" + "\n")
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
main()