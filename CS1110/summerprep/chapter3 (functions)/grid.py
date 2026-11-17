def header():
    print('+----+----+----+')

def columns():
    print('|    |    |    |')

def do_four(f):
    f()
    f()
    f()
    f()

def repeat_print(f, n):
    f()
    do_four(n)
    f()
    do_four(n)

repeat_print(header, columns)
header()