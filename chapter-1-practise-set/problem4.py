# write a program to read content from a directory using os module

import os

# path of the directory from which you want to list file contents
directory_path = "/"

# list all files in the directory
contents = os.listdir(directory_path)

#print the contents
for item in contents:
    print(item)