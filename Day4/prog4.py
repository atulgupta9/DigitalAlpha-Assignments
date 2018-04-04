# 4. Write a program to print the prime numbers in the interval 900-1000, and also find if any palindrome is in the result.
import math
def prime(x):
    flag= True
    for i in range(1,int(math.sqrt(x))):
        if(i!=1 and x%i==0):
            flag=False
            return
    return flag
def palindrome(x):
    number=0
    while x>0:
        digit=x%10
        number*=10
        number=number+digit
        x=x/10
print("Prime Numbers are:")
for i in range(900,1000):
    if(prime(i)):
        print(i)
        if(palindrome(i)==i):
            print("Also a palindrome")



