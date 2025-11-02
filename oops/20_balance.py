
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
       
    def check_balance(self):
        print(self.balance)
        
account = BankAccount("Alice", 1000)

account.deposit(500) 
account.withdraw(300) 
account.check_balance()
