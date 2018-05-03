from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
iris_dataset = datasets.load_iris()
x = iris_dataset['data']
y = iris_dataset['target']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

def euclidean_dist(x1,x2):
    d=0
    for i in range(len(x1)):
      d = d + (x1[i]-x2[i])**2
    return np.sqrt(d)  

def get_distance_list(x_train,test):
    distance_list = []
    for i in range(len(x_train)):
        distance_list.append(euclidean_dist(x_train[i],test))
    return distance_list

def indices_of_closest_3(closest_3,distance_list):
    index_list = []
    for i in closest_3:
        for j in range(len(distance_list)):
            if(i==distance_list[j]):
                index_list.append(j)
    return index_list

def get_max_vote(y_train,index_of_closest_3):
    count_0,count_1,count_2 = 0,0,0 
    for i in index_of_closest_3:
        if(y_train[i] == 0):
            count_0 += 1
        elif(y_train[i] == 1):
            count_1 += 1
        elif(y_train[i] == 2):
            count_2 += 1
    if(count_0>count_1 and count_0>count_2):
        return 0
    elif(count_1>count_2 and count_1>count_0):
        return 1
    else:
        return 2
y_pred = []
for i in range(len(x_test)):
    distance_list = get_distance_list(x_train,x_test[i])
    sorted_distance_list = sorted(distance_list)
    closest_3 = sorted_distance_list[0:3]

    index_of_closest_3 = indices_of_closest_3(closest_3,distance_list)
    y_pred.append(get_max_vote(y_train,index_of_closest_3))

print("Original \t vs \t Predictions")
for i in range(len(y_test)):
    print("%f \t   \t%f"%(y_test[i],y_pred[i]))

print("Accuracy :",accuracy_score(y_test,y_pred))       
