"Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order."

def sort_students(student_dict):
    return sorted(student_dict.keys())
students = {"Jensi": 95, "Rutvi": 80, "Chanvi": 75, "Drashti": 58}
sorted_names = sort_students(students)
print(sorted_names)