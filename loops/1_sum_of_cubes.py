num=int(input())
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d ** 3
    temp//=10

if num==sum:
    print(f"{num} is equal")
else:
    print(f"{num} is not equal")
