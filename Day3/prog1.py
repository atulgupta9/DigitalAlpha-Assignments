#1.	Given the rent data file, write a Python program to do the following.
#a)	Calculate the mean, mode and median of the rents.
#b)	Generate a frequency distribution and print the table
#c)	Print the cumulative frequent distribution
#d)	Calculate 25th, 50th and 75th percentile values
#e)	Calculate variance and coefficient of variance
import statistics
rent_list = []
rent_dict = {}
unique_rent_list = []
with open("rentData.txt","r") as file:
    for line in file:
        rent_list.append(int(line.replace("\n","")))
print("Mean is "+str(statistics.mean(rent_list)))
print("Median is "+str(statistics.median(rent_list)))
print("Mode is "+str(statistics.mode(rent_list)))


for i in rent_list:
    if(rent_dict.get(i)):
        rent_dict[i]+=1
    else:
        rent_dict[i]=1
print("Frequency Distribution Table:-")
print("Value \t Frequency")
for key,value in rent_dict.items():
    print("%d \t %d"%(key,value))


freq = 0
for key,value in rent_dict.items():
    rent_dict[key]+= freq
    freq=rent_dict[key]
print("Cummulative Frequency Distribution Table:-")
print("Value \t Frequency")
for key, value in rent_dict.items():
    print("%d \t %d" % (key, value))


print("25th Percentile Value is",rent_list[int(len(rent_list)/4)])
print("50th Percentile Value is",rent_list[int(len(rent_list)/2)])
print("75th Percentile Value is",rent_list[int( ( len(rent_list)*3)/4)])



print("Variance is ",statistics.variance(rent_list))
print("Coefficient of Variance is ",(statistics.stdev(rent_list)/statistics.mean(rent_list))*100,"%")
