from collections import Counter
no = input()
x = [i for i in input().split()]
l = Counter(x)
r = []
for i, j in l.items():
	if j > 1:
		r.append(i)
if r:
	r.sort()
	print(' '.join(r))
else:
	print("unique")
