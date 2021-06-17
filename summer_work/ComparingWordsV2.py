class ComparingWordsV2():
    def __init__(self):
        self.givenWord = ""
        self.saidWord = ""

        self.saidList = list(self.saidWord)
        self.givenList = list(self.givenWord)

        self.wrongIndexList = []
        self.revisedWrongIndexList = []

        self.wrongLetterList = []

        self.typeOfErrors = ''

        self.LCS = ""
        self.shiftedWord = ""
        self.returnList = []

        self.whereErrorOccurred = ""
        self.totalList = []

    # Constructor, take the givenWord and the saidWord, have this be called first!!
    def constructor(self,givenWord,saidWord):
        self.givenWord = givenWord
        self.saidWord = saidWord

    def controller(self):
        if len(self.saidWord) == len(self.givenWord):
            self.equalSizedWordFunction()

            self.calcWrongListInputLess()

            self.whereErrorOccurs()

            self.calcLetters()

            self.typeOfError()


        elif len(self.saidWord) > len(self.givenWord):
            self.inputGreaterLCS()
            self.calcWrongListInputGreater()
            self.shiftGiven()
            self.equalShiftedGivenFunction()
            self.whereErrorOccurs()
            self.calcLetters()
            self.typeOfError()


        else:
            self.inputLessLCS()
            self.calcWrongListInputLess()
            self.shiftInput()
            self.equalShiftedInputFunction()
            self.whereErrorOccurs()
            self.calcLetters()
            self.typeOfError()


    def equalSizedWordFunction(self):
        inputList = list(self.saidWord)
        givenList = list(self.givenWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def equalShiftedGivenFunction(self):
        inputList = list(self.saidWord)
        givenList = list(self.shiftedWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def equalShiftedInputFunction(self):
        inputList = list(self.shiftedWord)
        givenList = list(self.givenWord)
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                self.revisedWrongIndexList.append(index)

    def inputLessLCS(self):
        lenInputWord = len(self.saidWord)
        lenGivenWord = len(self.givenWord)

        maxLength = 0  # stores the max length of LCS
        endingIndex = lenInputWord  # stores the ending index of LCS in `X`

        # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
        lookup = [[0 for x in range(lenGivenWord + 1)] for y in range(lenInputWord + 1)]

        # fill the lookup table in a bottom-up manner
        for i in range(1, lenInputWord + 1):
            for j in range(1, lenGivenWord + 1):

                # if the current character of `X` and `Y` matches
                if self.saidWord[i - 1] == self.givenWord[j - 1]:
                    lookup[i][j] = lookup[i - 1][j - 1] + 1

                    # update the maximum length and ending index
                    if lookup[i][j] > maxLength:
                        maxLength = lookup[i][j]
                        endingIndex = i

        # return longest common substring having length `maxLength`
        self.LCS = self.saidWord[endingIndex - maxLength: endingIndex]

    def inputGreaterLCS(self):

        lenGiven = len(self.givenWord)
        lenInput = len(self.saidWord)

        maxLength = 0  # stores the max length of LCS
        endingIndex = lenGiven  # stores the ending index of LCS in `X`

        # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
        lookup = [[0 for x in range(lenInput + 1)] for y in range(lenGiven + 1)]

        # fill the lookup table in a bottom-up manner
        for i in range(1, lenGiven + 1):
            for j in range(1, lenInput + 1):

                # if the current character of `X` and `Y` matches
                if self.givenWord[i - 1] == self.saidWord[j - 1]:
                    lookup[i][j] = lookup[i - 1][j - 1] + 1

                    # update the maximum length and ending index
                    if lookup[i][j] > maxLength:
                        maxLength = lookup[i][j]
                        endingIndex = i
        # return longest common substring having length `maxLength`
        self.LCS = self.givenWord[endingIndex - maxLength: endingIndex]

    def shiftInput(self):

        listOfInputWordShifted = list(self.saidWord)
        startDiff = self.returnList[1][0] - self.returnList[0][0]
        for index in range(0,startDiff):
            listOfInputWordShifted.insert(index, "_")
        while len(listOfInputWordShifted) < len(self.givenWord):
            listOfInputWordShifted.append("_")
        self.shiftedWord = self.listToString(listOfInputWordShifted)

    def shiftGiven(self):
        listOfOutputWordShifted = list(self.givenWord)
        startDiff = self.returnList[0][0] - self.returnList[1][0]
        for index in range(0,startDiff):
            listOfOutputWordShifted.insert(index, "_")
        while (len(listOfOutputWordShifted) < len(self.saidWord)):
            listOfOutputWordShifted.append("_")
        self.shiftedWord = self.listToString(listOfOutputWordShifted)

    def listToString(self, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele
        # return string
        return str1

    def calcWrongListInputLess(self):
        startIndexInput = self.saidWord.index(self.LCS)
        endIndexInput = startIndexInput + len(self.LCS) - 1
        self.returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = self.givenWord.index(self.LCS)
        endIndexOutput = startIndexOutput + len(self.LCS) - 1
        self.returnList.append([startIndexOutput, endIndexOutput])

    def calcWrongListInputGreater(self):

        startIndexInput = self.saidWord.index(self.LCS)
        endIndexInput = startIndexInput + len(self.LCS) - 1
        self.returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = self.givenWord.index(self.LCS)
        endIndexOutput = startIndexOutput + len(self.LCS) - 1
        self.returnList.append([startIndexOutput, endIndexOutput])
    def whereErrorOccurs(self):
        for index in self.revisedWrongIndexList:
            if index == 0:
                self.whereErrorOccurred = "Beginning"
            elif (index == len(self.shiftedWord)):
                self.whereErrorOccurred = "End"
            else:
                self.whereErrorOccurred = "Middle"

    def calcLetters(self):
        if len(self.givenWord) > len(self.saidWord):
            for index in self.revisedWrongIndexList:
                self.wrongLetterList.append(self.givenWord[index])
        elif len(self.givenWord) < len(self.saidWord):
            for index in self.revisedWrongIndexList:
                self.wrongLetterList.append(self.shiftedWord[index])
        elif len(self.givenWord) == len(self.saidWord):
            for index in self.revisedWrongIndexList:
                self.wrongLetterList.append(self.saidWord[index])
    def typeOfError(self):
        if (self.saidWord == self.givenWord):
            self.typeOfErrors = "None"
        else:
            if(len(self.saidWord) == len(self.givenWord)):
                self.typeOfErrors = "Substitution"

            elif len(self.saidWord) > len(self.givenWord):
                self.typeOfErrors = "Addition"

            elif len(self.saidWord) < len(self.givenWord):
                self.typeOfErrors = "Deletion"

    def reset(self):
        self.givenWord = ""
        self.saidWord = ""

        self.saidList = list(self.saidWord)
        self.givenList = list(self.givenWord)

        self.wrongIndexList = []
        self.revisedWrongIndexList = []

        self.wrongLetterList = []

        self.typeOfErrors = []

        self.LCS = ""
        self.shiftedWord = ""
        self.returnList = []

        self.whereErrorOccurred = []

        self.totalList = []

input = "hue"
old = "blue"
#
app = ComparingWordsV2()

app.constructor(saidWord=input,givenWord=old)
app.controller()

print(app.shiftedWord)
print(app.LCS)
print(app.saidList)
print(app.wrongLetterList)
print(app.wrongIndexList)
print(app.revisedWrongIndexList)
