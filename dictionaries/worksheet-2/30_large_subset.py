words =  ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
a= {}
for i in words:
    key = ''.join(sorted(i))
    if key in a:
        a[key].append(i)
    else:
        a[key] = [i]

r = list(a.values())
c=0
for i in r:
    if len(i)>c:
        c=len(i)
print(c)