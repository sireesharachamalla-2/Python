nums = [10, 15]
n=[]
for i in nums:
    for j in range(1,i+1):
        if i%j==0:
            n.append(j)
r=[]
result={}
for i in n:
    if i not in r:
        result[i]=n.count(i)
print(result)