class Student:
    section = "A" #this is a class attribute

student1 = Student()
student1.name = "Girish" # this is instance attribute

student1.section = "S"

print(student1.section)