## Example of for loop reading letters

for letter in 'Gadsby':
    print(letter, end=' ')

## We can also generalize this idea:


def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False


## Reading a word list:

file_object = open('words.txt')

## Reads all characters until new line:
line = file_object.readline()
print(line)

## We can also read the line, stripping all whitespaces, tabs, and newlines
word = line.strip()
print(word)

## We can increment just like in Java!:
z=1
z += 2

## Counting number of words in word list:
total = 0
for line in open('words.txt'):
    word = line.strip()
    total += 1


total = 0
count = 0

for line in open('words.txt'):
    words = line.split() # Originally was strip; but that assumes there is only one
    # word per line. This is cannot be the case.
    for word in words:
        total = total + 1
        if has_e(word):
            count += 1
print(count)
print(total)


## in operator

## We can use built in operators to check rather than building a crazy function

## These two do the same thing:

def has_e(word):
    if 'E' in word or 'e' in word:
        return True
    else:
        return False

def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False

## We can even go one step further:
def has_e(word):
    return 'E' in word or 'e' in word
## NOW we can go one step EVEN further:
word.lower()
def has_e(word):
    return 'e' in word.lower() ##The efficiency of this is debatable, but it looks


def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
