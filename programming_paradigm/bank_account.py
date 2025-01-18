class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    initial_balance = 0

    def deposit(self, amount):
        return self.account_balance + amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            return self.account_balance - amount
        else:
            return False

    def display_balance(self):
        print(f"Your account balance is {self.account_balance}: ")
