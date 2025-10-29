def sign(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "Zero"
num=int(input())
print(sign(num))