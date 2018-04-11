import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\\Users\\user\\Python Programs\\April11\\adult.data.csv")
df = df.replace(' ?',np.NaN)
df = df.replace(' <=50K',0)
df = df.replace(' >50K',1)
df = df.dropna()
df = df.drop(["education","fnlwgt"],axis=1)

Y = df["income"]
cat_X = [i for i in df.columns if i!="income"]
X = df[cat_X]

table = pd.crosstab(X["age"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income(0<=50K,1>50K)')



table1 = pd.crosstab(X["workclass"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Workclass vs Income')
plt.xlabel('Workclass')
plt.ylabel('Income(0<=50K,1>50K)')

table2 = pd.crosstab(X["education-num"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Education-Num vs Income')
plt.xlabel('Education-Num')
plt.ylabel('Income(0<=50K,1>50K)')

table3 = pd.crosstab(X["marital-status"],Y)
table3.div(table3.sum(1).astype(float),axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Marital Status vs Income')
plt.xlabel('Marital Status')
plt.ylabel('Income(0<=50K,1>50K)')

table4 = pd.crosstab(X["occupation"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Occupation vs Income')
plt.xlabel('Occupation')
plt.ylabel('Income(0<=50K,1>50K)')

table5 = pd.crosstab(X["relationship"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Occupation vs Income')
plt.xlabel('Occupation')
plt.ylabel('Income(0<=50K,1>50K)')

table5 = pd.crosstab(X["race"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Race vs Income')
plt.xlabel('Race')
plt.ylabel('Income(0<=50K,1>50K)')
print(df.groupby("race").count())
print("Data is biased with more data of white men than any other")


table6 = pd.crosstab(X["sex"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Sex vs Income')
plt.xlabel('Sex')
plt.ylabel('Income(0<=50K,1>50K)')
print(df.groupby("sex").count())
print("Data is biased with more data of males than any other")


table7 = pd.crosstab(X["capital-gain"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of capital-gain vs Income')
plt.xlabel('capital-gain')
plt.ylabel('Income(0<=50K,1>50K)')
print(df.groupby("capital-gain").count())
print("Data is biased with more data of capital-gain 0 than any other")


table8 = pd.crosstab(X["capital-loss"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of capital-loss vs Income')
plt.xlabel('capital-loss')
plt.ylabel('Income(0<=50K,1>50K)')
print(df.groupby("capital-loss").count())
print("Data is biased with more data of capital-loss 0 than any other")


table9 = pd.crosstab(X["hours-per-week"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of hours per week vs Income')
plt.xlabel('hours per week')
plt.ylabel('Income(0<=50K,1>50K)')


table10 = pd.crosstab(X["native-country"],Y).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of native Country vs Income')
plt.xlabel('Country')
plt.ylabel('Income(0<=50K,1>50K)')
print(df.groupby("native-country").count())

X = X.drop(["race","sex","capital-gain","capital-loss","native-country"],axis=1)

cat_vars = ['workclass','marital-status','occupation','relationship']
for i in cat_vars:
    cat_list = 'var'+'_'+i
    cat_list = pd.get_dummies(X[i],prefix=i)
    x1= X.join(cat_list)
    X=x1

to_keep = [i for i in X.columns if i not in cat_vars]
X_Final = X[to_keep]

# Packages for RFE and LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
logistic = LogisticRegression()
rfe = RFE(logistic,20)
rfe.fit(X_Final,Y)
print(rfe.support_)
print(rfe.ranking_)
selected_columns =[]
for i in range(len(rfe.support_)):
    if(rfe.support_[i] == True):
        selected_columns.append(to_keep[i])
 
X_Report = X_Final[selected_columns]       

from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq,df)
import statsmodels.api as sm
logit_model=sm.Logit(Y,X_Report)
result=logit_model.fit()
print(result.summary())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_Report, Y, test_size=0.3, random_state=0)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
    
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)