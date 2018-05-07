"""
1.	Write a python program to implement different types of inheritance with the ‘Animal’ class.
"""
#Simple Inheritance
class Animal:
    def __init__(self,animal_type):
        self.x=animal_type
    def what_i_am(self):
        print("I am ",self.x)
    
class Dog(Animal):
    def __init__(self,animal_type):
        super().__init__(animal_type)
    def what_do_i_do(self):
        print("I bark at strangers")

d = Dog("Dog")
d.what_i_am()
d.what_do_i_do()

#Multiple Inheritance
class Human(Dog,Animal):
    def __init__(self,animal_type):
        super().__init__(animal_type)
print("\nMultiple Inheritance")
h = Human("Human")
h.what_i_am()
h.what_do_i_do()

#Multilevel Inheritance
class puppy(Dog):
    def __init__(self,animal_type):
        super().__init__(animal_type)
print("\nMultilevel Inheritance")
p = puppy("Puppy")
p.what_i_am()
p.what_do_i_do()
