class car:
    brand="Toyota"
    speed=180
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")
    
c1=car()
c1.show_details()


# ==============================
# Python OOP Notes
# ==============================

"""
OOP = Object Oriented Programming
---------------------------------
A programming style where we organize code using:
1. Classes (blueprints/templates)
2. Objects (instances of classes)
3. Methods (functions inside class)
4. Attributes (data inside class)

Why OOP?
---------
- Code becomes organized and reusable
- Models real-world objects easily
- Helps manage large programs
"""

# --------------------------------
# 1. Class
# --------------------------------
# A class is a blueprint/template for creating objects
# Example:

class Car:
    brand = "Toyota"   # class variable
    speed = 180        # class variable

    def show_details(self):
        # self refers to the current object
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")

# --------------------------------
# 2. Object
# --------------------------------
# An object is an instance of a class

c1 = Car()  # creating object c1
c1.show_details()

c2 = Car()  # creating object c2
c2.brand = "Honda"  # instance variable for c2
c2.speed = 220
c2.show_details()

# --------------------------------
# 3. self
# --------------------------------
# self = refers to the current object
# Always used as the first parameter in methods
# Example:
# def show_details(self):
#     print(self.brand)

# --------------------------------
# 4. __init__() Constructor
# --------------------------------
# Used to give object its own initial values when created

class Bike:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Speed : {self.speed}")

b1 = Bike("Yamaha", 120)
b2 = Bike("Honda", 150)

b1.show_details()
b2.show_details()

# --------------------------------
# 5. Key Points
# --------------------------------
# - Class: Blueprint (Car, Bike, Student)
# - Object: Real instance (c1, c2, b1, b2)
# - Attributes: Data inside class/object (brand, speed)
# - Methods: Functions inside class (show_details())
# - self: Refers to the current object
# - Class variables: shared by all objects
# - Instance variables: unique to each object

# --------------------------------
# 6. Example Exercise (Try it!)
# --------------------------------
# Create a class 'Student' with attributes: name, grade
# Method: show_details()
# Create 2 student objects with different values