num=int(input())
for i in range(1,11):
    res=0
    for j in range(i):
        res+=num
    print(f"{num} x {i} = {res}")