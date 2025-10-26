n=int(input())
for i in range(2,n):
    m=0
    for j in range(2,i):
        if(i%j==0):
            m=m+1
    if(m==0):
        print(i)