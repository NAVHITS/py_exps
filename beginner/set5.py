def max(a, b, c):
  if a > b and a > c:
    big = a
  elif b > a and b > c:
    big = b
  else:
    big = c
  return big
a, b, c = map(int,input().split())
print(max(a, b, c))
