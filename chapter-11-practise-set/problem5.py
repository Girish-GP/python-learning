# Write a class vector representing a vector of n dimensions . Overload the + and * operator which calculates the sum and dot product of them

class Vector:

    def __init__(self,*components):
    #*components: This allows you to pass any number of arguments to the constructor, and those arguments will be gathered into a tuple named components.
        self.components = components

    def __add__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors should be of same dimensions")
        result = (self.components[i]+other.components[i] for i in range(len(self.components)))
        return Vector(*result)

    def __mul__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors should be of same dimensions")
        return sum(self.components[i] * other.components[i] for i in range(len(self.components)))
    
    def __str__(self):
        return f"({' ,'.join(map(str, self.components))})"
     

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1+v2)
print(v1*v2)