import random


letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v",
              "w","x","y","z"]
vowelList = ["a", "e", "i", "o", "u", "ai", "au", "aw", "ay", "ea", "ee", "ei", "eo", "eu", "ew", "ey", "ie", "oa", "oi",
             "oe", "oo", "ou", "ow","oy", "ue", "ui"]

def PatientSimulator(word,string):
    word = word.strip()
    if string == "firstIndex":
        changedWord = firstIndex(word)
    elif string == "vowel":
        changedWord = middleVowel(word)
    elif string == "addition":
        changedWord = additionEnding(word)
    elif string == "remove":
        changedWord = removeLetter(word)
    else:
        changedWord = flipLetters(word)



    fileHandle = open("patient3.csv", "a")
    fileHandle.write(word)
    fileHandle.write(";")
    fileHandle.write(str(changedWord))
    fileHandle.write("\n")

    fileHandle.close()

# def getNewIndex(list1, word, index):
#     wordList = list(word)
#     tempLetter = random.randrange(len(list1))
#     wordList[index] = list1[tempLetter]
#     if wordList[index] == word[index]:
#         if tempLetter < (len(list1) - 1):
#             wordList[index] = list1[tempLetter + 1]
#         else:
#             wordList[index] = list1[tempLetter - 1]
#     return wordList

def firstIndex(word):
    wordList = list(word)
    for index in range(len(word)):
        if word[index] in letterList:
            tempLetter = random.randrange(len(letterList))
            wordList[index] = letterList[tempLetter]
            if wordList[index] == word[index]:
                if tempLetter < (len(letterList) - 1):
                    wordList[index] = letterList[tempLetter + 1]
                else:
                    wordList[index] = letterList[tempLetter - 1]
            # wordList = getNewIndex(letterList, word, index)
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
            # wordList = getNewIndex(vowelList,word,index)
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

def flipLetters(word):
    wordList = list(word)
    tempLetter = wordList[0]
    wordList[0] = wordList[len(wordList) - 1]
    wordList[len(wordList) - 1] = tempLetter
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

# subPercentage = int(input("Type % of Consonant Substitution Errors: "))
# subPercentage1 = int(input("Type % of Vowel Substitution Errors: "))
# addPercentage = int(input("Type % of Addition Errors: "))
# delPercentage = int(input("Type % of Deletion Errors: "))
# swapPercentage = int(input("Type % of Swapping Substitution Errors: "))

subPercentage = 25
subPercentage1 = 25
addPercentage = 0
delPercentage = 0
swapPercentage = 50

wordFile = open("ThousandWords", "r")
wordList = wordFile.read().split("\n")
wordListLength = len(wordList)
for item in range(len(wordList)):
    if item < ((subPercentage * wordListLength) / 100):
        PatientSimulator(wordList[item],"firstIndex")
    elif item < (((subPercentage + subPercentage1) * wordListLength) / 100):
        PatientSimulator(wordList[item],"vowel")
    elif item < (((subPercentage + subPercentage1 + addPercentage) * wordListLength) / 100):
        PatientSimulator(wordList[item], "addition")
    elif item < (((subPercentage + subPercentage1 + addPercentage + delPercentage) * wordListLength) / 100):
        PatientSimulator(wordList[item], "deletion")
    else:
        PatientSimulator(wordList[item], "swap")


