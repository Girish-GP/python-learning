# write a program to calculate sum of n natural numbers using while loop

num = int(input("Enter number:"))

i=1
sum =0
if num < 1:
    print("Invalid number please enter number greater than 0")
else:
    while (i < (num+1)):
        sum += i
        i+=1
    print(f"Sum of first {num} natural numbers is : {sum}")