def parrot_trouble(talking, hour):
  if talking == False:
    return False
  
  if (hour < 7 or hour > 20):
    return True
  else:
    return False

## messed up here by failing to think about else statement
