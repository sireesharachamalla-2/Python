salaries = {'A': 20000, 'B': 30000}
for key,value in salaries.items():
    salaries[key]=value+(value*10/100)
print(salaries)