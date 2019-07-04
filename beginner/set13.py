n = int(input())
flag = True
for i in range(1, n):
  if n % i == 0:
    flag = False
    break
if flag == True:
  print("yes")
else:
  print("no")
