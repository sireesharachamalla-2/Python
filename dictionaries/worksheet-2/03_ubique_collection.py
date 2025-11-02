auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
u=[]
for key in auction:
    u.append(auction[key])
u=set(u)
u=list(u)
print(u)