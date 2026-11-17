## You can select characters from a string
## Example below:

fruit = 'banana'
letter = fruit[1]

## Returns a 
## We can also use a variable in the brackets

i = 1
fruit[i]

## Shortcut to find last letter in string:

fruit[-1]

## Counts from last letter, so you can use -2 to find the second to last letter and so on



## String Slices
## Starts from 0 (inclusive) ends at 3 (exclusive)
fruit[0:3]

## You can omit the start index and it will default to 0
fruit[:3]

## You can omit the end index and it will default to the end of the string
fruit[3:]

# If the first index is greater than or equal to the second, 
# the result is an empty string, represented by two quotation marks:
fruit[3:3]

## Cannot use it to change assignment:
greeting = 'Hello, world!'
greeting[0] = 'J'

## DOES NOT WORK!!!!!!

## But you can do this:

new_greeting = 'J' + greeting[1:]
new_greeting

## HAS NO EFFECT ON THE ORIGINAL STRING


## String comparison:

word = 'banana'

if word == 'banana':
    print('All right, banana.')

## WE can also use the less than or greater than operators:

def compare_word(word):
    if word < 'banana':
        print(word, 'comes before banana.')
    elif word > 'banana':
        print(word, 'comes after banana.')
    else:
        print('All right, banana.')

compare_word('apple')

## PRINTS:
## apple comes before banana.

## NOTE: Python does not handle uppercase and lowercase letters the same way people do. 
# All the uppercase letters come before all the lowercase letters, so:
compare_word('Pineapple')

## PRINTS:
## Pineapple comes before banana.


## Regular Expressions

text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."

pattern = 'Dracula'

import re

result = re.search(pattern, text)
print(result)

## Results also has fields such as:

result.string ## Contains the text that was searched.

result.group() ## Contains the part of the string that matched the pattern.

result.span() ## Returns idnex of where the pattern starts and ends.

## String substitution:

pattern = 'cent(er|re)'

## In this pattern, the parentheses enclose the part of the pattern the vertical bar applies to.

## Meaning: Match 'center' or 'centre'.

result = find_first(pattern)
result.string


pattern = 'colou?r'
#This pattern matches either “colour” with the 'u' or “color” without it.

result = find_first(pattern)
line = result.string


# Now suppose we want to produce an edition of the book with American spellings. 
# We can use the sub function in the re module, which does string substitution.
re.sub(pattern, 'color', line)






