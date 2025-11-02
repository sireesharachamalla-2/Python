my_dict = {'a': 1, 'b': 2, 'c': 3}
keys, values = zip(*my_dict.items())
print(list(keys))  
print(list(values)) 

#or
keys=[]
values=[]
for i in my_dict:
    keys.append(i)
    values.append(my_dict[i])
print(keys)
print(values)