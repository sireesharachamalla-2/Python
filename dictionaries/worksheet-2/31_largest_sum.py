nums = [11, 20, 12, 21, 3]
n=[]
count=0
for i in nums:
    i=str(i)
    c=0
    for j in i:
        j=int(j)
        c=c+j 
    if len(str(c))>count:
        count=len(str(c))
print(count)