"""
Created on Tue May  8 09:41:00 2018
2.	Evaluate the following 
a.	(1 + ( ( 2 + 3)  *  ( 4 * 5 )  ) )
b.	231*+9-
c.	-+7*45+2
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
    
    
def evaluate(operand1,operand2,operation):
    operand1 = int(operand1)
    operand2 = int(operand2)
    if operation =="+":
        return operand1+operand2
    elif operation =="-":
        return operand1-operand2
    elif operation =="*":
        return operand1*operand2
    elif operation =="/":
        return operand1/operand2
        
    

def infix_eval(infixexpr):
    prec={}
    prec["#"] = 0
    prec["("] = 1
    prec["+"] = 2
    prec["-"] = 2
    prec["*"] = 3
    prec["/"] = 3
    operator = "+-*/"
    opstack = stack()
    operand_stack = stack()
    opstack.push("#")
    for token in infixexpr:
        if token in "0123456789":
            operand_stack.push(token)
        elif token ==")":
            operation = opstack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operand_stack.push(evaluate(operand1,operand2,operation))            
        elif token in operator:            
            opstack.push(token)
    
    while(opstack.peek()!="#"):               
          operand2 = operand_stack.pop()
          operand1 = operand_stack.pop()
          operation = opstack.pop()
          operand_stack.push(evaluate(operand1,operand2,operation))
          
    return operand_stack.peek()

def postfix_eval(postfixexpr):    
    operand_stack = stack()
    operator = "+-*/"
    for token in postfixexpr:
        if token in "0123456789":
            operand_stack.push(token)
        elif token in operator:
            operand2= operand_stack.pop()
            operand1= operand_stack.pop()
            operand_stack.push(evaluate(operand1,operand2,token))
    return operand_stack.peek()
 
def prefix_eval(prefixexpr):
    operand_stack = stack()
    operator = "+-*/"
    for token in prefixexpr[::-1]:
        if token in "0123456789":
            operand_stack.push(token)
        elif token in operator:
            operand1= operand_stack.pop()
            operand2= operand_stack.pop()
            operand_stack.push(evaluate(operand1,operand2,token))
    return operand_stack.peek()
        
        
        
    
    
expr1 = "(1+((2+3)*(4*5)))"
expr2 = "231*+9-"
expr3 = "-+7*452"


print(infix_eval(expr1))
print(postfix_eval(expr2))
print(prefix_eval(expr3))