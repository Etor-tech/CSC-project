from account import Account

class SavingsAccount(Account):
    limit = 25000000  # Set the limit for withdrawals

    def _init_(self, balance):
        super()._init_(balance)

    def withdraw(self, amount):
        if amount > self.limit:
            raise ValueError(f"Cannot withdraw more than the limit of {self.limit}")
        super().withdraw(amount)  # Call the base class withdraw method

    def deposit(self, amount):
        super().deposit(amount)  # Call the base class deposit method
