# write a program to calculate the factorial of a given number using for loop

num = int(input("Enter the number:"))
if num < 0:
    print("Please enter number greater than or equal to 0") #factorial of 0 is 1
elif num == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(num,0,-1): #here range is used with negative step
        fact*=i
    print(f"Factorial of {num} is {fact}")