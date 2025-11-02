d = {'x': 100, 'y': 'hello', 'z': 200}
r={key:value for key,value in d.items() if isinstance(value, int)}
print(r)