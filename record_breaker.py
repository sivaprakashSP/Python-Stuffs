test_case=int(input())
while(test_case>0):
    lis2=[]
    lis3=[]
    c=0
    n=int(input())
    lis=[int(x) for x in input().split()]
    for i in range(len(lis)):
        lis2.append(lis[i])
    test_case-=1
    for i in range(0,len(lis2)):
        for j in range(i+1,len(lis2)):
            if lis2[j]>lis2[i] and lis2[j]>lis2[j-1]:
                lis3.append(lis2[j])
                break
    final_list = list(set(lis3))
    for i in range(len(final_list)):
        c+=1
    print()
    print(c)


n=int(input())
lis4=[int(x) for x in input().split()]
max=lis4[0]
for i in range(len(lis4)):
    if lis4[i]>max:
        max=lis4[i]
print(max)