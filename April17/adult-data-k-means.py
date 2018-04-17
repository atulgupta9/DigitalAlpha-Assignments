import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"C:\\Users\\user\\Python Programs\\April17\\adult.data.csv")
df.columns = range(0,len(df.columns))
df = df.replace(' ?',np.NaN)
df = df.replace(' <=50K',0)
df = df.replace(' >50K',1)

df = df.dropna()
y=df[12]
df = df.drop(12,axis=1)

le = preprocessing.LabelEncoder()

df=df.apply(preprocessing.LabelEncoder().fit_transform)

# =============================================================================
# for i in range(0,len(df.columns)):
#     if(df.dtypes[i] ==object):
#         le.fit(df[i])
#         df[i]= le.transform(df[i])
# =============================================================================
    
x=df
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)
kmeans = KMeans(n_clusters=2)  
kmeans.fit(x_train)
result=kmeans.predict(x_test)
  
kmeans.cluster_centers_
print(kmeans.score(x_test))
print(accuracy_score(y_test,result))


