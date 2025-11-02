s=input()
r=""
count=1
o=""
for i in range(0,len(s)):
    c=0
    if s[i] not in r:
        r=r+s[i]
        for j in range(0,len(s)):
            if (s[i]==s[j]):
                c=c+1
    if c>count:
        count=c
        o=o+s[i]
print(o)