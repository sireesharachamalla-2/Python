list1=list(map(str,input().split()))
n=int(input())
new=[]
for i in list1:
    if len(i)>n:
        new.append(i)
print(new)