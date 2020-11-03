m,n=map(int,input().split())
lis1=[int(x) for x in input().split()]
lis2=[int(y) for y in input().split()]
count=0
for i in range(len(lis2)):
    if lis2[i] in lis1:
        count+=1
print(count)