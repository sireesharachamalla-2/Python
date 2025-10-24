a,b,c=14,27,19
#largest=max(a,b,c)
largest=(a+b+abs(a-b))//2
largest=(largest+c+abs(largest-c))//2
print(largest)