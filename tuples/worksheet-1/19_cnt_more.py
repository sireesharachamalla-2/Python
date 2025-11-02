t=(2,4,6,2,8,4,6,2)
r=[]
for i in t:
    if t.count(i) >=2 and i not in r:
        print(i)
        r.append(i)