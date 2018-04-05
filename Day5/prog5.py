# 5.Create a calculator to perform the following operations,
# i) find the factorial
# ii) find LCM
# iii) find HCM
# iv) factor of a number
def factorial(x):
    if(x!=0):
        return int(x)*int(factorial(int(x)-1))
    else:
        return 1
def LCM(a,b):
    if a >b :
        min1 = a
    else:
        min1=b
    while 1:
        if(min1%a==0 and min1%b==0):
            return min1
        min1+=1
def HCF(a,b):
    prod=1
    if(a>b):
        max1=a
    else:
        max1=b
    for i in range(1,max1+1):
        if(a%i==0 and b%i==0):
            prod*=i
    return prod

def factorize(n):
    factorList =[]
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            factorList.append(i)
    return factorList
print("Enter a number to get factorial")
print("Factorial is:",factorial(int(input())))

print("Enter two numbers to get their LCM")
print("LCM is:",LCM(int(input()),int(input())))

print("Enter two numbers to get their HCF")
print("HCF is:",HCF(int(input()),int(input())))

print("Enter a number to get its factors")
factorList = factorize(int(input()))
print("Factors are")
for i in factorList:
    print(i,end=" ")
