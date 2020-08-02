s=input().strip()
lis=[]
for i in range(len(s)):
    lis.append(s[i])
lis2=[]
for i in lis:
    lis2.append(lis.count(i))
print(max(lis2))
