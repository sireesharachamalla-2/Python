l=list(map(int,input().split()))
p=int(input())
new_list=l[p:]
new_list=l[:p]+new_list[::-1]
print(new_list)