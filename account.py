class Account:
    def _init_(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount 
        else:
            raise ValueError("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount
