"Create a program that takes a list of numbers and returns the sum of all prime numbers in the list."

def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num % 0.5)+1):
        if num % i==0:
            return False
        return True
    
def sum_prime(number):
    total=0

    for n in number:
        if prime(n):
            total=+n
        return total
    
    number=list(map(int, input("Enter number:").split()))

    result=sum_prime(number)

    print("The result is:",result)
