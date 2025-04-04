# write a program to find out whether a file is identical and matches the content of another file

with open("file1_problem9.txt") as f:
    content1 = f.read()

with open("file2_problem9.txt") as f:
    content2 = f.read()

if len(content1) == len(content2) and content1 == content2:
    print("File content is identical")
else:
    print("File content is not identical")