kids = {"Amy", "Bob", "Cara", "Dan", "Eva"}
size = 3
l=[]
c=0
for i in kids:
    if len(i)==size and c<size:
        c=c+1
        l.append(i)
print(tuple(l))