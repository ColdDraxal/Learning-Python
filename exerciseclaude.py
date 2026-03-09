
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

a=[1,2,3,4]
trip=lambda x: x*3
print(trip(a))