x = input()
k = int(x[-1])
y = [int(z) for z in input().split()]
print(sum(y[:k-1]))
