class ComparingWords():
    # This should be the function that is always called to give the indexs of the differences:
    def equalSizedWordFunction(self, inputWord, givenWord):
        inputList = list(inputWord)
        givenList = list(givenWord)
        wrongList = list("")
        for index in range(0, len(inputList)):
            if inputList[index] != givenList[index]:
                wrongList.append(index)
        return wrongList

    def inputLessSubStringReturn(self, inputWord, givenWord):
        lenInputWord = len(inputWord)
        lenGivenWord = len(givenWord)

        maxLength = 0  # stores the max length of LCS
        endingIndex = lenInputWord  # stores the ending index of LCS in `X`

        # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
        lookup = [[0 for x in range(lenGivenWord + 1)] for y in range(lenInputWord + 1)]

        # fill the lookup table in a bottom-up manner
        for i in range(1, lenInputWord + 1):
            for j in range(1, lenGivenWord + 1):

                # if the current character of `X` and `Y` matches
                if inputWord[i - 1] == givenWord[j - 1]:
                    lookup[i][j] = lookup[i - 1][j - 1] + 1

                    # update the maximum length and ending index
                    if lookup[i][j] > maxLength:
                        maxLength = lookup[i][j]
                        endingIndex = i

        # return longest common substring having length `maxLength`
        return inputWord[endingIndex - maxLength: endingIndex]

    def inputGreaterSubStringReturn(self, inputWord, givenWord):

        lenGiven = len(givenWord)
        lenInput = len(inputWord)

        maxLength = 0  # stores the max length of LCS
        endingIndex = lenGiven  # stores the ending index of LCS in `X`

        # `lookup[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
        lookup = [[0 for x in range(lenInput + 1)] for y in range(lenGiven + 1)]

        # fill the lookup table in a bottom-up manner
        for i in range(1, lenGiven + 1):
            for j in range(1, lenInput + 1):

                # if the current character of `X` and `Y` matches
                if givenWord[i - 1] == inputWord[j - 1]:
                    lookup[i][j] = lookup[i - 1][j - 1] + 1

                    # update the maximum length and ending index
                    if lookup[i][j] > maxLength:
                        maxLength = lookup[i][j]
                        endingIndex = i

        # return longest common substring having length `maxLength`
        return givenWord[endingIndex - maxLength: endingIndex]

    def calcWrongListInputLess(self, inputWord, givenWord):
        returnList = list()
        LCS = self.inputLessSubStringReturn(inputWord, givenWord)
        startIndexInput = inputWord.index(LCS)
        endIndexInput = startIndexInput + len(LCS) - 1
        returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = givenWord.index(LCS)
        endIndexOutput = startIndexOutput + len(LCS) - 1
        returnList.append([startIndexOutput, endIndexOutput])

        return returnList

    def calcWrongListInputGreater(self, inputWord, givenWord):
        returnList = list()
        LCS = self.inputGreaterSubStringReturn(inputWord, givenWord)
        startIndexInput = inputWord.index(LCS)
        endIndexInput = startIndexInput + len(LCS) - 1
        returnList.append([startIndexInput, endIndexInput])

        startIndexOutput = givenWord.index(LCS)
        endIndexOutput = startIndexOutput + len(LCS) - 1
        returnList.append([startIndexOutput, endIndexOutput])

        return returnList

    def shiftInput(self, inputWord, givenWord, returnList):

        listOfInputWordShifted = list(inputWord)
        startDiff = returnList[1][0] - returnList[0][0]
        for index in range(startDiff):
            listOfInputWordShifted.insert(index, "+")
        while len(listOfInputWordShifted) != len(givenWord):
            listOfInputWordShifted.append("+")

        return self.listToString(listOfInputWordShifted)

    def shiftGiven(self, inputWord, givenWord, returnList):
        listOfOutputWordShifted = list(givenWord)
        startDiff = returnList[0][0] - returnList[1][0]
        for index in range(startDiff):
            listOfOutputWordShifted.insert(index, "+")
        while (len(listOfOutputWordShifted) != len(inputWord)):
            listOfOutputWordShifted.append("+")

        return listOfOutputWordShifted

    def listToString(self, s):
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

            # return string
        return str1

    def inputAddition(self, inputWord, givenWord, wrongList):
        returnList = list("")
        for index in wrongList:
            returnList.append([inputWord[index], givenWord[index]])
        return returnList

    def inputDeletion(self, inputWord, givenWord, wrongList):
        returnList = list("")
        for index in wrongList:
            returnList.append([inputWord[index], givenWord[index]])
        return returnList

    def inputSubstition(self, inputWord, givenWord, wrongList):
        returnList = list("")
        for index in wrongList:
            returnList.append([inputWord[index], givenWord[index]])
        return returnList

    def controlFunctionExact(self, inputWord, givenWord):
        if len(inputWord) == len(givenWord):
            letterOfError = list("")
            wrongList = self.equalSizedWordFunction(inputWord, givenWord)
            placesSubAddDele = self.inputSubstition(inputWord, givenWord, wrongList)
            returnString = "Letters Substituted:\n"

            for outer in placesSubAddDele:
                returnString += "\t Replaced '" + outer[0] + "' with '" + outer[1] + "'\n"
                letterOfError.append(outer[1])
            return returnString
        elif len(inputWord) < len(givenWord):
            wrongList = self.calcWrongListInputLess(inputWord, givenWord)
            wordShifted = self.shiftInput(inputWord, givenWord, wrongList)
            wrongListRevised = self.equalSizedWordFunction(wordShifted, givenWord)
            placesSubAddDele = self.inputDeletion(wordShifted, givenWord, wrongListRevised)
            letterOfError = list("")

            returnString = "deletions or substitution:\n"
            for outer in placesSubAddDele:
                if (outer[0] == "+"):
                    returnString += "\t did not pronounce'" + outer[1] + "'\n"
                    letterOfError.append(outer[1])
                else:
                    returnString += "\t Replaced '" + str(outer[0]) + "' with '" + (outer[1]) + "'\n"
                    letterOfError.append(outer[1])

            return returnString
        elif len(inputWord) > len(givenWord):
            letterOfError = list("")
            wronglist = self.calcWrongListInputGreater(inputWord, givenWord)
            wordShifted = self.shiftGiven(inputWord, givenWord, wronglist)
            wronglistRevised = self.equalSizedWordFunction(inputWord, wordShifted)
            placesSubAddDele = self.inputAddition(inputWord, wordShifted, wronglistRevised)

            returnString = "additions or substitution:\n"
            for outer in placesSubAddDele:
                if (outer[0] == "+"):
                    returnString += "\t added '" + outer[1] + "'\n"
                    letterOfError.append(outer[1])
                else:
                    returnString += "\t Replaced '" + str(outer[0]) + "' with '" + (outer[1]) + "'\n"
                    letterOfError.append(outer[1])
                return returnString

    def typeOfError(self, inputWord, compareWord):
        inputList = list(inputWord)
        compareList = list(compareWord)
        if (inputWord == compareWord):
            return "None"
        else:
            if len(inputList) == len(compareList):
                return "Substitution"

            elif len(inputList) > len(compareList):
                return "Addition"

            elif len(inputList) < len(compareList):
                return "Deletion"

    def whereErrorOccurs(self, shiftedWord, wrongList):
        for index in wrongList:

            if index == 0:
                return "Beginning"
            elif (index == len(shiftedWord) - 1):
                return "End"
            else:
                return "Middle"

    def returnRevisedWrongList(self, inputWord, givenWord):
        if len(inputWord) == len(givenWord):
            letterOfError = list("")
            wrongList = self.equalSizedWordFunction(inputWord, givenWord)
            return wrongList
        elif len(inputWord) < len(givenWord):
            letterOfError = list("")
            wrongList = self.calcWrongListInputLess(inputWord, givenWord)
            wordShifted = self.shiftInput(inputWord, givenWord, wrongList)
            wrongListRevised = self.equalSizedWordFunction(wordShifted, givenWord)
            return wrongListRevised
        elif len(inputWord) > len(givenWord):
            wronglist = self.calcWrongListInputGreater(inputWord, givenWord)
            wordShifted = self.shiftGiven(inputWord, givenWord, wronglist)
            wronglistRevised = self.equalSizedWordFunction(inputWord, wordShifted)
            return wronglistRevised

    def letterList(self, inputWord, givenWord):
        if len(inputWord) == len(givenWord):
            letterOfError = list("")
            wrongList = self.equalSizedWordFunction(inputWord, givenWord)
            placesSubAddDele = self.inputSubstition(inputWord, givenWord, wrongList)
            for outer in placesSubAddDele:
                letterOfError.append(outer[1])
            return letterOfError
        elif len(inputWord) < len(givenWord):
            letterOfError = list("")
            wrongList = self.calcWrongListInputLess(inputWord, givenWord)
            wordShifted = self.shiftInput(inputWord, givenWord, wrongList)
            wrongListRevised = self.equalSizedWordFunction(wordShifted, givenWord)
            placesSubAddDele = self.inputDeletion(wordShifted, givenWord, wrongListRevised)
            for outer in placesSubAddDele:
                if (outer[0] == "+"):
                    letterOfError.append(outer[1])
                else:
                    letterOfError.append(outer[1])

            return letterOfError
        elif len(inputWord) > len(givenWord):
            letterOfError = list("")
            wronglist = self.calcWrongListInputGreater(inputWord, givenWord)
            wordShifted = self.shiftGiven(inputWord, givenWord, wronglist)
            wronglistRevised = self.equalSizedWordFunction(inputWord, wordShifted)
            placesSubAddDele = self.inputAddition(inputWord, wordShifted, wronglistRevised)

            for outer in placesSubAddDele:
                if outer[0] == "+":
                    letterOfError.append(outer[0])
                else:
                    letterOfError.append(outer[0])
                return letterOfError
