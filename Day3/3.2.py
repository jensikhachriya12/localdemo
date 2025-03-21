"Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly"
"divided by c from the range a, b inclusive"

def sum(a, b, c):
    total_sum = 0
    
    for number in range(a, b + 1):
        if number % c == 0:
            total_sum += number
    
    return total_sum

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result = sum(a, b, c)
print(f"The sum of numbers between {a} and {b} that are divisible by {c} is: {result}")


