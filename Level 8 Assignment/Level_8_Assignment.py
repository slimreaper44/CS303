import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")