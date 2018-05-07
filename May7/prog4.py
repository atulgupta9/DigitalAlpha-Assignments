"""
1.	Write a python program to implement abstraction and encapsulation in school management system. Restrict the user by their role,
a)	 Principal must have access to all the details
b)	 non-teaching staff – give access to their section only
c)	Teaching staff – student details
"""
class SMS:
    __student_list = ["ABC","XYZ","DEF"]
    __teacher_list = ["ayz","xef","dbc"]   
    
    def __add_teacher(self,x):
        self.__teacher_list.append(x)
    
    def __view_teacher(self):
        print("\nPrinting list of teachers")
        print(self.__teacher_list)
    
    def view_student(self):
        print(self.__student_list)   
    
    def access_to_principal(self):
        self.__view_teacher()
        self.__add_teacher(str(input("Enter a teacher name to add to the list ")))
        self.__view_teacher()
        

class Staff:
    personal_details = "Update Details here"
    def view_personal_details(self):
        print(self.personal_details)
        
    def update_personal_details(self):
        print("\nOld Details")
        self.view_personal_details()
        self.personal_details = str(input("Enter new details "))
        print("\nNew Details")        
        self.view_personal_details()        
    
class Teaching_Staff(SMS,Staff):
    pass    

class Non_Teaching_Staff(Staff):
    pass
        

staff = Teaching_Staff()
print("\nTeaching Staff accessing student List")
staff.view_student()

print("\nNon Teaching Staff accessing personal details")
staff = Non_Teaching_Staff()
staff.view_personal_details()
staff.update_personal_details()


sms = SMS()
print("\nPrincipal access to student List")
sms.view_student()
sms.access_to_principal() 


        
    
    

