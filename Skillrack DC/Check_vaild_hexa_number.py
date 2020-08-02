s=input().strip()
a="abcdefABCDEF"
f=0
for i in s:
    if i.isdigit() or i in a:
        pass
    else:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")