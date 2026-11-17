def repeat(word, n):
    print(word * n)

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam, Wonderful Spam!)')
    repeat(spam, 2)

spam = 'Spam, '
first_two_lines()
last_three_lines()