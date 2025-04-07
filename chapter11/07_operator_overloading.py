class Number:

    def __init__(self,n):
        self.n = n
    
    def __add__(self,num):
        return self.n + num.n
    
    def __sub__(self,num):
        return self.n - num.n

    def __mul__(self,num):
        return self.n * num.n

    def __truediv__(self,num):
        return self.n/num.n

n1 = Number(1)
n2 = Number(2)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)