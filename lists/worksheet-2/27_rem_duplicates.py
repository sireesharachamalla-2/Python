l=list(map(int,input().split()))
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)