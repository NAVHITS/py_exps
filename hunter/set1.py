from collections import Counter
no = input()
lst = [i for i in input().split()]
l = Counter(lst)
res = []
for i, j in l.items():
	if j > 1:
		res.append(i)
if res:
	res.sort()
	print(' '.join(res))
else:
	print("unique")
