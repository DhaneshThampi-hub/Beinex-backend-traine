'''Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account
with a starting balance,withdraw funds, and handle
 a custom exception called NegativeBalanceError when the account balance goes below zero.'''

class NegativeBalanceError(Exception):
    pass
 
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise NegativeBalanceError("Insufficient funds: Cannot withdraw more than the available balance.")
        self.balance -= amount
        return amount
 
# Example usage
try:
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)
    while True:
        print("\nCurrent balance:", account.balance)
        withdrawal_amount = float(input("Enter withdrawal amount: "))
        withdrawn = account.withdraw(withdrawal_amount)
        print("Withdrawn amount:", withdrawn)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except NegativeBalanceError as e:
    print("Error:", e)
