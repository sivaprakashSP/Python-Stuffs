s1=input()
s2=input()
lis1=[]
lis2=[]
for i in range(len(s1)):
    lis1.append(s1[i])
for i in range(len(s2)):
    lis2.append(s2[i])
l1=len(s1)-1
l2=len(s2)-1
print(l1,l2)
if l2<l1:
    lis1.remove(lis1[l1])
    print(lis1,end=" ")
    print(lis2)
elif l1<l2:
    lis2.remove(lis1[l2])
    print(lis1,end=" ")
    print(lis2)
