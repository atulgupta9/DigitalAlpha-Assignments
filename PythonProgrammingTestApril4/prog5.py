import statistics as stat
x=[11.95,11.91,11.86,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]
weightDict = {}
for i in x:
    if(weightDict.get(i)):
        weightDict[i] +=1
    else:
        weightDict[i]=1
print("Printing frequency distribution for the given data of actual liquid weight in 16 'twelve-ounces' cans")
print("Weight \t Frequency")
for key,value in weightDict.items():
    print("%f \t %d"%(key,value))

print ("Mean is :",stat.mean(x))
print("Median is:",stat.median(x))
print("Mode is:",stat.mode(x))
