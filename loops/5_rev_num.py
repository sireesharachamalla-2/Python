num=int(input())
if num==0:
    print(0)
else:
    if(num<0):
        print('-',end='')
        num=-num
    while num > 0:
        d=num%10
        print(d,end=' ')
        num=num//10
