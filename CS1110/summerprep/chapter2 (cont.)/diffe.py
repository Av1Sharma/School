import math

x = 2

print(math.e ** 2,
math.pow(math.e, 2), 
math.exp(2))

# all these three are essentially doing the same thing but have different values
# both math.pow and math.e ** 2 use an approximation of the value of e
# however math.exp(2) is more accurate because it uses the actual value of e
# it is a specific operator used for e