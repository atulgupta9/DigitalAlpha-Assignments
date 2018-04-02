#Write a program to accept the height and weight of students in a class. Use Tuples
# to store them and print their BMI on screen
height =[]
weight= []
print("Enter the number of students")
n=int(input())
print("Enter their height and weight")
for x in range(n):
    print("Enter height:")
    height.append(int(input()))
    print("Enter weight:")
    weight.append(int(input()))
heightTuples = tuple(height)
weightTuples = tuple(weight)
print("BMI of the respective students is as follows")
for x in range(n):
    print("BMI of the student is :"+str(weightTuples[x]/pow(heightTuples[x],2)))
