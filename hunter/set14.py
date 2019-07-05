from itertools import permutations 
data = input()
permlst = permutations(str) 
for perm in list(permlst):
  print (''.join(perm)) 
