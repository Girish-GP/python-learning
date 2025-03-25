# write a program to find greatest of 4 numbers entered by user

#using list and max method
numbers = []
for i in range(1,5):
    num = int(input(f"enter number {i}:"))
    numbers.append(num)
print(f"Greatest of 4 numbers is {max(numbers)}")

#using if elif else ladder
greatest = numbers[0]
# if(numbers[1] > greatest):
#     greatest = numbers[1]
# if(numbers[2] > greatest):
#     greatest = numbers[2]
# if(numbers[3] > greatest):
#     greatest = numbers[3]


for i in numbers[1:]:
    if(i > greatest):
        greatest = i
print(f"Greatest using conditionals : {greatest}")