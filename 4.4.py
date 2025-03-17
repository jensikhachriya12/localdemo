"Create a function/input that, given a number, returns the corresponding value of that index in the Fibonacci series."

def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(4, n + 1):
            a, b = b, a + b
        return b

# Example usage
index = int(input("Enter an index: "))
print(f"Fibonacci number at index {index} is {fibonacci(index)}")