# 3. Given two sets A and B,
#    A = {5, 3, 8, 6, 1}
#    B = {1, 5, 3, 4, 2}
#       Perform the following operations and print the resulting set,
# 	i) union
# 	ii) intersection
# 	iii) set difference
# 	iv) find maximum and the minimum value of set A and B
A = {5, 3, 8, 6, 1}
B = {1, 5, 3, 4, 2}
print("Union : ",A|B)
print("Intersection :",A&B)
print("Difference :",A-B)
print("Maximum value",max(A|B))
print("Minimum value",min(A|B))