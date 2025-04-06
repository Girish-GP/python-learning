class Student:
    section = "A"
    gender = "Male"

    # def getInfo():
    #     print(f"The student section is {section} and gender is {gender}")
    def getInfo(self): #self parameter refers to the instance/object with which the method was called
        print(f"The student section is {self.section} and gender is {self.gender}")

    @staticmethod
    def greet():
        print("hello")


student1 = Student()

# print(student1.getInfo()) ----> internally converted into ---> Student.getInfo(student1)
# TypeError: Student.getInfo() takes 0 positional arguments but 1 was given

print(student1.getInfo()) # As we used self parameter now it will call getInfo with the
# The student section is A and gender is Male
# None

#every method should have self parameter


#@staticmethod --> a decorator to define static method

print(student1.greet()) #hello



