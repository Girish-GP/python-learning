# function to calculate average of three numbers

def average(num1 = 10,num2 = 10,num3 = 10): #here 10 is default value i.e default arguments
    return (num1+num2+num3)/3 #we are returning the average
x = average(1,2,3)
print(x)

# function definition
def greetUser():
    username = input("Enter name:")
    print(f"Good Day {username}")

greetUser() #function call
greetUser()
greetUser()

print(average()) #here we are not passing any arguments so default parameters will be used

#Parameter: name is the parameter. A parameter is a variable in the function definition that acts as a placeholder for the value passed into the function.

# Argument: 'ggp' is the argument. An argument is the actual value you pass into the function when you call it.


# Return Value 

# default function returns None 


