# Factorial for n numbers

def factorial(n):
    if n == 0 or n == 1: #This is the base condition
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))   
print(factorial(0))   

# Recursion is a function which calls itself