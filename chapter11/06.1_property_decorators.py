# You are building a class to manage a Student's academic record. The Student class should store the student’s birth_year and calculate their age based on the current year. However, the age should always be computed dynamically, and the birth_year should not be directly modified after being set.

# Implement a Student class where:
# The birth_year is a private attribute that can be set only once during initialization, and it cannot be changed after that.
# The age is a computed property based on the current year and the birth_year. This property should be updated dynamically every time it is accessed.
# The birth_year should not be accessed directly from outside the class but should be accessed and set through the birth_year property.

# Constraints:

# Ensure that the age is computed based on the current year.

# If someone tries to modify birth_year after initialization, it should raise an exception.

# The class should also handle cases where birth_year might be invalid (like a year in the future).


import datetime

class Student:

    def __init__(self,birth_year):
        self._birth_year = None
        self.birth_year = birth_year

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self,birth_year):
        current_year = datetime.datetime.now().year
        if int(birth_year) > int(current_year):
                raise Exception("Birth year cannot be of future")
        if self._birth_year is not None:
            raise Exception("Birth year cannot be modified")
        self._birth_year = birth_year                
            
    
    @property
    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self._birth_year

try:
    student1 = Student(2026)
    print(student1.age)
except Exception as e:
    print(f"{e}")
# student1.birth_year = 3000 #Exception: Birth year cannot be modified

    
    