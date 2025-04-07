# create a class Pets from Class Animals and further create class Dogs from Pets . Add a method bark to class Dog

class Animals:
    def __init__(self):
        print("Class Animals constructor")

class Pets(Animals):
    def __init__(self):
        print("Class Pets constructor")
        super().__init__()

class Dogs(Pets):
    def __init__(self,name):
        self.name = name
        print("Class Dogs constructor")
        super().__init__()
        self.bark()

    def bark(self):
        print(f"{self.name} bark")

tommy = Dogs('tommy')