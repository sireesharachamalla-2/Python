dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
c=0
r={}
for i in dicts:
    if len(i)>c:
        c=len(i)
        r=i 
print(r)