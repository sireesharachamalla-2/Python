s=input()
temp=""
for i in s:
    if i not in temp:
        temp=temp+i
    
print(temp)