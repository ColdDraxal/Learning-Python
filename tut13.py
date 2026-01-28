age=int(input("Enter your age\t"))
if age<=7 or age>75:
    print("Invalid age")
elif age==18:
    print("We cannot decide here you have to visit us personally for us to check.")
elif 18<age:
    print("You can drive")


else:
    print("you cannot drive")