import math as m
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p <= m.sqrt(n)): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(1, n+1): 
        if prime[p]: 
            print(p,end=" ")
n=int(input())
SieveOfEratosthenes(n)