import random


letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v","w","x","y","z"]
vowelList = ["a", "e", "i", "o", "u"]

def PatientSimulator(word):
    word = word.strip()
    firstIndexWord = firstIndex(word)
    middleVowelWord = middleVowel(word)
    additionEngingWord = additionEnding(word)



    fileHandle = open("patient3.csv", "a")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(firstIndexWord)
    fileHandle.write("\n")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(middleVowelWord)
    fileHandle.write("\n")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(additionEngingWord)
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
            word = listToString(wordlist)
            return word

def additionEnding(word):
    wordList = list(word)
    sList = ["s"]
    for letters in sList:
        wordList.append(letters)
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


wordFile = open("colorstext", "r")
for line in wordFile:
    PatientSimulator(line)

    print(line)
