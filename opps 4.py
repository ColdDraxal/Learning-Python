"""
========================================
INHERITANCE, OVERRIDING, super() IN PYTHON
========================================

----------------------------------------
1. INHERITANCE
----------------------------------------
Inheritance allows one class (child) to use
properties and methods of another class (parent).

Syntax:
class Child(Parent):
    pass

Python searches methods in this order:
Child → Parent → Parent's Parent (MRO)

----------------------------------------
EXAMPLE
----------------------------------------
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} barks")


d = Dog("Tommy")

# Dog can use BOTH its own and inherited methods
d.speak()   # from Animal
d.bark()    # from Dog


"""
----------------------------------------
TYPES OF INHERITANCE
----------------------------------------
"""

# Single Inheritance
class A:
    pass

class B(A):
    pass


# Multilevel Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass


# Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass


"""
----------------------------------------
2. METHOD OVERRIDING
----------------------------------------
When a child class defines a method with
the SAME NAME as parent → it overrides it.

Python will ALWAYS prefer child method first.
"""

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")


d = Dog()
d.speak()   # Dog version runs (NOT Animal)


"""
----------------------------------------
3. super()
----------------------------------------
super() is used to call parent class methods.

WHY?
- reuse parent logic
- avoid rewriting code
- works correctly in multiple inheritance

----------------------------------------
EXAMPLE 1: CALLING PARENT METHOD
----------------------------------------
"""

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Before parent call")
        super().speak()   # call parent method
        print("After parent call")


d = Dog()
d.speak()


"""
Execution flow:
1. Dog.speak() is called
2. prints "Before parent call"
3. super().speak() → calls Animal.speak()
4. prints "Animal makes a sound"
5. prints "After parent call"
"""


"""
----------------------------------------
EXAMPLE 2: super() WITH CONSTRUCTOR
----------------------------------------
"""

class Person:
    def __init__(self, name):
        print("Person constructor called")
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        print("Student constructor called")
        super().__init__(name)   # calls Person constructor
        self.grade = grade


s = Student("Ram", 10)

print(s.name)
print(s.grade)


"""
Execution flow:
1. Student() called
2. Student __init__ runs
3. super().__init__ → calls Person __init__
4. Person sets self.name
5. back to Student → sets grade
"""


"""
----------------------------------------
WITHOUT super() (IMPORTANT)
----------------------------------------
"""

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        self.grade = grade   # parent constructor NOT called


s = Student("Ram", 10)

# print(s.name)  # ❌ ERROR: 'Student' object has no attribute 'name'


"""
Reason:
- Person __init__ never executed
- so 'name' was never created
"""


"""
----------------------------------------
REAL-LIFE STYLE EXAMPLE
----------------------------------------
"""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show(self):   # overriding
        super().show()
        print(f"Model: {self.model}")


c = Car("Toyota", "Corolla")
c.show()


"""
----------------------------------------
FINAL UNDERSTANDING
----------------------------------------

INHERITANCE:
Child gets parent features

OVERRIDING:
Child replaces parent method

super():
Used to call parent method safely

----------------------------------------
VERY IMPORTANT CONCEPT (MRO)
----------------------------------------

Method Resolution Order:
Python searches in this order:

Child → Parent → Grandparent → ...

You can check using:
print(ClassName.__mro__)
"""