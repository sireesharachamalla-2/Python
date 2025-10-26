num=int(input())
temp=num
r=0
while num>0:
    d=num%10
    r=r*10+d
    num//=10
if(r==temp):
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")