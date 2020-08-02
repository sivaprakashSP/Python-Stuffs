lis=[int(x) for x in input().split()]
max_no=max(lis)
lis2=list(set(lis))
lis3=[]
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]==lis[j]:
            lis3.append(lis[j])
missing_no=[x for x in range(1,lis2[-1]+1) if x not in lis2]
for i in range(len(lis3)):
    for j in range(len(missing_no)):
        print(lis3[i],missing_no[j])