# Rock Paper Scissors Game
"""
print("Rock  ,  Paper   ,   Scissors")
i=""
while True:
    i=input("Choose: ").lower()
    if i=="exit":
        break
    if i!= "rock" and i!= "paper" and i!= "scissors":
        print("invalid")
    elif i== "rock" or i== "paper" or i== "scissors":
        print(f"You choose: {i}" )
"""
"""

# Create a Atm System with Menu.
# ATM
# Starts with balance = 1000
# Shows menu:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

balance=1000
while True:
    print("Menu:")
    print("Choose a number between to do following:\n")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit\n")
    print("Your current balance is Rs",balance,end="\n\n")
    press=int(input("Enter a number: "))
    if press==4:
        break
    if press==2:
        dep=int(input("Enter the amount you want to deposit: "))
        if dep<=0:
            print("Invalid")
        else:
         print("Deposit Sucessful")
         balance+=dep
         print("Your new balance is: Rs",balance,end="\n\n")
    elif press==3:
        withd=int(input("Enter the amount you want to withdraw: "))
        if balance<withd:
            print("Insufficent balance")
        elif withd<=0:
            print("Invalid")
        else:
            print("Withdraw Sucessful")
            balance-=withd
            print("Your new balance is: Rs",balance,end="\n\n")
    elif press==1:
        print("Your current balance is: Rs",balance,end="\n\n")
    else:
        print("invalid")
print("Exited Sucessfully")

"""

# Task
# Write a program that:
# Keeps asking the user to enter a sentence
# stops only when the user types:

# stop

# At the end, print how many sentences the user entered.

"""

count=0
while True:
    sentence=input("Enter a sentence: ").lower()
    if sentence=="stop":
     break
    count+=1
print(f"User wrote {count} sentences")

"""


# Task
# Write a program that:
# Keeps asking user to enter numbers
# Stops when the user enters 0
# At the end, prints the largest number entered

greater_number=None
while True:
    number=int(input("Enter a number (or press 0 to stop): "))
    if number==0:
        break
    elif greater_number is None or number>greater_number:
        greater_number=number
if greater_number is None:
    print("No number entered")
else:
     print(f"The greatest number is {greater_number}")

