"A fruit juice company tags their fruit juices by concatenating the first three letters of the words in a flavor's name, with its capacity."
"Create a Program that creates product IDs for different fruit juices."

def product_id(flavor, capacity):
    words = flavor.split()  
    first_three_letters = [word[:3].upper() for word in words]
    
    product_id = ''.join(first_three_letters) + capacity.strip()  
    
    return product_id

flavor = input("Enter the flavor name: ")
capacity = input("Enter the capacity: ")

generated_product_id = product_id(flavor, capacity)
print(f"The product ID for the juice is: {generated_product_id}")

