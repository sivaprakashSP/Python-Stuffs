n=int(input())
l=[int(l) for l in input().split()]
k=int(input())
if n==k:
    print(*l)
else:
    l1=l[k-1::-1]+l[-(n-k):]
    l2=l1[:n-k]+l1[:-k-1:-1]
    print(*l2)