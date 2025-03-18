"Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string."

"The Person class will only include these attributes in the following order:"
"firstname,lastname,age"

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def __repr__(self):
        return f"{self.firstname} {self.lastname}, {self.age}"  

def people_sort(people, attribute):
    return sorted(people, key=lambda person: getattr(person, attribute))


p1 = Person("ayushi", "varasani", 40)
p2 = Person("hemanshi", "chhatrola", 21)
p3 = Person("palak", "satasiya", 29)

print(people_sort([p1,p2], "firstname"))  
print(people_sort([p2,p3], "lastname"))   
print(people_sort([p1,p3], "age"))        
