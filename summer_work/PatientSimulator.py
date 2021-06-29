import random

consonantList = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v",
              "w","x","y","z"]
vowelList = ["a", "e", "i", "o", "u", "ai", "au", "aw", "ay", "ea", "ee", "ei", "eo", "eu", "ew", "ey", "ie", "oa", "oi",
             "oe", "oo", "ou", "ow","oy", "ue", "ui"]

def PatientSimulator(word,string):
    word = word.strip()
    if string == 1:
        changedWord = firstIndex(word)
    elif string == 2:
        changedWord = middleVowel(word)
    elif string == 3:
        changedWord = additionEnding(word)
    elif string == 4:
        changedWord = removeLetter(word)
    else:
        changedWord = flipLetters(word,"c","h")



    fileHandle = open("patient3.csv", "a")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(str(changedWord))
    fileHandle.write("\n")

    fileHandle.close()

def firstIndex(word):
    wordList = list(word)
    for index in range(len(word)):
        if word[index] in consonantList:
            tempLetter = random.randrange(len(consonantList))
            wordList[index] = consonantList[tempLetter]
            if wordList[index] == word[index]:
                if tempLetter < (len(consonantList) - 1):
                    wordList[index] = consonantList[tempLetter + 1]
                else:
                    wordList[index] = consonantList[tempLetter - 1]
            word = listToString(wordList)
            return word

def middleVowel(word):
    wordList = list(word)
    for index in range(len(word)):
        if word[index] in vowelList:
            if len(word) >= (index + 2) and word[index: index + 2] in vowelList:
                del wordList[index + 1]
            tempLetter = random.randrange(len(vowelList))
            wordList[index] = vowelList[tempLetter]
            if wordList[index] == word[index]:
                if tempLetter < (len(vowelList) - 1):
                    wordList[index] = vowelList[tempLetter + 1]
                else:
                    wordList[index] = vowelList[tempLetter - 1]
            word = listToString(wordList)
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

def flipLetters(word,letter1,letter2):
    wordList = list(word)
    if letter1 in word and letter2 in word:
        index1 = wordList.index(letter1)
        index2 = wordList.index(letter2)
        tempLetter1 = wordList[index1]
        wordList[index1] = wordList[index2]
        wordList[index2] = tempLetter1
    else:
        tempLetter2 = wordList[0]
        index3 = random.randrange(1,len(word)-1)
        wordList[0] = wordList[index3]
        wordList[index3] = tempLetter2
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
try:
    subPercentage = int(input("Type % of Consonant Substitution Errors: "))
    subPercentage1 = int(input("Type % of Vowel Substitution Errors: "))
    addPercentage = int(input("Type % of Addition Errors: "))
    delPercentage = int(input("Type % of Deletion Errors: "))
    swapPercentage = int(input("Type % of Swapping Substitution Errors: "))
except:
    print("You entered invalid numbers. Please enter whole numbers.")
    subPercentage = 20
    subPercentage1 = 20
    addPercentage = 20
    delPercentage = 20
    swapPercentage = 20

percentSum = subPercentage + subPercentage1 + addPercentage + delPercentage + swapPercentage
if percentSum != 100:
    print("Warning: Your percentages do not add up to 100!")

wordFile = open("musictext", "r")
wordList = wordFile.read().split("\n")
wordListLength = len(wordList)
for item in range(len(wordList)):
    if item < ((subPercentage * wordListLength) / 100):
        PatientSimulator(wordList[item],1)
    elif item < (((subPercentage + subPercentage1) * wordListLength) / 100):
        PatientSimulator(wordList[item],2)
    elif item < (((subPercentage + subPercentage1 + addPercentage) * wordListLength) / 100):
        PatientSimulator(wordList[item], 3)
    elif item < (((subPercentage + subPercentage1 + addPercentage + delPercentage) * wordListLength) / 100):
        PatientSimulator(wordList[item], 4)
    else:
        PatientSimulator(wordList[item], 5)