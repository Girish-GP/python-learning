#write a program to store seven fruits in a list entered by user
fruits = []
for i in range(7):
    fruit_name = input(f"Enter fruit {i+1} :")
    fruits.append(fruit_name)
print(f'Fruits list is {fruits}')