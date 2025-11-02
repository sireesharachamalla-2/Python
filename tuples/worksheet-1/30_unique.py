t=((1,2),(2,3),(3,4))
f=tuple(x for i in t for x in i)
print(set(f))