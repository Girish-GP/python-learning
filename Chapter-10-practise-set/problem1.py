# Write a program to create a class Programmers for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    salary = 1200000
    # above are default class attributes of Programmer every object created using this class will have same above values when created

    def __init__(self,name,salary): #here name and salary will be the instance attributes which take preference over class attributes
        self.name = name
        self.salary = salary
        

jack = Programmer("Jack",2000000)

jim = Programmer("Jim",1200000)

print(jack.name)
print(jim.name)