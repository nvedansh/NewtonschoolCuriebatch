def isArmstrong(N):
  result = 0
  temp = N # temp = 153
  # N = 153
  while N > 0:
     #termination condition
     last_digit = N % 10 #last_digit = 1
     result += (last_digit * last_digit * last_digit) #result = 153
     N //= 10 #N = 0

  if result == temp:
    return True
  else:
    return False