# write a python function to print multiplication table of a given number


n = int(input("enter the number:"))

def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multiply(n)