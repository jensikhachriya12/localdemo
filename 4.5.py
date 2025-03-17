"Create a function/input that returns the sum of all even elements in a 2D matrix. in  display this code"

def sum_of_even_elements(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 == 0:
                total += num
    return total

# Example usage:
matrix = [
    [1, 2, 3],
    [10,25,86],
    [57, 88, 49]
]

result = sum_of_even_elements(matrix)
print("Sum of even elements:", result)
