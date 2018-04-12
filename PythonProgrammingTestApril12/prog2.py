import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_dataset = pd.read_excel(r"C:\Users\user\Python Programs\April12PythonTest\prog2.xlsx")
print("\nPrinting the data from the file")
print(student_dataset)

print("\nPrinting students in the order of their height")
student_sorted_by_height = student_dataset.sort_values('height (meters)')
print(student_sorted_by_height)


bmi = student_dataset["weight(kgs)"]/(student_dataset["height (meters)"]**2)
student_dataset["BMI"]=bmi
print("\nPrinting Students data along with their BMI")
print(student_dataset)

print("\n\nPrinting Data Count after grouping")
print(student_dataset.groupby("BMI").count())

print("\nPrinting Student with BMI 18.5 to 25 Healthy")
print(student_dataset.loc[(student_dataset['BMI'] >=18.5) & (student_dataset['BMI'] <=25)])

print("\nPrinting Student with BMI 25 to 30 Overweight")
if((student_dataset.loc[(student_dataset['BMI'] >25) & (student_dataset['BMI'] <=30)])).empty:
    print("No Student")
else:
    print((student_dataset.loc[(student_dataset['BMI'] >25) & (student_dataset['BMI'] <=30)]))
    
    


print("\nPrinting Student with BMI over 30 Obese")
if student_dataset.loc[student_dataset['BMI'] >30].empty :
    print("No Student")
else:
    print(student_dataset.loc[student_dataset['BMI'] >30])

