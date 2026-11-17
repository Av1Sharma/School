def ackermann(m, n):
    if(m==0):
        return n+1
    elif (m> 0 and n ==0 ):
        return ackermann(m-1, 1)
    elif (m> 0 and n> 0):
        return ackermann(m-1, ackermann(m, n-1))
    else:
        print("Something went wrong...")



ackermann(5, 5) 
## This is runnable, but Python has a maximum recursion depth of about 1000 function calls.
## Therefore we never get the output of this code! Each m increase, exponentially increases the amount of function calls!