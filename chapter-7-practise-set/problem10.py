# write a program to multiplication table of n using for loop in reverse order

num = int(input("enter the number:"))
for i in range(10,0,-1):
    print(f"{num} * {i} = {num*i}")