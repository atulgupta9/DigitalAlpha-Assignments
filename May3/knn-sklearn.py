from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris_dataset = datasets.load_iris()
x = iris_dataset['data']
y = iris_dataset['target']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train,y_train)

print("Accuracy is :",knn.score(x_test,y_test))

print("Original \t vs \t Prediction")
y_pred = knn.predict(x_test)
for i in range(len(x_test)):
    print("%f \t\t %f"%(y_test[i],y_pred[i]))