""""
Date: 6/22
"""

# Imports


# Class
class ErrorFileDict:
    def __init__(self):
        self.alphabetDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
         "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
         "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
         "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
         "y": 0, "z": 0}

        self.letter2Char = {"!": 0, "@": 0, "#": 0, "$": 0, "%": 0, "^": 0, ")": 0, "*": 0, "(": 0,"_":0}

        self.bothDictComb = self.merge(self.alphabetDict,self.letter2Char)

        self.occursDictionary = self.createOccursDict(self.bothDictComb)
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
    def createOccursDict(dict):
        """
        :description: Creates a temp dictionary then updates temp so that it contains the dict (param), then temp nests
        into temp. (ie: dict = {"a":0,"b":0} then temp becomes temp = {"a":{"a":0,"b":0}, "b":{"a":0,"b":0}})
        :param dict: dict is the dictionary that temp will be created with
        :return: returns the nested dictionary
        """
        # Creates to blank dicts
        temp = {}
        temp1 = {}
        # Assigns both to be equal to dictionary
        temp.update(dict)
        temp1.update(dict)
        for char in temp:
            temp[char] = temp1
        return temp

lol = ErrorFileDict()
print(lol.occursDictionary["a"]["b"])
