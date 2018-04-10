"""
4.  Create a dictionary Exam_result  with name, score, no_of_attempts and qualify, perform the following,
a. create another dictionary label with inputs a, b, c, d, e…..etc and display a DataFrame from exam_result dictionary data which has the index labels.
		b. print the first 4 rows of the data frame
		c. print name and qualify from this data frame
		d. print number of score in between 20- 35 and also print the sum of attempts by       each students
"""
import pandas as pd
exam_result = { "name":["asd","bas","ccxz","def","eda"], "score":[20,30,25,38,47],"no_of_attempts":[4,1,2,3,1],"qualify":[False,False,False,False,True]}


label = {"inputs":["a","b","c","d","e"]}
exam_result_df = pd.DataFrame(exam_result,index=label["inputs"])

print("Values in label dictionary")
print("INPUTS=",end="")
for  key,value in label.items():
    print(value,end=" ")

print("\nPrinting from exam_result using INPUTS")
for value in label["inputs"]:
    print(exam_result_df.loc[value,:])
    print("\n")

print("\nPrinting name and qualify from the dataframe")
print(exam_result_df[["name","qualify"]])


print("\nNumber of score in between 20-35",len(exam_result_df.query("score >20  & score < 35")))

print("Attempts made by each student scoring b/w 20 -35\n",exam_result_df.query("score >20  & score < 35")[["name","no_of_attempts"]])