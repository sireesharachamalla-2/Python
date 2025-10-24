n=150
k=2
bit=8
print(bin(n))
rotate=((n<<k)|(n>>(n-k))) & ((1<<n)-1)
print(bin(rotate))