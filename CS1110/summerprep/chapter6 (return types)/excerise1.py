def hypot(x, y):
    xsq = x ** 2 ## Note: Orginally tried to assign variable with x-sq; this is illegal in Python!
    ysq = y ** 2


    return (xsq + ysq) ** 0.5 

x = input("Enter length of first side: \n")
y = input("Enter length of first side: \n")
x = int(x) ## Note originally forgot to change the value into an int...After an input, it's still a string!
y = int(y)

print(hypot(x, y))