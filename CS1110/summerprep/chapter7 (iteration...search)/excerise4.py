def checkWord(word, available, required):
    required_bool = False
    word = word.lower()
    available = available.lower()
    required = required.lower()
    if required not in word:
        return False
    for letter in word:
        if letter not in available:
            return False
    return True


def score_word(word, available):
    pangram = True
    for letter in available:
        if letter not in word:
            pangram = False
    if pangram == True:
        return 14
    elif len(word) == 4:
        return 1
    elif len(word) > 4:
        return len(word)



bello = input("Your Word: ")
print(checkWord(bello, "ACDLORT", "R"))


## Took me a minute bruh

## Definitely a way to simplify this code...
## TODO: Simplify