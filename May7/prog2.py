"""
2.	Write a python program to implement hybrid inheritance with ‘person’ class
"""
class Living_Thing:
    pass

class Person(Living_Thing):
    def what_i_am(self):
        print("I am a person")

class Employee(Person):
    def what_do_i_do(self):
        print("I work")

class Teacher(Person):        
    def what_do_i_do(self):
        print("I teach")
        
p = Person()
p.what_i_am()

print("\n")
p = Employee()
p.what_i_am()
p.what_do_i_do()

print("\n")
p = Teacher()
p.what_i_am()
p.what_do_i_do()