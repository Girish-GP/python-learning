a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

if b==0:
    raise ZeroDivisionError("Invalid division by 0. Please enter another number for b")
else:
    print(f"The output of a/b is {a/b}")