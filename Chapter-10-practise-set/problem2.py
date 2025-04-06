# write a class Calculator capable of finding square , cube and square root of given num

class Calculator:

    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"Sqaure of {self.num} is {self.num**2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num **3}")

    def square_root(self):
        print(f"Square root of {self.num} is {self.num**(1/2)}")
    
num1 = Calculator(2)
print(num1.square())
print(num1.cube())
print(num1.square_root())
#Whenever a function is executed by default it returns None