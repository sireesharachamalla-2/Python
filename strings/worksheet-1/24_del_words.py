def count_word(n):
    words=n.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    for word in freq:
        print(f"{word}:{freq[word]}")

n=input()
count_word(n)