start = int(input())
if start == 0 or start == 1:
  print(1)
else:
  factorial = 1
  for i in range(2, start+1):
    factorial *= i
  print(factorial)
