"Import python program(previous OOP based calculator) and run in this program."

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

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(10, 25))
    print("Subtraction:", calc.subtract(15, 5))
    print("Multiplication:", calc.multiply(18, 5))
    print("Division:", calc.divide(25, 5))
