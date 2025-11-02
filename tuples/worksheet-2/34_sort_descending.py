t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
t=list(t)
t = [list(i) for i in t]  

s = sorted(t)
t1 = s[::-1]             

t1 = [tuple(i) for i in t1] 
t1 = tuple(t1)              

print(t1)