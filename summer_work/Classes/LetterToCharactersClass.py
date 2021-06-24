class LetterToCharacters():
    def __init__(self):
        self.letters = ["ch", "sh", "th", "wh", "ng", "nk", "wr", "str", "spr", "bl", "cl", "fl", "gl", "pl", "br",
                        "cr", "dr", "fr",
                        "gr", "pr", "tr", "sk", "sl", "sp", "st", "sw"]
        self.alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
                         "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                         "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
                         "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                         "y": 0, "z": 0, "!": 0, "@": 0, "#": 0, "$": 0, "%": 0, "^": 0, ")": 0, "*": 0, "(": 0, "_": 0}
        self.digraph_dict = {"ch": "!", "sh": "@", "th": "#", "wh": "$", "ng": "%", "nk": "^", "wr": ")"}

        self.blend_dict = {"str": "*", "spr": "(", "bl": "[", "cl": "]", "fl": "|", "gl": ":", "pl": "<", "br": ">",
                           "cr": "?", "dr": "~",
                           "fr": "`", "gr": "\u00d8", "pr": "\u00d9", "tr": "\u00da", "sk": "\u00db", "sl": "\u00dd",
                           "sp": "\u00de",
                           "st": "\u00df", "sw": "\u00e0"}

        self.combined_dict = {}
        self.combined_dict.update(self.digraph_dict)
        self.combined_dict.update(self.blend_dict)

        self.reverse_dict = {value: key for (key, value) in self.combined_dict.items()}

        self.allCombined = self.returnAllCombined()

    def lettersToCharacters(self, word):

        for item in self.letters:
            if item in word:
                var = word.index(item)
                word = word.replace(word[var: var + len(item)], self.combined_dict[item])
        return word

    def charactersToLetters(self, word):
        for item in self.reverse_dict.keys():
            if item in word:
                var = word.index(item)
                word = word.replace(word[var], self.reverse_dict[item])
        return word

    def returnCombined(self):
        return self.combined_dict

    def returnReversed(self):
        return self.reverse_dict
    def returnAllCombined(self):
        temp = self.alphabet
        temp.update(self.reverse_dict)
        return temp
    def formatDictForReturn(self,dict1):
        temp = dict1
        for char in temp:
            temp[char] = 0
        return temp
    def nestDict(self,dict1):
        temp = {}
        temp.update(dict1)
        temp1 = {}
        for char1 in temp:
            temp1 = {}
            temp1.update(dict1)
            temp[char1] = temp1
        return temp

    def returnFormated(self):
        temp = self.nestDict(self.formatDictForReturn(self.returnAllCombined()))
        return temp

