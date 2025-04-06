class A:
    a = 1
    
    @classmethod
    def print(cls):
        print(f"Class value of a is {cls.a}")

test = A()
test.print()