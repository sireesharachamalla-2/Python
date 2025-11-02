str=input()
l=len(str)
substr=input()
l1=len(substr)
for i in range(l):
    if str[i:i+l1]==substr:
        print(str[:i+l1])