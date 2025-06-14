"""
0. Create a Simple Bank Account Class
mandatory
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:
Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.
main-0.py for Command Line Interaction:
This script utilizes BankAccount through command line arguments for banking operations.

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
Sample Command Line Usage and Expected Outputs:
Deposit:
   python main-0.py deposit:50
Expected Output: Deposited: $50

Withdraw with Sufficient Funds:
   python main-0.py withdraw:20
Expected Output: Withdrew: $20

Withdraw with Insufficient Funds:
   python main-0.py withdraw:150
Expected Output: Insufficient funds.

Display Balance:
   python main-0.py display
Expected Output: Current Balance: $[amount]

Implementation Notes for you:
Ensure your BankAccount class in bank_account.py correctly implements the specified functionalities and adheres to the principles of encapsulation.
Use main.py to test your BankAccount class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.

"""

# bank_account.py by Gemni

class BankAccount:
    """
    A simple BankAccount class to demonstrate OOP principles.
    Encapsulates banking operations like deposit, withdraw, and balance display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance # Using __ for "private" attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount
        # print(f"Successfully deposited: ${amount}. New balance: ${self.__account_balance}") # For debugging/extra info

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            # print(f"Successfully withdrew: ${amount}. New balance: ${self.__account_balance}") # For debugging/extra info
            return True

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

    # Optional: You might want a getter method for the balance if needed for other parts of a larger system,
    # but for this assignment, display_balance() is sufficient for showing it.
    # def get_balance(self):
    #     return self.__account_balance