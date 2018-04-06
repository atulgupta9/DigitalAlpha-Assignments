# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:40:10 2018

@author: user
"""
"""
4. From the given data plot the following, 
i) scatter plot 
ii) line of best fit.
Temperature in Celsius 	Ice cream sales
14.2	215
16.4	325
11.9	185
15.2	332
18.5	406
22.1	522
19.4	412
25.1	614
"""
import matplotlib.pyplot as plt
import numpy as np
x = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1]
y = [215,324,185,332,406,522,412,614]
x_mean = np.mean(x)
y_mean = np.mean(y)
numer = 0
denom = 0
for i in range(len(x)):
    numer += ((x[i]-x_mean)*(y[i]-y_mean))
    denom += ((x[i]-x_mean)**2)
b2 = numer/denom
b1 = y_mean - b2*x_mean
print("IceCreamSales = %f + %f TemperatureInCelsius"%(b1,b2))
plt.scatter(x,y)
max_x = np.max(x)
min_x = np.min(x)
X = np.linspace(max_x, min_x,10)
Y = b1 + b2 * X
plt.plot(X,Y) 



