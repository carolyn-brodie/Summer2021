import ErrorFileProb
import LetterToCharactersClass
import random

class PatientSimulatorClass():
    def __init__(self):
        self.LTCC = LetterToCharactersClass.LetterToCharacters()
        self.listAlph = list(self.LTCC.alphabet.keys())
        self.listDiag = list(self.LTCC.digraph_dict.values())
        self.listBlend = list(self.LTCC.blend_dict.values())
        self.listVowelBlend = list(self.LTCC.vowel_dict.values())
        self.listVowel = ["a", "e", "i", "o", "u"]

        self.listVowelTogether = self.listVowel + self.listVowelBlend
        self.listAllCombined = self.listAlph + self.listDiag + self.listBlend + self.listVowelBlend

        self.path = "./inData/ThousandWords"
        self.file1 = open(self.path, "r")
        self.wordList = self.file1.read().split("\n")
        self.fileLength = len(self.wordList)

        self.percentAddition = 25
        self.percentDeletion = 25
        self.percentVowel = 25
        self.percentFirstIndex = 25

    def constructor(self, percentAddition, percentDeletion, percentVowel, percentFirstIndex,percentFlip):
        self.percentAddition = percentAddition
        self.percentDeletion = percentDeletion
        self.percentVowel = percentVowel
        self.percentFirstIndex = percentFirstIndex
        self.percentFlip = percentFlip

        self.numberOfAddition = int(self.fileLength* (100/percentAddition))
        self.numberOfDeletion = int(self.fileLength*(100/percentDeletion))
        self.numberOfVowel = int(self.fileLength* (100/percentVowel))
        self.numberOfFirstIndex = int(self.fileLength* (100/percentFirstIndex))
        self.numberOfPercentFlip = int(self.fileLength*(100/percentFlip))

        for indexAd in range(self.numberOfAddition):
            numberAd = random.randrange(0,self.fileLength)

            word = self.wordList[numberAd]
            wordChanged = self.LTCC.lettersToCharacters(word)
            wordEdited = self.additionEnding(wordChanged)
            self.readOutWord(wordChanged,wordEdited)

        for indexDel in range(self.numberOfDeletion):
            numberDel = random.randrange(0,self.fileLength)
            word = self.wordList[numberDel]
            wordChanged = self.LTCC.lettersToCharacters(word)
            wordEdited = self.removeLetter(wordChanged)
            self.readOutWord(wordChanged,wordEdited)

        for indexVo in range(self.numberOfVowel):
            numberVow = random.randrange(0,self.fileLength)
            word = self.wordList[numberVow]
            wordEdited = self.middleVowel(word)
            self.readOutWord(wordChanged,wordEdited)

        for indexFirst in range(self.numberOfFirstIndex):
            numberVow = random.randrange(0,self.fileLength)
            word = self.wordList[numberVow]
            wordChanged = self.LTCC.lettersToCharacters(word)
            wordEdited = self.firstIndex(wordChanged)
            self.readOutWord(wordChanged,wordEdited)

        for indexFlip in range(self.numberOfPercentFlip):
            numberVow = random.randrange(0,self.fileLength)
            word = self.wordList[numberVow]
            wordChanged = self.LTCC.lettersToCharacters(word)

            firstLetter = wordChanged[random.randrange(len(wordChanged))]
            secondLetter = self.listAlph[random.randrange(len(self.listAlph))]
            wordEdited = self.flipLetters(wordChanged,firstLetter,secondLetter)
            self.readOutWord(wordChanged,wordEdited)


    def firstIndex(self,word):
        wordList = list(word)
        for index in range(len(word)):
            if word[index] in self.listAllCombined:
                wordList[index] = (self.listAllCombined)[random.randrange(len(self.listAllCombined)-1)]
                word = listToString(wordList)
                return word
        return word

    def middleVowel(self,word):
        wordlist = list(word)
        for index in range(len(word)):
            if word[index] in self.listVowelTogether:
                wordlist[index] = self.listVowelTogether[random.randrange(len(self.listVowelTogether))]
                word = listToString(wordlist)
                return word
        return word


    def additionEnding(self,word):
        wordList = list(word)
        sList = ["s"]
        for letters in sList:
            wordList.append(letters)
        word = listToString(wordList)
        return word

    def flipLetters(self,word, letter1, letter2):
        wordList = list(word)
        if letter1 in word and letter2 in word:
            index1 = wordList.index(letter1)
            index2 = wordList.index(letter2)
            tempLetter1 = wordList[index1]
            wordList[index1] = wordList[index2]
            wordList[index2] = tempLetter1
        else:
            index1 = wordList.index(letter1)
            index3 = random.randrange(len(word))
            wordList[index1] = wordList[index3]
            wordList[index3] = letter1
        word = listToString(wordList)
        return word

    def removeLetter(self,word):
        wordList = list(word)
        deletingLetter = wordList[random.randrange(len(wordList))]
        wordList.remove(deletingLetter)
        word = listToString(wordList)
        return word

    def readOutWord(self,givenWord,OutputWord):
        fileHandle = open("./inData/patient4.csv", "a")

        givenWord = self.LTCC.charactersToLetters(givenWord)
        OutputWord = self.LTCC.charactersToLetters(OutputWord)
        fileHandle.write(givenWord)

        fileHandle.write(";")
        fileHandle.write(OutputWord)

        fileHandle.write("\n")
        fileHandle.close()
        print(givenWord)
        print(OutputWord)
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

lol = PatientSimulatorClass()
lol.constructor(5,5,5,5,5)