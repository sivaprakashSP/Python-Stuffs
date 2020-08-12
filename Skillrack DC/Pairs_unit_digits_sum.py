from itertools import combinations as com
N=input().strip()
unitdigit=int(N[-1])
otherdigits=[int(digit) for digit in N[:-1]]
pair_count=0
checklist=[]
f=0
for pair in com(otherdigits,2):
    if sum(pair)==unitdigit and pair not in checklist:
        pair_count+=1
        checklist.append(pair)
        checklist.append(pair[::-1])
        f=1
if f==1:
    print(pair_count)
if f==0:
    print("-1") 