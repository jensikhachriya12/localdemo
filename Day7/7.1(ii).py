
"ii) Create a Program that takes a string (a random name). If the last and first character of the name is an 'd', return True, otherwise return False."


def first_and_last_are_d(name):
    
    return name[0].lower() == 'd' and name[-1].lower() == 'd'


name3 = "devang"
name4 = "Dev"
name5 = "Jensi"
print(first_and_last_are_d(name3))  
print(first_and_last_are_d(name4))  
print(first_and_last_are_d(name5))  
