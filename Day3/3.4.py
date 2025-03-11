"Write a function/program that takes a list of numbers and returns a list with two elements:"
"The first element should be the sum of all even numbers in the list."
"The second element should be the sum of all odd numbers in the list."

def even_odd(num):
    even_sum=0
    odd_sum=0

    for n in num:
        if n % 2==0:
            even_sum=+sum
        else:
            odd_sum=+sum
        return [even_sum,odd_sum]
    
    num[1,2,5,7,8,9]
    result = even_odd(num)
    print("result is :",result)
