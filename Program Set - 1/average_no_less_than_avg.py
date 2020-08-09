lis=[int(x) for x in input().split()]
no_sum=sum(lis)
avg=no_sum//len(lis)
for i in range(len(lis)):
    if lis[i]>avg:
        print(lis[i],end=" ")