def getEvenCount(numList):
    count=0
    for val in numList:
        if val%2==0:
            count+=1
    return count
R,C=map(int,input().split())
matrix=[list(map(int,input().split())) for row in range(R)]
matrix=sorted(matrix,key=getEvenCount)
for row in matrix:
    print(*row)