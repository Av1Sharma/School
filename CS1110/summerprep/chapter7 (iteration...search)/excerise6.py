## “Given a function, uses_any, which takes two strings and checks whether the first uses any of the letters in the second, 
# can you use it to write uses_all, which takes two strings and checks whether the first uses all the letters in the second, allowing repeats.”


def uses_any(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return True
    return False


def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True



## Going one step further:


def uses_all(word, required):
    for letter in required:
        if not uses_any(word, letter):
            return False
    return True