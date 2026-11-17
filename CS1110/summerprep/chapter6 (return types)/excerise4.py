def gcd(a,b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)


print(gcd (17, 12))


## Notes: Had to write and thinnk about this on a piece of paper. After multiple examples with numbers, I realized
## that once modulo == 0, the lower number would just end up as the GCD. So I simply returned b when the modulo was 0
## I also noted that if the modulo was not zero, then it's just a factor of the two numbers, which is just 1. 
## However, this is not entirely correct. Example: gcd(20, 15) = 5


## So, I rehauled it. I added a second case, where we go down one step further to make sure the modulo explores
## all possible cases


## And then I still had cases that messed up. I realized that I could just recursively call until I ended at my base case!
## This changed my perception on how to handle recursive problems.abs

## First, always set ur base case. Once you've done that,
## Then ask "what do I need to do until I get to my base case?" as in what do I change when I call this function again.

