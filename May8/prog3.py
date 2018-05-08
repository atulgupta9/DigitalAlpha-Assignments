"""
Created on Tue May  8 10:31:37 2018
3.	Convert the following
a.	a + b * (c ^ d - e) ^ ( f + g * h) -i    into postfix 
b.	( a- b / c )* ( a / k - l)    into prefix
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
        return self.x==[]
    
    def size(self):
        return len(self.x)
    
def infix_to_postfix(infixexpr):
    prec ={}
    prec["("] = 1
    prec["+"] = 2
    prec["-"] = 2
    prec["*"] = 3
    prec["/"] = 3     
    prec["^"] = 4
    opstack = stack()
    output = []
    for token in infixexpr:           
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            output.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":            
            top_token = opstack.pop()
            while(top_token!="("):
                output.append(top_token)
                top_token = opstack.pop() 
        else:
            while((not opstack.is_empty()) and prec[token]<prec[opstack.peek()]):                
                output.append(opstack.pop())                
            opstack.push(token)
    while(not opstack.is_empty()):
        output.append(opstack.pop())        
    return output

def infix_to_prefix(infixexpr):
    postfix=""
    for token in infixexpr[::-1]:
        if(token==")"):
                postfix +="("
        elif(token=="("):
                postfix +=")"
        else:
            postfix+=token
    return infix_to_postfix(postfix)[::-1]
result=""
for i in infix_to_postfix("A+B*(C^D-E)^(F+G*H)-I"):
    result += i
print("\nInfix: A+B*(C^D-E)^(F+G*H)-I")
print("Postfix: ",result)

result=""
for i in infix_to_prefix("(A-B/C)*(A/K-L)"):
    result += i
print("\nInfix: (A-B/C)*(A/K-L)")
print("Prefix: ",result)