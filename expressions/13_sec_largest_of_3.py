a,b,c=20,12,18
large=(a+b+abs(a-b))/2
large=(large+c+abs(large-c))/2
small=(a+b-abs(a-b))/2
small=(small+c -abs(small-b))/2
slarge=(a+b+c)-large-small
print(int(slarge))