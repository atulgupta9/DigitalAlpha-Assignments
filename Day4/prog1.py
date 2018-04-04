#1.consider the matrix A with the values,
	# a = ([['Rhia',10,20,30,40,50],
 #           ['Alan',75,80,75,85,100],
 #           ['Smith',80,80,80,90,95]])
 # perform the following operations and print the resulting matrix.
	# 1. slice the matrix and the output will be
 # 	 	[['Rhia',10],
 #  		['Alan',75],
 #  		['Smith',80]]
	# 2. update third row as ['Sam',82,79,88,97,99]
	# 3. replace the 4th element of first row as 95
	# 4. add a new column in this matrix with the following values, 73, 80 and 85.

a = [['Rhia',10,20,30,40,50],['Alan',75,80,75,85,100],['Smith',80,80,80,90,95]]
slicedMatrix = [a[i][0:2] for i in range(0,3)]

print("\nMatrix after slicing")
print(slicedMatrix)

print("\nUpdating the third row")
newRow = ['Sam',82,79,88,97,99]
for i in range(len(newRow)):
    a[2][i]=newRow[i]
print(a)

print("\nReplacing the 4th element of first row as 95")
a[0][3]=95
print(a)

print("\nAdding a new column in the matrix")
a[0].append(73)
a[1].append(80)
a[2].append(85)
print(a)
