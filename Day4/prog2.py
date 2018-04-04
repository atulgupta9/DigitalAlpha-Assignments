# 2. Consider the following sentence,
#
# #Python is an interpreted high level programming language for general-purpose programming*.
#
# i) remove all special characters from this.
# ii) Print all   palindromes in the sentence
# iii) print the repeating words and  number of times it repeats
import re
string ="#Python is an interpreted high level programming language for general-purpose programming*."
cleanedString=re.sub("[^A-Za-z0-9 -]","",string)
print("String after removing all special characters")
print(cleanedString)
print("Printing all palindromes from the sentence")
wordList = cleanedString.split(" ")
for i in range(len(wordList)):
    if(str(wordList[i])== str(wordList[i][::-1])):
        print(str(wordList[i]))
repeatingWords = {}
for i in range(len(wordList)):
    if(repeatingWords.get(wordList[i])):
        repeatingWords[wordList[i]]+=1
    else:
        repeatingWords[wordList[i]] = 1
print("Repeating words are:-")
print("Word \t Frequency")
for key,value in repeatingWords.items():
    if value>1 :
        print("%s \t %d"%(key,value))



