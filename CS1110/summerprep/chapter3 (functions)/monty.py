def right_justify(s):
    leading_spaces = 70 - len(s)
    print(' ' * leading_spaces + s)
    
right_justify('monty')