# write a python function which converts inches to centimeter

def inchesToCenti(inches):
    return inches/2.54

centimeter = int(input("Enter value:"))
print(f"Inches to centimeters :{inchesToCenti(centimeter)}")