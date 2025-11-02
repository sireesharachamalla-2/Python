d = {'m': 1, 'n': 2, 'o': 1}
r = {}
for key, value in d.items():
    r.setdefault(value, []).append(key)
print(r)