import re
str = input()
if re.match(r'[a-z]', str, re.I):
  print("Alphabet")
else:
  print("No")
