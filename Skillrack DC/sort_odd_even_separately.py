n=int(input())
lis=[int(x) for x in input().split()]
lis1=set(lis)
#print(lis1)
l=[]
even=[]
odd=[]
for i in range(len(lis)):
    if lis[i]%2==0:
        even.append(lis[i])
    elif lis[i]%2==1:
        odd.append(lis[i])
odd.sort()
even.sort()
#print(odd)
#print(even)
a=0
b=0
l=[]
for i in range(len(lis)):
    if lis[i]%2==1:
        l.append(odd[a])
        a+=1
    else:
        l.append(even[b])
        b+=1
for i in range(len(l)):
    print(l[i],end=" ")