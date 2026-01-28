# #
# print("Hello\n\"python\"\nThis is back lash:\\")
# #
# print("name:alex\nage:20")
# s=("WADDUP MA PEOPLE")
# print(s[0:5])
# print(s[-5:-1])
# print(s[::-1])
# print(s[::2])
# a=int(input("Enter 1st number"))
# b=int(input("Enter second number"))
# print("sum is",a+b)
# print("diff is",a-b)
# print("product is",a*b)
# print("division is",a/b)
# c=input("Enter a number")
# print(type(c))
# c=int(c)
# print(type(c))


# Take numbers from user (space-separated)
# Convert them into a list of integers
# Print:
# list
# length of list
# sum of elements
# num=input("Enter numbers seperated by spaces:\t")
# list=num.split()
# print(list)
# # print(len(list))
# # print(sum(list))
# list=[int(x)for x in num.split()]
# print(list)
# print(len(list))
# print(sum(list))



#
# a=[2,2,2,3,45,6,7,4]
# print(a)
# set1=set(a)
# print(set1)


# # 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# num=int(input("Enter a number: "))
# if num in a.union(b):
#     print("It exist")
# else:
#     print("It don't exist")


# 
# info = { "python": "programming language",
#          "list": "ordered collection",
#          "set": "unique values"}


# word=input("Enter a word:").lower().strip()
# mean=info.get(word)
# if mean is None:
#     print("It doesn't exist")
#     add1=input("Will you like to add the word to dictationary:(yes/no)").strip().lower()
    
#     if add1=="yes":
#        mean1=input("what is the meaning?")
#        info[word]=mean1
#        print("It is added")
#     elif add1=="no":
#      print("I see! See ya than.")
# else:
#     print("The meaning is:",mean)
# print(info)

# 
# Take marks (0–100) from the user and print:
# Invalid → marks < 0 or marks > 100
# Fail → marks < 40
# Pass → 40–59
# First Division → 60–79
# Distinction → 80–100
# Use if / elif / else only

# marks=int(input("Enter the marks you got:"))
# if 0>marks or marks>100:
#     print("It is invalid")
# elif marks<40:
#     print("Failed")
# elif 40<=marks<=59:
#     print("You have Passed")
# elif 60<=marks<=79:
#     print("First Division")
# else:
#  print("Distinction")



# 
# Take numbers from the user (space-separated)
# Store them in a list
# Convert the list into a set
# Ask the user for a number
# If the number exists in the set → print "Found"
# Else → print "Not Found"

# numbers=input("Enter numbers seperated by space: ")

# numlist=numbers.split()
# okay=[int(x)for x in numlist]
# numset=set(okay)
# ask=int(input("Write a number: "))
# if ask in numset:
#     print("Found")
# else:
#     print("not found")


# 
# num=input("Enter numbers with space: ")
# numlist=num.split()
# okay=[int(x) for x in numlist]
# print(okay)
# print(len(okay))
# print(sum(okay))
# okay[0],okay[-1]=okay[-1],okay[0]
# print(okay)


# 
info={"mutable":"can be changed",
      "immutable":"cannot be changed",
      "set":"collection of variables"}
ask=input("Enter a word: ").strip().lower()
ex=info.get(ask)
if ex is None:
    print("It doesn't exist")
    hmm=input("Would you like to add that word: (yes/no)").strip().lower()
    if hmm=="yes":
        mean=input("Please write its meaning: ")
        info[ask]=mean
        print("It is added")
    elif hmm=="no":
        print("sheesh! Alright than see ya later.")
else:
        print("The meaninig is: ",ex)

print(info)
