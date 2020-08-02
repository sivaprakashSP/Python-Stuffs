s=input()
alphalis=[]
digitslis=[]
sum=0
for i in range(len(s)):
    if s[i].isalpha():
        alphalis.append(s[i])
for i in range(len(s)):
    if s[i].isdigit():
        digitslis.append(int(s[i]))
for i in range(len(digitslis)):
    sum+=digitslis[i]
for i in range(len(alphalis)):
    print(alphalis[i],end="")
print(sum)