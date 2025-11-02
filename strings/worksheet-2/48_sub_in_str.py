s=list(input().split())
sub=list(input().split())
p=[]
for i in s:
    c=0
    for j in sub:
        if j in i:
            c=c+1
    if c==len(sub):
        p.append(i)
print(p)