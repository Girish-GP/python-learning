# write a list comprehension to print a list which contains the multiplication table of a user entered number

def multiplication_table(n):
    list1 = [n*i for i in range(1,11)]
    for index,item in enumerate(list1):
        print(f"{n} x {index+1} = {item}")

try:
    n = int(input('Enter n:'))
    print(f"Multiplication table of {n}")
    multiplication_table(n)
except ValueError as e:
    print(f"Error: {e}")

