import pandas as pd
import numpy as np
import math 

def random_centroids(k,x,y):
    random_list = np.random.randint(0,len(x),k)
    centroid_list=[]
    for i in range(k):
        centroid_list.append([x[random_list[i]],y[random_list[i]]])
    return centroid_list

def euclidean_dist(x,y,centroids):    
    centroid_dist_list =[]
    for i in range(len(centroids)):
        dist_each_centroid = []
        for j in range(len(x)):
            dist_each_centroid.append(math.sqrt(((x[j]-centroids[i][0])**2 + (y[j]-centroids[i][1])**2)))
        centroid_dist_list.append(dist_each_centroid)
    return centroid_dist_list  
            
def get_clusters(x,y,dist_from_centroids):
    dist_from_centroids = list(dist_from_centroids)
    cluster_list = []
    flag =False
    for i in range(len(dist_from_centroids[0])):
        minimum = 99999999
        index=-1
        for j in range(len(dist_from_centroids)):
            if(dist_from_centroids[j][i]==0):
                cluster_list.append(j)                
                flag=False
                break
            elif(dist_from_centroids[j][i] < minimum):
                minimum=dist_from_centroids[j][i]
                index=j
                flag=True
        if(flag):
            cluster_list.append(index)
    return cluster_list
            
def get_new_centroids(k,x,y,cluster_list):
    sum_x = 0
    sum_y = 0
    count =0
    centroid_list=[]
    for i in range(k):
        count = 0
        for j in range(len(cluster_list)):
            if(cluster_list[j]==i):
                sum_x = sum_x + x[j]
                sum_y = sum_y + y[j]
                count += 1
        if(count>0):
            centroid_list.append([sum_x/count,sum_y/count])
    return centroid_list             
                
        
        
def should_i_stop(old_centroid,new_centroid):
    print(old_centroid)
    print(new_centroid)
    return old_centroid == new_centroid
        
        
df = pd.read_excel(r"C:\Users\user\Python Programs\April19\kmean.xlsx")
x = np.array(df["A"])
y = np.array(df["B"])
print("Enter the no. of clusters")
k = int(input())
centroids = random_centroids(k,x,y)
dist_from_centroids = euclidean_dist(x,y,centroids)
cluster_list = get_clusters(x,y,dist_from_centroids)
new_centroid = get_new_centroids(k,x,y,cluster_list)
while not (should_i_stop(centroids,new_centroid)):
    centroids=new_centroid
    print(centroids)
    dist_from_centroids = euclidean_dist(x,y,centroids)
    cluster_list = get_clusters(x,y,dist_from_centroids)
    new_centroid = get_new_centroids(k,x,y,cluster_list)
print(cluster_list)    

    
