letters = ["ch", "sh", "th", "wh", "ng", "nk", "wr", "str", "spr", "bl", "cl", "fl", "gl", "pl", "br", "cr", "dr", "fr",
           "gr", "pr", "tr", "sk", "sl", "sp", "st", "sw", "ai", "au", "aw", "ay", "ea", "ee", "ei", "eo", "eu", "ew",
           "ey", "ie", "oa", "oe", "oi", "oo", "ou", "ow", "oy", "ue", "ui"]
digraph_dict = {"ch": "!", "sh": "@", "th": "#", "wh": "$", "ng": "%", "nk": "^", "wr": ")"}
blend_dict = {"str": "*", "spr": "(", "bl":"[", "cl":"]", "fl":"|", "gl":":", "pl":"<", "br":">", "cr":"?", "dr":"~",
                  "fr":"`", "gr":"\u00d8", "pr":"\u00d9", "tr":"\u00da", "sk":"\u00db", "sl":"\u00dd", "sp":"\u00de",
                  "st":"\u00df", "sw":"\u00e0"}
blend_dict = {}
vowel_dict = {"ai":"\u00e1", "au":"\u00e2", "aw":"\u00e3", "ay":"\u00e4", "ea":"\u00e5", "ee":"\u00e6", "ei":"\u00e7",
              "eo":"\u00e8", "eu":"\u00e9", "ew":"\u00ea", "ey":"\u00eb", "ie":"\u00ec", "oa":"\u00ed", "oe":"\u00ee",
              "oi":"\u00ef", "oo":"\u00f0", "ou":"\u00f1", "ow":"\u00f2", "oy":"\u00f3", "ue":"\u00f4", "ui":"\u00f5"}
digraph_dict.update(blend_dict)
digraph_dict.update(vowel_dict)
reverse_dict = {value:key for(key, value) in digraph_dict.items()}

def lettersToCharacters(word):

    for item in digraph_dict.keys():
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
