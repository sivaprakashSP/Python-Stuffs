num=input()
lis=[]
sum=0
for i in range(len(num)):
    lis.append(num[i])
for i in range(len(lis)):
    sum+=int(lis[i])
print(sum)