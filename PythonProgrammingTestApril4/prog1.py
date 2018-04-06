import re
print("Enter a paragraph(with at least 4 sentences)")
paragraph = str(input())

print("\nParagraph Entered :-")
print(paragraph)

paraList =[]
paraList = paragraph.split(".")

newPara=""
print("\nUpdating the middle sentence")
paraList[int(len(paraList)/2)] = "UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial Services, Telecom, Media & Technology, Insurance, Transportation & Logistics and Manufacturing & Utilities"
for i in range(len(paraList) -1):
    newPara +=paraList[i]
    newPara +="."
print(newPara)

countVowels = 0
countUpper = 0
countLower = 0
countSpecial = 0
countNum = 0

for ch in newPara:
    if ch.isalpha():
        if re.match("[AEIOUaeiou]",ch):
            countVowels += 1
        if ch.isupper():
            countUpper += 1
        elif ch.islower():
            countLower += 1
    elif ch.isnumeric():
        countNum += 1
    else:
        countSpecial+=1

wordDict = {}
wordList = []
wordList = newPara.split(" ")
for word in wordList:
    if wordDict.get(word):
        wordDict[word] += 1
    else:
        wordDict[word] = 1

print("\nNumber of Vowels: ",countVowels)
print("Number of Uppercases: ",countUpper)
print("Number of Lowercases: ",countLower)
print("Number of Special Characters: ",countSpecial)
print("\nRepeating Words and their frequency is as follows:-")
print("Word \t Frequency")
for key,value in wordDict.items():
    if(value > 1  and key!=" "):
        print("%s \t\t\t %d"%(key,value))

paraList = newPara.split(".")
tempPara = paraList[0]
paraList[0] = paraList[int(len(paraList))-2]
paraList[int(len(paraList))-2] = tempPara
newPara = ""
for i in range(int(len(paraList))-1):
    newPara += paraList[i]
    newPara +="."
print("\n New Paragraph after swapping first and last sentence")
print(newPara)