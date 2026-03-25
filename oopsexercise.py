# Basic OOPS
"""
class Book:
    def __init__(self,title,year):
        self.title=title
        self.year=year
    def show_info(self):
        return f"Title: {self.title}\nPublished Year: {self.year}"
book1=Book("A Song of Ice and Fire",1996)
print(book1.show_info())
"""
# Single Inheritance and Overriding

"""
class Animal:
    def make_sound(self):
        self.sound="Some Sound"
        print(self.sound)
class Dog(Animal):
    def make_sound(self):
        self.sound="Woof Woof"
        print(self.sound)
class Cat(Animal):
    def make_sound(self):
        self.sound="Meow Meow"
        print(self.sound)

# animal1=Cat()
# animal1.make_sound()
# animal2=Dog()
# animal2.make_sound()
# animal3 = Animal()
# animal3.make_sound()
animals=[Dog(),Cat(),Animal()]
for a in animals:
    a.make_sound()
"""
# Multiple Inheritance

"""
class Flyable():
    def fly(self):
        print("I can fly")
class Swimmable():
    def swim(self):
        print("I can swim")
class Duck(Flyable,Swimmable):
    pass

animal1=Duck()
animal1.fly()
animal1.swim()
"""
# Multi Level Inheritance
"""
class Vechile:
    def vechile_type(self):
        return "This is generic vechile. "
class Car(Vechile):
    def vechile_type(self):
        return super().vechile_type()+"This is Car. "
class ElectricCar(Car):
    def vechile_type(self):
        return super().vechile_type()+"This is Electric Car. "
    
Vechile1=ElectricCar()
print(Vechile1.vechile_type())
"""
# Diamond Problem Resolution
"""
class A:
    def show(self):
        return "A "
class B(A):
    def show(self):
        return super().show() + "B "
class C(A):
    def show(self):
        return super().show() + "C "
class D(B,C):
    def show(self):
        return super().show() + "D "
order=D()
print(order.show())
"""

# Encapsulation and Access Modifiers
"""
class BankAccount:
    def __init__(self):  
        self.__balance=1000
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def show_balance(self):
        return self.__balance

Darpan=BankAccount()
Draxal=BankAccount()
Darpan.deposit(500)
Draxal.withdraw(100)
print(Darpan.show_balance())
print(Draxal.show_balance())
Draxal.deposit(200)
print(Draxal.show_balance())
"""

# Polymorphism
"""
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
s1=Rectangle(5,4)
s2=Square(3)
s3=Shape()
print(s1.area())
print(s2.area())
print(s3.area())
"""
# Combination Exercise (Mini Project)

class Person:
    _school="Kalika Manavgyan"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"Name:{self.name}\nAge:{self.age}\nSchool:{Person._school}"
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject
    def info(self):
        return f"{super().info()}\nSubject:{self.subject}"
class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade=grade
    def info(self):
        return f"{super().info()}\nGrade:{self.grade}"
    
persons=[Student("Darpan",22,12),Teacher("Draxal",35,"Python"),Person("Miya",23)]
for i in persons:
    print(i.info())
        