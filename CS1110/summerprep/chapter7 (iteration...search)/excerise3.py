def uses_all(word, required_letters):
    for letter in required_letters.lower():
        if letter not in word.lower():
            return False
    return True


word = input("Enter your word:")
