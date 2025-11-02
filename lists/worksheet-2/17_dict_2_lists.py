list1=list(map(str,input().split()))
list2=list(map(int,input().split()))
new_list=dict(zip(list1,list2))
print(new_list)

# or
new_list1={}
for i in range(len(list1)):
    new_list1[list1[i]]=list2[i]
print(new_list1)