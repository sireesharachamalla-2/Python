s=input().split()
r=[]
replace={
    "apples":"oranges","bananas":"grapes"
}
for i in s:
    
    if i in replace:
        r.append(replace[i])
    else:
        r.append(i)
o=" ".join(word for word in r)
print(o)