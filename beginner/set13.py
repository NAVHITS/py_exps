x = int(input())
flag = True
for i in range(1, x):
  if x % i == 0:
    flag = False
    break
if flag:
  print("yes")
else:
  print("no")
