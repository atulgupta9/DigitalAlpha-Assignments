
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = datasets.load_iris()
iris_dataset = pd.DataFrame(data["data"])
iris_dataset.columns = data["feature_names"]
iris_dataset["label"] = data["target"]
print(iris_dataset)


# In[2]:


print("Correlation Matrix:\n",iris_dataset.corr())


# In[3]:


sns.heatmap(iris_dataset.corr())


# In[4]:


x = iris_dataset[data["feature_names"]]
y = iris_dataset["label"]
plt.figure()
plt.scatter(x["sepal length (cm)"],x["sepal width (cm)"],c=y)
plt.title("Clusters based on sepal length and width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.colorbar()
plt.show()


# In[5]:


plt.figure()
plt.scatter(x["petal length (cm)"],x["petal width (cm)"],c=y)
plt.title("Clusters based on Petal length and width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.colorbar()
plt.show()


# In[14]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
clf = svm.SVC()
clf.fit(x_train,y_train)
print("Prediction:",clf.predict(x_test))
print("Score: ",clf.score(x_test,y_test))

