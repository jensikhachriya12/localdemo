"i) Create a Program that takes a string (a random name). If the last character of the name is an 'a', return True, otherwise return False."

def ends_with_a(name):
   
    return name[-1].lower() == 'a'


name1 = "mishava"
name2 = "maya"
print(ends_with_a(name1))  
print(ends_with_a(name2)) 

