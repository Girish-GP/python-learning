# write a program to print multiplication table of a given number using while loop

num = int(input("enter the number:"))
print("Multiplication Table of",num)
i = 1
while(i<11):
    print(f"{num}*{i} = {num*i}")
    i+=1

