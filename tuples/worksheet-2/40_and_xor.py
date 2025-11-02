t1 = (1, 2, 3)
t2 = (2, 2, 2)
And=[]
xor=[]
for i in range(len(t1)):
    a=t1[i]&t2[i]
    x=t1[i]^t2[i]
    And.append(a)
    xor.append(x)
And=tuple(And)
xor=tuple(xor)
print(And)
print(xor)