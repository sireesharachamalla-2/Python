codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}
r = {new_labels[key]: value for key, value in codes.items()}
print(r)