class Employee:
    company = "JPL"
   
    def __init__(self):
        self.print_company()

    def print_company(self):
        print(f"The company is {self.company}")


class Coder:
    lang = "Python"

    def __init__(self):
        self.print_language()

    def print_language(self):
        print(f"The language is {self.lang}")

class Programmer(Employee,Coder):

    def __init__(self,name):
       self.name = name
       self.print_programmer()
       super().__init__() #Here is czlling method of super parent main parent EMployee

    def print_programmer(self):
        print(f"The programmer is {self.name}")

girish = Programmer("GGP")
girish.print_company()
girish.print_language()
girish.print_programmer()