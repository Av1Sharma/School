def is_between(x, y, z):
    if( x < y and y < z):
        return True
    elif (z < y and y < x):
        return True
    else: 
        return False

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))

print(is_between(x, y, z))