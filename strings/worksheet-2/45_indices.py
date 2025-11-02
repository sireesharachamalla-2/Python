str=input()
substr=input()
p=[]
for i in range(len(str)-len(substr)+1):
    if str[i:i+len(substr)]==substr:
        p.append(i)
print(p)