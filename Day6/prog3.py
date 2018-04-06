# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:59:50 2018

@author: user
"""
"""
3. The following is a list of price (in dollars) of birthday cards in various stores, make a frequency distribution table and then plot a histogram.
   1.45  2.20  0.75  1.23  1.25
   1.25  3.09  1.99  2.00  0.78
   1.32  2.25  3.15  3.85  0.52
   0.99  1.38  1.75  1.22  1.75
"""
import matplotlib.pyplot as plt
x=[1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.22,1.75]
freqDist = {}
for i in x:
    if freqDist.get(i):
        freqDist[i] +=1
    else:
        freqDist[i] = 1
print("Frequency Distribution Table")
print("Dollars \t Frequency")
for key,value in freqDist.items():
    print("%f \t %d"%(key,value))
plt.hist(x,5,alpha=0.5)
    