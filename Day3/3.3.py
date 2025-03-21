"Create a program that takes a list of numbers and returns the sum of all prime numbers in the list."

def is_prime(num):
  
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    total_sum = 0
    for number in numbers:
        if is_prime(number):
            total_sum += number
    return total_sum

input_list = [int(x) for x in input("Enter a list of numbers : ").split()]
result = sum_of_primes(input_list)
print(f"The sum of all prime numbers in the list is: {result}")
