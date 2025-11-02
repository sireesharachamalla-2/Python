orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
f=[]
r={}
for i in orders:
    if i not in f:
        r[i]=orders.count(i)
        f.append(i)
print(r)