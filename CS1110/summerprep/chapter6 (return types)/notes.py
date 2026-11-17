## Checking Types:


def factorial(n):
    if not isinstance(n, int):
        print('factorial is only defined for integers.')
        return None
    elif n < 0:
        print('factorial is not defined for negative numbers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


## Simple recursive algorithm to find factorial
## However, by using isinstance, we can get a boolean for our type
## And if it's not an int, we print the error and return none
