n=int(input())
lis=[]
china_count=0
usa_count=0
india_count=0
canada_count=0
japan_count=0
lis2=[]
for i in range(n):
    lis.append(input().split())
for i in range(len(lis)):
    if 'China' in lis[i]:
        china_count+=1
    elif 'USA' in lis[i]:
        usa_count+=1
    elif 'India' in lis[i]:
        india_count+=1
    elif 'Canada' in lis[i]:
        canada_count+=1
    elif 'Japan' in lis[i]:
        japan_count+=1
print(china_count)
print(usa_count)
print(india_count)
print(canada_count)
print(japan_count)