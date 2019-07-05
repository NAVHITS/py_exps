g = input()
rev = [int(i) for i in input().split()]
if rev.count(0) == len(rev):
	print(0)
else:
	a = ""
	rev.sort()
	for i in rev[::-1]:
		a+=str(i)
	print(a)
