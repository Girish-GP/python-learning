# write a program to calculate greatest of three numbers

# taking parameters/arguments
def greatest(num1,num2,num3):
    return max(num1,num2,num3)

print(greatest(233,32,11))


def greatest2():
    x1 = int(input("Enter number 1:"))
    x2 = int(input("Enter number 2:"))
    x3 = int(input("Enter number 3:"))
    print(max(x1,x2,x3))

greatest2()