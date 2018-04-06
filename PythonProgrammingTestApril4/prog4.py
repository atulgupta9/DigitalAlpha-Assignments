print("Enter details of the family members")
memberName = []
memberAge = []
childrenGroup=[]
youthGroup = []
middleAge = []
seniorGroup = []
for i in range(20):
    print("Enter Name:")
    memberName.append(str(input()))
    print("Enter age:")
    memberAge.append(int(input()))
    print("\n")
    if(memberAge[i]>80):
        seniorGroup.append(str(memberName[i]))
    elif (memberAge[i]>45):
        middleAge.append(str(memberName[i]))
    elif (memberAge[i]>20):
        youthGroup.append(str(memberName[i]))
    else:
        childrenGroup.append(str(memberName[i]))
print("Family Members belonging to senior group")
for i in range(len(seniorGroup)):
    print(seniorGroup[i],end=", ")

print("\nFamily Members belonging to middle age group")
for i in range(len(middleAge)):
    print(middleAge[i],end=", ")

print("\nFamily Members who are still youth")
for i in range(len(youthGroup)):
    print(youthGroup[i],end=", ")
print("\nChildren in the family")
for i in range(len(childrenGroup)):
    print(childrenGroup[i],end=", ")






