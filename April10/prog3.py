"""
3. Write a python program to represent marks of 4 students (roll number 1-4) in 4 subjects,
		a. find the highest mark of each student
		b. find the topper
		c. print the marks of first two roll numbers
		d. print the marks of all students in ascending order. 
		e. update the details by adding marks of roll number 5 and 6
"""
student_dict  = {1 : [45,65,87,98], 2: [43,65,83,90] , 3:[34,28,60,82], 4:[24,65,34,76]}
total= []
for i in student_dict:
   print("Highest Mark of Student %d : %d"%(i,max(student_dict[i])))
   total.append(sum(student_dict[i]))
   student_dict[i].sort()

print("\nStudent %d is the topper"%(total.index(max(total))+1))

for i in student_dict:    
    print("\nMarks of student %d in ascending order:"%(i))
    print(student_dict[i])



student_dict[5]=[54,25,68,85]
student_dict[6]=[43,52,86,58]

for key,value in student_dict.items():    
   print("\nMarks of Student %d"%(key))
   for val in value:
       print(val, end=" ")
   print("\n")
       
