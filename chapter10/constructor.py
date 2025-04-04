class Employee:
    salary = 123000
    lang = "Python"
    def __init__(self,name,salary): #it can take more arguments
        print("I am creating a object")
        self.name = name
        self.salary = salary
        #constructor function init / dunder function which is automatically called when object is created

# harry = Employee()
# harry.name = "GGP"
# instead of assigning instance attributes like above use the below

harry = Employee("GGP",234555)
print(harry.name,harry.salary) # GGP 234555