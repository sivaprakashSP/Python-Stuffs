n=int(input())
p=0
p+=n
rev=0
m=bin(n)
l=[]
l1=[]
l2=[]
for i in range(len(str(m))):
    l.append(m[i])
l1.append(l[2:])
l2.append(l[2:])
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
print(l1[0])
print(l2[0][::-1])
if p==rev and l1[0]==l2[0][::-1]:
    print("yes")
else:
    print("no")