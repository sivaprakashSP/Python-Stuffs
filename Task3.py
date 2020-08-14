from itertools import permutations as p
n=int(input())
permutate=p(n,len(str(n)))
permlist=list(permutate)
for i in range(len(permlist)):
    print(permlist[i],end="\n")
