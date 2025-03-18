"Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:"
"Form the fullname by simply joining the first and last name together, separated by a space."
"Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase."

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{self.first_name} {self.last_name}"  
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"  

emp_1 = Employee("Jenil", "Smith")
emp_2 = Employee("Mishva", "Sue")
emp_3 = Employee("Ayush", "Walker")

print(emp_1.last_name) 
print(emp_2.email)     
print(emp_3.first_name)  
