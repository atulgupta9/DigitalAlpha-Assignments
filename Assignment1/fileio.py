import sys, csv, operator
file = open("city_test.csv","w")
print("Enter the no. of data you want to enter")
n = int(input())
for i  in range(n):
    print("Enter city Name")
    file.write(str(input()))
    file.write(",")
    print("Enter Population")
    file.write(str(input()))
    file.write(",")
    print("Enter area")
    file.write(str(input()))
    file.write("\n")
file.close()

li = []
file = open("city_test.csv","r")
for i in range(n):
    li.append(str(file.readline().replace(","," ")))
li.sort()
file.close();
file = open("city_test.csv","w")
newlist = []
for i in range(n):
    newlist = li[i].split(" ")
    for i in range(3):
        file.write(newlist[i])
        if i < 2:
            file.write(",")

file.close()
