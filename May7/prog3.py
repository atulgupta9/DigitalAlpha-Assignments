"""
1.	Write a python program to Implement polymorphism with the following
a)	Find the area of triangle, rectangle, circle
b)	Features of animals 

"""
import math
class area:
    def figure_area(self,a=None,b=None,c=None):
        if c is None:
            if b is not None:
                return "Area of rectangle: "+str(a*b)
            elif a is not None:
                return "Area of circle: " + str(3.14*a**2)
            else:
                print("Supply one parameter atleast")
        else:
            if (a+b > c and a+c >b and b+c > a):
                s= (a+b+c)/2
                area = math.sqrt(s*(s-a)*(s-b)*(s-c))
                return "Area of triangle: "+ str(area)
            else:
                return "Such a triangle is not possible"

area_calculator = area()
area_calculator.figure_area()
print(area_calculator.figure_area(1))
print(area_calculator.figure_area(2,4))
print(area_calculator.figure_area(8,4,6))

class Animals:
    def features(self,ear=None,nose=None,special=None):
        if special is None:
            if nose is not None:
                print("Animal has ",nose)
                print("Animal has ",ear)
            elif ear is not None:
                print("Animal has ",ear)
            else:
                print("Animal has no feature")
        else:
            print("Animal has ",special)
            print("Animal has ",nose)
            print("Animal has ",ear)

animal = Animals()
animal.features("1 ear","2 nose")
animal.features("2 ears")
animal.features()
            
                
        