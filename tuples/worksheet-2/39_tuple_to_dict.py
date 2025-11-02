t = (('a', 1), ('b', 2), ('c', 3))
temp={}
for i in range(len(t)):
    for j in range(len(t[i])):
        temp[t[i][j]]=t[i][1]
        break
print(temp)
    