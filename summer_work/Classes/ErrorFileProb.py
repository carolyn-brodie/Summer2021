""""
Date: 6/22
"""

# Imports
import operator
import os
import LetterToCharactersClass as LTC
# Class
class ErrorFileDict:
    def __init__(self):
        ltc = LTC.LetterToCharacters()
        self.bothDictComb = ltc.returnAllCombined()

        self.occursDictionary = ltc.returnFormated()

        self.filePath = ""
        self.fileHandle = ""
        # If fileHandle is open the boolean set to True else boolean set to False
        self.fileHandleBoolean = False
    @staticmethod
    def merge(dict1, dict2):
        """
        :description: Merges two dictionaries together without modifying either
        :param: dict1 - The base dictionary
        :param: dict2 - The dictionary that will be appended onto the back of dict1
        :var: tempDict - Temporary dictionary to stop dict1 or dict2 from being overwritten
        :return: Returns a dict consisting of the combined dict1 and dict2
        """
        tempDict = dict1 | dict2
        return tempDict

    @staticmethod
    def createOccursDict(dict1):
        """
        :description: Creates a temp dictionary then updates temp so that it contains the dict (param), then temp nests
        into temp. (ie: dict = {"a":0,"b":0} then temp becomes temp = {"a":{"a":0,"b":0}, "b":{"a":0,"b":0}})
        :param dict: dict is the dictionary that temp will be created with
        :return: returns the nested dictionary
        """

    @staticmethod
    def populateOccurs(dict1,listOfLetters):
        """
        :desc: populates the occursList
        :param dict1: the occurs list that you want populated
        :param listOfLetters: The list of errors within the file read
        :return: returns the changed list
        """
        temp = {}
        temp.update(dict1)
        for listInside in listOfLetters:
            letter1 = listInside[0]
            letter2 = listInside[1]
            if letter1 in temp:
                if letter2 in temp[letter1]:
                    temp[letter1][letter2] = temp[letter1][letter2] + 1

        return temp

    def occursController(self,filePath):
        """
        :description: Is the controller for occurs
        :param filePath: Sets the filePath so it can be passed into self.SetFileHandle
        :return:
        """
        self.setFileHandle(filePath)
        self.openFileHandler()
        returnedList = self.formatFileHandle()
        self.closeFileHandler()
        self.occursDictionary = self.populateOccurs(self.occursDictionary,returnedList)

    def setFileHandle(self,filePath):
        """
        :Description: sets the path for the fileHandler to use
        :param filePath: The filepath.
        :return: No return
        """
        self.filePath = filePath
    def openFileHandler(self):
        """
        :description: Opens the fileHandler
        :return: No return
        """
        self.fileHandle = open(self.filePath,"r")
        self.fileHandleBoolean = True
    def closeFileHandler(self):
        """
        :description: Closes the fileHandler
        :return: No return
        """
        if self.fileHandleBoolean == True:
            self.fileHandle.close()
            self.fileHandleBoolean = False
        else:
            print("fileNotOpen")

    def checkFileHandle(self):
        """
        :Descrtiption: Checks if the fileHandle is open or closed
        :var:
        :return: No return
        """
        if self.fileHandle.closed:
            self.fileHandleBoolean == False
        else:
            self.fileHandleBoolean == True
    def formatFileHandle(self):
        """
        :description: creates a nestedList so that the occursDict can be populated
        :return: Returns a nestedList that includes the letters within the file. (ie: [[a,b]])
        """
        returnList = []

        for line in self.fileHandle:

            lineStripped = line.strip()
            lineSplit = lineStripped.split(";")

            letter1 = str(lineSplit[6]).strip("[]'")
            letter2 = str(lineSplit[7]).strip("[]'")

            returnList.append([letter1,letter2])
        return returnList

    def getOccursList(self):
        """ :return: returns the occursDictionary"""
        return self.occursDictionary

    def createHighestOccurenceList(self):
        returnList = []
        temp = {}
        temp.update(self.occursDictionary)

        for firstChar in temp:
            highestOccurence = 0
            highestSecondChar = None
            for secondChar in temp[firstChar]:
                if temp[firstChar][secondChar] > highestOccurence:
                    highestOccurence = temp[firstChar][secondChar]
                    highestSecondChar = secondChar
            returnList.append([firstChar,highestSecondChar,highestOccurence])
        return returnList

    def createHighestOccurence(self):
        returnList = []
        temp = {}
        temp.update(self.occursDictionary)
        highestOccurence = 0
        highestSecondChar = None
        highestFirstChar = None

        for firstChar in temp:

            for secondChar in temp[firstChar]:
                if temp[firstChar][secondChar] > highestOccurence:
                    highestOccurence = temp[firstChar][secondChar]
                    highestSecondChar = secondChar
                    highestFirstChar = firstChar
        returnList.append([highestFirstChar,highestSecondChar,highestOccurence])
        return returnList

lol = ErrorFileDict()
