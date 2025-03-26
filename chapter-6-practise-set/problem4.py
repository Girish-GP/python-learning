# Write a program to find whether the username contains less than 10 characters or not

validUserName = input("Enter username:")

if(len(validUserName.strip()) != len(validUserName)):
    print("Username cannot start and end with whitespaces")
if '' in validUserName:
    print("Username cannot contain blank space")
if(len(validUserName) < 10):
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 characters")