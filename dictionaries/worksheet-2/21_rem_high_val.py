d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10
for key, value in list(d.items()): 
    if isinstance(value, (int, float)) and value > limit:
        d.pop(key)
print(d)