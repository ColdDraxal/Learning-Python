class BankAccount:
    def __init__(self):
        self.__balance=1000
    @property
    def balance(self):
        return{self.__balance}
    def deposit(self,depo):
        if depo<1:
            print("Enter a Valid Amount")
        else:
            self.__balance+=depo
    def withdraw(self,withd):
        if withd<1:
            print("Enter a Valid Amount")
        elif withd>self.__balance:
            print("Enter a Valid Amount")
        else:
            self.__balance-=withd
p1=BankAccount()
print(p1.balance)
p1.deposit(120)
print(p1.balance)
p1.withdraw(20)
print(p1.balance)

