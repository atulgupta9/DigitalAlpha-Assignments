# 3. Write a python program to generate a dictionary of n length and that contains (i, i*i)
user_dictionary ={}
print("Enter the length of the dictionary")
n = int(input())
for i in range(n):
    user_dictionary[i] = i*i
print(user_dictionary)