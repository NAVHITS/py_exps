dem = input()
a = list(map(int, input().split()))
x = []
for i in range(len(a)):
	if i == a[i]:
		x.append(i)
if x:
	for i in sorted(x):
		print(i, end=" ")
else:
	print(-1)
