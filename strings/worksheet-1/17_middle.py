s=input()
l=len(s)
if l%2==1:
    print(s[l//2])
else:
    print(s[(l//2)-1:(l//2)+1])