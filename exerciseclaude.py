
#----------------------LAMBDA--------------------------

# a=int(input("Enter a number: "))
# print((lambda x:x*x)(a))

# high=lambda x,y:x if x>y else y
# print(high(7,6))
# a=[4,5,2,3,7,32,4]                          #sorted but reverse(descending)
# print(sorted(a,reverse=True))

# students = [("Ali", 22), ("Sara", 19), ("John", 25), ("Zara", 20)]
# sorting=lambda x:x[1]
# print(sorted(students,key=sorting))
# print(sorted(students,key=sorting,reverse=True))


# ------------------------MAP-------------------

# numbers = [1, 2, 3, 4, 5]
# a=list(map(lambda x:x*2,numbers))
# print(a)

# a=[1,2,3,4]
# trip=lambda x: x*3
# print(list(map(trip,a)))

# prices = [100, 200, 300, 400, 500]
# discount = [10, 20, 30, 40, 50]

# fp= lambda x,y: x-y
# print(list(map(fp,prices,discount)))

# names = ["ali", "sara", "john", "zara"]
# Title=lambda x: x.capitalize()
# print(list(map(Title,names)))



# -----------------Filter()--------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even= lambda x: x%2==0
# print(list(filter(even,numbers)))

# names = ["Ali", "Sara", "John", "Zara", "Mike", "Ana"]
# charrr=lambda x: len(x)>3
# print(list(filter(charrr,names)))

# students = [("Ali", 12), ("Sara", 19), ("John", 15), ("Zara", 20), ("Mike", 17)]
# lage=lambda x:x[1]>=18
# print(list(filter(lage,students)))


#--------------------------reduce-----------------------------



# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# plus=lambda x,y=0: y+x
# print(reduce(plus,numbers))


# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# prod=lambda x,y: y*x
# print(reduce(prod,numbers))


# from functools import reduce
# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# largest=lambda x,y: x if x>y else y
# print(reduce(largest,numbers))


#--------------------------f-string---------------------

# name = "Darpan"
# age = 21
# print(f"My name is {name} and I am {age} years old.")

# price = 49.98765
# print(f"Price of this milk is {price:.2f}")

# name = "Darpan"
# score = 95.5678
# total = 100
# print(f"{name} scored {score:.2f} marks in exams which is a total of {(score/total)*100:.2f}%")

#=================================Enumerate()====================================

# fruits = ["apple", "banana", "mango", "orange"]
# for index,fruit in enumerate(fruits):
#     print(index,fruit)

# students = ["Ali", "Sara", "John", "Zara"]
# for index,student in enumerate(students,start=1):
#     print(f"Student {index}: {student}")


# Use `enumerate()` to print each task, but mark the **3rd task** (index 2) as **Done** and the rest as **Pending** like this:


# tasks = ["Buy groceries", "Clean house", "Do homework", "Cook dinner"]
# for index,task in enumerate(tasks,start=1):
#     if index==3:
#         print(f"Task {index} : {task} is Done")
#     else:
#         print(f"Task {index} : {task} is Pending")


#=================================Join()====================================

# words = ["Python", "is", "awesome"]
# print(" ".join(words))

# fruits = ["apple", "banana", "mango", "orange"]
# print(" | ".join(fruits))

# letters = ["P", "y", "t", "h", "o", "n"]
# print("-".join(letters))
# print("".join(letters))


#===============================*args,**kwargs==================================

# def add_all(*args):
#     return sum(args)
# print(add_all(5,23,4,5,21,3))

# def introduce(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")


# introduce(name="Darpan", age=21, city="Butwal")
# -----------------------------------------------------------------
# -- Exercise 3 — Step up more:
# -- Create a function order_summary() that accepts:

# -- A regular argument name (customer name)
# -- *args for items ordered
# -- **kwargs for extra details like delivery address, payment method etc.

# def order(name,*args,**kwargs):
#    print(f"Customer : {name}")
#    print(f"Items Ordered : {",".join(args)}")
#    for key,value in kwargs.items():
#         print(f"{key} : {value}")

# order("Darpan", "Pizza", "Burger", "Coke", address="Butwal", payment="Cash")



#=================================Decorators====================================


