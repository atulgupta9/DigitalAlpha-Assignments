# 2.Given matrix
# A = [[3, 5, 6]
#      [4, 8, 10]
#      [2, 1, 8]]
# and I = [[1, 0, 0]
#          [0, 1, 0]
#          [0, 0, 1]]
# Prove that, A = A.I
A = [[3, 5, 6],[4, 8, 10],[2, 1, 8]]
I = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
AI = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(I[0])):
        for k in range(len(I)):
            AI[i][j] += A[i][k] * I[k][j]

print("A =",A)
print("A.I =",AI)
print("Hence A=A.I")