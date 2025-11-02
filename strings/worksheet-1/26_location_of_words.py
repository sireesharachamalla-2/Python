string = input()
word = input()

position = string.find(word)

if position != -1:
    print(position)
else:
    print("Word not found.")