"Create a function that returns the selected filename from a path. Include the extension in your answer."

import os

def get_filename_from_path(file_path):
    return os.path.basename(file_path)


path = "D:\PYTHON\p4.py"
print(get_filename_from_path(path))  
