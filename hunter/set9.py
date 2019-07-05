from itertools import permutations
dem = input()
inp = list(map(int, input().split()))
r = 0
c = 10000
for i in permutations(inp, 2):
    if sum(i) == 0:
        j = i
        break
    elif 0-sum(i) < c:
        c = 0-sum(i)
        j = i
print(j[0], j[1])
