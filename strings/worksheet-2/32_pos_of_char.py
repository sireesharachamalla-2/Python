l=list(input().split())
k=int(input())
c=input()
for i in l:
    p=i.find(c)
    if p!=-1:
        print(p)
        