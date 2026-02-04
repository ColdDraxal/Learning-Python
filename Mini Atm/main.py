balance=1000
def money_withdraw(balance):
    try:
        withdraw=int(input("Enter the amount of money you want to withdraw: "))
    except ValueError:
        print("Please enter a valid number.")
        return balance
    if balance<withdraw:
        print("Insufficent Balance")
        return balance
    elif withdraw<=0:
        print("Please enter valid amount to withdraw.")
        return balance
    else:
        balance=balance-withdraw
        print(f"Withdraw is Sucessful\nYour new balance is {balance}")
    return balance
def money_deposit(balance):
    try:
        deposit=int(input("Enter the amount of money you want to deposit: "))
    except ValueError:
        print("Please enter a valid number.")
        return balance
    if deposit<=0:
        print("Please enter valid amount to deposit.")
        return balance
    else:
        balance=balance+deposit
        print(f"Deposit is Sucessful\nYour new balance is {balance}")
    return balance
def menu_slc():
    try:
        select1=int(input("Menu:\n1)Balance\n2)Withdraw\n3)Deposit\n4)Exit\nEnter a number from the menu: "))
    except ValueError:
        print("Please enter a valid number.")
        return None
    if select1<1 or select1>4:
        print("Please select a number from the option.")
        return None
    return select1
        

while True:
    choice=menu_slc()
    if choice is None:
        continue
    if choice==1:
        print(f"Your current ballance is {balance}.")
    elif choice==2:
        balance=money_withdraw(balance)
    elif choice==3:
        balance=money_deposit(balance)
    else:
        break
print("Thank you for using Draxal ATM service")