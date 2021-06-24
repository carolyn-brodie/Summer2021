import random


letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v","w","x","y","z"]
vowelList = ["a", "e", "i", "o", "u", "ai", "au", "aw", "ay", "ea", "ee", "ei", "eo", "eu", "ew", "ey", "ie", "oa", "oi", "oe", "oo", "ou", "ow","oy", "ue", "ui"]

def PatientSimulator(word,string):
    word = word.strip()
    if string == "firstIndex":
        changedWord = firstIndex(word)
    elif string == "vowel":
        changedWord = middleVowel(word)
    elif string == "addition":
        changedWord = additionEnding(word)
    else:
        changedWord = removeLetter(word)



    fileHandle = open("patient3.csv", "a")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(changedWord)
    fileHandle.write("\n")

    fileHandle.close()

def firstIndex(word):
    wordList = list(word)
    for index in range(len(word)):
        if word[index] in letterList:
            wordList[index] = letterList[random.randrange(len(letterList))]
            word = listToString(wordList)
            return word

def middleVowel(word):
    wordlist = list(word)
    for index in range(len(word)):
        if word[index] in vowelList:
            wordlist[index] = vowelList[random.randrange(len(vowelList))]
            if wordlist[index + 1] in vowelList:
                del wordlist[index + 1]
            word = listToString(wordlist)
            return word

def additionEnding(word):
    wordList = list(word)
    sList = ["s"]
    for letters in sList:
        wordList.append(letters)
    word = listToString(wordList)
    return word

def removeLetter(word):
    wordList = list(word)
    deletingLetter = wordList[random.randrange(len(wordList))]
    wordList.remove(deletingLetter)
    word = listToString(wordList)
    return word

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

subPercentage = int(input("Type % of Consonant Substitution Errors: "))
subPercentage1 = int(input("Type % of Vowel Substitution Errors: "))
addPercentage = int(input("Type % of Addition Errors: "))
delPercentage = int(input("Type % of Deletion Errors: "))


wordFile = open("musictext", "r")
wordList = wordFile.read().split("\n")
wordListLength = len(wordList)
for item in range(len(wordList)):
    if item < ((subPercentage * wordListLength) / 100):
        PatientSimulator(wordList[item],"firstIndex")
    elif item < (((subPercentage + subPercentage1) * wordListLength) / 100):
        PatientSimulator(wordList[item],"vowel")
    elif item < (((subPercentage + subPercentage1 + addPercentage) * wordListLength) / 100):
        PatientSimulator(wordList[item], "addition")
    else:
        PatientSimulator(wordList[item], "deletion")


