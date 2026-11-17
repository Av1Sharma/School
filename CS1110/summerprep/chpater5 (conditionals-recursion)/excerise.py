def is_triangle(a, b, c):
    if(a + b > c) and (a+c > b) and (b + c > a):
        return True
    else:
        return False


a = input("Enter the first length of the stick (in inches): ")
b = input("Enter the second length of the stick (in inches): ")
c = input("Enter the third length of the stick (in inches): ")

print(is_triangle(a, b, c))








