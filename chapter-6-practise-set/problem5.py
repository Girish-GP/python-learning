# Write a program to check whether a given number is present in the list or not

numbersList = [23,112,33,244,211,453]

given_number = int(input("Enter the number:"))

if given_number in numbersList:
    print("Number present in the list")
else:
    print("Number not present in the list")