l=[(3,6),(9,12,15),(4,8)]
k=3
count=0
for i in range(len(l)):
    c=0
    for j in range(len(l[i])):
        if (l[i][j])%3==0:
            c=c+1
    if c==len(l[i]):
        count+=1
print(count)