""""Imports"""
import os
import glob

""""Class"""
class DictionaryCreator():
    def __init__(self):
        self.files = []
    def readFilesFromDir(self,directoryPath):
        for fileName in glob.glob("*/ErrorFile*.csv"):

            self.files.append(fileName)

lol = DictionaryCreator()
lol.readFilesFromDir("./outData")
print(lol.files)


