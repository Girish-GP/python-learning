# A file contains word "Donkey" multiple times . Write a program to replace this word with ###### by updating the same file

file_content = ""
with open("problem4.txt") as f:
    file_content = f.read()
file_content = file_content.replace("Donkey".lower(),'######')

with open("problem4.txt","w") as f:
    f.write(file_content)