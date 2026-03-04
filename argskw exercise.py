# ADD
"""

def plus(*args):
    total=0
    for i in args:
        total+=i
    return total
x=(5,2,3,453,5435,5,345,4)
print(plus(*x))

"""
#Easier way

"""

def plus(*args):
    return sum(args)
x=(5,2,3,453,5435,5,345,4)
print(plus(*x))

"""

#count arguments
"""

def counting(*args,c=0):
    for i in args:
        c+=1
    return c
x=5,2,3,4,56
print(counting(*x))

"""
# or
"""
def counting(*args):
    return len(args)
x=[1,2,3,4,5,6,7,43,324,432]
print(counting(*x))
"""

# Print each keyword
"""
def keyw(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
x={"name":"Draxal","age":"21","job":"jobless"}
# keyw(name="Draxal", age=21, country="Nepal")
keyw(**x)
"""

#print maximum number
"""
def maxi(*args):
    return max(args)
x=(1,234,233,235,12)
print(maxi(*x))
"""
# Multiply nums
"""
def multip(*args):
    total=1
    for i in args:
        total = total*i
    return total
nums = [4,5,6]
print(multip(*nums))
"""
# Creating Profile

def create_profile(**info):
    if "name" not in info:
        print("Name not found")
        return
    else:
        print(f"Hello {info['name']}")
    for key,value in info.items():
        if key=="name":
            continue
        else:
            print(f"{key} : {value}")

create_profile(name="Draxal", age=21)