"""
1.	Write a python program to reverse a string using stack
"""
class stack:
    def __init__(self):
        self.x = []
        
    def push(self,val):
        self.x.append(val)
        
    def pop(self):
        return self.x.pop()
    
    def peek(self):
        return self.x[len(self.x)-1]
    
    def is_empty(self):
        return self.x == []
    
    def size(self):
        return len(self.x)
        
    
        
print("Enter a string")
input_string = str(input())
s1 = stack()
reverse_string = ""
for i in input_string:
    s1.push(i)
while(not s1.is_empty()):
    reverse_string += s1.pop()
print("Reverse String :",reverse_string)