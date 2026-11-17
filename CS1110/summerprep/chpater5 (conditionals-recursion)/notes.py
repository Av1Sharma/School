minutes = 105
print(minutes / 60)

## This prints out 1.75 -> we don't denote hours in decimals but rather in minutes

minutes = 105
hours = minutes // 60
print(hours)

## Quick and easy way to find the hour or the "floor"

remainder = minutes - hours * 60
print(remainder)

## Now we can find the amount of minutes remaining

## Another way shown below:

hours = minutes // 60
remainder = minutes % 60
print("There is " + str(hours) + " hours and " + str(remainder) + " minutes remaining.")


## Chained Conditionals:
x = 10
y = 25 

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

## Nested Conditionals:
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

## Keyboard Input

text = input()

# We can include text before prompting the user
name = input('What...is your name?\n')
