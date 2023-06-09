from abc import ABC, abstractmethod
class Transaction(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class BankAccount(Transaction):
    balance = 0
    def deposit(self, amount):
        previous_balance = self.balance
        self.balance = self.balance + amount
        print("Previous Balance: ", previous_balance, "Deposited: ", amount, " ", end='')
        self.showBalance()
    def withdraw(self, amount):
        previous_balance = self.balance
        if amount >= self.balance:
            print("Insufficient Balance!")
        else:
            self.balance = self.balance - amount
            print("Previous Balance: ",previous_balance, "Withdrawn: ", amount, " ", end='')
            self.showBalance()
    def showBalance(self):
        print("Current Balance: ", self.balance)



myaccount = BankAccount()
myaccount.deposit(7000)
myaccount.withdraw(5000)
myaccount.deposit(15000)
myaccount.withdraw(5000)
myaccount.deposit(30000)
myaccount.withdraw(15000)
myaccount.deposit(90000)
myaccount.withdraw(50000)







