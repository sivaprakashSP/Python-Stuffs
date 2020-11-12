def smallestdigitproduct(n):
    if n<10:
        print(10)
        return
    dig = []
    for i in range(9,1,-1):
        while n%i == 0:
            n=n/i
            dig.append(i)
    if n>10:
        print("Not Possible")
        return
    n=dig[len(dig)-1]
    for i in range(len(dig)-2,-1,-1):
        n=10*n+dig[i]
    print(n)

n=int(input())
smallestdigitproduct(n)