# write a python function to print first n lines of the following pattern

# ***
# **
# *

def displayPattern():
    n = int(input("Enter value of n:"))
    for i in range(n,0,-1):
        print("*" * i)
        
displayPattern()


n2 = int(input("Enter value of n for recusrion:"))
def displayPatternRevursion(n2):
    if n2 == 1:
        print("*")
    else:
        print("*" * n2)
        displayPatternRevursion(n2-1)

displayPatternRevursion(n2)

