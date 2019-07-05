data = input()
words = data.split(" ")
newWords = [word[::-1] for word in words] 
print(" ".join(newWords))
