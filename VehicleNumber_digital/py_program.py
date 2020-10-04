from itertools import permutations

no_of_district=int(input())
alpha_start,alpha_end=map(str,input().split())
digit_start,digit_end=map(int,input().split())

num_lis=[]
for i in range(no_of_district):
    num_lis.append('0'+str(i+1))
print(num_lis)

'''
for i in range(len(num_lis)):
    print("ST",end=" ")
    print(num_lis[i])
'''

alpha_lis=[]
for i in range(ord(alpha_start),ord(alpha_end)+1):
    alpha_lis.append(chr(i))
print(alpha_lis)

perm=permutations(alpha_lis,2)

combo_lis=[]
for i in list(perm):
    combo_lis.append(i)
for i in range(len(combo_lis)):
    print(combo_lis[i],end="\n")