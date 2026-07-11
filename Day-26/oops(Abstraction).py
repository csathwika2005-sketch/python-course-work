'''from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")

    def viewhistory(self):
        print("you can your transactions")


    def userinfo(self):
        print("You can see your details")

    def transaction(self):
        print("you can do transactions")

    @abstractmethod
    def depost(self):
        pass
    @abstractmethod
    def withdraw(self):
            pass
class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit - CA")
    def withdraw(self):
        print("you can withdraw - CA")
class SavingAccount(Bankaccount):
    def deposit(self):
        print("You can deposit - SA")
    def withdraw(self):
        print("you can withdraw - SA")

class FixedDeposit(BankAccount):
     def deposit(self):
        print("You can deposit - FD")
    def withdraw(self):
        print("you can withdraw - FD")

class SalaryAccount(BankAccount):
     def deposit(self):
        print("You can deposit - SAA")
    def withdraw(self):
        print("you can withdraw - SAA")

class ZeroBalanceAccount(BankAccount):
     def deposit(self):
        print("You can deposit - ZBA")
    def withdraw(self):
        print("you can withdraw - ZBA")

sathu = ZeroBalanceAccount()
sathu.deposit()
sathu.withdraw()
sathu.checkbalance()
sathu.viewhistory()
sathu.userinfo()
sathu.transactions()

sathwi =SalaryAccount()
sathwi.depost()
sathwi.withdraw()
sathwi.checkbalance()
sathwi.userinfo()
sathwi.transactions()
'''

    
