# Faulty calculator
# Design a calculator which will solve all the calculation except the following ones:
# 45*3=555, 56+9=77, 56/6=4
# Your program should take operators and two numbers as inputfrom the user and than return the user.

n1=int(input("Enter 1st number: "))
ask=input("Now what would you like to perform here: ( + , - , * , / ) Choose any one.").strip()
n2=int(input("Enter 2nd number: "))
sum=(n1+n2)
diff=(n1-n2)
product=(n1*n2)
division=(n1/n2)
if n1==45 and ask=="*" and n2==3:
    print(555)
elif n1==56 and ask=="+" and n2==9:
    print(77)
elif n1==56 and ask=="/" and n2==6:
    print(4)
elif ask=="+":
    print(sum)
elif ask=="-":
    print(diff)
elif ask=="*":
    print(product)
elif ask=="/":
    print(division)
else:
    print("Invalid operator")