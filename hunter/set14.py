from itertools import permutations 
data_input = input()
permlst = permutations(data_input) 
for perm in list(permlst):
  print (''.join(perm)) 
