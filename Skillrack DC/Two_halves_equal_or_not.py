"""
s = input()
m=len(s)
t = int(m/2)
f=0
temp = s.replace(s[t],'')
t = temp
first_half = t[0:len(t)//2]
second_half = t[len(t)//2 if len(t)%2 == 0 else ((len(t)//2)+1):]
print(first_half)
print(second_half)
if first_half == second_half:
    print("yes")
else:
    print("no")
"""

