class Animal:

    def __init__(self,name):
        self.name = name 
        self.greet()
    
    def greet(self):
        print(f"Hello {self.name}")

class Tiger(Animal): #All the class attributes and methods are inherited from Animal class

    def move(self):
        print(f"Tiger named {self.name} moved")


simbha = Tiger('Simbha')