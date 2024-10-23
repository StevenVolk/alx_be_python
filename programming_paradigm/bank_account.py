class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > account_balance:
            return False
        return True

    def display_balance():
        print(f"Current Balance: ${account_balance}")
