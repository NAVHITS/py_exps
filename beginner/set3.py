import re
vowel = ['a','e','i','o','u']
str = input()
if re.match(r'[a-z0-9]', str, re.I):
  if str in vowel:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
