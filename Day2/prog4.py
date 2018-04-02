#Write a program which will accept two inputs matrices A and B.
#Multiply  A&B and print the output.
print("Enter no. of rows for matrix A")
k = int(input())
print("Enter no. of columns for matrix A")
l = int(input())
print("Enter no. of rows for matrix B")
m = int(input())
print("Enter no. of columns for Matrix B")
n =int(input())
matrixA = [[0 for x in range(k)] for y in range(l)]
matrixB = [[0 for x in range(m)] for y in range(n)]
result = [[0 for x in range(k)] for y in range(n)]
k=0
z=0
resultant=0
print(matrixA)
if not (l==m):
    print("Not possible to multiply matrices")
    exit()
else:
    print("Enter the values for matrix A")
    for x in range(k):
        for y in range(l):
            matrixA[x][y]=int(input())
    for x in range(m):
        for y in range(n):
            print(x,y)
            matrixB[x][y]=int(input())
    for i in range(k):
        for j in range(l):
            if(k<n):
                resultant += matrixA[j][i]*matrixB[i][k]
                k += 1
        result[i][z]=resultant
        k = 0
        z += 1
print(resultant)
