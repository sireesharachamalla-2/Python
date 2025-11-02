spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']
r={key:value for key,value in spells.items() if key not in banned}
print(r)