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