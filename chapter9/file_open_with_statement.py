f = open("file.txt")
print(f.read())
f.close()


#above can be written with "With" statement for removing the need of explicit close

with open("file.txt") as f:
    print(f.read())