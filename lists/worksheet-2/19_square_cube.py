list1=[]
for i in range(1,21):
    if i%2==0:
        list1.append(i**2)
    else:
        list1.append(i**3)
print(list1)