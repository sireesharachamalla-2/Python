s=input()
l=[]
for i in s:
    if i.isalnum() or i.isspace():
        l.append(i)
r="".join(char for char in l)
print(r)