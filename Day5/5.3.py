"Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list."

def count_data_types(*args):
    type_count = {}
    
    for arg in args:
        t = type(arg)
        if t in type_count:
            type_count[t] += 1
        else:
            type_count[t] = 1
    
    return list(type_count.values())

print(count_data_types(1, "hello", 3.14, 1, True, None, [1, 2, 3], {"key": "value"}, 3.14))
