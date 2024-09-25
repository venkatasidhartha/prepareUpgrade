

class Calculator:
    def __init__(self,num1:int,num2:int):
        self.num1 = num1
        self.num2 = num2
        
        accept_datatype = [int,float]
        if type(self.num1) not in  accept_datatype:
            raise TypeError("num1 should be integer or float")
        if type(self.num2) not in  accept_datatype:
            raise TypeError("num2 should be integer or float")
        
    
    def add(self):
        output = f"the addition of {self.num1} and {self.num2} = {self.num1 + self.num2}"
        return output
        
    def sub(self):
        output = f"the subtraction of {self.num1} and {self.num2} = {abs(self.num1 - self.num2)}"
        return output
        
    def mul(self):
        output = f"the multiplication of {self.num1} and {self.num2} = {self.num1 * self.num2}"
        return output
        
    def div(self):
        try:
            output = f"the divition of {self.num1} and {self.num2} = {self.num1 / self.num2}"
            return output
        except ZeroDivisionError:
            return f"{self.num1} and {self.num2} numbers can't divide"
            
        

cal = Calculator(3,0)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())