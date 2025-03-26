# write a program to find a given number is prime or not

num = int(input("enter the num:"))

if(num > 1):
    print("check for prime")
    for i in range(2,6):
        if num%i ==0 and num != i:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print("Please enter number greater than 1")