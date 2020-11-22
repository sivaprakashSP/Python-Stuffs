n=input()
hyphen='-'
lis1=[]
lis2=[]
for i in range(len(n)):
    if n[i] in hyphen:
        lis1.append(n[i])
    else:
        lis2.append(n[i])
for i in range(len(lis1)):    
    print(lis1[i],end='')
for i in range(len(lis2)):
    print(lis2[i],end='')