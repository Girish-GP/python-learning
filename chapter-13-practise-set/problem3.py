# A list contains the multiplication table of 7. Write a program to convert it to string of same numbers

list1 = [7*i for i in range(1,11)]

temp = "\n".join(str(x) for x in list1)

print(temp)