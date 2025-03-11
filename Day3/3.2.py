"Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly"
"divided by c from the range a, b inclusive"

def sum(a,b,c):
    total_sum=0

    for num in range(a,b+1):
        if num % c==0:
           total_sum=+num
        return total_sum
    
    a=int(input("Enetr value a:"))
    b=int(input("Enter value b:"))
    c=int(input("Enetr value c:"))

    result=sum(a,b,c)

    print("result is :",result)

