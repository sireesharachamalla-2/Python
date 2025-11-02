import itertools

n=list(map(int,input().split()))


perms = list(itertools.permutations(n))
for p in perms:
    print(list(p))