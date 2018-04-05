# 1. Write a python program to generate and print the armstrong numbers within the interval 1-1000.
print("Printing the Armstrong numbers between 1 to 1000")
for i in range(1,1001):
    number = list(str(i))
    sum=0
    for j in number:
        sum = sum + int(j)**len(number)
    if sum == int(i):
        print(sum)

