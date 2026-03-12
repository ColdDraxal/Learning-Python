# fruits = ["apple", "banana", "mango", "orange"]
# for index,items in enumerate(fruits,start=1):
#     print(f"{index}-> {items}")



# words = ["Python", "is", "very", "powerful"]
# print(" ".join(words))


# def intro(name,age):
#     return f"My name is {name} and I am {age} years old."
# print(intro("Darpan",21))

# ---------------------------------------------------------------------------------
# from functools import reduce

# numbers = [1,2,3,4,5]
# squr=lambda x: x*x
# print(list(map(squr,numbers)))


# numbers = [12,5,8,21,30,7]
# greater=lambda x:x>10
# print(list(filter(greater,numbers)))


# numbers = [1,2,3,4,5]
# prod=lambda x,y: x*y
# print(reduce(prod,numbers))

# # this program down here is extra program i wrote for testing something
# numbers = [12,5,8,21,30,7]
# greater=lambda x,y:x if x>y else y
# print(reduce(greater,numbers))

# ---------------------------------------------------------------------

# def total(*numbers):
#     return sum(numbers)
# print(total(1,23,4,56,4))

# def student_info(**data):
#     for item,value in data.items():
#         print(f"{item} : {value}")
# student_info(name="Darpan",age=21,address="Butwal-15")

# ----------------------------------------------------------------------------

# def timer(func):
#     def wrapper(*args):
#         print("Starting the program.")
#         result=func(*args)
#         print("Program ended!!!")
#         return result
#     return wrapper
# @timer
# def test():
#     print("Hello World!!!")
# test()

# --------------------------------------------------------------------------

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x:x%2==0,(numbers)))
# evsq=list(map(lambda x:x*x,even))
# print(even)
# print(evsq)



names = ["ram","hari","sita","gita"]
scores = [45,67,82,90]
cap=list(map(lambda x:x.title(),names))
for i, (name, score) in enumerate(zip(cap, scores), start=1): #zip pairs name and scors to each other
    print(f"{i}){name} --> {score}")
# for index,item in enumerate(cap):
#     print(f"{index+1}){item} --> {scores[index]}")


