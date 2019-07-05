a = list(map(int, input().split()))
b = []
for i in range(a[0], a[1]):
  flag = True
  for j in range(2, i):
    if i % j == 0:
      flag = False
      break
  if flag and i != 1:
    b.append(str(i))
print(' '.join(b))
