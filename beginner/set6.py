yr = int(input())
if yr % 4 == 0:
  if yr % 100 == 0:
    if yr % 400 == 0:
      print("Yes")
    else:
      print("No")
  else:
    print("Yes")
else:
  print("No")
