def calc(a,b,choice):
    if choice=="s":
        return f"sum:{a+b}" 
    elif choise=="d":
        return f"Difference:{a-b}" 
a=int(input())
b=int(input())
choice=input()
print(calc(a,b,choice))