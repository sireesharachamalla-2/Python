valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
print(max(valuables,key=valuables.get))
print(min(valuables,key=valuables.get))