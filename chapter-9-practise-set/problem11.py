# write a program to rename a file to "renamed_by_python.txt"

with open("problem11_old.txt") as f:
    content = f.read()

with open("problem11_renamed_by_python.txt","w") as f:
    f.write(content)