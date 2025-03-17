"Create a function that returns the amount of duplicate characters in a string."
"It will be case sensitive and spaces are included. If there are no duplicates, return 0."

from collections import Counter

def count(s):
    char_count = Counter(s)
    
    duplicates = sum(1 for count in char_count.values() if count > 1)
    
    return duplicates

string = "Abbcde"
result = count(string)
print("Output:", result)


    