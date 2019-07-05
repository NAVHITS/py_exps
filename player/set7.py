a = input()
b = a[::2]
c = a[1::2]
x = ''
for i,j in zip(b,c):
    x += (j + i)
print(x)
