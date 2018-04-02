# Generate a dictionary contains radius and area of the circle,
# radius ranging from 1 to n. Print the dictionary. Input is n.
print("Enter value of n")
n = int(input())
areaDictionary = {}
for x in range(1, n + 1):
    areaDictionary[x] = (22 / 7) * pow(x, 2)
print(areaDictionary)
print("Pretty Printing the area dictionary")
for num, area in areaDictionary.items():
    print("Radius is %d, Area is %f"%(num,area))
