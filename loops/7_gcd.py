a=int(input())
b=int(input())

a=abs(a)
b=abs(b)

while b!=0:
    a,b=b,a%b
print(f"GCD is {a}")