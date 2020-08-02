a=input().split('_')
if len(a)>1:
  print(a[0],end='_')
  for x in range(1,len(a)-1):
    print(*(list(reversed(a[x]))),sep='',end='_')
  print(a[-1])
else:
  print(a[0])