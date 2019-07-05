dem = list(map(int, input().split()))
n = list(map(int, input().split()))
n.sort(reverse=True)
print(n[dem[-1]-1])
