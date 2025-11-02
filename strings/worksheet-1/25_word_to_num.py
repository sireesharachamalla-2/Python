
words = input().split()
numwords = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,"ten": 10}
    
c = []
for word in words:
    if word in numwords:
        c.append(str(numwords[word]))
    else:
        c.append(word)
r=" ".join(str for str in c)
print(r)