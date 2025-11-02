list1=list(map(int,input().split()))
r=int(input())
for i in list1:
    if i==r:
        list1.remove(i)
print(list1)