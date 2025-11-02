
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


nested_data = {
    "user": {
        "name": "Alice",
        "address": {
        "city": "Wonderland",
        "zip": "12345"
        }
    },
    "status": "active"
}

flat_data = flatten_dict(nested_data)
print("Flattened Dictionary:")
for k, v in flat_data.items():
    print(f"{k}: {v}")
