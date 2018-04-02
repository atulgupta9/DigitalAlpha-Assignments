#Write a program to check password validity.
# Password should satisfy the conditions below
# Minimum of 8 characters
# Atleast one capital letter
# Atleast one number
# Atleast one special character
# Maximum 14 characters
import re
print("Enter the password you want to use")
pwd= str(input())
valid= True
while valid:
    if(len(pwd)<8 or len(pwd) >14 ):
        break
    elif not re.search("[A-Z]",pwd):
        break
    elif not re.search("[0-9]",pwd):
        break
    elif not re.search("[^A-Za-z0-9]",pwd):
        break
    else:
        print("Its a valid Password")
        valid= False
if (valid):
    print("Its not a valid password")





