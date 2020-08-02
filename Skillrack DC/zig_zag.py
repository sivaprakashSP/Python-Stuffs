"""
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix
print("Printing the elements in matrix format");
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 
    """

r,c = [int(x) for x in input().split()]
l=[]
for i in range(r):
    a=[int(a) for a in input().split()]
    l.append(a)
print(l)
