class BankAccount:
    def __init__(self, Current_Balance =0):
        self.account_balance = Current_Balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")