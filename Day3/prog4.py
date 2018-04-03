#4.	Write a binary search function to search an item in a sorted list.
def binarySearchFunction(dataList,l,u,element):
    mid = (l+u)//2
    if(l<u):
        if (dataList[mid] == element):
            print("Element is found at ",mid+1," position")
        elif(dataList[mid]<element):
            binarySearchFunction(dataList,mid+1,u,element)
        elif(dataList[mid]>element):
            binarySearchFunction(dataList,l,mid-1,element)
    else:
        print("Element not found")

print("Enter no. of data you want to store")
n = int(input())
inputDataList = []
print("Enter Data")
for i in range(n):
    inputDataList.append(int(input()))
print("Enter the element you want to search")
toSearchForElement = int(input())
inputDataList.sort()
binarySearchFunction(inputDataList,0,n-1,toSearchForElement)