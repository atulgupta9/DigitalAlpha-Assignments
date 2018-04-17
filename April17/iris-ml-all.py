#=======================LINEAR REGRESSION================================#
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

iris_dataset = datasets.load_iris()
x= pd.DataFrame(iris_dataset.data)
y = pd.DataFrame(iris_dataset.target)
x.columns = iris_dataset.feature_names

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
linear_regression = LinearRegression()
linear_regression.fit(x_train,y_train)
print("Label = %f %s + %f %s + %f %s + %f %s + %f"%(linear_regression.coef_[0][0],x.columns[0],linear_regression.coef_[0][1],x.columns[1],linear_regression.coef_[0][2],x.columns[2],linear_regression.coef_[0][3],x.columns[3],linear_regression.intercept_[0]))

print("Accuracy of Linear Regression",linear_regression.score(x_test,y_test))

y_predict = linear_regression.predict(x_test)

print("Original \tvs\tPrediction")
for i in range(len(y_test)):
    print("%f \tvs\t%f"%(np.array(y_test)[i],y_predict[i]))
    
    
#=======================LOGISTIC REGRESSION================================#

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

iris_dataset = datasets.load_iris()

x = pd.DataFrame(iris_dataset.data)
y = pd.DataFrame(iris_dataset.target)
x.columns = iris_dataset.feature_names


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
logistic_regression = LogisticRegression()
logistic_regression.fit(x_train,y_train)

print("Accuracy of Logistic Regression",logistic_regression.score(x_test,y_test))

y_predict = logistic_regression.predict(x_test)

print("Original \tvs\tPrediction")
for i in range(len(y_test)):
    print("%f \tvs\t%f"%(np.array(y_test)[i],y_predict[i]))


#=======================SVM (Support Vector Machine)================================#  

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

iris_dataset = datasets.load_iris()
x = pd.DataFrame(iris_dataset.data)
y = pd.DataFrame(iris_dataset.target)

x.columns = iris_dataset.feature_names

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.35)
svm = SVC()
svm.fit(x_train,y_train)

print("Accuracy of SVM ",svm.score(x_test,y_test))

y_predict = svm.predict(x_test)

print("Original \tvs\tPrediction")
for i in range(len(y_test)):
    print("%f \tvs\t%f"%(np.array(y_test)[i],y_predict[i]))

