n=list(map(str,input().split()))
c=0
for i in n:
    if len(i)>=2 and i[0]==i[len(i)-1]:
        c=c+1
print(c)