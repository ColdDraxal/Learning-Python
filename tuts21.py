# Operators In Python
"""
# Arithmetic Operator
# Assignment Operator
# Comparison Operator
# Logical Operator
# Identity Operator
# Membership Operator
# Bitwise Operators
"""



#ARITHMETIC OPERATORS
"""
print("5 + 2 =", 5+2)  # Addition
print("5 - 2 =", 5-2)  # Subtraction
print("5 * 2 =", 5*2)  # Multiplication
print("5 / 2 =", 5/2)  # Division
print("5 % 2 =", 5%2)  # Modulus {Remainder}
print("5 ** 2 =", 5**2)  # Exponentiation {Power}
print("9 // 2 =", 9//2)  # Floor Division (Quotient)
"""


#ASSIGNMENT OPERATORS
"""
a = 5
a += 2  # a = a + 2
print("a += 2 :", a)
a -= 2  # a = a - 2
print("a -= 2 :", a)
a *= 2  # a = a * 2
print("a *= 2 :", a)
a /= 2  # a = a / 2
print("a /= 2 :", a)
a %= 2  # a = a % 2
print("a %= 2 :", a)
a **= 2  # a = a ** 2
print("a **= 2 :", a)
a //= 2  # a = a // 2
print("a //= 2 :", a)

# You can use these operators with other data types as well

b = "Hello "
b += "World!"  # b = b + "World!"
print("b += 'World!':", b)
c = [1, 2, 3]
c += [4, 5]  # c = c + [4, 5]
print("c += [4, 5]:", c)
"""


#COMPARISON OPERATORS
"""
x = 5
y = 2
print("x == y :", x == y)  # Equal
print("x != y :", x != y)  # Not Equal
print("x > y  :", x > y)   # Greater Than
print("x < y  :", x < y)   # Less Than
print("x >= y :", x >= y)  # Greater Than or Equal To
print("x <= y :", x <= y)  # Less Than or Equal To
"""


#LOGICAL OPERATORS
"""
a = True
b = False
print("a and b :", a and b)  # Logical AND
print("a or b  :", a or b)   # Logical OR
print("not a   :", not a)     # Logical NOT
"""


#IDENTITY OPERATORS
"""
x = ["apple", "banana"] 
y = x
z = ["apple", "banana"]
print("x is y :", x is y)       # True because y references to x
print("x is z :", x is z)       # False because z is a different object
print("x is not z :", x is not z) # True because z is a different object
"""


#MEMBERSHIP OPERATORS
"""
fruits = ["apple", "banana", "cherry"]
print("banana in fruits :", "banana" in fruits)       # True
print("grape not in fruits :", "grape" not in fruits) # True
print("Mango not in fruits :", "Mango" not in fruits) # False
"""

#BITWISE OPERATORS
"""
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print("a & b  :", a & b)  # Bitwise AND: 0001 -> 1
print("a | b  :", a | b)  # Bitwise OR:  0111 -> 7
print("a ^ b  :", a ^ b)  # Bitwise XOR: 0110 -> 6
print("~a     :", ~a)     # Bitwise NOT: 1010 -> -6
print("a << 1 :", a << 1) # Left Shift: 1010 -> 10
print("a >> 1 :", a >> 1) # Right Shift: 0010 -> 2
"""


# End of the Operators tutorial
