#declaration of variables and assigning values to it
n=int(input())
s=input()
a=[0 for i in range(n)]
flag=0
a_votes=0
b_votes=0

#b_votes count validation
for i in range(n):
    if s[i]=="B":
        c=0
        flag=1
        b_votes+=1
    if s[i]=="A":
        flag=0
    if s[i]=="-" and flag:
        a[i]=c+1
        c+=1
    else:
        a[i]=0

#declaration of flag & c variables and b as a list
c=0
flag=0
b=[0 for i in range(n)]

for i in range(n-1,-1,-1):
    if s[i]=="A":
        c=0
        flag=1
        a_votes+=1
    if s[i]=="B":
        flag=0
    if s[i]=="-" and flag:
        b[i]=c+1
        c+=1
    else:
        b[i]=0

#Checking for least number of votes nominated
    if a[i]<b[i]:
        a_votes+=1
    elif b[i]<a[i]:
        b_votes+=1

#Final condition to end the election
if a_votes==b_votes:
    print("Coalition government")
else:
    print("A" if a_votes>b_votes else "B")