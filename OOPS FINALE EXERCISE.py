"""
from abc import ABC,abstractmethod
class Account(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class BankAccount(Account):
    def __init__(self,balance):
        self.balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("Invalid Amount")
        else:
             self.__balance=value
    def deposit(self,amount):
        if amount<0:
            raise ValueError("Invalid Amount")
        else:
            self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount>self.balance:
            raise ValueError(f"Insufficient balance: available {self.balance}")
        elif amount<0:
            raise ValueError("Invalid Amount")
        else:
            self.balance = self.balance - amount
acc1=BankAccount(1000)
print(acc1.balance)

# print(acc1.withdraw(500))
# acc1.deposit(-1)
"""

"""
class cNumbers:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        return f"{self.real}+{self.imag}!"
    def __add__(self,other):
        return cNumbers(self.real+other.real,self.imag+other.imag)
a=cNumbers(5,6)
b=cNumbers(7,8)
print(b)
"""

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def aname(self):
        return f"The name is {self.name}."
    def aage(self):
        return f"The age is {self.age}"
    def result(self):
        return self.marks>=40
Darpan=Student("Darpan",22,41)
setattr(Darpan,"grade",17)
a=["name","age","marks","grade","aname","aage","result"]
for attr in a:
    value=getattr(Darpan,attr,"Not Found")
    if callable(value):
        print(value())
    else:
        print(value)
        