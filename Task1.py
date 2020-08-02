import math as m
import sympy as s

def SieveOfEratosthenes(n): 
    sum=0
    c=0
    lis1=[]
    lis2=[]
    lis3=[]
    prime = [True for i in range(n+1)] 
    p = 2
    while (p <= m.sqrt(n)): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n+1): 
        if prime[p]:
            lis1.append(p)
    #print(l)
    for i in range(len(lis1)-1):
        sum+=lis1[i]
        lis2.append(sum)
    #print(lis2)
    for i in range(len(lis2)):
        if(s.isprime(lis2[i])):
            lis3.append(lis2[i])
    for i in lis3:
        if i<=n and i>2:
            c+=1
            print(i,end=" ")
    print()
    print(c)
n=int(input())
SieveOfEratosthenes(n)