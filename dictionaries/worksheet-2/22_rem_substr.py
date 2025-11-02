d = {'sun': 1, 'sunny': 2, 'rain': 3}
substring = 'sun'
for key in d:
    if substring not in key:
        print({key:d[key]})