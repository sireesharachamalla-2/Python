n=input()
n=list(n)
for i in range(len(n)):
    if n[i]==",":
        n[i]="."
    elif n[i]==".":
        n[i]=","
n="".join(n)
print(n)