"Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers."



def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero'
    else:
        return 'Error: Invalid operator'




num1, num2, operator = 15, 52, '*'
calc_result = calculate(num1, num2, operator)
print("Calculation result:", calc_result)
