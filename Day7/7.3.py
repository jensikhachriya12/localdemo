"Write a function to replace all instances of character c1 with character c2 and vice versa."

def double_swap(string, c1, c2):
    translation_table = str.maketrans({c1: '$', c2: c1, '*': c2})
    
    return string.translate(translation_table)

print(double_swap("jjkkmm", "j", "m"))  
print(double_swap("random w#rds", "#", "&"))  
print(double_swap("128  788 999", "8", "9"))  
