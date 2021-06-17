#Replace in GUI.py def writeFilePerc(self): ... all of it

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
    if self.fileHandle == False:
        self.fileHandle.write("Sessions, Correct, Incorrect, NoResponse")
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