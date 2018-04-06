import statistics as stat
print("Enter student name and their corresponding marks in three subjects")
studentNameList = []
sub1List = []
sub2List = []
sub3List = []
for i in range(10):
    print("\nEnter Student %d Details"%(i+1))
    studentNameList.append(str(input("Enter student name: ")))
    sub1List.append(int(input("Enter subject 1 marks: ")))
    sub2List.append(int(input("Enter subject 2 marks: ")))
    sub3List.append(int(input("Enter subject 3 marks: ")))

print("\nStudent Details Registered as follows:-")
print("\nStudent Name \t Subject 1 \t Subject 2 \t Subject 3")
for i in range(10):
    print("%s \t\t\t %d \t\t\t %d \t\t\t %d"%(str(studentNameList[i]),int(sub1List[i]),int(sub2List[i]),int(sub3List[i])))

print("Median for Subject 1:",stat.median(sub1List))
print("Mean for Subject 1:",stat.mean(sub1List))

print("\nMedian for Subject 2:",stat.median(sub2List))
print("Mean for Subject 2:",stat.mean(sub2List))

print("\nMedian for Subject 3:",stat.median(sub3List))
print("Mean for Subject 3:",stat.mean(sub3List))

# Getting Grade Function
def getGrades(x):
    if(x>90):
        return "A+"
    elif(x>80):
        return "A"
    elif(x>70):
        return "B+"
    elif x>60:
        return "B"
    elif x>50:
        return "C"
    elif x<50:
        return "D"
    else:
        return "NotValid"

print("\nPrinting Student List along with their grades")
for i in range(10):
    print("\nStudent Name:",studentNameList[i])
    print("Subject 1:", getGrades(sub1List[i]))
    print("Subject 2:", getGrades(sub2List[i]))
    print("Subject 3:", getGrades(sub3List[i]))







