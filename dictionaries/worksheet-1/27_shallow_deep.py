import copy

original = {
    'name': 'Alice',
    'scores': [90, 85, 92]
}

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

# Change inner list in original
original['scores'][0] = 100

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)