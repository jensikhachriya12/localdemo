"Create a function/input that counts the integer's number of digits.Solve this without using strings."

def count_digits(n):
    if n == 0:
        return 1  
    
    count = 0
    n = abs(n)  
    
    while n > 0:
        n //= 10  
        count += 1
    
    return count


num = 123456
print("Number of digits:", count_digits(num))