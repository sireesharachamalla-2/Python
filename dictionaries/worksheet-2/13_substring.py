d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'
r=[]
for key in d:
    if substring in key:
        r.append(key)
print(r)