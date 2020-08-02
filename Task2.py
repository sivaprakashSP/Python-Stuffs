import math
import itertools as i
a=input()
n=int(input())
permlist=i.permutations(a)
unique=set(permlist)
l=list(unique)
l.sort()
for i in range(len(l)):
    if(i==n-1):
        print(l[i]) 
'''
for perm in permlist:
    c+=1
    print(c,''.join(perm))
'''
'''
l=[]
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            c+=1
    l.append(c)
print(l)
if len(set(a))!=len(a):
    for i in range(len(a)):
        g=1
        for j in set(a[i:]):
            if a[i:].count(j)!=1:
                g*=math.factorial(a[i:].count(j))
        l[i]=l[i]/g
print(l)
k=0
for i in range(len(a)-1,-1,-1):
    l[i]*=math.factorial(k)
    k+=1
print(l)
print(int(sum(l)+1))
'''