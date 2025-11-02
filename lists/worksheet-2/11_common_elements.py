list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
common=(set(list1) & set(list2))
print(list(common))