n=input()
l=len(n)
c=0
for i in n:
    if i=="1" or i =="0":
        c=c+1
if c==l:
    print("Yes")
else:
    print("No")