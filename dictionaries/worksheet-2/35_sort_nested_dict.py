d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
r = {group: sorted(data.items()) for group, data in d.items()}
print(r)