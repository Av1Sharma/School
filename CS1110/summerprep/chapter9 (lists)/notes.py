numbers = [42, 123]

cheeses = ['Cheddar', 'Edam', 'Gouda']

## ELEMENTS DONT NEED TO BE SAME TYPE:

t = ['spam', 2.0, 5, [10, 20]]

## len returns list size:
len(cheeses)


## Lists are mutable:

numbers[1] = 17
print(numbers)

## 42, 123 -> 42, 17

## in operator works on lists too:

print('Edam' in cheeses)


## Lists can have other lists, but nested list still counts as one element:

t = ['spam', 2.0, 5, [10, 20]]
len(t)
## prints 4

## and 10 is not considered to be an element of t because it is an element of a nested list, not t.
print(10 in t)
## false

## List Slices:

letters = ['a', 'b', 'c', 'd']
letters[1:3]
## ['b', 'c']

letters[:2]
## ['a', 'b']

letters[2:]
## ['c', 'd']

letters[:]
## ['a', 'b', 'c', 'd']

## Other way to copy list:
list(letters)

## This is called a shallow copy


## We can also add lists:
t1 = [1, 2]
t2 = [3, 4]
t1 + t2

# We can also use * to repeat:
['spam'] * 4
## ['spam', 'spam', 'spam', 'spam']

sum(t1)
## adds up all the elements in the list: 3

min(t1)
## 1
max(t2)
## 4

letters.append('e')


letters.extend(['f', 'g'])

t = ['a', 'b', 'c']
t.pop(1)
## returns 'b' and removes it from the list

t = ['a', 'b', 'c']
t.remove('b')
## removes the first occurence of 'b'


## If element is not in list, error occurs:
t.remove('d')
## ValueError: list.remove(x): x not in list

s = 'pining for the fjords'
t = s.split()

## ['pining', 'for', 'the', 'fjords']


s = 'ex-parrot'
t = s.split('-')

##['ex', 'parrot']


## We can also do this in the reverse:
delimiter = ' '
t = ['pining', 'for', 'the', 'fjords']
s = delimiter.join(t)

## Creates a string of 'pining for the fjords'