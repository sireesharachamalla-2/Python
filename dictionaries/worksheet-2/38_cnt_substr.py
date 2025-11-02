from itertools import permutations
s = "abc"
perm_list = [''.join(p) for p in permutations(s)]
print(len(perm_list))