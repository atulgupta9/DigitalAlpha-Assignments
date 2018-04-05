# 4. Write a program that accepts a sentence(with letters and digits) and calculate the number of letters and digits
print("Enter a sentence")
sentence = str(input())
countLetters=0
countDigits=0
for i in sentence:
    if i.isalpha():
        countLetters+=1
    elif i.isnumeric():
        countDigits+=1
print("Number of Letters are:",countLetters)
print("Number of Digits are:",countDigits)