t = (("11", "22"), ("33", "44"))
print(t)
result = tuple(tuple(int(num) for num in inner) for inner in t)
print(result)