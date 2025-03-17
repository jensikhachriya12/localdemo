"Given a list nums where each integer is between 1 and 100, return a sorted list "
"containing only duplicate numbers from the given nums list"

from collections import Counter

def duplicate_num(num):
    num_count=Counter(num)
    duplicates = sorted([num for num, count in num_count.items() if count > 1])

    return duplicates 

print(duplicate_num([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_num([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))