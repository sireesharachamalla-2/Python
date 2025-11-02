l=list(map(int,input().split()))
max_sum=0
for i in l:
    if i>0:
        max_sum+=i 
print(max_sum)