d = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}]
index=1
r = sorted(d, key=lambda item: item['a'][index])
print(r)