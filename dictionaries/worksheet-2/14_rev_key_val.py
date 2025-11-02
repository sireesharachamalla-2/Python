d = {'x': 100, 'y': 200}
v = 200

for key, value in d.items():
    if value == v:
        print({v: key}) 
        break  