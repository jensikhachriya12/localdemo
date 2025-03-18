"Given an integer, create a function that returns the next prime. If the number is prime, return the number itself."

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

print(next_prime(28))  
print(next_prime(26))  
print(next_prime(40)) 
