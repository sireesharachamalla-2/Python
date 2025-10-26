e=int(input())
if e>=1000:
    print("Critical")
elif(e>=100) and (e<=999):
    print("Warning")
elif e<100:
    print("info")