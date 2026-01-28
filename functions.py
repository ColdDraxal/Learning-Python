# def Greet(name):
#     """This function is for greetings only"""
#     print("Hello",name)
# # Greet("Darpan")
# # Greet("Firoj")
# # Greet("Draxal")
# # print(Greet.__doc__)

# def double(a):
#     """This functions double the number"""
#     print(a*2)
# double(5)
# double(7)
# double(12)


# def add(a,b):
#     """This Function Does addition """
#     c=a+b
#     return c
# x=add(12,12)
# print(x)


def max_of_two(a, b):
    """This function tests the greatest numbers between 2 number"""
    if a>=b:
        return a
    else:
        return b
print(max_of_two(9,11))
print(max_of_two(16,13))