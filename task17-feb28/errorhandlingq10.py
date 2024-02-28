'''Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account
with a starting balance,withdraw funds, and handle
 a custom exception called NegativeBalanceError when the account balance goes below zero.'''

class NegativeBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise NegativeBalanceError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        
        if self.balance - amount < 0:
            raise NegativeBalanceError("Insufficient funds to make the withdrawal.")
        
        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance}")

if __name__ == "__main__":
    try:
        # Example usage
        initial_balance = float(input("Enter the initial balance: "))
        account = BankAccount(initial_balance)

        withdraw_amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(withdraw_amount)

    except ValueError as ve:
        print(f"Error: {ve}")
    except NegativeBalanceError as nbe:
        print(f"Error: {nbe}")
