words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
a= {}
for i in words:
    key = ''.join(sorted(i))
    if key in a:
        a[key].append(i)
    else:
        a[key] = [i]

r = list(a.values())
print(r)