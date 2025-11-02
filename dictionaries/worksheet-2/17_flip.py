d = {'x': {'p': 1}, 'y': {'q': 2}}
r={}
for i,j in d.items():
    for k,l in j.items():
        r[k]={i:l}
print(r)