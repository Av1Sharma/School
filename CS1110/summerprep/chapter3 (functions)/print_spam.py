def print_spam():
    print('spam') 

def do_twice(f, value):
    f(value)
    f(value) 
    
def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')

def do_four(f, value):
    do_twice(value)
    do_twice(value)


# Basically a way to do loops with functions...
# Learned how to called a function within a function...hinting at recursive algorithms

