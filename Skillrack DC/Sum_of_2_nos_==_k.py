#l=[int(x) for x in input().split()]
n,y=input().split()
people = [int(x) for x in input().split()]

def tessa(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

pairings = tessa(people)
lis1=[]
lis2=[]
sumlist=[]
f=0
i=1
for i in range(len(pairings)):
  x,y=pairings[i]
  lis1.append(x)
  lis2.append(y)
for (i,j) in zip(lis1,lis2):
  sumlist.append(i+j)
for i in range(len(sumlist)):
  if sumlist[i] == int(y):
    f=1
    break
if f==1:
  print("yes")
else:
  print("no")