def iso(x):
  y = list(set([i for i in x]))
  a = []
  for i in y:
      a.append(x.count(i))
  return a
val = input().split()
c1 = iso(val[0])
c2 = iso(val[1])
if sorted(c1) == sorted(c2):
  print("yes")
else:
  print("no")
