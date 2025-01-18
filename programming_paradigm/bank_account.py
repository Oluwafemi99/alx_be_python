class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
    initial_balance = 0

    def deposit(self, amount):
        result = self.account_balance + amount
        return result

    def withdraw(self, amount):
        if self.account_balance >= amount:
            result = self.account_balance - amount
            return result
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
