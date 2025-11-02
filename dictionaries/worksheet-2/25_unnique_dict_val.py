d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
r=[]
for key in d:
    if d[key] not in r:
        r.append(d[key])
print(r)