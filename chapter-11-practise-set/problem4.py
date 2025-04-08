# Write a class "Complex" to represent complex numbers along with overloaded operators + and * which adds and multiplies them

# class Complex:
#     complex_num = None
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.complex_num = f"{self.a} + {self.b}i"
    
#     def __add__(self,num):
#         n1 = self.complex_num.split('+')
#         n2 = num.complex_num.split('+')
#         temp = f"{int(n1[0].strip())+int(n2[0].strip())} + {int(n1[1].strip().replace('i',''))+int(n2[1].strip().replace('i',''))}i"
#         return temp

#     def __mul__(self,num):
#         n1 = self.complex_num.split('+') # n1[0] : a   n1[1] : bi   n2[0]: c n2[1]:di
#         n2 = num.complex_num.split('+')  #(a+bi)(c+di) = ac + adi + bci + bd(-1) = (ac-bd) + (ad+bc)i = (n1[0]*n2[0] - n1[1]*n2[1]) + (n1[0]*n2[1] + n1[1]*n2[0])i
#         temp = f"{(int(n1[0].strip()))*(int(n2[0].strip()))-(int(n1[1].strip().replace("i","")))*(int(n2[1].strip().replace("i","")))} + {(int(n1[0].strip()))*(int(n2[1].strip().replace("i","")))+(int(n1[1].strip().replace("i","")))*(int(n2[0].strip()))}i"
#         return temp

class Complex:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        real = self.a + other.a # 1 + 3 ==> 4
        imag = self.b + other.b # 2 + 4 ==> 6
        return Complex(real,imag) # Complex(4,6) ===> self.a = 4 and self.b = 6
    
    def __mul__(self,other): #(ac-bd) + (ad+bc)
        real = self.a * other.a - self.b * other.b # 1*3-2*4 ==> 3-8 ==> -5
        imag = self.a * other.b + self.b * other.a # 1*4 + 2*3 ==> 4+6 ===> 10
        return Complex(real,imag) # Complex(-5,10) ===> self.a = -5 and self.b = 10

    def __str__(self):
        return f"{self.a} + {self.b}i" if self.b > 0 else f"{self.a} - {-self.b}i"
num1 = Complex(1,2) # a =1 b=2  ==>  1+2i
num2 = Complex(3,4) # a=3 b=4 ===> 3+4i
# (3-8)+(4+6)i = -5+10i
print(num1 + num2) # here add is called with complex numbers 1+2i and 3+4i ==> return Complex object and the print statement calls the string version of complex object by using __str__ function
print(num1*num2)