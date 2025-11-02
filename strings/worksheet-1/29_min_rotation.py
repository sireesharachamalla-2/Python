n=input()
i=1
l=len(n)
for i in range(1,l+1):
    r=n[l-i:]+n[:l-i]
    if(r==n):
        print(i)
        break