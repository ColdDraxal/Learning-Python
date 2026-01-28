# for greatest_value in range(1,31):
#     if greatest_value%3==0:
#         continue

#     print(greatest_value)

# greatest_value=0
# while True:
#     greatest_value=int(input("Enter number"))
#     if greatest_value<=50:
#         print(greatest_value)
#     else:
#         break
# print("Invalid")

# for greatest_value in range(1,11):
#     if greatest_value%2!=0:
#         continue
#     print(greatest_value)


# greatest_value=""
# while greatest_value!="stop":
#     greatest_value=input("enter something:")
#     print("You typed: ",greatest_value)

# data = ["Ram", 5, "Hari", 12, "Sita", 8]
# for greatest_value in data:
#     if not isinstance(greatest_value,str):
#         continue
#     print(greatest_value)

# max_attempt=5
# current_attempt=1
# while current_attempt<=max_attempt:
#     p=input("Enter the corrrect password: ")
#     if p=="python123":
#         print("Correct Password!!")
#         print("It took",current_attempt,"tries.")
#         break
#     print(5-current_attempt,"remaining")
#     current_attempt=current_attempt+1
# if current_attempt==6:
#     print("Access Denied")

# greatest_value=0
# j=0
# while True:
#     greatest_value=int(input("Enter a number:- "))
#     if greatest_value>=0:
#      j=greatest_value+j
#     elif greatest_value<0:
#         break
# print(j)


# for greatest_value in range(5,0,-1):
#     print(f"{greatest_value*'*':>5}")
    


# print(f"Choose one of the following:")
# print(f"1 - add 2 numbers")
# print(f"2 - multiply 2 numbers")
# print(f"3 - Exit")
# while True:
#     k=int(input("Choose a number: "))
#     if k==3:
#         break
#     if k>3 or k<1:
#         print("Invalid")
#         continue
#     greatest_value=int(input("Enter 1st number: "))
#     j=int(input("Enter 2nd number: "))
#     if k==1:
#         print(greatest_value+j)
#     else:
#         print(greatest_value*j)
# print("You have exited sucessefully")


# count = 0

# while count < 15:
#     num = int(input("Enter a number: "))

#     if num > 999:
#         break

#     if num < 0:
#         continue

#     print(num)
#     count += 1


number=int(input("Enter a number: "))
if number==0:
    print("Please enter a valid number")
else:
    greatest_value=number
while True:
    number=int(input("Enter a number: "))
    if number==0:
        break
    if number>greatest_value:
        greatest_value=number
    else:
        continue
print(greatest_value)    
        