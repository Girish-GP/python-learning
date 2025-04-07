class A:
    a =1
    def __init__(self):
        print("constructor of A")

    def dummy(self):
        print("dummy of A")

class B(A):
    b = 2
    def __init__(self):
        print("constructor of B")
        # super().__init__()
        # super().dummy()

class C(B):
    c = 3
    def __init__(self):
        print("constructor of C")
        # super().__init__()
        A.__init__(self)
        super().dummy()

# o = A()
# print(o.a)


# o = B()
# print(o.a,o.b)

o = C()
print(o.a,o.b,o.c)