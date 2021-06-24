letters = ["ch", "sh", "th", "wh", "ng", "nk", "wr", "str", "spr", "bl", "cl", "fl", "gl", "pl", "br", "cr", "dr", "fr",
           "gr", "pr", "tr", "sk", "sl", "sp", "st", "sw"]
digraph_dict = {"ch": "!", "sh": "@", "th": "#", "wh": "$", "ng": "%", "nk": "^", "wr": ")"}
blend_dict = {"str": "*", "spr": "(", "bl":"[", "cl":"]", "fl":"|", "gl":":", "pl":"<", "br":">", "cr":"?", "dr":"~",
                  "fr":"`", "gr":"\u00d8", "pr":"\u00d9", "tr":"\u00da", "sk":"\u00db", "sl":"\u00dd", "sp":"\u00de",
                  "st":"\u00df", "sw":"\u00e0"}
digraph_dict.update(blend_dict)
reverse_dict = {value:key for(key, value) in digraph_dict.items()}

def lettersToCharacters(word):

    for item in letters:
        if item in word:
            var = word.index(item)
            word = word.replace(word[var: var+len(item)], digraph_dict[item])
    return word


def charactersToLetters(word):
    for item in reverse_dict.keys():
        if item in word:
            var = word.index(item)
            word = word.replace(word[var], reverse_dict[item])
    return word

