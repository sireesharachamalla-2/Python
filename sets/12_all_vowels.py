words = ["education", "python", "sequoia"]
v="aeiou"
n=[]
for i in words:
    c=0
    for j in v:
        if j in i:
            if j in i:
                c=c+1
    if c==len(v):
        n.append(i)
print(n)