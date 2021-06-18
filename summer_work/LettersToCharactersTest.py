letters = ["ch", "sh", "th", "wh", "ng", "nk", "wr", "str", "spr"]

input1 = input("Type: ")

def lettersToCharacters(word):
    letters_dict = {"ch": "!", "sh": "@", "th": "#", "wh": "$", "ng": "%", "nk": "^", "wr": ")", "str": "*", "spr": "("}
    for item in letters:
        if item in word:
            var = word.index(item)
            word = word.replace(word[var: var+len(item)], letters_dict[item])
    return word

out = lettersToCharacters(input1)
print(out)

def charactersToLetters(word):
    character_dict = {"!": "ch", "@": "sh", "#": "th", "$": "wh", "%": "ng", "^": "nk", ")": "wr", "*": "str", "(": "spr"}

    for item in character_dict.keys():
        if item in word:
            var = word.index(item)
            word = word.replace(word[var], character_dict[item])
    return word

print(charactersToLetters(out))