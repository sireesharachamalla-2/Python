lst = ['a', 'b', 'c', 'd']
r = {}
for item in reversed(lst):
    r = {item: r}
print(r)