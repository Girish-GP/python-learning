# add the multiplication table of problem 3 in a file


def multiplication_table(n):
    list1 = [n*i for i in range(1,11)]
    with open(f"{n}_table.txt","w") as f:
        for index,item in enumerate(list1):
            f.write(f"{n} x {index+1} = {item}\n")

try:
    n = int(input("Enter n:"))
    multiplication_table(n)
except ValueError as e:
    print(e)