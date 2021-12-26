def OddAndEven(Arr,N):
  for i in range(N):
    if Arr[i] % 2 == 0:
      Arr[i] += 1
    else:
      Arr[i] -= 1
  print(*Arr)