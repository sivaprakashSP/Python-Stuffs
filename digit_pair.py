n=int(input())
lis=list(map(int,input().split()))
r=list()
for i in lis:
    t=(int(max(str(i)))*11) + (int(min(str(i)))*7)
    if len(str(t))==3:
        r.append(int(str(t)[1:]))
    else:
        r.append(t)
o=[str(r[i])[0] for i in range(n) if i%2==0]
e=[str(r[i])[0] for i in range(n) if i%2!=0]
count=0
for i in range(0,10):
    temp_even=0
    temp_odd=0
    if o.count(i)>1:
        temp_odd=o.count(str(i))
    if e.count(i)>1:
        temp_even=e.count(str(i))
    if temp_even+temp_even>4:
        count+=2
    elif temp_even+temp_odd>1 and temp_even+temp_odd<4:
        count+=(temp_odd+temp_even)-1
print(count)