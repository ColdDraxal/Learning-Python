"""
# def test(*args):
#     print(args)

# nums = [1,2,3]

# test(nums)
# test(*nums)

def test(*args):
     print(args)
test(5,6)
"""

#NOTES

# ==========================================
# *args and **kwargs in Python
# ==========================================

# -------------------------------
# 1. *args (Variable Positional Arguments)
# -------------------------------

# *args collects extra positional arguments into a TUPLE

def show_numbers(*args):
    # args is a tuple containing all positional arguments
    print("args =", args)
    
    # we can loop through args like any tuple
    for num in args:
        print("number:", num)

# calling the function
show_numbers(10, 20, 30, 40)


print("\n-----------------------------\n")


# -------------------------------
# 2. **kwargs (Variable Keyword Arguments)
# -------------------------------

# **kwargs collects keyword arguments into a DICTIONARY

def show_info(**kwargs):
    # kwargs is a dictionary
    print("kwargs =", kwargs)

    # loop through dictionary
    for key, value in kwargs.items():
        print(key, ":", value)

# calling the function with keyword arguments
show_info(name="Harry", age=20, city="London")


print("\n-----------------------------\n")


# -------------------------------
# 3. Using *args and **kwargs together
# -------------------------------

def example(a, *args, **kwargs):
    # a = first positional argument
    print("a =", a)

    # args = remaining positional arguments (tuple)
    print("args =", args)

    # kwargs = keyword arguments (dictionary)
    print("kwargs =", kwargs)

example(5, 10, 15, 20, x=1, y=2)


print("\n-----------------------------\n")


# -------------------------------
# 4. Unpacking with *
# -------------------------------

# * can also unpack lists/tuples when calling functions

numbers = [1, 2, 3]

def add(a, b, c):
    print("sum =", a + b + c)

# *numbers becomes 1,2,3
add(*numbers)


print("\n-----------------------------\n")


# -------------------------------
# 5. Unpacking dictionary with **
# -------------------------------

data = {"name": "Alice", "age": 25}

def person(name, age):
    print(name, age)

# **data becomes name="Alice", age=25
person(**data)


print("\n-----------------------------\n")


# ===============================
# Summary
# ===============================

# *args  → collects positional arguments → tuple
# **kwargs → collects keyword arguments → dictionary

# * can unpack iterables (list, tuple, string, etc.)
# ** can unpack dictionaries