#  Create a 2D vector class and then use it to create another 3D vector class

class twoDVector:

    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.show()

    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        self.k = k
        super().__init__(i,j)
        self.show()

    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")

vector1 = twoDVector(1,3)

vector2 = threeDVector(1,3,5)

print(vector1.i,vector1.j)
print(vector2.i,vector2.j,vector2.k)