t=(1,2,2,3,3,3)
r={}
for i in t:
    if i not in r:
        r[i]=t.count(i)
print(r)