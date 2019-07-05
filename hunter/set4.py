from collections import Counter
dem = input()
inp = list(map(int, input().split()))
t = Counter(inp)
print(min(t.keys(), key=(lambda inp: t[inp])))
