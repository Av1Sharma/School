def uses_none(word, forbidden_letters):
    for letter in word.lower():
        if letter in forbidden_letters.lower():
            return False
    return True


word = input("Enter your word")
forbidden_letters = input("Enter forbidden letters")

print(uses_none(word, forbidden_letters))