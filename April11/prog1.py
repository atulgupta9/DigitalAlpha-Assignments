"""
1.	Given employee dataset and predict the salary by performing linear regression 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
df = pd.read_csv(r"D:\digital Alpha\April11\prog1.csv")
print("Correlation Matrix")
print(df.corr())

plt.figure(1)
plt.scatter(df["Certification"],df["Salary"])
plt.title("Certification vs Salary")
plt.xlabel("Certification")
plt.ylabel("Salary")

plt.figure(2)
plt.scatter(df["Experience in years"],df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience in years")
plt.ylabel("Salary")

X= df[["Certification","Experience in years"]]
Y= df["Salary"]

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)
linear = LinearRegression()
linear.fit(x_train,y_train)
print("\nSalary = %f Certification + %f Experience in Years + %f"%(linear.coef_[0],linear.coef_[1],linear.intercept_))

print("\nSalary predicted for the given conditions are as follows:")
salary_predicted = linear.predict(x_test)
certi_list=x_test["Certification"].values.tolist()
exp_list =x_test["Experience in years"].values.tolist()
print("\nCertifications \t Experience in years \t Salary")
for i in range(len(x_test)):
    print("%d \t\t\t %f \t\t %f"%(certi_list[i],exp_list[i],salary_predicted[i]))



