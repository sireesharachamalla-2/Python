lst = [(10,20,30),(40,50,60),(70,80,90)]
n=100
for i in range(len(lst)):
    temp=list(lst[i])
    temp[2]=n
    lst[i]=tuple(temp)
print(lst)