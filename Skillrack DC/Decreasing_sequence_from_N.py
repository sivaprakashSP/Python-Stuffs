n=[int(x) for x in input().split()]
k=n[1]
f=0
while(n[0]>0):
    n[0] = n[0] - k
    if n[0] > 0:
        print(n[0],end=" ")
