#Using sklearn (scikit) gaussian Nb
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

spam_dataset = pd.read_csv(r"C:\Users\user\Python Programs\April16\spambase.data.csv")

x = spam_dataset.iloc[:,0:48]
y = spam_dataset.iloc[:,-1]
"""
x = spam_dataset.drop("SpamClassify",axis=1)
y = spam_dataset["SpamClassify"]
"""
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
gnb = GaussianNB()
gnb.fit(x_train,y_train)
print(gnb.score(x_test,y_test))

