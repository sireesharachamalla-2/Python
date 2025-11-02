n=list(input().split())
m=list(input().split())
u=[]
for i in n:
    if i not in m:
        u.append(i)
for j in m:
    if j not in n:
        u.append(j)
print(u)