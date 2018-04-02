def fibonacci(n):
    firstElement=0
    secondElement=1
    print(firstElement)
    print(secondElement)
    i=2;
    while i < n:
        thirdElement=firstElement+secondElement
        print(thirdElement)
        firstElement=secondElement
        secondElement=thirdElement
        i+=1
print("Enter the no of terms you want")
n= int(input())
fibonacci(n)
