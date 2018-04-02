#Write a program that accepts a comma separated sequence of words as input.
# SOrt and print them in alphabetical order
print("Enter a comma separated sequence of words")
commaSeparatedString = str(input())
words=commaSeparatedString.split(',')
words.sort()
print("Printing words in alphabetical order")
for word in words:
    print(word)