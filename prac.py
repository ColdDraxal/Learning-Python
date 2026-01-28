# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# print("press 1 for addition")
# print("press 2 for subtraction")
# print("press 3 for multiplication")
# print("press 4 for division")
# choice=int(input("Enter your choice: "))
# if choice==1:
#     print("sum is:",num1+num2)
# if choice==2:
#     print("difference is:",num1-num2)
# if choice==3:
#     print("product is:",num1*num2)
# if choice==4:
#     print("quotient is:",num1/num2)
# num_list = [int(x) for x in input("Enter numbers: ").split()]
# print("Your list is:", num_list)


# Ask the user for a sentence.

# Ask the user for numbers separated by spaces.

# Then print:

# Length of the sentence

# Sentence reversed

# The list of numbers (as integers)

# Sum of the numbers

# Swap the first and last number in the list and print the list again

# sentence=input("Say a sentence: ")
# numbers=input("Enter numbers separated by space: ")
# print("length of sentence is",len(sentence))
# print("reversed sentence is :-",sentence[::-1])
# list=[int(x) for x in numbers.split()]
# print("your list is|:",list)
# print("sum of numbers in list is :",sum(list))
# list[0],list[-1]=list[-1],list[0]
# print("list after swapping first and last number:",list)

numbers=(input("enter numbers:"))
list=[int(x)for x in numbers.split()]
print(list)
print("sum",sum(list))