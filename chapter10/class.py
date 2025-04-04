# class is a blueprint for creating a object

class Employee:
    destination = "Developer"
    salary = "20lakhs"

dummy_object = Employee()
print(dummy_object.name)
print(dummy_object.age)
print(Employee) # <class '__main__.Employee'>
print(Employee()) # <_main_.Employee object at 0x748c31e90da0>


person1 = Employee()
person2 = Employee()


#Here designation and salary are Class attributes as they are attached to class Employee and every object created using Employee class will have same designation and salary

person1.name = "GGP"
person2.name = "XYZ"

#Here name is object attribute as it is attached to the object its value will be different for different objects