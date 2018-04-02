#1.	Write a program that accepts a sentence and calculate the number
# of letters, digits, uppercase letters, lower case
# letters and special characters.
print("Enter the sentence")
sentence = str(input())
cletters=0
cupper=0
clower=0
cnum=0
cspecial=0
for x in sentence:
    if x.isalpha():
        cletters+=1
        if(x.isupper()):
            cupper+=1
        else:
            clower+=1
    elif x.isnumeric():
        cnum+=1
    elif not x.isspace():
        cspecial+=1

print("The number of letters is %d , upper case letters is %d lower case letters is %d , numeric characters  are %d , special characters are %d "%(cletters,cupper,clower,cnum,cspecial))
