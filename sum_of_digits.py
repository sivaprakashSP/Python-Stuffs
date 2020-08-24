def sum_of_digit( n ):
    if n == 0: 
        return 0
    return (n % 10 + sum_of_digit(int(n / 10))) 
result_sum=int(input())
lis=[]
for i in range(1,999+1):
    result=sum_of_digit(i)
    if len(str(result))==1:
        if result_sum==result:
            #print(i,end="\n")
            lis.append(i)
    elif len(str(result))==2:
        res=sum_of_digit(result)
        if result_sum==res:
            #print(i,end="\t") 
            lis.append(i)
for i in range(len(lis)):
    print(lis[i],end=" ")