s1=input()
s2=input()
lis1=[]
lis2=[]
for i in range(len(s1)):
    lis1.append(s1[i])
for i in range(len(s2)):
    lis2.append(s2[i])
for x in lis1:
    if lis1.count(x)>1:
        lis1.remove(x)
for y in lis2:
    if lis2.count(y)>1:
        lis2.remove(y)
lis1.sort()
lis2.sort()
print(set(lis1))
print(set(lis2))
if set(lis1)==set(lis2):
    print("yes")
else:
    print("no")