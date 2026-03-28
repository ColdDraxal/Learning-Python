"""
class Student:
    def __init__(self, name):
        self.name = name
Draxal=Student("Darpan")
print(type(Draxal))
print(hasattr(Draxal,"name"))
method=getattr(Draxal,"name")
print(method)
method2=setattr(Draxal,"age",22)
print(Draxal.age)

"""
# Exercise for obj inspection

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def greet(self):
        return f"Hello, I am {self.name}"

    def is_pass(self):
        return self.marks >= 40
    
s = Student("Darpan", 75)

# print(getattr(s,"name"))
# method=getattr(s,"greet")
# print(method)
# print(method())
# method1=getattr(s,"name")
# print(callable(method1))
# method2=getattr(s,"greet")
# print(callable(method2))
# print(method2())
# method3=getattr(s,"age","notfound")
# print(method3)
# method4=getattr(s,"name","notfound")
# print(method4)
# setattr(s,"age",20)
# print(getattr(s,"age"))
# print(s.age)
for attr in ["name", "marks", "greet", "is_pass"]:
    value=getattr(s,attr,"notFound")
    if callable(value):
        print(value())
    else:
        print(value)