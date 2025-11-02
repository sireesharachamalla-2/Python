def sum_list(n):
    if not n:
        return 0
    return (n%10)+sum_list(n//10)

n=input()
print("sumof digits =",sum_list(n))
