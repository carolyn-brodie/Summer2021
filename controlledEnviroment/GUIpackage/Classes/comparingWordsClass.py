from GUIpackage.Classes import LetterToCharactersClass as LCT

class ComparingWordsC():
    def __init__(self):
        self.lct = LCT.LetterToCharacters()
        self.cTl = LCT.LetterToCharacters()
        self.givenWord = ""
        self.saidWord = ""

        self.wrongIndexList = []
        self.revisedWrongIndexList = []

        self.wrongLetterListInput = []
        self.wrongLetterListOutput = []

        self.typeOfErrors = ''

        self.LCS = ""
        self.shiftedWord = ""
        self.returnList = []

        self.whereErrorOccurred = ""
        self.totalList = []
        self.changedGivenWord = ""
        self.changedSaidWord = ""
    # Constructor, take the givenWord and the saidWord, have this be called first!!
    def constructor(self,givenWord,saidWord):
        self.givenWord = givenWord.lower()
        self.saidWord = saidWord.lower()
        self.changedGivenWord = self.lct.lettersToCharacters(self.givenWord)
        self.changedSaidWord = self.lct.lettersToCharacters(self.saidWord)
        self.saidList = list(self.changedSaidWord)
        self.givenList = list(self.changedSaidWord)
    def controller(self):
        if len(self.changedSaidWord) == len(self.changedGivenWord):
            self.equalSizedWordFunction()

            self.calcWrongListInputLess()

            self.whereErrorOccurs()

            self.calcLetters()

            self.typeOfError()


        elif len(self.changedSaidWord) > len(self.changedGivenWord):
            self.findLCS(self.changedGivenWord,self.changedSaidWord)
            self.calcWrongListInputGreater()
            self.shiftGiven()
            self.equalShiftedGivenFunction()
            self.whereErrorOccurs()
            self.calcLetters()
            self.typeOfError()


        else:
            self.findLCS(self.changedGivenWord,self.changedSaidWord)
            self.calcWrongListInputLess()
            self.shiftInput()
            self.equalShiftedInputFunction()
            self.whereErrorOccurs()
            self.calcLetters()
            self.typeOfError()

        for index in range(len(self.wrongLetterListInput)):
            change = self.cTl.charactersToLetters(self.wrongLetterListInput[index])
            self.wrongLetterListInput[index] = change

        for index in range(len(self.wrongLetterListOutput)):
            change = self.cTl.charactersToLetters(self.wrongLetterListOutput[index])
            self.wrongLetterListOutput[index] = change


    def equalSizedWordFunction(self):
        inputList = list(self.changedSaidWord)
        givenList = list(self.changedGivenWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def equalShiftedGivenFunction(self):
        inputList = list(self.changedSaidWord)
        givenList = list(self.shiftedWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def equalShiftedInputFunction(self):
        inputList = list(self.shiftedWord)
        givenList = list(self.changedGivenWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def findLCS(self,givenWord, inputWord):
        maxLength = 0
        if givenWord > inputWord:
            endingIndex = len(inputWord)

            longerWord = givenWord
            lenLonger = len(givenWord)
            smallerWord = inputWord
            lenSmaller = len(inputWord)

        elif givenWord < inputWord:
            endingIndex = len(givenWord)

            longerWord = inputWord
            lenLonger = len(inputWord)
            smallerWord = givenWord
            lenSmaller = len(givenWord)

        lookUpTable = [[0 for x in range(lenLonger + 1)] for y in range(lenSmaller + 1)]

        for smallerIndex in range(1, lenSmaller + 1):
            for longerIndex in range(1, lenLonger + 1):

                if smallerWord[smallerIndex - 1] == longerWord[longerIndex - 1]:
                    lookUpTable[smallerIndex][longerIndex] = lookUpTable[smallerIndex - 1][longerIndex - 1] + 1

                    if lookUpTable[smallerIndex][longerIndex] > maxLength:
                        maxLength = lookUpTable[smallerIndex][longerIndex]
                        endingIndex = smallerIndex
        self.LCS = (smallerWord[endingIndex - maxLength:endingIndex])

    def inputGreaterLCS(self):

        lenGiven = len(self.changedGivenWord)
        lenInput = len(self.changedSaidWord)

        maxLength = 0  # stores the max length of LCS
        endingIndex = lenGiven  # stores the ending index of LCS in `X`

        # `lookup[i][j]` stores the length of LCS of substring `X[0???i-1]` and `Y[0???j-1]`
        lookup = [[0 for x in range(lenInput + 1)] for y in range(lenGiven + 1)]

        # fill the lookup table in a bottom-up manner
        for i in range(1, lenGiven + 1):
            for j in range(1, lenInput + 1):

                # if the current character of `X` and `Y` matches
                if self.changedGivenWord[i - 1] == self.changedSaidWord[j - 1]:
                    lookup[i][j] = lookup[i - 1][j - 1] + 1

                    # update the maximum length and ending index
                    if lookup[i][j] > maxLength:
                        maxLength = lookup[i][j]
                        endingIndex = i
        # return longest common substring having length `maxLength`
        self.LCS = self.changedGivenWord[endingIndex - maxLength: endingIndex]

    def shiftInput(self):
        listOfOutputWordShifted = list(self.changedGivenWord)
        listOfInputWordShifted = list(self.changedSaidWord)
        startDiff = self.returnList[1][0] - self.returnList[0][0]
        for index in range(0,startDiff):
            listOfInputWordShifted.insert(index, "_")
        while len(listOfInputWordShifted) < len(self.changedGivenWord):
            listOfInputWordShifted.append("_")
        while len(listOfInputWordShifted) > len(listOfOutputWordShifted):
            listOfOutputWordShifted.append("_")
        self.shiftedWord = self.listToString(listOfInputWordShifted)
        self.changedGivenWord = self.listToString(listOfOutputWordShifted)

    def shiftGiven(self):
        listOfOutputWordShifted = list(self.changedGivenWord)
        listofInputWordShifted = list(self.changedSaidWord)
        startDiff = self.returnList[0][0] - self.returnList[1][0]
        for index in range(0,startDiff):
            listOfOutputWordShifted.insert(index, "_")
        while (len(listOfOutputWordShifted) < len(self.changedSaidWord)):
            listOfOutputWordShifted.append("_")
        while(len(listOfOutputWordShifted) > len(self.changedSaidWord)):
            listofInputWordShifted.append("_")

        self.shiftedWord = self.listToString(listOfOutputWordShifted)
        self.changedSaidWord = self.listToString(listofInputWordShifted)

    def listToString(self, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele
        # return string
        return str1

    def calcWrongListInputLess(self):
        startIndexInput = self.changedSaidWord.index(self.LCS)
        endIndexInput = startIndexInput + len(self.LCS) - 1
        self.returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = self.changedGivenWord.index(self.LCS)
        endIndexOutput = startIndexOutput + len(self.LCS) - 1
        self.returnList.append([startIndexOutput, endIndexOutput])

    def calcWrongListInputGreater(self):

        startIndexInput = self.changedSaidWord.index(self.LCS)
        endIndexInput = startIndexInput + len(self.LCS) - 1
        self.returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = self.changedGivenWord.index(self.LCS)
        endIndexOutput = startIndexOutput + len(self.LCS) - 1
        self.returnList.append([startIndexOutput, endIndexOutput])
    def whereErrorOccurs(self):
        for index in self.revisedWrongIndexList:
            if index == 0:
                self.whereErrorOccurred = "Beginning"
            elif (index == len(self.shiftedWord)-1):
                self.whereErrorOccurred = "End"
            else:
                self.whereErrorOccurred = "Middle"

    def calcLetters(self):
        if len(self.changedGivenWord) > len(self.changedSaidWord):
            for index in self.revisedWrongIndexList:
                self.wrongLetterListOutput.append(self.changedGivenWord[index])
                self.wrongLetterListInput.append(self.shiftedWord[index])
        elif len(self.changedGivenWord) < len(self.changedSaidWord):
            for index in self.revisedWrongIndexList:

                self.wrongLetterListInput.append(self.changedSaidWord[index])
                self.wrongLetterListOutput.append(self.shiftedWord[index])

        elif len(self.changedGivenWord) == len(self.changedSaidWord):
            for index in self.revisedWrongIndexList:
                self.wrongLetterListInput.append(self.changedSaidWord[index])
                self.wrongLetterListOutput.append(self.changedGivenWord[index])

    def typeOfError(self):
        if (self.changedSaidWord == self.changedGivenWord):
            self.typeOfErrors = "None"

        else:
            if(len(self.changedSaidWord) == len(self.changedGivenWord)):
                self.typeOfErrors = "Substitution"

            elif len(self.changedSaidWord) > len(self.changedGivenWord):
                self.typeOfErrors = "Addition"

            elif len(self.changedSaidWord) < len(self.changedGivenWord):
                self.typeOfErrors = "Deletion"

    def reset(self):
        self.changedGivenWord = ""
        self.changedSaidWord = ""

        self.saidList = list(self.changedSaidWord)
        self.GivenWord = list(self.changedGivenWord)

        self.wrongIndexList = []
        self.revisedWrongIndexList = []

        self.wrongLetterListInput = []
        self.wrongLetterListOutput = []

        self.typeOfErrors = []

        self.LCS = ""
        self.shiftedWord = ""
        self.returnList = []

        self.whereErrorOccurred = []

        self.totalList = []


