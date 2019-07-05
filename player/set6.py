def iso(x):
  y = list(set([i for i in x]))
  a = []
  for i in y:
      a.append(x.count(i))
  return a
val = input().split()
t1 = iso(val[0])
t2 = iso(val[1])
if sorted(t1) == sorted(t2):
  print("yes")
else:
  print("no")
