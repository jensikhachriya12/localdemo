"Create methods for the Calculator class that can do the following:"
"Add two numbers.,Subtract two numbers.,Multiply two numbers.,Divide two numbers"

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


calculator = Calculator()
print(calculator.add(15, 75))      
print(calculator.subtract(25, 16))  
print(calculator.multiply(40, 5))  
print(calculator.divide(45, 5))    
 
