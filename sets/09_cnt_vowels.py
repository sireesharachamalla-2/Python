msg = "hello world"
v="aeiouAEIOU"
c=0
for i in msg:
    if i in v:
        c=c+1
print(c)