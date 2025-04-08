# write the __len__() method in problem5 to get the dimensions of the vector

class Vector:

    def __init__(self,*components):
        self.components = components

    def __len__(self):
        return len(self.components)

vector1 = Vector(1,2,4)
vector2 = Vector(1,2)
vector3 = Vector(1,2,4,8)
vector4 = Vector(1)

print(len(vector1))
print(len(vector2))
print(len(vector3))
print(len(vector4))