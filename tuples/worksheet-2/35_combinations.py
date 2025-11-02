t1=(1,2)
t2=(3,4)
r=[]
for i in range(len(t1)):
    for j in range(len(t2)):
        r.append((t1[i],t2[j]))
print(r)