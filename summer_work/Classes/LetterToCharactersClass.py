class LetterToCharacters():
    def __init__(self):
        self.letters = ["ch", "sh", "th", "wh", "ng", "nk", "wr", "str", "spr", "bl", "cl", "fl", "gl", "pl", "br",
                        "cr", "dr", "fr",
                        "gr", "pr", "tr", "sk", "sl", "sp", "st", "sw"]

        self.digraph_dict = {"ch": "!", "sh": "@", "th": "#", "wh": "$", "ng": "%", "nk": "^", "wr": ")"}

        self.blend_dict = {"str": "*", "spr": "(", "bl": "[", "cl": "]", "fl": "|", "gl": ":", "pl": "<", "br": ">",
                           "cr": "?", "dr": "~",
                           "fr": "`", "gr": "\u00d8", "pr": "\u00d9", "tr": "\u00da", "sk": "\u00db", "sl": "\u00dd",
                           "sp": "\u00de",
                           "st": "\u00df", "sw": "\u00e0"}

        self.combined_dict = dict
        self.combined_dict.update(self.digraph_dict)
        self.combined_dict.update(self.blend_dict)

        self.reverse_dict = {value: key for (key, value) in self.combined_dict.items()}

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

