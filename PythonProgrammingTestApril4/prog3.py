def sortAndPrint(numList,x):
    numList.sort()
    flag = False
    for i in range(len(numList)):
        if (numList[i] == x):
            flag = True
            return ("Number found at position "+str(i + 1))
            break
    if flag == False:
        return ("Number not found")


x = [12,6,48,37,88,31,54,11,60,122,105,88,122,155,105]
print("Enter the number to search from the list ",x)

n = int(input())
x.sort()
flag=False
for i in range(len(x)):
    if(x[i]==n):
        flag=True
        print("Number found at position ",i+1)
        break
if flag == False:
    print("Element not found")

print("Try entering your own list")
print("How many numbers will you like to enter?")
numberList = []
n = int(input())
print("Please enter the numbers")
for i in range(n):
    numberList.append(int(input()))
print("Enter the number you will like to find")
print(sortAndPrint(numberList,int(input())))



