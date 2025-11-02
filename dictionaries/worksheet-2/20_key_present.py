d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']
r={}
for i in lst:
    if i in d:
        r[i]=d[i]
print(r)