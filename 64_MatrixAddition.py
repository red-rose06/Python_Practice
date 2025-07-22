'''Program to add two matrices'''

A = []
B = []
C = []
r = []

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("Enter details of matrix A: ")
for i in range(0,rows):
    r=[]
    for j in range(0,columns):
        r.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
    A.append(r)

print("Enter details of matrix B: ")
for i in range(0,rows):
    r=[]
    for j in range(0,columns):
        r.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
    B.append(r)

print(f"Entered matrix A is: {A}")
print(f"Entered matrix B is: {B}")

for i in range(0,rows):
    r=[]
    for j in range(0,columns):
        r.append(A[i][j]+B[i][j])
    C.append(r)
print(f"Sum of Matrix A and Matrix B is: {C}")