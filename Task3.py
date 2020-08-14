from itertools import permutations as p
n=input()
permutate=p(n,len(n))
permlist=list(permutate)
for i in permlist:
    print("".join(i))
