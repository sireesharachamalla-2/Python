s=input()
f=[]
d={}
for i in s:
    if i not in f:
        c=s.count(i)
        f.append(i)
        d[i]=c
print(d)