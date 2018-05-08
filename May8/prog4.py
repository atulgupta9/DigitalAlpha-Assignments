"""
Created on Tue May  8 12:19:26 2018
Queue
1.	Write a python program to implement CPU - priority scheduling
"""
class Queue:
    def __init__(self):
        self.x = []
        
    def enqueue(self,val):
        self.x.insert(0,val)
        
    def dequeue(self):
        return self.x.pop()
    
    def size(self):
        return len(self.x)
    def is_empty(self):
        return self.x==[]
 
process_dict = {}
print("Enter no. of processes")
priority_list = []
n = int(input())
for i in range(n):
    print("For Pid ",i)
    print("Enter burst time")
    burst_time = int(input())
    print("Enter priority")
    priority = int(input())
    priority_list.append(priority)
    process_dict[priority] = [i,burst_time]
priority_list.sort(reverse=True)
process_queue = Queue()

wait_time = []
turn_around_time =[]
for priori in priority_list:
    print(priori,end="\t")
    print(process_dict[priori])
    process_queue.enqueue(process_dict[priori])
    wait_time.append(0)
    turn_around_time.append(0)
print("Order of execution of Processes:")
print("Process Id \t Burst Time")
for i in range(process_queue.size()-1,-1,-1):
    print(process_queue.x[i][0],end=" \t\t ")
    print(process_queue.x[i][1])
while(not process_queue.is_empty()):
    p1 = process_queue.dequeue()
    for i in range(process_queue.size()):        
        wait_time[i]+= p1[1]
        
        
    
    
    




    
    

