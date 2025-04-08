# write __str__ function to print vector 7i + 8j + 10k

class threeDVector:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        # if self.b > 0 and self.c > 0:
        #     return f"{self.a}i + {self.b}j + {self.c}k"
        # elif self.b < 0 and self.c > 0:
        #     return f"{self.a}i - {-self.b}j + {self.c}k"
        # elif self.b > 0 and self.c < 0:
        #     return f"{self.a}i + {self.b}j - {-self.c}k"
        # elif self.b < 0 and self.c < 0:
        #     return f"{self.a}i - {-self.b}j - {-self.c}k"

        #for i 
        vector_str = f"{self.a}i"

        #for j
        if self.b >= 0:
            vector_str += f" + {self.b}j"
        else:
            vector_str -= f" - {-self.b}j"

        #for k
        if self.c >= 0:
            vector_str += f" + {self.c}k"
        else:
            vector_str -= f" - {-self.c}k"
        
        return vector_str

test = threeDVector(7,8,10)
print(test)