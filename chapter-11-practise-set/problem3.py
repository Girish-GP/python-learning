#Create a class "Employee" and add salary and increment properties to it. Write a method 'salaryAfterIncrement' with a @property decorator with a setter which changes the value of increment based on the salary


class Employee:

    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100



person1 = Employee(1200000,20)

print(person1.salaryAfterIncrement)

person1.salaryAfterIncrement = 1222222
print(person1.increment)
print(person1.salaryAfterIncrement)
