n=int(input())
lis=[int(x) for x in input().split()]
for i in range(len(lis)):
    if n==lis[i]:
        print(i+1,end="")