# Write a program to input eight numbers from user and print unique

uniqueElements = set()
for i in range(1,9):
    num = int(input(f"Enter number {i}:"))
    uniqueElements.add(num)
print(f"Unique element are:{uniqueElements}")