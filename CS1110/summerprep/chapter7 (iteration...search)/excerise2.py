def uses_only(word, available):
    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True



word = input("Your Word:")
available = input("Available letters:")

print(uses_only(word, available))

