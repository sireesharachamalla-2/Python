s=input()
c=0
for i in s:
    if i!=i.isalnum():
        c=c+1 
if c>0:
    print("Yes")
else:
    print("No")