vowel = ['a','e','i','o','u']
str = input()
if str =~ /^[a-z0-9]+$/i:
  if str in vowel:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
