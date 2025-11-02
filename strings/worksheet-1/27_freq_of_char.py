from collections import Counter

def char_frequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in freq:
        print(f"{char} : {freq[char]}")


#or

text = input()
freq = Counter(text)
char_frequency(text)
print()
for char, count in freq.items():
    print(f"{char} : {count}")