# write a program to input name, marks and phone number of a student and format it using format function like below:

# "The name of the student is harry, his marks are 72 and phone number is 99999999"

name = input("enter name of the student:")
marks = int(input("enter marks of the student:"))
phone = int(input("enter phone number of the student:"))

temp = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)

print(temp)