'''
def find_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
lis=[int(x) for x in input().split()]
m=lis[0]
n=lis[1]
lis2=[]
for i in range(m):
    lis2.append(int(input()))
print(lis2)
x=lis2[0]
y=lis2[1]
gcd=find_gcd(x,y)
for i in range(2,len(lis2)):
    gcd=find_gcd(gcd,lis2[i])
print(gcd)
lis2=[]
lis3=[]
for i in range(m):
    lis2.append(int(input()))
print(lis2)
for i in range(n):
    x=int(input())
    y=int(input())
    lis3.append(x)
    lis3.append(y)
print(lis3)
for i in range(len(lis3)-1):
    for i in range(lis3[i],lis3[i+1]):
        print(lis2[lis3[i]])
        while(lis2[lis3[i+1]]):
            lis2[lis3[i]],lis2[lis3[i+1]]=lis2[lis3[i+1]],lis2[lis3[i]]%lis2[lis3[i+1]]
        print(lis2[lis3[i]])
'''
'''
import math
lis=[int(x) for x in input().split()]
m=lis[0]
n=lis[1]
lis1=[]
for i in range(1,m+1):
    lis1.append(int(input()))
lis2=[]
for i in range(n):
    x,y=int(input()),int(input())
    for i in range(x-1,y-1):
        
        print(math.gcd(lis1[i],lis1[i+1]),end=" ")
    print()
'''
'''
    lis2.append(x)
    lis2.append(y)
'''
'''
print(lis2)
for i in range(len(lis1)):
    print(lis1[i],end=" ")
'''
import math as m
def gcd(l):
    a=0
    for i in range(len(l)):
        a=m.gcd(a,l[i])
    return a
a,b=[int(a) for a in input().split()]
x=[int(x) for x in input().split()]
for i in range(b):
    c,d=[int(c) for c in input().split()]
    print(gcd(x[c-1:d]))

import math
a="banana"
print(a)
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