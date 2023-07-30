import os

file_path = 'FILE_PATH'

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been removed.")
else:
    print("This file does NOT exist!")
