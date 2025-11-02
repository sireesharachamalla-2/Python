s=input()
c=0
v=set('aeiouAEIOU')
for i in s:
    if i in v:
        c=c+1 
print(c)