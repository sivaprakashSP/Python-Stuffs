n= int(input())
l=[]
l1=[]
i=1
while i<=n:
    l.append(i)
    i=i+1
for i in range(len(l)):
    print(l[i],end="")
    if l[i]!=n:
        print(" + ",end="")
    else:
        break
print()
l.remove(l[-1])
for i in range(len(l)):
    l1.append(l[i])
print(l1)

"""
def pyramid( n ): 
      
    # outer loop to handle number 
    # of rows n in this case 
    for i in range(n, 0, -1): 
          
        # inner loop to create right triangle 
        # gaps on left side of pyramid 
        for gap in range(n-1, i-1, -1): 
            print(" ", end = '') 
            print(" ", end = '') 
          
        # initializing value corresponding 
        # to 'A' ASCII value 
        num = ord('A') 
          
        # loop to print characters on 
        # left side of pyramid 
        for j in range(1, i+1): 
            print(chr(num), end = ' ') 
            num += 1
              
        # loop to print characters on 
        # right side of pyramid 
        for j in range(i - 1, -1, -1): 
            num -= 1
            print(chr(num), end = ' ')
        print("\n", end = '') 
n=int(input())
pyramid(n)
"""