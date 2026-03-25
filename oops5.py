class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        return f"{self.real}+{self.imag}i"
    def __repr__(self):
        return f"ComplexNumber({self.real},{self.imag})"
    def __add__(self, other):
        return ComplexNumber(self.real+other.real,self.imag+other.imag)

a=ComplexNumber(5,6)
b=ComplexNumber(3,4)
print(a)
print(repr(a))
c=a+b
print(c)